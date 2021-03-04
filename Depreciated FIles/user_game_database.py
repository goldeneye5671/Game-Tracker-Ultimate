from user_drive_database import userVerification, createDatabaseConnections
import json
import os
#   [
#       {"userLoggedIn":"boolean_value", "UserAccess":"access_level"},
#       {"name":"drive_name", "gameName":"game_name", "gameSize":"int(gameSize)", "sizeMetric":"gameSizeMetric", "gameTags":"[listOfTags]","dateAdded":"mm/dd/yyyyy","playTime":"YYYY:DD:HH:MM"},
#       ['username','password','email','dir_to_drive_database','dir_to_game_database', int(acclev), int(randid)],
#       int(randID_sentByBrowser)
#   ]

tableName = ''

def addGameToDB(information):
    verified = json.loads(userVerification(information))
    if int(verified["errorcode"])==0:
        databaseConnections = createDatabaseConnections(information)
        gameInformation = list(information[1].values())
        matchingGameInformation = len(list(databaseConnections[1].execute("""SELECT * FROM""")))


#removeGameFromDB()
#retrieveGamesFromDB()
#addUpdateToGame()
#removeUpdateFromGame()
#retrieveAllInfoOnGameInDB()
#addMath()
#subMath()