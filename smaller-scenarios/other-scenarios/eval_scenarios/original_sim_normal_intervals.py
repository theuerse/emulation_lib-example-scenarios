from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.d_bl import D_BL

emu = Emulation("../example.config.py", [0, 1])
emu.setLinkCmdBackend(D_BL())
n0 = emu.getNode(0)
n1 = emu.getNode(1)


nb1 = NetworkBlock("./blocks/original_sim_normal")
nb1.setNodes([n0, n1])

emu.addNetworkBlocks([nb1])

udperf_app = UdperfApp(n1, n0, 0.0, 110, 7500, 6000, 6001)

n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched" + str(n1.getId()) + ".log_%RUN%")

emu.setDuration(112)

emu.addApplications([udperf_app])
emu.setSecondsBetweenRuns(5)
emu.setNumberOfRuns(1)

for interval in [1000, 500, 250, 100]:
    nb1.selectInterval(interval)
    emu.setName('original_sim_normal_interval_' + str(interval))
    emu.setOutputDirectory('./results/' + emu.getName())
    emu.start()
