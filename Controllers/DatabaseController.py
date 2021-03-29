#Create user profile and insert information
#Retrieve user profile and information (read only)
#Modify user profile and information
#Remove user profile and information
#import Engines.JSONStringEngine
import json
import os
import __init__
from Engines import databaseCommandEngine


#NOTE: Will need to make modification so that tables in database_info.json that have a value of none
#       Can use a parameter specified value instead of a json specified value.

#creates the database if it doesn't already exists.
def database_initialization(databaseName=str, tableLayout=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+databaseName)
    if fileExists:
        return -1
    else:
        databaseCommandEngine.create_database(databaseName, tableLayout["Database Directory"])
        databaseCommandEngine.create_table(databaseName, tableLayout["Database Directory"], tableLayout["Database Tables"][0], tableLayout["Database Headers"])
        return 0


#opens database
#creates a user entry in the main table
#saves the database
#closes the database
def addrow(tableLayout=dict, rowData=list, databaseName=str):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+databaseName)
    if fileExists:
        databaseCommandEngine.insert_row(databaseName, tableLayout["Database Directory"], tableLayout["Database Tables"][0], tableLayout["Database Headers"], rowData)
        return 0
    else:
        return -1


#opens the database
#finds the user profile based on userName
#saves the profile to a variable
#closes the database
#returns the user profile
#NOTE: Needs all user criteria or a criteria that specifically identifies the user, such as a user name or email, since those values are unique
def getRows(tableLayout=dict, rowData_dict=dict, databaseName=str):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+databaseName)
    if fileExists:
        return databaseCommandEngine.retrieve_row(databaseName, tableLayout["Database Directory"], tableLayout["Database Tables"][0], rowData_dict)
    else:
        return -1


def getRowsOr(tableLayout=dict, rowData_dict=dict, databaseName=str):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+databaseName)
    if fileExists:
        return databaseCommandEngine.retrieve_row_or(databaseName, tableLayout["Database Directory"], tableLayout["Database Tables"][0], rowData_dict)
    else:
        return -1


#opens the database
#gets all data in the table
#saves the profiles to a variable
#closes the database
#returns the user profiles
def getTable(tableLayout=dict, databaseName=str):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+databaseName)
    if fileExists:
        return databaseCommandEngine.retrieve_table(databaseName, tableLayout["Database Directory"],tableLayout["Database Tables"][0])
    else:
        return -1


#runs the retrieve_user_profile() function and saves data to variable
#modifies user profile accordingly
#deletes old entry
#saves new entry
#closes the database
def modifyRow(name=str, tableLayout=dict, modifications=dict, spot=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"])
    if fileExists:
        return databaseCommandEngine.update_table_at_spot(name, tableLayout["Database Directory"], tableLayout["Database Tables"][0], modifications, spot)
    else:
        return -1


#runs the retrieve_user_profile function and saves data to variable
#deletes the entry
#saves the database
#closes the database

#NOTE: This functionality will not work correctly yet. The functionality of these points need to be programmed into the other database controllers
#deletes the drive database associated with the user
#deletes the game database associated with the user
def removeRow(tableLayout=dict, databaseName=str, rowID=str):
    return None

def deleteDatabase():
    print()
