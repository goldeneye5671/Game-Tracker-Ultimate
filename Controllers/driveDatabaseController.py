#NOTE: The database that is represented here is just so store information about the drives. It is mainly refrenced and has size changes.
#CONT: It will be very rare that a user will remove a drive from a database.

#creates a table that will store the user's drive information
#retrieve information from a user's drive database which could include drive names, sizes, etc. or all/none of the above
#modify information from a user's drive database which could include drive names, sizes, etc. or all/none of the above
#remove information from a user's drive database which could include one or many drive entries at once
#insert information into a user's drive database which could include one or many drive entries at once
#delete a use's drive database when a user deletes their profile

import json
import os
import __init__
from Engines import databaseCommandEngine
import DatabaseController


#creates a database for the user if it doesn't exist
#creates a table in the database that will hold the data about each drive
#NOTE: name of database is the username
#NOTE: USE DatabaseController's database_initialization function to make the database!!

#opens the drive database
#opens the drive table
#checks to see if an entry exists or else returns an error
#inserts a drive entry
#saves the database
#closes the database
def create_drive_entry(name=str, tableLayout=dict, driveInfo_dict=dict):
    fileExists = os.path.isFile(tableLayout["Database Directory"]+name)
    if fileExists:
        matchingDrives = DatabaseController.getRows(tableLayout, driveInfo_dict ,name)
        if type(matchingDrives) == list:
            if len(matchingDrives) == 0:
                DatabaseController.addrow(tableLayout, list(driveInfo_dict.values()), name)
            else:
                return {"errorcode":"8a","desc":"Drive already exists"}
        else:
            return {"errorcode":"8b", "desc":"Drive Database doesn't exist for the user. Need to make one"}
        
#opens the drive database
#opens the drive table
#checks to see if the drive exists otherwise returns an error
#returns the drive entry
#closes the database
def retrieve_drives(name=str, tableLayout=dict, driveInfo_dict=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+name)
    if fileExists:
        matchingDrives = DatabaseController.getRows(tableLayout, driveInfo_dict, name)
        if len(matchingDrives) == 0:
            return {"errorcode":"9","desc":"Search querry resulted in no matches for the given drive. Drive doesn't exist."}
    else:
        return {"errorcode":"8b","desc":"Drive Database doesn't exist for the user. Need to make one"}


#opens the database
#opens the drive table
#gets all drive entries and saves them to a variable
#closes the database
#returns the variable
def retrieve_all_drives(name=str, tableLayout=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+name)
    if fileExists:
        return databaseCommandEngine.retrieve_table(name, tableLayout["Database Directory"], tableLayout["Database Tables"])

#opens the database
#opens the drive table
#updates the given drive entry. Uses the name to look up the drive
#   even if the drive name is being changed
#saves the database
#closes the database
def modify_drive():
    return None

#opens the database
#opens the drive table
#deletes the specified drive entry
#saves the databse
#closes the database
def remove_drive():
    return None

#uses the os lib to check if the database exists
#if the database exists, uses the os lib to delete the database
#else returns an error
def delete_database():
    return None
