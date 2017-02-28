import ConfigParser
import os
from additional import ConfigSectionMap

Config = ConfigParser.ConfigParser()
Config.read("./config/general.ini")

def one():
	print "connect to server\n"
	os.system("ssh %s@%s -p %s"% (user, ip, port))

def two():
	print "\n"
	os.system("scp -r -P %s %s/. %s@%s:~%s"% (port, fromFolder,user, ip, toFolder))


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
fromFolder = ConfigSectionMap(Config, "Folder")['from']
toFolder = ConfigSectionMap(Config, "Folder")['to']

c = raw_input("1: connect to server\n2: upload 01\n")
os.system("clear")

options[c]()



