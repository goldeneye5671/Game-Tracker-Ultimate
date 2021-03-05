#Create user profile and insert information
#Retrieve user profile and information (read only)
#Modify user profile and information
#Remove user profile and information
#import Engines.JSONStringEngine
import json
import os

import __init__
from Engines import JSONStringEngine, databaseCommandEngine
#creates the database if it doesn't already exists.
def database_initialization(tableLayout=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+tableLayout["Database File Name"])
    if fileExists:
        return -1
    else:
        databaseCommandEngine.create_database(tableLayout["Database File Name"], tableLayout["Database Directory"])
        databaseCommandEngine.create_table(tableLayout["Database File Name"], tableLayout["Database Directory"], tableLayout["Database Tables"][0], tableLayout["Database Headers"])
        return 0

print(database_initialization(JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")))
# print(database_initialization())

#opens database
#creates a user entry in the main table
#saves the database
#closes the database
def create_user_profile(tableLayout=dict, userInfo=list):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+tableLayout["Database File Name"])
    if fileExists:
        databaseCommandEngine.insert_row(tableLayout["Database File Name"], tableLayout["Database Directory"], tableLayout["Database Tables"][0], tableLayout["Database Headers"], userInfo)
        return 0
    else:
        return -1

print(create_user_profile(JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo"), ["Joshua", "Password", "test12@test.com", "3"]))

#opens the database
#finds the user profile based on userName
#saves the profile to a variable
#closes the database
#returns the user profile
#NOTE: Needs all user criteria or a criteria that specifically identifies the user, such as a user name or email, since those values are unique
def retrieve_user_profile(tableLayout=dict, userInfo_dict=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+tableLayout["Database File Name"])
    if fileExists:
        return databaseCommandEngine.retrieve_row(tableLayout["Database File Name"], tableLayout["Database Directory"], tableLayout["Database Tables"][0], userInfo_dict )
    else:
        return -1


print(retrieve_user_profile(JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo"), {"Username":"Anthony"}))


#opens the database
#gets all data in the table
#saves the profiles to a variable
#closes the database
#returns the user profiles
def retreive_all_user_profiles(tableLayout=dict):
    fileExists = os.path.isfile(tableLayout["Database Directory"]+tableLayout["Database File Name"])
    if fileExists:
        return databaseCommandEngine.retrieve_table(tableLayout["Database File Name"], tableLayout["Database Directory"],tableLayout["Database Tables"][0])
    else:
        return -1


print(retreive_all_user_profiles(JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")))


#runs the retrieve_user_profile() function and saves data to variable
#opens the database
#modifies user profile accordingly
#deletes old entry
def modify_user_profile():
    return None


def remove_user_profile():
    return None