import account
import os
import filemanager
import config

def main():
	config.init()
	
	userAccount = account.Account(config.get("AuthKey"))
	filemanager.FileManager.saveDirectory = config.get("SaveDir")

	print userAccount.games
	print userAccount.getCurrentTurns()
	userAccount.getCurrentTurns()[0].playTurn(config.get("AuthKey"))

if __name__ == '__main__':
	main()