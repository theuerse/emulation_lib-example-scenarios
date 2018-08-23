from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.ndn_demoapps import NDN_DemoApps
from emulation_lib.apps.ndn_demoapps_wldr import NDN_DemoAppsWLDR
from emulation_lib.apps.cpu_logapp import CPUlogApp
from emulation_lib.preprocessing.set_constant_value_for_column import SetConstantValueForColumn
from emulation_lib.preprocessing.repeat_file_until import RepeatIntermedFileUntil
from emulation_lib.preprocessing.cut_out_part_of_file import CutOutPartOfFile
from emulation_lib.linkcmd_backends.bdl_ import BDL_
from emulation_lib.apps.ndn_network_overlay import NDN_NetworkOverlay
from emulation_lib import constants
import os
import random

NUM_RUNS = 15
NUM_CLIENTS = 2
WIFI_EMU_CMD_INTERVAL = 100
EMULATION_DURATION = 23 * 60  # 23 minutes in seconds

all_blocks = ["./blocks/zeroLossZerodelay", "./blocks/5%LossZerodelay",
              "./blocks/constantPosition4040", "./blocks/randomDirection4040",
              "./blocks/randomWalk2d4040"]

wifi_blocks = ["./blocks/randomWalk2d4040", "./blocks/constantPosition4040","./blocks/randomDirection4040"]
for wifi_block in wifi_blocks:
    for app_type in ["NDN_DemoApps"]:
        for run in range(0, NUM_RUNS):

            # determine client-server groups
            random.seed(run*1000)
            serverNode = random.randint(0,11)
            client_gateways = []
            for c in range(0, NUM_CLIENTS):
                client_gateways.append(random.randint(0,11))
            client_startTimes = random.sample(range(0, int(EMULATION_DURATION / 2)), NUM_CLIENTS)
            print("client_start-times: " + str(client_startTimes))

            # general emulation settings
            emu = Emulation("./example.config.py", list(range(0,12 + NUM_CLIENTS)))
            emu.setName(os.path.basename(wifi_block) + "_" + app_type + "_" + str(run))
            emu.setLinkCmdBackend(BDL_())
            emu.setSecondsBetweenRuns(5)
            emu.setOutputDirectory('./results/onlyNdnDemoApps_experiment/' + emu.getName())
            emu.setDuration(EMULATION_DURATION) # seconds


            # ensure NFD-logfiles are cleaned up and wldrdaemons are shutdown
            for node in emu.getNodes():
                node.scheduleUserCmd(constants.SETUP_TIME, "sudo rm /var/run/shm/nfd_packet_log/nfd_packet_log.csv")
                node.scheduleUserCmd(constants.SETUP_TIME, "sudo killall wldrdaemon_udp")
                node.scheduleUserCmd(constants.SETUP_TIME, "sudo killall tail")

            # set up network-blocks
            abileneNetwork = NetworkBlock("./blocks/abilene")
            abileneNetwork.setNodes(emu.getNodes()[0:12])
            abileneNetwork.selectInterval(1000) # without consequence as network-properties are static anyway (in this scenario)
            abileneNetwork.addPreprocessingStep(RepeatIntermedFileUntil(EMULATION_DURATION, False))

            network_blocks = []

            # read topology from file
            with open("./topologies/abilene.txt","r") as topologyFile:
                topology = topologyFile.readlines()

            groups = {emu.getNode(serverNode): []}
            clientGatewayAssoc = {}

            # add blocks for "last-miles"
            for client_num in range(0, len(client_gateways)):

                gateway_id = client_gateways[client_num]
                client_id = 12 + client_num
                groups[emu.getNode(serverNode)].append(emu.getNode(client_id))
                print("server/client: " + str(serverNode) + "," + str(client_id))

                clientGatewayAssoc[client_id] = emu.getNode(gateway_id)

                wifiNetwork = NetworkBlock(wifi_block)
                wifiNetwork.setNodes([emu.getNode(gateway_id), emu.getNode(client_id)]) # 2 nodes?
                wifiNetwork.selectInterval(WIFI_EMU_CMD_INTERVAL)

                wifiNetwork.addPreprocessingStep(CutOutPartOfFile(client_startTimes[client_num], client_startTimes[client_num] + EMULATION_DURATION, False))
                wifiNetwork.addPreprocessingStep(SetConstantValueForColumn("", 3, 27000.0))  # empty prefix -> apply to all files

                wifiNetwork.addPreprocessingStep(RepeatIntermedFileUntil(EMULATION_DURATION, False))
                network_blocks.append(wifiNetwork)

                topology.append(str(gateway_id) + "," + str(client_id)+'\n')
                print("abilene-access/client-id: " + str(gateway_id) + "," + str(client_id))

            network_blocks.append(abileneNetwork)
            emu.addNetworkBlocks(network_blocks)




            # parse topology file and retrieve connections (abilene)
            ndn_NetworkOverlay = NDN_NetworkOverlay(emu.getNodes(),topology,"shortest","/localhost/nfd/strategy/best-route")
            
            # log cpu% on every node
            cpuLogging = CPUlogApp(emu.getNodes(), 1)
            
            # setup applications based on groups established before
            ndn_apps = []

            for server in groups:
                clients = groups[server]
                gateways = []
                for client in clients:
                    gateways.append(clientGatewayAssoc[client.getId()])

                #   dashproducer
                server_params = "--prefix /Node" + str(server.getId()) + " --document-root /home/nfd/data/concatenated/ --data-size 2048 --threads 1"

                #   dashplayer
                client_params = "--name /Node" + str(server.getId()) + "/BBB_ED.mpd -r 12000 -l 500 -a buffer"

                if app_type == "NDN_DemoApps":
                    # NDN_DemoApps(server, clients, start, duration, server_params, client_params, routingcmds)
                    ndn_apps.append(NDN_DemoApps(server, clients, 0.0, 0, server_params, client_params,[]))
                elif app_type == "NDN_DemoAppsWLDR":
                    # NDN_DemoAppsWLDR(server, clients, start, duration, server_params, client_params, routingcmds)
                    ndn_apps.append(NDN_DemoAppsWLDR(server, clients, gateways, 0.0, 0, server_params, client_params, []))
                else:
                    raise ValueError("unknown application type: " + app_type)


            emu.addApplications([ndn_NetworkOverlay, cpuLogging] + ndn_apps)
            emu.start(run)
