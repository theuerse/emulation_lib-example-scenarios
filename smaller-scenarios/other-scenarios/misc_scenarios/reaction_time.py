from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_

emu = Emulation("./config_files/example.config.py", [0, 1])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)


nb1 = NetworkBlock("./blocks/profile1")
nb1.setNodes([n0, n1])
nb1.selectInterval(1000)

emu.addNetworkBlocks([nb1])

udperf_app1 = UdperfApp(n0, n1, 0.0, 19, 3000, 6000, 6001)
udperf_app2 = UdperfApp(n1, n0, 0.0, 19, 3000, 6000, 6001)

n0.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched0.log_%RUN%")
n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched1.log_%RUN%")

emu.setDuration(20)

emu.addApplications([udperf_app1, udperf_app2])

emu.setName('reactionTime')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(3)
emu.setSecondsBetweenRuns(15)

emu.start()
