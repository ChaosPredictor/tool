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
	settingsMenu()

def folder1():
	os.system("scp -r -P %s %s/. %s@%s:~%s"% (port, fromFolder,user, ip, toFolder))
	
def folder2():
	return true

def folder3():
	return true

def updateFolderList():
	t = os.popen("ls -author -S -t -H -LR /home/master/MyWork/freeCodeCamp/01-TributePage/").read()
	#t = os.system("ls /home/master/MyWork/freeCodeCamp/")
	print(t)
	print("update folder list")

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

settingsOptions = {
	'1' : updateFolderList
}

user = ConfigSectionMap(Config, "Main")['user']
ip = ConfigSectionMap(Config, "Main")['ip']
port = ConfigSectionMap(Config, "Main")['port']
fromFolder = ConfigSectionMap(Config, "Folder")['from']
toFolder = ConfigSectionMap(Config, "Folder")['to']

def main():
	t = raw_input("1: connect to server\n2: upload\n3: setings\n")
	os.system("clear")
	mainOptions[t]()


def uploadMenu():
	t = raw_input("1: folder1\n2: folder2\n")
	uploadOptions[t]()	


def settingsMenu():
	t = raw_input("1: update folder list\n")
	settingsOptions[t]()	
	
main()


