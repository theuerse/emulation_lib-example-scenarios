from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.b_ import B_

emu = Emulation("../example.config.py", [0, 1])
emu.setLinkCmdBackend(B_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)


nb1 = NetworkBlock("./blocks/baseline_10Mbps")
nb1.setNodes([n0, n1])
nb1.selectInterval(1000)

emu.addNetworkBlocks([nb1])

udperf_app = UdperfApp(n1, n0, 0.0, 12, 6000, 6000, 6001)

n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched" + str(n1.getId()) + ".log_%RUN%")

emu.setDuration(14)

emu.addApplications([udperf_app])

emu.setName('baseline_10Mbps')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(10)
emu.setSecondsBetweenRuns(5)

emu.start()
