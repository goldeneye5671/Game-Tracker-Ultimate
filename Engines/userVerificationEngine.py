#NOTE: Will need to pull from the JSON File and the Database file to verify user login
#NOTE: Will need to pull from the JSON File and the Database file to verify that a username and email has been used already

import json
from random import randint
import __init__
from Controllers import DatabaseController, driveDatabaseController, gameDatabaseController
from Engines import JSONStringEngine

databaseNameForUsers = "userLoginInfo.db"
userLoginInfoTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")
driveDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Drives")
gameDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Games")

DatabaseController.database_initialization(databaseNameForUsers, userLoginInfoTBLayout)


#NOTE: Bug exists where is a username and user's database name may not match
#       This causes the user to access the wrong drive. Assumed here that the
#       browser will make sure that the username and the database name match.

#NOTE No encryption will be implemented on the server end. The browser will do
#       the encryption and send it. The reason being that the bottle framework
#       doesn't support HTTPS. Because of this, to make sure that the user's data
#       is as secure as I can make it, the data that the server will recieve will
#       already be sent, preventing a man in the middle attack. I will hopefully
#       be transitioning to a flask based server framework for increased security.


#NOTE: Before the action can be run, the data required for verification must be checked
#      The unique identifier must match what is stored in the users_logged_in.json file
#      and the user must also be logged in as well.
#NOTE: In the future, IP Addresses may be required to verify that the user is only
#       accessing their information from one location.
def verify_user_request(jsonData=dict):
    selectors = ["Username", "ID", "Login", "AccessLevel"]
    specifiedUser = DatabaseController.getRows(userLoginInfoTBLayout,{"Username":jsonData["Username"]},databaseNameForUsers, selectors)
    errorOnValue = []
    retVal = []
    if type(specifiedUser)==list and len(specifiedUser) == 1:
        specifiedUser = list(specifiedUser[0])
        recievedUser = list(jsonData.values())
        for i in range(len(specifiedUser)):
            if specifiedUser[i] != recievedUser[i]:
                errorOnValue.append(i)
    else:
        errorOnValue.append(-1)
    if len(errorOnValue) == 0:
        if jsonData["for"]=="User" and specifiedUser[3] == "Root" and jsonData["for"][:4] =="user":
            exec(jsonData["function required"])
        else:
            exec(jsonData["function required"])
    else:
        if -1 in errorOnValue:
            retVal.append({"errorcode":"-1a", "desc":"User not found. Check database."})
        elif 0 in errorOnValue:
            retVal.append({"errorcode":"-1b", "desc":"Username does not match database"})
        elif 1 in errorOnValue:
            retVal.append({"errorcode":"-1c", "desc":"ID does not match database"})
        elif 2 in errorOnValue:
            retval.append({"errorcode":"-1d", "desc":"User is not logged in, so can not make changes"})
        elif 3 in errorOnValue:
            retVal.append({"errorcode":"-1e", "desc":"User does not have the security clearence to make desired change"})
        else:
            retval.append({"errorcode":"-1f", "desc":"An unknown error has occured"})
#{
#       "Username":    "username",
#       "Password":    "password",
#       "Email":       "email@domain.com",
#       "ID":          0,
#       "Login":       0,
#       "AccessLevel": "basic",
#       "SecurityQ1":  "???",
#       "AnswerQ1":    "ANS",
#       "SecurityQ2":  "???",
#       "AnswerQ2":    "ANS",
#       "SecurityQ3":  "???",
#       "AnswerQ3":    "ANS",
#   }
def verify_user_creation(jsonData):
    searchCriteria = {"Username":jsonData["Username"],"Email":jsonData["Email"]}
    specifiedUser = DatabaseController.getRowsOr(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers, list(searchCriteria.keys()))
    retVal = []
    if type(specifiedUser) == list and len(specifiedUser) == 0:
            DatabaseController.addrow(userLoginInfoTBLayout, list(jsonData.values()),databaseNameForUsers)
            DatabaseController.database_initialization(searchCriteria["Username"]+".db", driveDatabaseTBLayout)
            DatabaseController.database_initialization(searchCriteria["Username"]+".db", gameDatabaseTBLayout)
    else:
        for item in specifiedUser:
            if item[0] == jsonData["Username"] and item[1] == jsonData["Email"]:
                retVal.append({"Errorcode":"-6ab","desc":"User already exists with that username and email. Try again"})
            elif item[0] == jsonData["Username"] and item[1] != jsonData["Email"]:
                retVal.append({"Errorcode":"-6a","desc":"User already exists with that username. Try again"})
            elif item[0] != jsonData["Username"] and item[1] == jsonData["Email"]:
                    retVal.append({"Errorcode":"-6b","desc":"User already exists with that email. Try again"})
            else:
                retVal.append({"Errorcode":"-6c","desc":"unknown"})
        return retVal
    


#This function is much shorter than the other verify functions because I realized something.
#   I am searching the database for a record that contains both the given username and password
#   Since I am looking for the username AND looking for the password, I am only going to get
#   records that have the same username AND password that I give it. So, I don't really need
#   to look at the username or password directly, but I do need to look at the length of the
#   list. If the list is 0, well then nothing was found. If it's 1, then one match was found,
#   if the list is greater than 1 or I don't get a type of list back, then there is a DB issue.
#
#{
#   Username:username,
#   Password:password
# }
def verify_user_login(jsonData):
    selectors = ["Username", "Password"]
    matchingUser = DatabaseController.getRows(userLoginInfoTBLayout, {"Username": jsonData["Username"], "Password": jsonData["Password"]}, databaseNameForUsers, selectors)
    if type(matchingUser) ==list and len(matchingUser)==1:
            #The way that this is set up allows you to log in from another browser. In theory,
            #you could log in through anouther browser and reset the ID this way. I am not sure
            #if I want to keep it this way though. I only want one browser at a time to access
            #this data
            DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {"ID":randint(0, 999999999), "Login":1}, {"spot":"Username", "AtValue":jsonData["Username"]})
    elif len(matchingUser) < 1: 
        return {"errorcode":"7a", "desc":"No user found with the given information. Try again"}
    else:
        return {"errorcode":"7b", "desc":"Database error. Contact customer support"}

#{
#   Username:user_name,
#   ID:randint(0, 9999999999),
#   Login:1
# }
def verify_user_logout(jsonData):
    searchCriteria = {"Username":jsonData["Username"], "ID":jsonData["ID"], "Login":jsonData["Login"]}
    matchingUser = DatabaseController.getRows(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers)
    if type(matchingUser) == list:
        if len(matchingUser)==1:
            DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {"ID":0, "Login":0}, {"spot":"Username", "AtValue":jsonData["Username"]})
        elif len(matchingUser) > 1:
            return {"errorcode":"8a","desc":"More than one user with the given data"}
        else:
            return {"errorcode":"8b", "desc":"No users found with the given data"}
    else:
        return {"errorcode":"8c", "desc":"Database does not exist. Contact customer support."}

#{
#   Username:user_name
#   Email: email
# }
def verify_password_reset(jsonData):
    searchCriteria = {"Username":jsonData["Username"], "Email": jsonData["Email"]}
    matchingUser = DatabaseController.getRows(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers)
    if type(matchingUser) == list:
        if length(matchingUser) == 1:
            return None
    return None


def initiate_password_reset():
    return None

#DatabaseController.addrow(jsonDataRetrieved, ["goldeneye5671", "Password", "choice@choice.com", 0, 1, "Root", "", "", "", "", "", ""], databaseNameForUsers)
#print(verify_user_request(sentData1))
for item in test:
    print(verify_user_creation(item))

verify_user_login({"Username":"Fantasy89", "Password":"Password"})

for item in commands:
    print (verify_user_request(item))

#eval(sentAct["function required"])

#print(verify_user_request(jsonData, myType, []))
