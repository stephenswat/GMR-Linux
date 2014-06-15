import gmrapi
import filemanager
import re
import turn
import config

from os import system

class Game:
	def __init__(self, gameData):
		self.players = gameData["Players"]
		self.gameID  = gameData["GameId"]
		self.name    = gameData["Name"]
		self.turn    = turn.Turn(gameData["CurrentTurn"])

	def playTurn(self, authKey):
		gameData = gmrapi.getSaveData(authKey, self.gameID)

		fileName = re.sub("[^a-zA-Z\d_]", "", self.name)
		fileName = re.sub(" ", "_", fileName)
		filemanager.FileManager.saveGame(fileName + ".Civ5Save", gameData)

		if config.get("StartCiv"):
			print "Starting Civ 5..."
			system("steam -applaunch 8930")

	def playerHasTurn(self, playerID):
		return self.turn.playerID == playerID

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name