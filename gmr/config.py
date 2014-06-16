import ConfigParser
import os

configPath = os.path.expanduser("~") + "/.local/share/gmr-linux/"
configName = "gmr.conf"

config = ConfigParser.ConfigParser()

def init():
	"""
	Initialize the configuration. Check if it exits, create it if not, the read
	it.
	"""

	if not os.path.isfile(configPath + configName):
		createConfig(config)

	config.read(configPath + configName)

def set(key, value):
	"""
	Set a key-value pair in the configuration and the write that pair to the
	config file immediately.
	"""

	config.set("GMR", key, value)
	with open(configPath + configName, 'wb') as configFile:
		config.write(configFile)

def createConfig(config):
	"""
	First time config creation. This creates some initial key-value pairs and
	also creates the file.
	"""

	config.add_section("GMR")
	config.set("GMR", "AuthKey", "")
	config.set("GMR", "SaveDir", os.path.expanduser("~") + "/.local/share/Aspyr/Sid Meier's Civilization 5/Saves/hotseat/")
	config.set("GMR", "StartCiv", True)

	if not os.path.exists(configPath):
		os.makedirs(configPath)

	with open(configPath + configName, 'wb') as configFile:
		config.write(configFile)
