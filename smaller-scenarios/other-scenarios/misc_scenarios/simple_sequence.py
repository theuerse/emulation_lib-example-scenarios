from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_

emu = Emulation("./config_files/example.config.py", [0, 1])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)

nb1 = NetworkBlock("./blocks/TwoNode_80211a_adhoc")
nb1.setNodes([n0, n1])

emu.addNetworkBlocks([nb1])

udperf_app1 = UdperfApp(n0, n1, 0.0, 99, 9000, 6000, 6001)
udperf_app2 = UdperfApp(n1, n0, 0.0, 99, 9000, 6000, 6001)

n0.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched0.log_%RUN%")
n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched1.log_%RUN%")

emu.setDuration(102)

emu.addApplications([udperf_app1, udperf_app2])

emu.setName('simple_sequence')
emu.setNumberOfRuns(3)
emu.setSecondsBetweenRuns(15)

for intervalSize in [1000, 500, 250, 100]:
    emu.setName(intervalSize)
    emu.setOutputDirectory('./results/simple_sequence/' + emu.getName())
    nb1.selectInterval(intervalSize)
    emu.start()
