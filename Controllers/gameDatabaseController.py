#create a database that stores a user's game information
#retrieve information from a user's game database which could include the names of games, the sizes of games, the tags of games, or all/none of the above
#modify information from a user's game database which could include the names of games, the size of games, the tags of games, or all/none of the above
#remove information from a user's game database which could include one or more game entries at once
#insert information into a user's game database, which could include one or more game entries at once
#delete a user's game database when the user deletes their profile

import json
import os
import __init__
from Engines import JSONStringEngine, databaseCommandEngine
from Controllers import DatabaseController, driveDatabaseController

userLoginInfoTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")
driveDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Drives")
gameDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Games")


#want to support mb, gb, tb
#{
#   name_of_user: user_name
#   name_of_drive: drivename
#   size_of_game: 485.67
#   size_metric: gb
# }

def makeSizeMetricInt(value):
    match value:
        case "mb":
            return 1
        case "gb":
            return 2
        case "tb":
            return 3
        case _:
            return -1


def makeSizeMetricStr(value):
    match value:
        case 1:
            return "mb"
        case 2:
            return "gb"
        case 3:
            return "tb"
        case _:
            return "unknown"

#[
#   100,
#   "gb"
# ]
#converts the smaller size to the bigger size, if there is a smaller
#and bigger size metric
def convert_to_Larger_Value(value1=[], value2=[]):
    value1[1] = makeSizeMetricInt(value1[1])
    value2[1] = makeSizeMetricInt(value2[1])
    if float(value1[1]) > float(value2[1]):
        for i in range(value1[1]-value2[1]):
            value2[0] /= 1000
        value2[1] = value1[1]
    elif float(value1[1]) < float(value2[1]):
        for i in range(value2[1]-value1[1]):
            value1[0]/=1000
        value1[1] = value2[1]
    return [value1, value2]


def is_enough_space(usr, drv, gmeInfo):
    drvInfo = DatabaseController.getRows(driveDatabaseTBLayout, {"DriveName":drv}, usr+".db", ["RemainingSpaceOnDrive", "DriveSizeMetric"])
    if type(drvInfo) == list and len(drvInfo) == 1:
        drvInfo = list(drvInfo[0])
        sameSize = convert_to_Larger_Value([gmeInfo[0], gmeInfo[1]], [float(drvInfo[0]), drvInfo[1]])
        drvInfo = sameSize[1]
        gmeInfo = sameSize[0]
        if gmeInfo[0] > drvInfo[0]:
            return [False, drvInfo[0]-gmeInfo[0]]
        else:
            return [True, drvInfo[0]-gmeInfo[0]]

#print(is_enough_space("Fantasy89", "d1", [900, "gb"]))


#opens game drive database
#opens table that contains the correct drive name
#checks to see if game exists in the database or else returns an error
#inserts a game entry
#saves the modification
#closes the database
def addGame(usr, drv, gameName, gameSize, gameMetric, gameTags, gameAdded, gameTime):
    space = is_enough_space(usr, drv, [gameSize, gameMetric])
    if space[0]:
        gamesOnDriveByName = databaseCommandEngine.retrieve_row(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, {"GameName":gameName}, ["GameName"])
        if type(gamesOnDriveByName) == list and len(gamesOnDriveByName) == 0:
            gameToAdd = {"GameName":gameName, "Size": gameSize, "GameSizeMetric":gameMetric, "GameTags":gameTags, "DateAdded":gameAdded, "PlayTime":gameTime}
            databaseCommandEngine.insert_row(usr+".db",gameDatabaseTBLayout["Database Directory"], drv, gameDatabaseTBLayout["Database Headers"], list(gameToAdd.values()))
            # DatabaseController.modifyRow(usr+".db", driveDatabaseTBLayout, {"RemainingSpaceOnDrive":space[1]},)
            driveDatabaseController.modify_drive(usr+".db", driveDatabaseTBLayout, {"RemainingSpaceOnDrive":space[1]}, {"spot":"DriveName", "AtValue":drv}, ["*"])
        else:
            return {"errorcode":"11", "desc":"Game already exists on drive"}
    else:
        return {"errorcode":"10", "desc":"Not enough space remaining"}

addGame("Fantasy89", "d1", "Bioshock: Infinate", 192, "gb", "", "4-3-2021", 200)
addGame("Fantasy89", "d1", "Crackdown 3", 204, "gb", "", "4-3-2021", 200)
addGame("Fantasy89", "d1", "Anthem", 125, "gb", "", "4-3-2021", 200)
addGame("Fantasy89", "d1", "Star Wars: Battlefront", 230, "gb", "", "4-3-2021", 200)
addGame("Fantasy89", "d1", "Tom Clancy's The Division 2", 120, "gb", "", "4-3-2021", 200)
addGame("Fantasy89", "d1", "Sonic Mania Plus", 900, "mb", "", "4-3-2021", 200)
#871.9 gb
#.8719 tb

#opens the game drive database
#opens table that contains the correct drive name
#uses a select statement to select the desired game (preferably the name)
#saves the retrieved data to a variable
#closes the database
#returns the variable in the desired format
def retrieve_game_on_drive(usr, drv, name):
    return databaseCommandEngine.retrieve_row(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, {"GameName":name}, ["*"])


#opens the game drive database
#opens table that contains the correct drive name
#uses a select statement to select all games on the drive
#saves the retrieved data to a variable
#closes the database
#returns the variable in the desired format
def retrieve_all_games_on_drive(usr, drv):
    return databaseCommandEngine.retrieve_table(usr+".db", gameDatabaseTBLayout["Database Directory"], drv)


#adds an update to a game if there is enough space remaining on a drive
def add_update_to_game(usr, drv, gameName, gameSize, gameMetric):
    space = is_enough_space(usr, drv, [gameSize, gameMetric])
    if space[0]:
        gamesOnDriveByName = databaseCommandEngine.retrieve_row(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, {"GameName":gameName}, ["GameName", "Size", "GameSizeMetric"])
        if type(gamesOnDriveByName) == list and len(gamesOnDriveByName) == 1:
            gamesOnDriveByName = list(gamesOnDriveByName[0])
            gameToUpdate = {}
            if gamesOnDriveByName[2] == gameMetric:
                gameToUpdate = {"GameName":gameName, "Size": gameSize + gamesOnDriveByName[1]}
            else:
                convertToLarger = convert_to_Larger_Value([gameSize, gameMetric],[gamesOnDriveByName[1], gamesOnDriveByName[2]])
                convertToLarger[0][1] = makeSizeMetricStr(convertToLarger[0][1])
                gameToUpdate = {"GameName":gameName, "Size": convertToLarger[0][0]+convertToLarger[1][0], "GameSizeMetric": convertToLarger[0][1]}
            driveToUpdate = {"RemainingSpaceOnDrive": space[1]}
            databaseCommandEngine.update_table_at_spot(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, gameToUpdate, {"spot":"GameName", "AtValue": gameName})
            databaseCommandEngine.update_table_at_spot(usr+".db", driveDatabaseTBLayout["Database Directory"], driveDatabaseTBLayout["Database Tables"][0], driveToUpdate, {"spot":"DriveName","AtValue":drv})
        else:
            return {"errorcode":"12","desc":"game doesn't exist"}
    else:
        return {"errorcode":"13", "desc":"Not enough space"}

print(add_update_to_game("Fantasy89", "d1", "Bioshock: Infinate", 1, "tb"))
print(add_update_to_game("Fantasy89", "d1", "Bioshock: Infinate", 1, "tb"))
print(add_update_to_game("Fantasy89", "d1", "Bioshock: Infinate", 1, "tb"))
print(add_update_to_game("Fantasy89", "d1", "Bioshock: Infinate", 1, "tb"))
print(add_update_to_game("Fantasy89", "d1", "Bioshock: Infinate", 1, "tb"))

#removes an update/content from a game
def remove_content_from_game():
    return None

#Changes the name, playtime, add-date, etc of a game. Will not
#change the storage inforamtion
def update_other_from_game():
    return None


#NOTE: Will need drive name so that it deletes the game from the right drive
#NOTE: Will need game name so that it deletes the game with the correct name
#opens the game drive database
#opens the table that contains the correct drive name
#deletes the game with the name given if exists or else makes no modification
#saves the modification
#closes the database
def remove_game_on_drive():
    
    return None


#opens the game drive database
#deletes the table with the given drive name if exists or else makes no modification
#saves the modification
#closes the database
def remove_drive_table():
    return None

#checks to see if file exists
#deletes the file
def delete_database():
    return None
