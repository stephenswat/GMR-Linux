import ConfigParser
import os

configPath = os.path.expanduser("~") + "/.local/share/gmr-linux/"
configName = "gmr.conf"

global config 
config = ConfigParser.ConfigParser()

def init():
	if not os.path.isfile(configPath + configName):
		createConfig(config)

	config.read(configPath + configName)

def get(key):
	return config.get("GMR", key)

def set(key, value):
	config.set("GMR", key, value)
	with open(configPath + configName, 'wb') as configFile:
		config.write(configFile)

def createConfig(config):
	config.add_section("GMR")
	config.set("GMR", "AuthKey", "")
	config.set("GMR", "SaveDir", os.path.expanduser("~") + "/.local/share/Aspyr/Sid Meier's Civilization 5/Saves/hotseat/")
	config.set("GMR", "StartCiv", True)

	if not os.path.exists(configPath):
		os.makedirs(configPath)

	with open(configPath + configName, 'wb') as configFile:
		config.write(configFile)
