import gmr_api
import filemanager
import re
import turn
import config
import gamelistener

from os import system

class Game:
	def __init__(self, gameData):
		self.players  = gameData["Players"]
		self.gameID   = gameData["GameId"]
		self.name     = gameData["Name"]
		self.safeName = self.__getSafeName()
		self.turn     = turn.Turn(gameData["CurrentTurn"])

	def playTurn(self):
		gameData = gmr_api.getSaveData(config.config.get("GMR", "AuthKey"), 
			self.gameID)

		filemanager.FileManager.saveGame(self.safeName + ".Civ5Save", gameData)

		listener = gamelistener.SaveGameUpdateListener(self.safeName, self)
		listener.start()

		if config.config.getboolean("GMR", "StartCiv"):
			print "Starting Civ 5..."
			system("steam -applaunch 8930")

	def submitTurn(self):
		gameData = filemanager.FileManager.loadGame(self.safeName + 
			".Civ5Save")
		gmr_api.submitTurn(config.config.get("GMR", "AuthKey"), 
			self.turn.turnID, gameData)

	def playerHasTurn(self, playerID):
		return self.turn.playerID == playerID

	def __getSafeName(self):
		fileName = re.sub("[^a-zA-Z\d_ ]", "", self.name)
		fileName = re.sub(" ", "_", fileName)
		return fileName

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name