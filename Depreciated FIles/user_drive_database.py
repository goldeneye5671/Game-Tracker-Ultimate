import sqlite3
import database_string_creater
import json
import os

#   The purpose of this file is to provide functionality to add, remove, and modify entries in a
#   specific user's database of hard drives. Each entry in the database will represent a hard drive.
#   The data in the hard drive entry will represent the following:
#       ~Name of the hard drive
#       ~Number of games on the hard drive (NOT INCLUDING GAME UPDATES)
#       ~Capacity of the hard drive (Otherwise referred to as the totalSize, EX: My hard drive is a 15TB Hard drive (15TB being the totalSize))
#       ~Current size of the hard drive (Referred to as the totalDriveSizeRemaining)
#       ~Size metrics of the hard drive (TB, GB, ETC.)
#   
#   Other table headers may be added in the future. The most imidiate being the total size of all of the games on the hard drive, to make it easier
#   to calculate the amount of space remaining.
#
#   NOTE: All functions contain an information arg. The following is the bare minimum each information arg is supposed to contain:
#   
#   ALL FUNCTIONS MUST CONTAIN THE AT LEAST THESE VARIABLES IN A LIST IN A JSON STRING:
#   [
#       {"userLoggedIn":"boolean_value", "UserAccess":"access_level"},
#       {"name":"drive_name"},
#       ['username','password','email','dir_to_drive_database','dir_to_game_database', int(acclev), int(randid)],
#       int(randID_sentByBrowser)
#   ]
#   NOTE: THE addNewDriveToDB(information) is the only function that requires more information:
#    [
#       {"userLoggedIn":"boolean_value", "UserAccess":"access_level"},
#       {"name":"drive_name", "numberOfGames":int(), "totalDriveSize":int(), "driveSizeType":"str()", "totalDriveSizeRemaining":"int()"},
#       ['username','password','email','dir_to_drive_database','dir_to_game_database', int(acclev), int(randid)],
#       int(randID_sentByBrowser)
#   ]

tableName = "DriveList"
driveTableHeaders = ['name', 'numberOfGames', 'totalDriveSize', 'driveSizeType', 'totalDriveSizeRemaining']
gameTableHeaders = ['name', 'gameName', 'gameSize', 'sizeMetric', 'gameTags', 'dateAdded', 'playTime']

#   helper function for all other functions. Expects the same argument information that is given to the function that this function helps.
#   Will verify that the user requesting to modify the drive database is actually that user, and that
#   said user is acutally logged in.
#   
#   A positive return value (errorcode: 0, desc: true) requires the following criteria:
#       ~The userLoggedIn variable is set to true and if the user's random id matches what the browser sends as the user's random id
#       ~The userAccess variable is set to either basic, advanced, or root.
#   A negative return value (errorcode: -1, desc: *insert description here*) is sent if the above criteria are not met.
def userVerification(information):
    userInfo = json.loads(information[0])
    if userInfo["userLoggedIn"] == True and information[2][6] in information:
        if userInfo["UserAccess"] == "Basic" or userInfo["UserAccess"] == "Advanced" or userInfo["UserAccess"] == "ROOT":
            return json.dumps({"errorcode":0, "desc":None})
        else:
            return json.dumps({"errorcode":-1, "desc":"User does not have authority to make changes to this db"})
    else:
        return json.dumps({"errorcode":-1,"desc":"User does not appear to be logged in"})


#   helper function for all other functions. Expects the information that is given to said function. The only purpose of
#   this function is to return a connection and cursor to a database specified in the arguments. The only databases that
#   should be connected to in this program are in the /Database Files/userDriveInfo/ directory.
def createDatabaseConnections(information, locationX, locationY):
    connection = sqlite3.connect(information[locationX][locationY]) #2, 3
    curs = connection.cursor()
    return [connection, curs]



#   function that will add hard drive information to a user's DriveInfo database. It has the following dependancies:
#       ~userVerification(information)  -   For verifying that a user can access the specified database
#       ~createDatabaseConnections(information) -   For creating a connection to the database given in the args
def addNewDriveToDatabase(information):
    verified = json.loads(userVerification(information))
    
    if int(verified["errorcode"]) == 0:
        
        driveDatabaseInformation = createDatabaseConnections(information, 2, 3)
        gameDatabaseInformation = createDatabaseConnections(information, 2, 4)
        
        valuesOfDrive = json.loads(information[1])
        valuesOfDrive = list(valuesOfDrive.values())
        
        matchingDrivesAmount = len(list(driveDatabaseInformation[1].execute("""SELECT * FROM """ + tableName + " WHERE name = ? AND totalDriveSize = ? AND driveSizeType = ?", (valuesOfDrive[0], valuesOfDrive[2], valuesOfDrive[3]))))
        
        if matchingDrivesAmount<1:
            driveDatabaseInformation[1].execute(database_string_creater.insert_into_table(tableName, driveTableHeaders), (valuesOfDrive[0], int(valuesOfDrive[1]), int(valuesOfDrive[2]), valuesOfDrive[3], int(valuesOfDrive[4])))
            gameDatabaseInformation[1].execute(database_string_creater.create_table(tableName, gameTableHeaders))
        
            driveDatabaseInformation[0].commit()
        
            driveDatabaseInformation[0].close()
        else:  
        
            return json.dumps({"errorcode":-1,"desc":"Duplicate detected. To ignore, run with flag --ignore-duplicate"})
        
        driveDatabaseInformation[0].close()
    else:
        
        return json.dumps(verified)


#   function that will remove hard drive information from a user's DriveInfo database. It has the following dependancies:
#       ~userVerification(information)  -   For verifying that a user can access the specified database
#       ~createDatabaseConnections(information) -   For creating a connection to the database given in the args
# TODO: NEED TO DELETE TABLE THAT CONTAINS DRIVE NAME
def removeDriveFromDB(information):
    verified = json.loads(userVerification(information))
    if int(verified["errorcode"]) == 0:
        driveToRemove = json.loads(information[1])["name"]
        databaseInformation = createDatabaseConnections(information, 2, 3)
        #note for the future:
        #This command will get the table names in a database. It's needed because a check needs to see if the table exists before any action is performed
        tablesInDB = list(databaseInformation[1].execute("""SELECT name FROM 'sqlite_master' WHERE type='table'""").fetchall()[0])
        if 0<len(tablesInDB)<2:
            allMatchingDrivesInDB = databaseInformation[1].execute("""SELECT * FROM """ + tableName + """ WHERE name = ?""", (driveToRemove,)).fetchall()
            if 0<len(allMatchingDrivesInDB)<2:
                databaseInformation[1].execute("DELETE FROM " + tableName + " WHERE name = ?", (driveToRemove,))
                databaseInformation[0].commit()
                databaseInformation[0].close()
            else:
                return json.dumps({"errorcode":-1,"desc":"No drive in database that exists with given name"})
        elif len(tablesInDB) == 0:
            return json.dumps({"errorcode":-1,"desc":"The database for the hard drives doesn\'t exist."})
        elif len(tablesInDB) >= 2:
            return json.dumps({"errorcode":-1,"desc":"The database has a duplicate tables"})
        databaseInformation[0].close()
    else:
        json.dumps(verified)
    return json.dumps({"message":"Removal of drive was successful"})


#   function that will retrieve all of the hard drives in the database that match a given criteria specified by the args. It has the following dependancies:
#       ~userVerification(information)  -   For verifying that a user can access the specified database
#       ~createDatabaseConnections(information) -   For creating a connection to the database given in the args
def retrieveDriveFromDB(information):
    verified = json.loads(userVerification(information))
    if int(verified["errorcode"]) == 0:
        databaseInformation = createDatabaseConnections(information, 2, 3)
        driveToRetrieve = json.loads(information[1])["name"]
        tablesInDB = list(databaseInformation[1].execute("""SELECT name FROM 'sqlite_master' WHERE type='table'""").fetchall()[0])         
        if len(tablesInDB)<2 and len(tablesInDB) >0:
            allMatchingDrivesInDB = databaseInformation[1].execute("""SELECT * FROM """ + tableName + """ WHERE name = ?""", (driveToRetrieve,)).fetchall()                
            if len(allMatchingDrivesInDB) > 0:
                propsOfDrive = list(allMatchingDrivesInDB[0])
                return json.dumps({"name":propsOfDrive[0], "numberOfGames":propsOfDrive[1], "totalDriveSizeRemaining":propsOfDrive[2], "driveSizeType":propsOfDrive[3], "combinedSpaceUsedOnDrive":propsOfDrive[4]})
            else:
                return json.dumps({"errorcode":-1,"desc":"The database does not contain the drive " + driveToRetrieve})
        elif len(tablesInDB) == 0:
            return json.dumps({"errorcode":"-1","desc":"The database for the hard drives doesn\'t exist."})
        elif len(tablesInDB) >= 2:
            return json.dumps({"errorcode":"-1","desc":"The database has a duplicate tables"})
        databaseInformation[0].close()
    else:
        return json.dumps(verified)