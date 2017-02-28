import ConfigParser
import os
from additional import ConfigSectionMap

Config = ConfigParser.ConfigParser()
Config.read("./config/general.ini")

def one():
	print "connect to server\n"
	os.system("ssh %s@%s -p %s"% (user, ip, port))

def two():
	print "22\n"

def three():
	print "3\n"

options = {
  '1' : one,
  '2' : two,
  '3' : three,
}


user = ConfigSectionMap(Config, "Main")['user']
ip = ConfigSectionMap(Config, "Main")['ip']
port = ConfigSectionMap(Config, "Main")['port']


c = raw_input("1: connect to server\n2:\n")
os.system("clear")

options[c]()



