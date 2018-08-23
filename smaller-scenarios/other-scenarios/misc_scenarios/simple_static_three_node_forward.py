from emulation_lib.network_blocks.static_connection import StaticConnection
from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.static_network_block import StaticNetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_

emu = Emulation("./config_files/example.config.py", [0, 1, 2])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)
n2 = emu.getNode(2)

#  n0 <==> n1 <==> n2
# apps            apps


s0_1 = StaticConnection(0, 1, 6442.800, 0.000724, 0.00)
s1_0 = StaticConnection(1, 0, 10983.440, 0.000632, 0.00)
s1_2 = StaticConnection(1, 2, 10983.440, 0.000632, 0.00)
s2_1 = StaticConnection(2, 1, 6442.800, 0.000724, 0.00)
snb = StaticNetworkBlock('./blocks/static3', [s0_1, s1_0, s1_2, s2_1], 1000)
snb.setNodes([n0, n1, n2])

emu.addNetworkBlocks([snb])

udperf_app1 = UdperfApp(n0, n2, 0.0, 99, 9000, 6000, 6001)
udperf_app2 = UdperfApp(n2, n0, 0.0, 99, 9000, 6000, 6001)

staticRoutes = [(0, 2, 1), (2, 0, 1)]
emu.setStaticRoutes(staticRoutes)

emu.setDuration(102)

emu.addApplications([udperf_app1, udperf_app2])

emu.setName('simpleStaticThreeNodeForward')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(3)
emu.setSecondsBetweenRuns(15)

emu.start()
