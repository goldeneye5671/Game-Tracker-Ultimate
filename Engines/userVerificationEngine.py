#NOTE: Will need to pull from the JSON File and the Database file to verify user login
#NOTE: Will need to pull from the JSON File and the Database file to verify that a username and email has been used already

import json
import __init__
from Controllers import DatabaseController
from Engines import JSONStringEngine
def verify_new_user_request():
    return None


#NOTE: Before the action can be run, the data required for verification must be checked
#      The unique identifier must match what is stored in the users_logged_in.json file
#      and the user must also be logged in as well.
#NOTE: In the future, IP Addresses may be required to verify that the user is only
#       accessing their information from one location.
def verify_user_request(mydata=dict, actionType=dict, dataRequiredForAction=list):
    if actionType["username"] in mydata:
        if actionType["id"] in list((mydata[actionType["username"]].values())):
            return actionType["action"] == DatabaseController.deleteDatabase

jsonData = JSONStringEngine.load_database_JSON("users_logged_in.json", "./JSON Data/")
myType = {"action":DatabaseController.deleteDatabase, "username":"goldeneye5671" ,"id":132435465, "Access Level":"Root"}


print(verify_user_request(jsonData, myType, []))