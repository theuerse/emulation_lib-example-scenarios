from emulation_lib.network_blocks.static_connection import StaticConnection
from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.network_block import NetworkBlock
from emulation_lib.network_blocks.static_network_block import StaticNetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_

emu = Emulation("./config_files/example.config.py", [0, 1, 2 ,3])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)
n2 = emu.getNode(2)
n3 = emu.getNode(3)


s0_1 = StaticConnection(0, 1, 6442.800, 0.000724, 0.00)
s1_0 = StaticConnection(1, 0, 10983.440, 0.000632, 0.00)
s0_2 = StaticConnection(0, 2, 6442.800, 0.000724, 0.00)
s2_0 = StaticConnection(2, 0, 10983.440, 0.000632, 0.00)
snb = StaticNetworkBlock('../../emulation/test/static', [s0_1, s1_0, s0_2, s2_0], 1000)
snb.setNodes([n0, n1, n2])

nb1 = NetworkBlock("./blocks/TwoNode_80211a_adhoc")
nb1.setNodes([n1, n3])
nb1.selectInterval(1000)

nb2 = NetworkBlock("./blocks/TwoNode_80211a_adhoc")
nb2.setNodes([n2, n3])
nb2.selectedInterval(1000)

emu.addNetworkBlocks([snb, nb1, nb2])

udperf_app0_1 = UdperfApp(n0, n1, 0.0, 99, 9000, 6000, 6001)
udperf_app1_0 = UdperfApp(n1, n0, 0.0, 99, 9000, 6000, 6001)
udperf_app0_2 = UdperfApp(n0, n2, 0.0, 99, 9000, 6000, 6001)
udperf_app2_0 = UdperfApp(n2, n0, 0.0, 99, 9000, 6000, 6001)
udperf_app1_3 = UdperfApp(n1, n3, 0.0, 99, 9000, 6000, 6001)
udperf_app3_1 = UdperfApp(n3, n1, 0.0, 99, 9000, 6000, 6001)
udperf_app2_3 = UdperfApp(n2, n3, 0.0, 99, 9000, 6000, 6001)
udperf_app3_2 = UdperfApp(n3, n2, 0.0, 99, 9000, 6000, 6001)


emu.setDuration(102)

emu.addApplications([udperf_app0_1, udperf_app1_0, udperf_app0_2, udperf_app2_0, udperf_app1_3, udperf_app3_1,
                     udperf_app2_3, udperf_app3_2])

emu.setName('simpleFourNodeStatic')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(3)
emu.setSecondsBetweenRuns(15)

emu.start()
