#Create user profile and insert information
#Retrieve user profile and information (read only)
#Modify user profile and information
#Remove user profile and information
#import Engines.JSONStringEngine
import json
import __init__
from Engines import JSONStringEngine
import os
#creates the database if it doesn't already exists.
def database_initialization():
    return JSONStringEngine.retrieve_json_property("database_info.json", "./JSON Data/", "UserLoginInfo", "Database Directory")
    #return os.path.isfile("./Database Files/")

print(database_initialization())

#opens database
#creates a user entry in the main table
#saves the database
#closes the database
def create_user_profile():
    return None


#opens the database
#finds the user profile based on userName
#saves the profile to a variable
#closes the database
#returns the user profile
def retrieve_user_profile():
    return None


#opens the database
#gets all data in the table
#saves the profiles to a variable
#closes the database
#returns the user profiles
def retreive_all_user_profiles():
    return None

#runs the retrieve_user_profile() function and saves data to variable
#opens the database
#modifies user profile accordingly
#deletes old entry
def modify_user_profile():
    return None


def remove_user_profile():
    return None