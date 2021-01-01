import sqlite3
import json
import os

#The purpose of this file is to provide functionality to add, remove, and modify entries in
#a specific user's database of game drives. The database file will contain many tables. The initial
#table will contain a list of drives and space. The other tables will be the hard drives referenced
#by the first table, and will contain the games installed on the specific drive and how much space they take up,
#as well as what tags are relevent to the game and playtime, if the user wants to encorperate playtime.

tableName = "DriveList"


#Expecting a list that contains 2 objects and a list:
#[{object contains data about user access and if the user is logged in},
# {object contains information about the drive which will be entered into the DB},
# [list that contains the user information for the database (location, accesslevel(although this is redundant), and the user's random access key (although this is also redundant))] ]
def addNewDriveToDatabase(information):
    #Expecting an object. Object layout expected:
    #{name: driveName,
    # numberOfGames: 0(should be zero),
    # totalDriveSize: int(should be greater than 0),
    # driveSizeType: "gb"(stands for the drive size indicater)
    # totalDriveSizeRemaining: int(should be the same as the total drive size),
    # combinedSpaceUsedOnDisk: int(should be 0)}
    # There will be a way to add a drive with games on it in later builds
    userInfo = json.loads(information[0])
    if bool(userInfo["userLoggedIn"]) == True:
        if userInfo["UserAccess"] == "Basic" or userInfo["UserAccess"] == "Advanced" or userInfo["Advanced"]:
            valuesOfDrive = json.loads(information[1])
            connection = sqlite3.connect(information[2][3])
            curs = connection.cursor()
            curs.execute("""CREATE TABLE IF NOT EXISTS """ + tableName + "(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining, combinedSpaceUsedOnDisk)""")
            valuesOfDrive = list(valuesOfDrive.values())
            matchingDrivesAmount = len(list(curs.execute("""SELECT * FROM """ + tableName + " WHERE name = ? AND totalDriveSize = ? AND driveSizeType = ?", (valuesOfDrive[0], valuesOfDrive[2], valuesOfDrive[3]))))
            if matchingDrivesAmount<1:
                curs.execute("""INSERT INTO DriveList(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining) VALUES (?,?,?,?,?)""", (valuesOfDrive[0], int(valuesOfDrive[1]), int(valuesOfDrive[2]), valuesOfDrive[3], int(valuesOfDrive[4])))
                connection.commit()
            else:  
                return '{"errorcode":"-1","desc":"Duplicate detected. To ignore, run with flag --ignore-duplicate"}'
        else:
            return '{"errorcode":"-1", "desc":"User does not have authority to make changes to this db"}'
    else:
        return '{"errorcode":"-1","desc":"User does not appear to be logged in"}'


#def removeDriveFromDB():
#def retrieveDriveFromDB()