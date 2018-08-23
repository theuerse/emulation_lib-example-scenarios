from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_
from emulation_lib.linkcmd_backends.bdl_2 import BDL_2
from emulation_lib.linkcmd_backends.netem_bdl_ import  netem_BDL_
from emulation_lib.linkcmd_backends.d_bl import D_BL
from emulation_lib.linkcmd_backends.dl_b import DL_B
from emulation_lib.preprocessing.set_constant_value_for_column import SetConstantValueForColumn
import os

emu = Emulation("../example.config.py", [0, 1])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)


blockPaths = ["./blocks/sim2/simple_mobility_802.11A_AdHoc", "./blocks/sim2/simple_mobility_802.11G_AdHoc_Arf",
              "./blocks/sim2/simple_mobility_802.11G_AdHoc_constant",
              "./blocks/sim2/two_nodes_802.11G", "./blocks/sim2/wifi_linearDistanceUDP_deferredStart_udperf",
              "./blocks/sim2/two_nodes_802.11G_unidir"]
nb1 = NetworkBlock(blockPaths[0]) # init nb1
emu.addNetworkBlocks([nb1])

udperf_app = UdperfApp(n1, n0, 0.0, 110, 10000, 6000, 6001)

n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched" + str(n1.getId()) + ".log_%RUN%")

emu.setDuration(112)

emu.addApplications([udperf_app])
emu.setSecondsBetweenRuns(5)
emu.setNumberOfRuns(1)

for bpath in blockPaths:
    # update nb1
    emu.removeNetworkBlocks([nb1])
    nb1 = NetworkBlock(bpath)
    nb1.setNodes([n0, n1])
    nb1.selectInterval(1000)
    nb1.addPreprocessingStep(SetConstantValueForColumn("", 3, 27000.0))
    emu.addNetworkBlocks([nb1])

    emu.setName('multisim_' +os.path.basename(bpath))
    emu.setOutputDirectory('./results/sim2/' + emu.getName())
    emu.start()
