#NOTE: Will need to pull from the JSON File and the Database file to verify user login
#NOTE: Will need to pull from the JSON File and the Database file to verify that a username and email has been used already


#imports
import json
from random import randint
import __init__
from Controllers import DatabaseController, driveDatabaseController, gameDatabaseController
from Engines import JSONStringEngine


#variables that are used in functions. I intend on moving these to a big file
#   that has all the vars needed so that I can use it inbetween files

#database names
databaseNameForUsers = "userLoginInfo.db"
#database layouts
userLoginInfoTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")
driveDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Drives")
gameDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Games")


#initial things that are required to be run when the server starts go here
DatabaseController.database_initialization(databaseNameForUsers, userLoginInfoTBLayout)

#variables that go in the lists and objects go here
usr            = "Username"
user           = "user"
rndID          = "ID"
login          = "Login"
acclvl         = "AccessLevel"
clearenceRoot  = "Root"
clearenceBasic = "Basic"
For            = "for"
forUsr         = "user"
forGme         = "game"
forDrv         = "drive"
funcReq        = "function required"
err            = "errorcode"
dsc            = "description"
eml            = "Email"
psw            = "Password"
db             = ".db"
spt            = "spot"
at             = "AtValue"
q1             = "SecurityQ1"
q2             = "SecurityQ2"
q3             = "SecurityQ3"
a1             = "AnswerQ1"
a2             = "AnswerQ2"
a3             = "AnswerQ3"
conf           = "I confirm that I have read the above statement and understand that all my information will be permenently deleted."
dr             = "Database Directory"
#NOTE: Bug exists where is a username and user's database name may not match
#       This causes the user to access the wrong drive. Assumed here that the
#       browser will make sure that the username and the database name match.
#NOTE No encryption will be implemented on the server end. The browser will do
#       the encryption and send it. The reason being that the bottle framework
#       doesn't support HTTPS. Because of this, to make sure that the user's data
#       is as secure as I can make it, the data that the server will recieve will
#       already be sent, preventing a man in the middle attack. I will hopefully
#       be transitioning to a flask based server framework for increased security.
#NOTE: In the future, IP Addresses may be required to verify that the user is only
#       accessing their information from one location.

#{
#   "Username"         :"User_Name",
#   "ID"               :randint(0, 999999999),
#   "AccessLevel"      :"basic, root",
#   "function required":"FileName.FunctionName(*jsonData['args])",
#   "for"              :"User, drive, game",
#   "args"             :[arg1, arg2, arg3,...,argN]
# }
def verify_user_request(jsonData=dict):
    selectors = [usr, rndID, login, acclvl]
    specifiedUser = DatabaseController.getRows(userLoginInfoTBLayout,{usr:jsonData[usr]},databaseNameForUsers, selectors)
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
        if jsonData[For]==forUsr and specifiedUser[3] == clearenceRoot and jsonData[For][:4] == user:
            exec(jsonData[funcReq])
        else:
            exec(jsonData[funcReq])
    else:
        if -1 in errorOnValue:
            retVal.append({err:"-1a", dsc:"User not found. Check database."})
        elif 0 in errorOnValue:
            retVal.append({err:"-1b", dsc:"Username does not match database"})
        elif 1 in errorOnValue:
            retVal.append({err:"-1c", dsc:"ID does not match database"})
        elif 2 in errorOnValue:
            retval.append({err:"-1d", dsc:"User is not logged in, so can not make changes"})
        elif 3 in errorOnValue:
            retVal.append({err:"-1e", dsc:"User does not have the security clearence to make desired change"})
        else:
            retval.append({err:"-1f", dsc:"An unknown error has occured"})
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
    searchCriteria = {usr:jsonData[usr],eml:jsonData[eml]}
    specifiedUser = DatabaseController.getRowsOr(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers, list(searchCriteria.keys()))
    retVal = []
    if type(specifiedUser) == list and len(specifiedUser) == 0:
            DatabaseController.addrow(userLoginInfoTBLayout, list(jsonData.values()),databaseNameForUsers)
            DatabaseController.database_initialization(searchCriteria[usr]+db, driveDatabaseTBLayout)
            DatabaseController.database_initialization(searchCriteria[usr]+db, gameDatabaseTBLayout)
    else:
        for item in specifiedUser:
            if item[0] == jsonData[usr] and item[1] == jsonData[eml]:
                retVal.append({err:"-6ab",dsc:"User already exists with that username and email. Try again"})
            elif item[0] == jsonData[usr] and item[1] != jsonData[eml]:
                retVal.append({err:"-6a",dsc:"User already exists with that username. Try again"})
            elif item[0] != jsonData[usr] and item[1] == jsonData[eml]:
                    retVal.append({err:"-6b",dsc:"User already exists with that email. Try again"})
            else:
                retVal.append({err:"-6c",dsc:"unknown"})
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
    selectors = [usr, psw]
    matchingUser = DatabaseController.getRows(userLoginInfoTBLayout, {usr: jsonData[usr], psw: jsonData[psw]}, databaseNameForUsers, selectors)
    if type(matchingUser) ==list and len(matchingUser)==1:
            #The way that this is set up allows you to log in from another browser. In theory,
            #you could log in through anouther browser and reset the ID this way. I am not sure
            #if I want to keep it this way though. I only want one browser at a time to access
            #this data
            DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {rndID:randint(0, 999999999), "Login":1}, {spt:usr, at:jsonData[usr]})
    elif len(matchingUser) < 1: 
        return {err:"7a", dsc:"No user found with the given information. Try again"}
    else:
        return {err:"7b", dsc:"Database error. Contact customer support"}

#{
#   Username:user_name,
#   ID:randint(0, 9999999999),
#   Login:1
# }
def verify_user_logout(jsonData):
    searchCriteria = {usr:jsonData[usr], rndID:jsonData[rndID], login:jsonData[login]}
    matchingUser = DatabaseController.getRows(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers, [usr, rndID, login])
    if type(matchingUser) == list:
        if len(matchingUser)==1:
            DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {rndID:0, login:0}, {spt:usr, at:jsonData[usr]})
        elif len(matchingUser) > 1:
            return {err:"8a",dsc:"More than one user with the given data"}
        else:
            return {err:"8b", dsc:"No users found with the given data"}
    else:
        return {err:"8c", dsc:"Database does not exist. Contact customer support."}

#{
#   Username:user_name
#   Email: email
# }
def verify_password_reset(jsonData):
    searchCriteria = {usr:jsonData[usr], eml: jsonData[eml]}
    matchingUser = DatabaseController.getRowsOr(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers, [q1, q2, q3])
    if type(matchingUser) == list and len(matchingUser) == 1:
        return list(matchingUser[0])
    return {err:"-10a", dsc:"No user found with that information"}

#{
#   Username:user_name
#   Email: email
#   question:answer
#   question:answer
#   question:answer
# }
def initiate_password_reset(jsonData):
    searchCriteria = {usr:jsonData[usr], eml:jsonData[eml]}
    matches = 0
    matchingUser = DatabaseController.getRowsOr(userLoginInfoTBLayout, searchCriteria, databaseNameForUsers, [a1, a2, a3])
    if type(matchingUser) == list and len(matchingUser) == 1:
        matchingUser = list(matchingUser[0])
        for item in matchingUser:
            if item in list(jsonData.values()):
                matches += 1
        if matches == 3:
            return [True, matches]
        else:
            return [False, matches]

#{
#   Authority:[Boolean: matches]
#   Username:username,
#   NewPassword:password
# }
def update_password(jsonData):
    if jsonData["Authority"][0] and jsonData["Authority"][1] == 3:
        DatabaseController.modifyRow(databaseNameForUsers, userLoginInfoTBLayout, {psw:jsonData[psw]}, {spt:usr, at:jsonData[usr]})

#   Confirmation: "I confirm that I have read the above statement and understand that all my information will be permenently deleted."
def delete_account(confirmation, username):
    if confirmation == conf:
        DatabaseController.deleteDatabase(username+db, gameDatabaseTBLayout[dr])
        DatabaseController.deleteDatabase(username+db, driveDatabaseTBLayout[dr])
        DatabaseController.removeRow(userLoginInfoTBLayout, databaseNameForUsers, {usr: username})
    return None
