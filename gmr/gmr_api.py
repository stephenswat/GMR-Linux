import requests
import json
import time

apiUrl = "http://multiplayerrobot.com/api/Diplomacy/"

def authenticateUser(authKey):
	arguments = {"authKey": authKey}
	response = __apiQuery("AuthenticateUser", arguments).text

	if response == "null":
		return None
	else:
		return int(response)

def getGames(authKey, playerID):
	arguments = {"authKey": authKey, "playerIDText": playerID}
	response = __apiQuery("GetGamesAndPlayers", arguments).text

	return json.loads(response)

def getSaveData(authKey, gameID):
	arguments = {"authKey": authKey, "gameId": gameID}
	response = __apiQuery("GetLatestSaveFileBytes", arguments, stream = True)

	return response.raw

def submitTurn(authKey, gameID, saveData):
	arguments = {"authKey": authKey, "turnId": gameID}

	url = apiUrl + "SubmitTurn" + "?"

	for arg, val in arguments.items():
		url += (arg + "=" + str(val) + "&")

	print url

	query = requests.post(url, data=saveData)

	if query.status_code == 200:
		return query
	else:
		query.raise_for_status()

def __apiQuery(method, arguments, postdata = None, stream = False, 
	payload = False):
	url = apiUrl + method + "?"

	for arg, val in arguments.items():
		url += (arg + "=" + str(val) + "&")

	query = requests.get(url, stream = stream)

	if query.status_code == 200:
		return query
	else:
		query.raise_for_status()

def convertTime(timeStr):
	timeStruct = time.strptime(timeStr.split(".")[0], "%Y-%m-%dT%H:%M:%S")
	return timeStruct