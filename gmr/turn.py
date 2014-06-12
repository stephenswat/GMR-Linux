import gmr_time

class Turn:
	def __init__(self, turnData):
		self.turnID       = turnData['TurnId']
		self.started      = gmr_time.convertTime(turnData['Started'])
		self.playerID     = turnData['UserId']
		self.number       = turnData['Number']
		self.firstTurn    = turnData['IsFirstTurn']
		self.playerNumber = turnData['PlayerNumber']

		if turnData['Expires'] == None:
			self.expires = None
		else:
			self.expires = gmr_time.convertTime(turnData['Expires'])

