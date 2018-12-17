
import ConfigParser

def get_command_from_config(nodename, commandsection):
    config = ConfigParser.ConfigParser()
    config.read('/etc/clustershell/ugent.ini')
    cmd = config.get(commandsection, nodename)
    return cmd

