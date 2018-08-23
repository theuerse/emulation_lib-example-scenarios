from emulation_lib.emulation import Emulation
from emulation_lib.network_blocks.random_static_network_block import RandomStaticNetworkBlock
from emulation_lib.apps.udperf_app import UdperfApp
from emulation_lib.linkcmd_backends.bdl_ import BDL_

emu = Emulation("./config_files/example.config.py", [0, 1])
emu.setLinkCmdBackend(BDL_())
n0 = emu.getNode(0)
n1 = emu.getNode(1)


rsb = RandomStaticNetworkBlock('./blocks/rstatic', 2, 0.15, 1337, [4000, 5000], [1, 5], [0, 0], 1000)
rsb.setNodes([n0, n1])

emu.addNetworkBlocks([rsb])

udperf_app1 = UdperfApp(n0, n1, 0.0, 99, 9000, 6000, 6001)
udperf_app2 = UdperfApp(n1, n0, 0.0, 99, 9000, 6000, 6001)

emu.setDuration(102)

emu.addApplications([udperf_app1, udperf_app2])

emu.setName('simpleRandomStatic')
emu.setOutputDirectory('./results/' + emu.getName())
emu.setNumberOfRuns(3)
emu.setSecondsBetweenRuns(15)

emu.start()
