import account
import os
import filemanager
import config
import time

def main():
	"""
	The main function for starting the Giant Multiplayer Robot client for Linux
	which creates the account and then does some fancy stuff with it. Should
	call the user interface later.
	"""

	config.init()

	userAccount = account.Account(config.config.get("GMR", "AuthKey"))
	filemanager.FileManager.saveDirectory = config.config.get("GMR", "SaveDir")

	print userAccount.games
	print userAccount.getCurrentTurns()
	userAccount.getCurrentTurns()[0].playTurn()
	time.sleep(500)

if __name__ == '__main__':
	main()
