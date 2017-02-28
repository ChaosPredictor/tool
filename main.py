import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("./config/general.ini")


print(Config.sections())
