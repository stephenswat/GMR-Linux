import requests
from gmrapi import *
from game import *

class Account:
	def __init__(self, authKey):
		self.authKey = authKey
		self.playerID = authenticateUser(authKey)

		if self.playerID == None:
			raise ValueError("Authentication key did not authenticate.")

		self.updateAccount()

	def updateAccount(self):
		response = getGames(self.authKey, self.playerID)

		self.points = response["CurrentTotalPoints"]
		self.name = response["Players"][0]["PersonaName"]

		self.updateGames(response["Games"])

	def updateGames(self, games):
		self.games = []

		for game in games:
			self.games.append(Game(self, game))