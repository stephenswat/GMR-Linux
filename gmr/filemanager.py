import config

class FileManager:
	@staticmethod
	def saveGame(fileName, data):
		destination = open(config.config.get("GMR", "SaveDir") + fileName, 'wb')
		destination.write(data.read())
		destination.close()

	@staticmethod
	def loadGame(fileName):
		destination = open(config.config.get("GMR", "SaveDir") + fileName, 'r')
		return destination.read()
