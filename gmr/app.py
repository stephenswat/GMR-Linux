import account
import ConfigParser
import os
import filemanager

configPath = os.path.expanduser("~") + "/.local/share/gmr-linux/"
configName = "gmr.conf"

def main():
	config = ConfigParser.ConfigParser()

	if not os.path.isfile(configPath + configName):
		createConfig(config)

	config.read(configPath + configName)

	userAccount = account.Account(config.get("GMR", "AuthKey"))
	filemanager.FileManager.saveDirectory = config.get("GMR", "SaveDir")

	print userAccount.games
	print userAccount.getCurrentTurns()
	userAccount.getCurrentTurns()[0].playTurn(config.get("GMR", "AuthKey"))

def createConfig(config):
	config.add_section("GMR")
	config.set("GMR", "AuthKey", "")
	config.set("GMR", "SaveDir", os.path.expanduser("~") + "/.local/share/Aspyr/Sid Meier's Civilization 5/Saves/hotseat/")
	config.set("GMR", "UseGUI", True)

	if not os.path.exists(configPath):
		os.makedirs(configPath)

	with open(configPath + configName, 'wb') as configFile:
		config.write(configFile)

if __name__ == '__main__':
	main()