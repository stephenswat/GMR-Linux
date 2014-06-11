class FileManager:
	saveDirectory = ""

	@staticmethod
	def saveGame(fileName, data):
		destination = open(FileManager.saveDirectory + fileName, 'wb')
		destination.write(data.read())
		destination.close()

	@staticmethod
	def loadGame(fileName):
		destination = open(FileManager.saveDirectory + fileName, 'r')
		return destination.read()