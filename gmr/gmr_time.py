import time

def convertTime(timeStr):
	timeStruct = time.strptime(timeStr.split(".")[0], "%Y-%m-%dT%H:%M:%S")
	return timeStruct