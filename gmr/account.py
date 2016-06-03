import requests
import gmr_api
import game
import time

class Account:
	"""
	This class represents an account on Giant Multiplayer Robot. It contains a
	player ID, an authentication key and a list of games which is to be
	constantly updated.
	"""

	def __init__(self, config):
		"""
		Creates an account object. Takes an authentication key which is used to
		authenticate the user.
		"""

		self.config = config
		self.authKey = config.config.get("GMR", "AuthKey")
		self.playerID = gmr_api.authenticateUser(self.authKey)
		self.games = []

		if self.playerID == None:
			raise ValueError("Authentication key did not authenticate.")

		self.updateAccount()

	def updateAccount(self):
		"""
		Updates an account. For now, this only updates the list of games from
		the GMR API. Only query server once every 15 seconds.
		"""
		lastcheck = self.config.config.get("GMR", "LastCheck")
		elapsed = time.time() - float(lastcheck);
		if elapsed > 15:
			response = gmr_api.getGames(self.authKey, self.playerID)

			self.points = response["CurrentTotalPoints"]
			self.name = response["Players"][0]["PersonaName"]

			self.updateGames(response["Games"])
			self.config.set("LastCheck", time.time())
		else:
			print "Last update only " + str(int(elapsed)) + " seconds ago."

	def updateGames(self, games):
		"""
		Creates Game objects from the given array and store them in the account
		object.
		"""

		self.games = []

		for gmrGame in games:
			self.games.append(game.Game(gmrGame))

	def getCurrentTurns(self):
		"""
		Get a list of turns in which this account currently has a turn.
		"""

		currentTurns = []

		for gmrGame in self.games:
			if gmrGame.playerHasTurn(self.playerID):
				currentTurns.append(gmrGame)

		return currentTurns
