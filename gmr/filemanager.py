import config

class FileManager:
	@staticmethod
	def saveGame(fileName, data):
		destination = open(config.get("SaveDir") + fileName, 'wb')
		destination.write(data.read())
		destination.close()

	@staticmethod
	def loadGame(fileName):
		destination = open(config.get("SaveDir") + fileName, 'r')
		return destination.read()
