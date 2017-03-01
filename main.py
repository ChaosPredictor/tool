import ConfigParser
import os
from additional import ConfigSectionMap

Config = ConfigParser.ConfigParser()
Config.read("./config/general.ini")

def main1():
	print "connect to server\n"
	os.system("ssh %s@%s -p %s"% (user, ip, port))

def main2():
	#print "\n"
	uploadMenu()

def main3():
	print "3\n"

def folder1():
	os.system("scp -r -P %s %s/. %s@%s:~%s"% (port, fromFolder,user, ip, toFolder))
	
def folder2():
	return true

def folder3():
	return true

mainOptions = {
  '1' : main1,
  '2' : main2,
  '3' : main3,
}

uploadOptions = {
	'1' : folder1,
	'2' : folder2,
	'3' : folder3,
}

user = ConfigSectionMap(Config, "Main")['user']
ip = ConfigSectionMap(Config, "Main")['ip']
port = ConfigSectionMap(Config, "Main")['port']
fromFolder = ConfigSectionMap(Config, "Folder")['from']
toFolder = ConfigSectionMap(Config, "Folder")['to']

def main():
	t = raw_input("1: connect to server\n2: upload\n")
	#os.system("clear")
	mainOptions[t]()


def uploadMenu():
	print("\n")	
	t = raw_input("1: folder1\n2: folder2\n")
	os.system("clear")
	uploadOptions[t]()	

main()


