import account
import os
import filemanager
import config

def main():
	config.init()

	userAccount = account.Account(config.config.get("GMR", "AuthKey"))
	filemanager.FileManager.saveDirectory = config.config.get("GMR", "SaveDir")

	print userAccount.games
	print userAccount.getCurrentTurns()
	userAccount.getCurrentTurns()[0].playTurn(config.config.get("GMR", "AuthKey"))

if __name__ == '__main__':
	main()