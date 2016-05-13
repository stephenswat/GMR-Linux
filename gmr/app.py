import account
import os
import filemanager
import config
import time
import ui

def main():
	"""
	The main function for starting the Giant Multiplayer Robot client for Linux
	which creates the account and then does some fancy stuff with it. Should
	call the user interface later.
	"""

	config.init()

	userAccount = account.Account(config.config.get("GMR", "AuthKey"))
	filemanager.FileManager.saveDirectory = config.config.get("GMR", "SaveDir")

	print 'Your current games are:'
	print userAccount.games

	print 'You have turns for these games:'
	print userAccount.getCurrentTurns()

	for current_turn in userAccount.getCurrentTurns():
		current_turn.playTurn()
		# Probably? waits for the file to change before moving turn. Untested.

	print 'Goodbye.'

if __name__ == '__main__':
	main()
