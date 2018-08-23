from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.b_ import B_
#    ==> n0
#   |^|
#   n1
#   |v|
#    ==> n2

emu = Emulation("../example.config.py", [0, 1, 2])
emu.setLinkCmdBackend(B_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)
n2 = emu.getNode(2)


nb1 = NetworkBlock("./blocks/symmetric")
nb1.setNodes([n0, n1])
nb1.selectInterval(1000)

nb2 = NetworkBlock("./blocks/symmetric")
nb2.setNodes([n2, n1])
nb2.selectInterval(1000)

emu.addNetworkBlocks([nb1, nb2])

udperf_app0 = UdperfApp(n1, n0, 0.0, 12, 6000, 6000, 6001)
udperf_app2 = UdperfApp(n1, n2, 0.0, 12, 6000, 6000, 6002)  # own-Ports must be unique on the same node!

n1.addUserResult("/home/nfd/cmdScheduler.log", "cmdSched" + str(n1.getId()) + ".log_%RUN%")

emu.setDuration(14)

emu.addApplications([udperf_app0, udperf_app2])

emu.setName('symmetric_twoFlows')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(10)
emu.setSecondsBetweenRuns(5)

emu.start()
