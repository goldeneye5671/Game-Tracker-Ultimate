import sqlite3
import json
import os

#The purpose of this file is to provide functionality to add, remove, and modify entries in
#a specific user's database of game drives. The database file will contain many tables. The initial
#table will contain a list of drives and space. The other tables will be the hard drives referenced
#by the first table, and will contain the games installed on the specific drive and how much space they take up,
#as well as what tags are relevent to the game and playtime, if the user wants to encorperate playtime.


#database and initial table creation for testing
def addNewDriveToDatabase(driveToAdd, locationOfUserDatabase, authorityToAdd):
    #Expecting an object. Object layout expected:
    #{name: driveName,
    # numberOfGames: 0(should be zero),
    # totalDriveSize: int(should be greater than 0),
    # driveSizeType: "gb"(stands for the drive size indicater)
    # totalDriveSizeRemaining: int(should be the same as the total drive size),
    # combinedSpaceUsedOnDisk: int(should be 0)}
    # There will be a way to add a drive with games on it in later builds
    connection = sqlite3.connect(locationOfUserDatabase)
    curs = connection.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS DriveList(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining, combinedSpaceUsedOnDisk)""")
    valuesOfDrive = json.loads(driveToAdd)
    valuesOfDrive = list(valuesOfDrive.values())
    curs.execute("""INSERT INTO DriveList(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining) VALUES (?,?,?,?,?)""", (valuesOfDrive[0], int(valuesOfDrive[1]), int(valuesOfDrive[2]), valuesOfDrive[3], int(valuesOfDrive[4])))
    connection.commit()