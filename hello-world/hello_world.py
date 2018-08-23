from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.preprocessing.set_constant_value_for_column import SetConstantValueForColumn
from emulation_lib.preprocessing.repeat_file_until import RepeatIntermedFileUntil
from emulation_lib.linkcmd_backends.bdl_ import BDL_
import iperf_logapp

NUM_RUNS = 2
EMULATION_DURATION = 100  # seconds
NUMBER_OF_NODES = 2

#
# general emulation settings
#
emu = Emulation("./example.config.py", list(range(0,NUMBER_OF_NODES)))
emu.setName("HelloWorld")
emu.setLinkCmdBackend(BDL_())
emu.setSecondsBetweenRuns(5)
emu.setOutputDirectory('./results/HelloWorld')
# time in seconds, after which a run is to be considered finished, which triggers the fetching
# of the results and the initiation of the next run
emu.setDuration(EMULATION_DURATION) # seconds


#
# configure network block
#
# the folder containing the pre-calculated intermediate files to be used
WIFI_BLOCK = "./blocks/simple_mobility_802.11G_AdHoc_constant"
# create a new network block object based on the given intermediate file folder
wlan = NetworkBlock(WIFI_BLOCK)
wlan.setNodes(emu.getNodes()[0:NUMBER_OF_NODES])  # assign all two nodes to be part of the network

# select interval of network condition changes
# ./blocks/simple_mobility_802.11G_AdHoc_constant/0_1_1000.txt
# ./blocks/simple_mobility_802.11G_AdHoc_constant/1_0_1000.txt
wlan.selectInterval(1000)

# preprocessing steps are ways to modify intermediate files without changing the originals (experimentation)
# if the given intermediate files were too long, here we could use a preprocessing step to only take the first n seconds
wlan.addPreprocessingStep(RepeatIntermedFileUntil(EMULATION_DURATION, False))
# for this example, we only want to restrict the bandwidth (column #3 in the intermediate file)
# and therefore overwrite the columns for delay (#1) and loss (#2) with zeros using the following preprocessing steps
wlan.addPreprocessingStep(SetConstantValueForColumn("", 1, 0))
wlan.addPreprocessingStep(SetConstantValueForColumn("", 2, 0))

# before (part of 1_0_1000.txt)
# 10.000000	0.001542	0.44	5522.400
# 11.000000	0.001679	0.22	5632.848
# 12.000000	0.002284	1.71	3522.064

# after (part of 1_0_1000.txt)
# 10.000000	0	0	5522.400
# 11.000000	0	0	5632.848
# 12.000000	0	0	3522.064

# add the network block to the emulation
emu.addNetworkBlocks([wlan])


#
# configure the applications to be run
#
# Perform iperf bandwidth measurement (UDP) from client_node to server_node.
# Create a new application functional block, passing node references.
# This application block takes care of the application lifecycle (here starting/stopping an iperf UDP bandwidth test)
# as well as the collection of results.
# server, client, client_runtime[s], client_bandwidth[Mbps]
iperfApp = iperf_logapp.IperfLogApp(server=emu.getNode(0), client=emu.getNode(1),
                                    client_runtime=EMULATION_DURATION-1, client_bandwidth=100)

# add the application to the emulation object
emu.addApplications([iperfApp])


# schedule some arbitrary commands at three time points (second 0, 30 and 90 of the emulation)
for node in emu.getNodes():
    node.scheduleUserCmd(0, "date > /home/nfd/cmdExample.txt")
    node.scheduleUserCmd(30, "date >> /home/nfd/cmdExample.txt")
    node.scheduleUserCmd(90, "date >> /home/nfd/cmdExample.txt")


# Fetch the files created by the previous commands, additionally fetch the logfiles of the command scheduler.
# addUserResult() adds a file to the emulation results that are to be fetched from the nodes.
# The marker "%RUN% is replaced with the actual run-number before the start of the run.
for node in emu.getNodes():
    node.addUserResult("/home/nfd/cmdExample.txt", "cmdExample"+ str(node.getId()) + ".log_%RUN%")
    node.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched" + str(node.getId()) + ".log_%RUN%")
    #                          remote path                   local path/name inside "results/"


#
# Execute the runs / start the emulation process
#
for run in range(0,NUM_RUNS):
    emu.start(run)

# The call of start() triggers some sanity checks, after passing those, all blocks (wlan and iperfApp) create
# their part of the setup-time and run-time commands needed to perform the emulation.
# The setup commands and runtime commands are wrapped in scripts and deployed to the nodes.
# The nodes execute the setup commands, the emulation waits for ALL nodes the finish their setup phase.
# After this, a common emulation start time is calculated and cmdscheduler instances are started on the nodes (waiting
# for the emulation to start)

# Runs which have been already performed as in "all expected results are present" are skipped.