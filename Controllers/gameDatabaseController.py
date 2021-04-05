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
def is_enough_space(usr, drv, gameSize, gameMetric):
    driveSizeMetrics = []
    driveSize = DatabaseController.getRows(driveDatabaseTBLayout, {"DriveName":drv}, usr+".db", ["RemainingSpaceOnDrive", "DriveSizeMetric"])
    if type(driveSize) == list and len(driveSize) == 1:
        driveSize = list(driveSize[0])
        match gameMetric:
            case "mb":
                driveSizeMetrics.append(1)
            case "gb":
                driveSizeMetrics.append(2)
            case "tb":
                driveSizeMetrics.append(3)
            case _:
                driveSizeMetric.append(-1)
        match driveSize[1]:
            case "mb":
                driveSizeMetrics.append(1)
            case "gb":
                driveSizeMetrics.append(2)
            case "tb":
                driveSizeMetrics.append(3)
            case _:
                driveSizeMetric.append(-1)
        #givenToMe              database
    conversionVal = None
    
    if driveSizeMetrics[0] < driveSizeMetrics[1]:
        conversionVal = gameSize
        if driveSizeMetrics[1]-driveSizeMetrics[0] > 1:
        #to convert, either devide by or multiply by 1,000
            for i in range(driveSizeMetrics[1]-driveSizeMetrics[0]):
                conversionVal/=1000
                conversionVal = float(driveSize[0])-conversionVal
            return [conversionVal > 0, conversionVal]
        else:
            conversionVal/=1000
            conversionVal = float(driveSize[0]) - conversionVal
            return [conversionVal > 0, conversionVal]
    #if the game has a larger size metric that would mean that the game is bigger than the drive
    elif driveSizeMetrics[0] > driveSizeMetrics[1]:
        return [False, -1]
    else:
        if gameSize > float(driveSize[0]):
            return [False, -1]
        else:
            return [float(driveSize[0])-gameSize > 0, conversionVal]
#print(is_enough_space("Fantasy89", "d1", 900, "gb"))


#opens game drive database
#opens table that contains the correct drive name
#checks to see if game exists in the database or else returns an error
#inserts a game entry
#saves the modification
#closes the database
def addGame(usr, drv, name, size, metric, tags, added, time):
    space = is_enough_space(usr, drv, size, metric)
    if space[0]:
        gamesOnDriveByName = databaseCommandEngine.retrieve_row(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, {"GameName":name}, ["GameName"])
        if type(gamesOnDriveByName) == list and len(gamesOnDriveByName) == 0:
            gameToAdd = {"GameName":name, "Size": size, "GameSizeMetric":metric, "GameTags":tags, "DateAdded":added, "PlayTime":time}
            databaseCommandEngine.insert_row(usr+".db",gameDatabaseTBLayout["Database Directory"], drv, gameDatabaseTBLayout["Database Headers"], list(gameToAdd.values()))
            # DatabaseController.modifyRow(usr+".db", driveDatabaseTBLayout, {"RemainingSpaceOnDrive":space[1]},)
            driveDatabaseController.modify_drive(usr+".db", driveDatabaseTBLayout, {"RemainingSpaceOnDrive":space[1]}, {"spot":"DriveName", "AtValue":drv}, ["*"])
        else:
            return {"errorcode":"11", "desc":"Game already exists on drive"}
    else:
        return {"errorcode":"10", "desc":"Not enough space remaining"}

addGame("Fantasy89", "d1", "Bioshock: Infinate", 192, "gb", "", "4-3-2021", 200)


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


#opens the game drive database
#opens table that contains the correct drive name
#uses a select statement to select the game entry to modify or else makes no modification if game doesn't exist
#saves the retrieved data to a variable
#deletes the old entry
#modifies the retrieved entry
#inserts the modified entry to the table with the correct drive name
#saves the modification
#closes the database

#Expected layout for adding more data to a game or subtracting data
#{
#   Size:20,
#   GameSizeMetric:gb
# }
#Expected layout for everythine else shouldn't matter as much
#{
#   GameName: newGameName,
#   GameTags: newGameTags,
#   DateAdded: 18-04-2021
#   Playtime: newplaytime
# }
#Can't change the size metric because that would require conversion
#To change the size metric, the user will have to delete the game and
#add the game again using the size metric they want
def modify_game_on_drive(usr, drv, name, updatedValues_Dict, spot, action):
    matchingGames = retrieve_game_on_drive(usr, drv, name)
    if type(matchingGames) == list and len(matchingGames) == 1:
        matchingGames = list(matchingGames[0])
        match action:
            case "+":
                space = is_enough_space(usr, drv, updatedValues_Dict["Size"], updatedValues_Dict["GameSizeMetric"])
                if space[0] and matchingGames[2] == updatedValues_Dict["GameSizeMetric"]:
                    updatedValues_Dict["Size"] = matchingGames[1] + updatedValues_Dict["Size"]
                    databaseCommandEngine.update_table_at_spot(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, updatedValues_Dict, {"spot":"GameName", "AtValue": name})
                    databaseCommandEngine.update_table_at_spot(usr+".db", driveDatabaseTBLayout["Database Directory"],driveDatabaseTBLayout["Database Tables"][0], {"RemainingSpaceOnDrive":space[1]}, {"spot":"DriveName", "AtValue":drv})
                    # driveDatabaseController.modify_drive()
                    return space[1]
            case "-":
                if updatedValues_Dict["GameSizeMetric"] ==matchingGames[2]:
                    updatedValues_Dict["Size"] = matchingGames[1] + updatedValues_Dict["Size"]
                    databaseCommandEngine.update_table_at_spot(usr+".db", gameDatabaseTBLayout["Database Directory"], drv, updatedValues_Dict, {"spot": "GameName", "AtValue":name})
                    driveSizeMetric = driveDatabaseController.retrieve_drives(usr+".db", driveDatabaseTBLayout, {"DriveName": drv}, ["DriveSizeMetric"])[0]
                    if driveSizeMetric[0] == matchingGames[2]:

                    elif driveSizeMetric == "tb" and matchingGames[2] == "gb":

                    else:
                        
                return None
            case _:
                return None
    else:
        return {"errorcode":"12", "desc":"Game does not exist"}

modify_game_on_drive("Fantasy89", "d1", "Bioshock: Infinate", {"Size":20, "GameSizeMetric":"gb"}, {"spot":"GameName", "AtValue":"Bioshock: Infinate"}, "-")

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
