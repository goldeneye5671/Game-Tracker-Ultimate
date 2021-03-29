#NOTE: Will need to pull from the JSON File and the Database file to verify user login
#NOTE: Will need to pull from the JSON File and the Database file to verify that a username and email has been used already

import json
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

commands = [
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData['args']**)",
    "for":"drive",
    "args":["game1", driveDatabaseTBLayout, driveInfo[0]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData['args']**)",
    "for":"drive",
    "args":["game2", driveDatabaseTBLayout, driveInfo[1]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData['args']**)",
    "for":"drive",
    "args":["game3", driveDatabaseTBLayout, driveInfo[2]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jonData['args']**)",
    "for":"drive",
    "args":["game4", driveDatabaseTBLayout, driveInfo[3]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData['args']**)",
    "for":"drive",
    "args":["game5", driveDatabaseTBLayout, driveInfo[4]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData['args']**)",
    "for":"drive",
    "args":["game6", driveDatabaseTBLayout, driveInfo[5]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(**jsonData['args'])",
    "for":"drive",
    "args":["game7", driveDatabaseTBLayout, driveInfo[6]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData[args])",
    "for":"drive",
    "args":["game8", driveDatabaseTBLayout, driveInfo[7]]
    },
    {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"1",
    "AccessLevel":"Root",
    "function required":"driveDatabaseController.create_drive_entry(jsonData[args])",
    "for":"drive",
    "args":["game9", driveDatabaseTBLayout, driveInfo[8]]
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

#DatabaseController.database_initialization(jsonDataRetrieved, databaseNameForUsers)


#NOTE: Before the action can be run, the data required for verification must be checked
#      The unique identifier must match what is stored in the users_logged_in.json file
#      and the user must also be logged in as well.
#NOTE: In the future, IP Addresses may be required to verify that the user is only
#       accessing their information from one location.
def verify_user_request(jsonData=dict):
    searchCriteria = {"Username":jsonData["Username"], "ID":jsonData["ID"], "AccessLevel":jsonData["AccessLevel"]}
    specifiedUser = DatabaseController.getRows(userLoginInfoTBLayout,searchCriteria ,databaseNameForUsers)
    zippedUsers = []
    if type(specifiedUser) == list:
        for item in specifiedUser:
            zippedUsers.append(dict(zip(userLoginInfoTBLayout["Database Headers"], list(item))))
    else:
        return {"errorcode":"7", "desc":"userDatabase does not exist. Contact support"}
    if len(zippedUsers) == 1:
        if int(zippedUsers[0]["Login"]) == 1:
            if zippedUsers[0]["ID"] == jsonData["ID"]:
                if zippedUsers[0]["AccessLevel"] == "Root" and jsonData["for"] == "user":
                    if zippedUsers[0]["AccessLevel"] == jsonData["AccessLevel"]:
                        exec(jsonData["function required"])
                        return [True, zippedUsers]
                    else:
                        return {"Errorcode":"1", "desc":"User submitted an access level that does not match assigned access level"}
                elif jsonData["for"]=="game" or jsonData["for"]=="drive":
                    exec(jsonData["function required"])
                else:
                    return {"Errorcode":"-2", "desc":"User submitted unknown action"}
            else:
                return {"Errorcode":"-3","desc":"ID Does not match"}
        else:
            return {"Errorcode":"-4", "desc":"user is not logged in"}
    elif len(zippedUsers) > 1:
        return {"Errorcode":"-5a", "desc":"duplicate users detected. Contact Customer Support"}
    else:
        return {"Errorcode":"-5b","desc":"user not detected. please make a user"}


def verify_user_creation(jsonData):
    searchCriteria = {"Username":jsonData["Username"],"Email":jsonData["Email"]}
    matchingUser = DatabaseController.getRowsOr(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers)
    zippedUsers = []
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
                    return {"Errorcode":"-6ab","desc":"User already exists with that username and email. Try again"}
                elif item["Username"] == jsonData["Username"] and item["Email"] != jsonData["Email"]:
                    return {"Errorcode":"-6a","desc":"User already exists with that username. Try again"}
                elif item["Username"] != jsonData["Username"] and item["Email"] == jsonData["Email"]:
                    return {"Errorcode":"-6b","desc":"User already exists with that email. Try again"}
                else:
                    return {"Errorcode":"-6c","desc":"unknown"}
    else:
        return {"errorcode":"7", "desc":"userDatabase does not exist. Contact support"}

def verify_user_login(username, password):
    return None


def verify_user_logout():
    return None


def verify_password_reset():
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
