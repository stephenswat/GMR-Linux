import gmrapi
import filemanager
import re

class Game:
	def __init__(self, account, gameData):
		self.players = gameData["Players"]
		self.gameID  = gameData["GameId"]
		self.name    = gameData["Name"]
		self.turn    = gameData["CurrentTurn"]

	def playTurn(self, authKey):
		gameData = gmrapi.getSaveData(authKey, self.gameID)

		fileName = re.sub("[^a-zA-Z\d_]", "", self.name)
		fileName = re.sub(" ", "_", self.name)
		filemanager.FileManager.saveGame(fileName + ".Civ5Save", gameData)
