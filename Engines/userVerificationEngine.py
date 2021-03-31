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

driveInfo =[
    {
    "DriveName":"d1",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d2",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d3",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d4",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d5",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d6",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d7",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d8",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
    {
    "DriveName":"d9",
    "BreifDesc":"xbox",
    "DriveSize":"5",
    "DriveSizeMetric":"tb",
    "UseableSpaceOnDrive":"5",
    "RemainingSpaceOnDrive":"5",
    "NumberOfGamesOnDrive":"0"
    },
]

#NOTE: Bug exists where is a username and user's database name may not match
#       This causes the user to access the wrong drive. Assumed here that the
#       browser will make sure that the username and the database name match.

#NOTE No encryption will be implemented on the server end. The browser will do
#       the encryption and send it. The reason being that the bottle framework
#       doesn't support HTTPS. Because of this, to make sure that the user's data
#       is as secure as I can make it, the data that the server will recieve will
#       already be sent, preventing a man in the middle attack. I will hopefully
#       be transitioning to a flask based server framework for increased security.
commands = [
    {
    "Username":"Tdeves1",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"userVerificationEngine.create_drive_entry(*jsonData['args'])",
    "for":"User",
    "args":["Tdeves1.db", driveDatabaseTBLayout, driveInfo[0]]
    },
    {
    "Username":"Bold",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Bold.db", driveDatabaseTBLayout, driveInfo[1]]
    },
    {
    "Username":"Frozen07",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Frozen07.db", driveDatabaseTBLayout, driveInfo[2]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[3]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[4]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[5]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[6]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[7]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
    "for":"drive",
    "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[8]]
    }
    ]

test=[
        {
        "Username":"Goldeneye5671",
        "Password":"Password",
        "Email":"test1@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"Fantasy89",
        "Password":"Password",
        "Email":"test2@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"FloppyTomato",
        "Password":"Password",
        "Email":"test3@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"Bold",
        "Password":"Password",
        "Email":"test4@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"tonymac",
        "Password":"Password",
        "Email":"test5@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"Tdeves1",
        "Password":"Password",
        "Email":"test6@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"Frozen07",
        "Password":"Password",
        "Email":"test7@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    },
    {
        "Username":"geye5617",
        "Password":"Password",
        "Email":"test8@test.com",
        "ID":"0",
        "Login":"1",
        "AccessLevel":"Root",
        "SecurityQ1":"",
        "AnswerQ1":"",
        "SecurityQ2":"",
        "AnswerQ2":"",
        "SecurityQ3":"",
        "AnswerQ3":"",
    }
]

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
    if len(errorOnValue) == 0:
        if jsonData["for"]=="User" and specifiedUser[3] == "Root" and jsonData["for"][:4] =="user":
            exec(jsonData["function required"])
        else:
            exec(jsonData["function required"])
    else:
        if 0 in errorOnValue:
            retVal.append()
        elif 1 in errorOnValue:
            retVal.append()
        elif 2 in errorOnValue:
            retval.append()
        elif 3 in errorOnValue:
            retVal.append()
        else:
            retval.append()
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
    matchingUser = DatabaseController.getRowsOr(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers)
    zippedUsers = []
    retVal = []
    if type(matchingUser) == list:
        for item in matchingUser:
            zippedUsers.append(dict(zip(userLoginInfoTBLayout["Database Headers"], list(item))))
        if len(zippedUsers) == 0:
            DatabaseController.addrow(userLoginInfoTBLayout, list(jsonData.values()),databaseNameForUsers)
            DatabaseController.database_initialization(searchCriteria["Username"]+".db", driveDatabaseTBLayout)
            DatabaseController.database_initialization(searchCriteria["Username"]+".db", gameDatabaseTBLayout)
        else:
            for item in zippedUsers:
                if item["Username"] == jsonData["Username"] and item["Email"] == jsonData["Email"]:
                    retVal.append({"Errorcode":"-6ab","desc":"User already exists with that username and email. Try again"})
                elif item["Username"] == jsonData["Username"] and item["Email"] != jsonData["Email"]:
                    retVal.append({"Errorcode":"-6a","desc":"User already exists with that username. Try again"})
                elif item["Username"] != jsonData["Username"] and item["Email"] == jsonData["Email"]:
                    retVal.append({"Errorcode":"-6b","desc":"User already exists with that email. Try again"})
                else:
                    retVal.append({"Errorcode":"-6c","desc":"unknown"})
            return retVal
    else:
        return {"errorcode":"7", "desc":"userDatabase does not exist. Contact support"}


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
    searchCriteria = {"Username": jsonData["Username"], "Password": jsonData["Password"]}
    matchingUser = DatabaseController.getRows(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers)
    if type(matchingUser) ==list:
        if len(matchingUser)==1:
            #The way that this is set up allows you to log in from another browser. In theory,
            #you could log in through anouther browser and reset the ID this way. I am not sure
            #if I want to keep it this way though. I only want one browser at a time to access
            #this data
            DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {"ID":randint(0, 999999999), "Login":1}, {"spot":"Username", "Username":jsonData["Username"]})
        elif len(matchingUser) < 1: 
            return {"errorcode":"7a", "desc":"No user found with the given information. Try again"}
        else:
            return {"errorcode":"7b", "desc":"Database error. Contact customer support"}
    else:
        return {"errorcode":"7c", "desc":"Database does not exist. Contact customer support"}

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
            DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {"ID":0, "Login":0}, {"spot":"Username", "Username":jsonData["Username"]})
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

for item in commands:
    print (verify_user_request(item))

#eval(sentAct["function required"])

#print(verify_user_request(jsonData, myType, []))
