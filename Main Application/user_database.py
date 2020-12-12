import sqlite3
import json

#database and initial table creation
initialDatabaseName = "DriveDB"
connection = sqlite3.connect(initialDatabaseName + ".db")
curs = connection.cursor()
curs.execute("""CREATE TABLE IF NOT EXISTS DriveList(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining, combinedSpaceUsedOnDisk)""")

def addNewDriveToDatabase(driveToAdd):
    #Expecting an object. Object layout expected:
    #{name: driveName,
    # numberOfGames: 0(should be zero),
    # totalDriveSize: int(should be greater than 0),
    # driveSizeType: "gb"(stands for the drive size indicater)
    # totalDriveSizeRemaining: int(should be the same as the total drive size),
    # combinedSpaceUsedOnDisk: int(should be 0)}
    # There will be a way to add a drive with games on it in later builds
    valuesOfDrive = driveToAdd.values()
    curs.execute("""INSERT INTO DriveList(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining, combinedSpaceUsedOnDisk) VALUES (?,?,?,?,?)""",
                (valuesOfDrive[0], int(valuesOfDrive[1]), int(valuesOfDrive[2]), valuesOfDrive[3], int(valuesOfDrive[4]), int(valuesOfDrive[5])))


addNewDriveToDatabase({name: "testdrive", numberOfGames: 0, totalDriveSize: 15, driveSizeType: "tb", totalDriveSizeRemaining})