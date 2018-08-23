import os
from emulation_lib import constants
from emulation_lib.apps import application

class IperfLogApp(application.Application):
    def __init__(self, server, client, client_runtime, client_bandwidth):
        self.server = server
        self.client = client
        self.bandwidth = client_bandwidth
        self.runtime = client_runtime

    def generateCommands(self, config):
        server_ip = self.server.getEmuIP(config)
        client_ip = self.client.getEmuIP(config)
        server_logfilepath =  os.path.join(config['REMOTE_RESULT_DIR'], "server.log")
        client_logfilepath = os.path.join(config['REMOTE_RESULT_DIR'], "client.log")
        kill_cmd = "pkill -KILL iperf"

        # ensure iperf server/client is stopped
        self.server.scheduleCmd(constants.SETUP_TIME, kill_cmd)
        self.client.scheduleCmd(constants.SETUP_TIME, kill_cmd)

        # start a new server instance
        self.server.scheduleCmd(constants.SETUP_TIME, "(sudo chrt -o -p 0 $BASHPID && iperf -s -i 1 -u > " + server_logfilepath + " 2>&1 &)")

        # start a new client instance at the beginning of the emulation
        client_cmd = "(sudo chrt -o -p 0 $BASHPID && iperf -c " + server_ip + " -i 1 -u -b " + str(self.bandwidth) + "M -t " + \
                     str(self.runtime) + " > " + client_logfilepath + " 2>&1 &)"
        self.client.scheduleCmd(0,client_cmd)

        # explicitly stop after client should have finished
        self.server.scheduleCmd(float(config["EMU_DURATION"]), kill_cmd)
        self.client.scheduleCmd(float(config["EMU_DURATION"]), kill_cmd)

        # add result files to be collected from the nodes
        self.server.addAppResult(server_logfilepath,
                                 os.path.join(config['RESULT_DIR'], server_ip + ".server.log_%RUN%"))
        self.client.addAppResult(client_logfilepath,
                                 os.path.join(config['RESULT_DIR'], client_ip + ".client.log_%RUN%"))