from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.b_ import B_
from emulation_lib.linkcmd_backends.bd_ import BD_
from emulation_lib.linkcmd_backends.bdl_ import BDL_
from emulation_lib.linkcmd_backends.netem_bdl_ import netem_BDL_
from emulation_lib.linkcmd_backends.d_bl import D_BL
from emulation_lib.linkcmd_backends.dl_b import DL_B

cmd_dists = [B_(), BD_(), BDL_(), netem_BDL_(), D_BL(), DL_B()]
emu = Emulation("../example.config.py", [0, 1])
n0 = emu.getNode(0)
n1 = emu.getNode(1)


nb1 = NetworkBlock("./blocks/original_sim_normal")
nb1.selectInterval(1000)
nb1.setNodes([n0, n1])

emu.addNetworkBlocks([nb1])

udperf_app = UdperfApp(n1, n0, 0.0, 110, 7500, 6000, 6001)

n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched" + str(n1.getId()) + ".log_%RUN%")

emu.setDuration(112)

emu.addApplications([udperf_app])
emu.setSecondsBetweenRuns(5)
emu.setNumberOfRuns(1)

for dist in cmd_dists:
    emu.setLinkCmdBackend(dist)
    emu.setName(str(dist))
    emu.setOutputDirectory('./results/original_sim_normal_dists/' + emu.getName())
    emu.start()
