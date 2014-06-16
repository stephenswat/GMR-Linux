import config

class FileManager:
	"""
	A class designed to be used by its static methods. Manages the saving and
	reading of save games.
	"""

	@staticmethod
	def saveGame(fileName, data):
		"""
		Save some raw save game data to the given filename in the configured
		save game directory.
		"""

		destination = open(config.config.get("GMR", "SaveDir") + fileName, 'wb')
		destination.write(data.read())
		destination.close()

	@staticmethod
	def loadGame(fileName):
		"""
		Load the data from a save game and return it to send to the GMR API
		when we submit it.
		"""
		
		destination = open(config.config.get("GMR", "SaveDir") + fileName, 'r')
		return destination.read()
