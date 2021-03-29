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


#creates a database for a user if it doesn't exist
#NOTE: name of database is the username
def database_initialization(tableLayout=dict, databaseName=str):
    fileExists = os.path.isFile(tableLayout["Database Directory"]+databaseName)
    if fileExists:
        return -1
    else:
        databaseCommandEngine.create_database(tableLayout["Database Directory"]+name)


#opens game drive database
#opens table that contains the correct drive name
#checks to see if game exists in the database or else returns an error
#inserts a game entry
#saves the modification
#closes the database
def create_game_entry_on_drive(tableLayout=dict, rowData_dict=dict, databaseName=str):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+databaseName)
    #checks the dictionary for the "Database Tables" key
        #
    return None


#opens game drive database
#searches to see if table exists
#creates a table with the name given
#saves the modification
#closes the database
def create_drive_table():
    return None


#opens the game drive database
#opens table that contains the correct drive name
#uses a select statement to select the desired game (preferably the name)
#saves the retrieved data to a variable
#closes the database
#returns the variable in the desired format
def retrieve_game_on_drive():
    return None


#opens the game drive database
#opens table that contains the correct drive name
#uses a select statement to select all games on the drive
#saves the retrieved data to a variable
#closes the database
#returns the variable in the desired format
def retrieve_all_games_on_drive():
    return None


#opens the game drive database
#opens table that contains the correct drive name
#uses a select statement to select the game entry to modify or else makes no modification if game doesn't exist
#saves the retrieved data to a variable
#deletes the old entry
#modifies the retrieved entry
#inserts the modified entry to the table with the correct drive name
#saves the modification
#closes the database
def modify_game_on_drive():
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
