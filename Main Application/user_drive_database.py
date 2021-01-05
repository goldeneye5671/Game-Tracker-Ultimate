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
    userInfo = json.loads(information[0])
    if userInfo["userLoggedIn"] == True:
        if userInfo["UserAccess"] == "Basic" or userInfo["UserAccess"] == "Advanced" or userInfo["UserAccess"] == "ROOT":
            valuesOfDrive = json.loads(information[1])
            connection = sqlite3.connect(information[2][3])
            curs = connection.cursor()
            curs.execute("""CREATE TABLE IF NOT EXISTS """ + tableName + "(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining, combinedSpaceUsedOnDisk)""")
            valuesOfDrive = list(valuesOfDrive.values())
            matchingDrivesAmount = len(list(curs.execute("""SELECT * FROM """ + tableName + " WHERE name = ? AND totalDriveSize = ? AND driveSizeType = ?", (valuesOfDrive[0], valuesOfDrive[2], valuesOfDrive[3]))))
            if matchingDrivesAmount<1:
                curs.execute("""INSERT INTO DriveList(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining) VALUES (?,?,?,?,?)""", (valuesOfDrive[0], int(valuesOfDrive[1]), int(valuesOfDrive[2]), valuesOfDrive[3], int(valuesOfDrive[4])))
                connection.commit()
                connection.close()
            else:  
                return json.dumps({"errorcode":"-1","desc":"Duplicate detected. To ignore, run with flag --ignore-duplicate"})
        else:
            return json.dumps({"errorcode":"-1", "desc":"User does not have authority to make changes to this db"})
    else:
        return json.dumps({"errorcode":"-1","desc":"User does not appear to be logged in"})
    return json.dumps({"message":"Addition of drive was successful"})


#Expecting a list that contains 2 objects and a list:
#[{object contains data about user access and if the user is logged in},
# {object contains name of the drive to be deleted from the database},
# [list that contains the user information for the database (location, accesslevel(although this is redundant), and the user's random access key (although this is also redundant))],
# randomIdentifier sent by the browser
#  ]
def removeDriveFromDB(information):
    userInfo = json.loads(information[0])
    if bool(userInfo["userLoggedIn"]) == True and information[2][6] in information:
        if userInfo["UserAccess"] == "Basic" or userInfo["UserAccess"] == "Advanced" or userInfo["UserAccess"]=="ROOT":
            driveToRemove = json.loads(information[1])["name"]
            connection = sqlite3.connect(information[2][3])
            curs = connection.cursor()
            #note for the future:
            #This command will get the table names in a database. It's needed because a check needs to see if the table exists before any action is performed
            tablesInDB = list(curs.execute("""SELECT name FROM 'sqlite_master' WHERE type='table'""").fetchall()[0])
            if 0<len(tablesInDB)<2:
                allMatchingDrivesInDB = curs.execute("""SELECT * FROM """ + tableName + """ WHERE name = ?""", (driveToRemove,)).fetchall()
                if 0<len(allMatchingDrivesInDB)<2:
                    curs.execute("DELETE FROM " + tableName + " WHERE name = ?", (driveToRemove,))
                    connection.commit()
                    connection.close()
                else:
                    return json.dumps({"errorcode":"-1","desc":"No drive in database that exists with given name"})
            elif len(tablesInDB) == 0:
                return json.dumps({"errorcode":"-1","desc":"The database for the hard drives doesn\'t exist."})
            elif len(tablesInDB) >= 2:
                return json.dumps({"errorcode":"-1","desc":"The database has a duplicate tables"})
        else:
            return json.dumps({"errorcode":"-1","desc":"The user does not have the privligaes to make changes"})
    else:
        return json.dumps({"errorcode":"-1","desc":"The person trying to make changes is not logged in"})
    return json.dumps({"message":"Removal of drive was successful"})

#Expecting a list that contains 2 objects and a list:
#[{object contains data about user access and if the user is logged in},
# {object contains name of the drive to be retrieved from the database},
# [list that contains the user information for the database (location, accesslevel(although this is redundant), and the user's random access key (although this is also redundant))] ]
def retrieveDriveFromDB(information):
    userInfo = json.loads(information[0])
    
    if bool(userInfo["userLoggedIn"]) == True:
        if userInfo["UserAccess"] == "Advanced" or userInfo["UserAccess"]=="ROOT":
            driveToRetrieve = json.loads(information[1])["name"]
            connection = sqlite3.connect(information[2][3])
            curs = connection.cursor()
            tablesInDB = list(curs.execute("""SELECT name FROM 'sqlite_master' WHERE type='table'""").fetchall()[0])
            
            if len(tablesInDB)<2 and len(tablesInDB) >0:
                allMatchingDrivesInDB = curs.execute("""SELECT * FROM """ + tableName + """ WHERE name = ?""", (driveToRetrieve,)).fetchall()
                
                if len(allMatchingDrivesInDB) > 0:
                    propsOfDrive = list(allMatchingDrivesInDB[0])
                    return json.dumps({"name":propsOfDrive[0], "numberOfGames":propsOfDrive[1], "totalDriveSizeRemaining":propsOfDrive[2], "driveSizeType":propsOfDrive[3], "combinedSpaceUsedOnDrive":propsOfDrive[4]})
                else:
                    return json.dumps({"errorcode":-1,"desc":"The database does not contain the drive " + driveToRetrieve})
            elif len(tablesInDB) == 0:
                 return json.dumps({"errorcode":"-1","desc":"The database for the hard drives doesn\'t exist."})
            elif len(tablesInDB) >= 2:
                 return json.dumps({"errorcode":"-1","desc":"The database has a duplicate tables"})
        else:
            return json.dumps({"errorcode":"-1","desc":"The user does not have the privligaes to make changes"})
    else:
        return json.dumps({"errorcode":"-1","desc":"The person trying to make changes is not logged in"})
    