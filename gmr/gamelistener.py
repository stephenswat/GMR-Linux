import threading
import time
import config
import os

class SaveGameUpdateListener(threading.Thread):
	def __init__(self, saveName, turn):
		threading.Thread.__init__(self)
		print "Creating listener for " + str(saveName)
		self.savePath = config.config.get("GMR", "SaveDir") + saveName + ".Civ5Save"
		self.timeZero = time.ctime(os.path.getmtime(self.savePath))
		self.turn = turn

	def run(self):
		print "Starting listener for " + str(self.savePath)

		while time.ctime(os.path.getmtime(self.savePath)) == self.timeZero:
			time.sleep(2)

		print "File changed!"

		self.turn.submitTurn()