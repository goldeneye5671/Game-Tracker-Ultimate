#NOTE: Will need to pull from the JSON File and the Database file to verify user login
#NOTE: Will need to pull from the JSON File and the Database file to verify that a username and email has been used already

import json
import __init__
from Controllers import DatabaseController
from Engines import JSONStringEngine
databaseNameForUsers = "userLoginInfo.db"
userLoginInfoTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")
DatabaseController.database_initialization(databaseNameForUsers, userLoginInfoTBLayout)

sentData1 = {
    "Username":"Fantasy89",
    "ID":"0",
    "Login":"0",
    "AccessLevel":"Root",
    "function required":"DatabaseController.deleteDatabase(*jsonData['args'])",
    "for":"user",
    "args":[]
    }

sentData2 = {
    "Username":"Fantasy89",
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
}

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
print(verify_user_request(sentData1))
print(verify_user_creation(sentData2))

#eval(sentAct["function required"])

#print(verify_user_request(jsonData, myType, []))
