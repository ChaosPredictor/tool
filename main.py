import ConfigParser
import os
from additional import ConfigSectionMap

Config = ConfigParser.ConfigParser()
Config.read("./config/general.ini")


user = ConfigSectionMap(Config, "Main")['user']
ip = ConfigSectionMap(Config, "Main")['ip']
port = ConfigSectionMap(Config, "Main")['port']


os.system("ssh %s@%s -p %s"% (user, ip, port))

Config
