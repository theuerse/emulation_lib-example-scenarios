from emulation_lib.network_blocks.static_connection import StaticConnection
from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.static_network_block import StaticNetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_

emu = Emulation("./config_files/example.config.py", [0, 1])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)


s1 = StaticConnection(0, 1, 6442.800, 0.001000, 50.00)
s2 = StaticConnection(1, 0, 10983.440, 0.00100, 50.00)
snb = StaticNetworkBlock('./blocks/static', [s1, s2], 1000)
snb.setNodes([n0, n1])

emu.addNetworkBlocks([snb])

udperf_app1 = UdperfApp(n0, n1, 0.0, 99, 9000, 6000, 6001)
udperf_app2 = UdperfApp(n1, n0, 0.0, 99, 9000, 6000, 6001)

emu.setDuration(102)

emu.addApplications([udperf_app1, udperf_app2])

emu.setName('simpleStatic')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(1)
emu.setSecondsBetweenRuns(15)

emu.start()
