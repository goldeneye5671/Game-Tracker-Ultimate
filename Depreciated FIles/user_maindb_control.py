import sqlite3
import json
import random
import os
import user_drive_database

userDBDir = "./Database Files/userLoginInfo/userLoginInfo.db"
user_game_info_dir = "./Database Files/userGameInfo/"
user_drive_info_dir = "./Database Files/userDriveInfo/"
driveTableName = "DriveList"
gameTableName = "" #keep if an init table needs to be made for an init game table
userLoginInfoTableName = "loginInfo"
userLoginInfoTableHeaders = ['uname', 'pword', 'email', 'dirDriveLocation', 'dirGameLocation' ,'acc_lev']
driveTableHeaders = [1, 2, 3, 4, 5, 6]

#expected layout of this var:
#{uname: [dir, acc_lev, uniqueIdentifier(should be saved as a cookie through the browser, uniquely generated and checked to grant data access)]}
usersLoggedIn = {}

#because this is used many times it doesn't make sense to open and close this constantly. Just leave it open untill a server hault is called and close the database.
userLoginInfoConnection = sqlite3.connect(userDBDir)
userLoginInfoCursor = userLoginInfoConnection.cursor()

#when creating table the function is only expecting a length of 4 for the list of headers
def initializeUserLoginInfoDB(dir, listOfHeaders, userLoginInfoTblName):
    if len(listOfHeaders) == 6:
        userLoginInfoConnection = sqlite3.connect(userDBDir)
        userLoginInfoCursor = userLoginInfoConnection.cursor()
        userLoginInfoCursor.execute("""CREATE TABLE IF NOT EXISTS """ + userLoginInfoTblName + """(""" + userLoginInfoTableHeaders[0] + ", " + userLoginInfoTableHeaders[1] + ", " + userLoginInfoTableHeaders[2] + ", " + userLoginInfoTableHeaders[3] + ", " + userLoginInfoTableHeaders[4] + "," + userLoginInfoTableHeaders[5] + """)""")
        return "Table initialized successfully"
    else:
        return "Error on table creation. The length of listOfHeaders is " + len(listOfHeaders) + "and not the expected value of 6"


#JSON data expected in the following format:
#{user: uname, pass: pword}
#the information sent to the server should be hashed. No unhashed data will be stored on the server.
#the data that will be sent will already be hashed
#if the uname/pword does not match anything in the database then an error JSON
#string will be sent in the following format:
#{errorcode: -1, desc: "uname/pasword either doesn't exist or information entered is incorrect"}
def verifyUserInformationandLogin(json_data):
    userLoginInfoRecieved = json.loads(json_data)
    userLoginInfoRecievedFromDB = userLoginInfoCursor.execute("SELECT * FROM " + userLoginInfoTableName + " WHERE " + userLoginInfoTableHeaders[0] + " = ?", (userLoginInfoRecieved["user"],)).fetchall()
    if -1 < len(userLoginInfoRecievedFromDB) < 1:
        return json.dumps({"errorcode": -1, "desc": "uname does not exist or information is incorrect"})
    elif len(userLoginInfoRecievedFromDB) > 1:
        return json.dumps({"errorcode": -1, "desc": "duplicate uname found in database. Database Check needed"})
    else:
        recievedUserInfo = list(userLoginInfoRecievedFromDB[0])
        if recievedUserInfo[1] == userLoginInfoRecieved["pass"]:
            randomIdentifier = random.randint(1, 100000000)
            usersLoggedIn[recievedUserInfo[0]] = [*recievedUserInfo, randomIdentifier]
            return json.dumps({recievedUserInfo[0]: [*recievedUserInfo, randomIdentifier]})
        else:
            return json.dumps({"errorcode": -1, "desc": "pword does not exist or information is incorrect"})


#JSON data expected in the following format
#{uname: [dir, acc_lev, uniqueIdentifier(should be saved as a cookie through the browser, uniquely generated and checked to grant data access)]}
#if this matches a user in the usersLoggedIn var, then it will log the user out (AKA delete them from the variable)
def verifyUserLogoutRequestandLogOut(json_data):
    userInfoRecieved = json.loads(json_data)
    usersIn = list(usersLoggedIn.keys())
    myUserIn = list(userInfoRecieved.keys())[0]
    if myUserIn in usersIn:
        del usersLoggedIn[myUserIn]
        return {"logout": "success"}
    else:
        return {"logout":"failed"}
    
    

#JSON data expected in the following format:
#{user: uname, pass: pword, email: email, accesslv: accesslv}
#user and pass will be expected to be hashed values when sent
#function will check user database for matches, if there is one,
#the action will be cancled and an error JSON string will be sent
#in the following format:
#{errorcode: -1, desc: "uname already exists"}
#will also check for duplicate emails, but not duplicate passwords.
#if there is a duplicate email then a similar error JSON string will
#be sent in the following format:
#{errorcode: -1, desc: "email already exists"}
#otherwise the user will be created by inserting a value into a table
#that will represent the user and store the user's hashed information.
def verifyCriteriaAndCreateUser(json_data):
    #needs a unique username and email. Accesslv will be a number. 0 represents a normal user and 1 represents a user with privleged access. Numbers can be added as program progresses
    userLoginInfoRecieved = json.loads(json_data)
    usersWithUsernameAndemail = userLoginInfoCursor.execute("SELECT * FROM " + userLoginInfoTableName + " WHERE " + userLoginInfoTableHeaders[0] + " = ? OR " + userLoginInfoTableHeaders[2] + " = ?", (userLoginInfoRecieved["user"], userLoginInfoRecieved["email"])).fetchall()
    if len(usersWithUsernameAndemail) > 0:
        checkingUserOut = list(usersWithUsernameAndemail[0])
        if checkingUserOut[0] == userLoginInfoRecieved["user"] and checkingUserOut[2] == userLoginInfoRecieved["email"]:
            return json.dumps({"errorcode":-1, "desc":"username and email already in use"})
        elif checkingUserOut[0] == userLoginInfoRecieved["user"] and checkingUserOut[1] != userLoginInfoRecieved["email"]:
            return json.dumps({"errorcode":"-1", "desc":"username already in use"})
        elif checkingUserOut[0] != userLoginInfoRecieved["user"] and checkingUserOut[2] == userLoginInfoRecieved["email"]:
            return json.dumps({"errorcode":"-1", "desc":"email already in use"})
        else:
             return json.dumps({"errorcode":"-1", "desc":"unknown error. Please contact support"})
    else:
        userLoginInfoCursor.execute("INSERT INTO " + userLoginInfoTableName + " VALUES (?,?,?,?,?,?)", (userLoginInfoRecieved["user"], userLoginInfoRecieved["pword"], userLoginInfoRecieved["email"], user_drive_info_dir + userLoginInfoRecieved["user"] + ".db", user_game_info_dir + userLoginInfoRecieved["user"]+"db",1))
        userLoginInfoConnection.commit()

        connectionUserCreationDrive = sqlite3.connect(user_drive_info_dir+userLoginInfoRecieved["user"]+".db")
        connectionUserCreationDrive.execute("""CREATE TABLE IF NOT EXISTS """ + driveTableName + "(name, numberOfGames, totalDriveSize, driveSizeType, totalDriveSizeRemaining, combinedSpaceUsedOnDisk)""")
        connectionUserCreationDrive.commit()
        connectionUserCreationDrive.close()
        
        connectionUserCreationGame = sqlite3.connect(user_game_info_dir+userLoginInfoRecieved['user']+".db")
        connectionUserCreationGame.commit()
        connectionUserCreationGame.close()
        
        return json.dumps({'success': "user created successfully"})

#   format of JSON String expected:
#   {user: uname, email: email, randID: number}
#   the randID represents the random number given to a user when they login to a session. That must match what is stored in the
#   usersLoggedIn dict so a user doesn't delete another user
def verifyAndDestroyUser(json_data):
    userLoginInfoRecieved = json.loads(json_data)
    userLoginInfoFromDB = userLoginInfoCursor.execute("SELECT * FROM " + userLoginInfoTableName + " WHERE " + userLoginInfoTableHeaders[0] + " = ? OR " + userLoginInfoTableHeaders[2] + " = ?", (userLoginInfoRecieved["user"], userLoginInfoRecieved["email"])).fetchall()
    if 0 < len(userLoginInfoFromDB) < 2:
        checkingUserOut = list(userLoginInfoFromDB[0])
        if (userLoginInfoRecieved["user"] == checkingUserOut[0]):
            if (userLoginInfoRecieved["user"] in list(usersLoggedIn.keys())):
                if (int(userLoginInfoRecieved["randID"]) == int(usersLoggedIn[checkingUserOut[0]][5])):
                    if (checkingUserOut[2]==userLoginInfoRecieved["email"]):
                        del usersLoggedIn[userLoginInfoRecieved["user"]]
                        userLoginInfoCursor.execute('DELETE FROM ' + userLoginInfoTableName + ' WHERE uname = ? AND email = ?', (userLoginInfoRecieved["user"], userLoginInfoRecieved["email"]))
                        userLoginInfoConnection.commit()
                        os.remove(user_drive_info_dir+userLoginInfoRecieved["user"])
            #log the user out/
            #delete the user from the database/
            #delete the database file created when the user was created/
            #delete any posts that the user may have posted on the blog ( cannot do yet blog not implemented yet)
        else:
            return json.dumps({"errorcode":-1, "desc": "Internal error. Please contact support."})
            # Return an error that there has been an internal error and the user must contact support to proceed
    else:
        return json.dumps({"errorcode":-1, "desc":"The user does not exist"})


#format of the json data:
#{uname: uname}
#This function will check to see if a user is logged in and if they are
#will proceed to check what access this user has, based off of the logged in user's
#access level.
def verifyUserAccessToDB(json_data):
    userToCheck = json.loads(json_data)
    retval = {}
    if userToCheck["user"] in usersLoggedIn.keys():
        userInformation = usersLoggedIn[userToCheck["user"]][5]
        retval['userLoggedIn'] = True
        if userInformation == 0:
            retval['UserAccess'] = "Basic"
        elif userInformation == 1:
            retval['UserAccess'] = "Advanced"
        elif userInformation == 2:
            retval['UserAccess'] = "ROOT"
        else:
            retval['UserAccess'] = "No Access/User data may be corrupted. Contact support."
    else:
        return json.dumps({"userLoggedIn":False,"UserAccess":None,"errorcode":-1, "desc":"The user is not logged in and therefore cannot make any changes"})
    return json.dumps(retval)
#testing code listed below:

def returnUserInformation(username):
    if username in usersLoggedIn.keys():
        return usersLoggedIn[username]
    else:
        return False


def test():
    initializeUserLoginInfoDB(userDBDir, userLoginInfoTableHeaders, userLoginInfoTableName)
    loginRequests = ['{"user": "Anthony", "pass": "1234a"}',
                     '{"user": "Josuha", "pass": "1234a"}', 
                     '{"user": "Maria", "pass": "1234a"}',
                     '{"user": "Antonia", "pass": "1234a"}',
                     '{"user": "Becka","pass":"1234a"}',
                     '{"user": "Nick","pass":"1234a"}',
                     '{"user": "Steven","pass":"1234a"}',
                     '{"user": "Joseph","pass":"1234a"}',
                     '{"user": "Michael","pass":"1234a"}',
                     '{"user": "Mario","pass":"1234a"}',
                     '{"user": "Luigu","pass":"1234a"}',
                     '{"user": "Peach","pass":"1234a"}',
                     '{"user": "Daisy","pass":"1234a"}',
                     '{"user": "William","pass":"1234a"}',
                     '{"user": "Sean","pass":"1234a"}',
                     '{"user": "Rita","pass":"1234a"}']
    userCreateReq = ['{"user": "Anthony", "pword":"1234a","email":"test1@test.com"}',
                     '{"user": "Joshua", "pword":"1234a", "email":"test2@test.com"}',
                     '{"user": "Maria", "pword":"1234a", "email":"test3@test.com"}',
                     '{"user": "Antonia", "pword":"1234a", "email":"test4@test.com"}',
                     '{"user": "Becka","pword":"1234a","email":"test5@test.com"}',
                     '{"user": "Nick","pword":"1234a","email":"test6@test.com"}',
                     '{"user": "Steven","pword":"1234a","email":"test7@test.com"}',
                     '{"user": "Joseph","pword":"1234a","email":"test8@test.com"}',
                     '{"user": "Michael","pword":"1234a","email":"test9@test.com"}',
                     '{"user": "Mario","pword":"1234a","email":"test10@test.com"}',
                     '{"user": "Luigu","pword":"1234a","email":"test11@test.com"}',
                     '{"user": "Peach","pword":"1234a","email":"test12@test.com"}',
                     '{"user": "Daisy","pword":"1234a","email":"test13@test.com"}',
                     '{"user": "William","pword":"1234a","email":"test14@test.com"}',
                     '{"user": "Sean","pword":"1234a","email":"test15@test.com"}',
                     '{"user": "Rita","pword":"1234a","email":"test16@test.com"}']
    
    for userToMake in userCreateReq:
        print(verifyCriteriaAndCreateUser(userToMake))
    
    for loginRequest in loginRequests:
        print(verifyUserInformationandLogin(loginRequest))
    
    
    ## IMPORTANT ##
    ## All data returned from the user needs to be checked to make sure that it is matching for that user.
    ## IF A USER DESIDES TO MODIFY A VARIABLE GIVEN THEY COULD GET ADMIN OR ROOT PRIVLIGAES!!!
    ## THE USERNAMES NEED TO MATCH IN ALL THE JSON DATA SENT BACK!!
    ## A SPECIFIC FUNCTION NEEDS TO BE CALLED IN THE JSON THAT WILL ONLY SEND A SPECIFIC TYPE OF DATABASE REQUEST!!
    print(user_drive_database.addNewDriveToDatabase(
        [
            verifyUserAccessToDB('{"user":"Anthony"}'),
            json.dumps({"name": "testdrive", "numberOfGames": 0, "totalDriveSize": 15, "driveSizeType": "tb", "totalDriveSizeRemaining":15}),
            returnUserInformation("Anthony"), 
            returnUserInformation("Anthony")[6]
        ]
        )
        )
    
    print(user_drive_database.removeDriveFromDB([(verifyUserAccessToDB('{"user":"Joshua"}')), json.dumps({"name":"testdrive"}), returnUserInformation("Anthony"), returnUserInformation("Anthony")[6]]))
    
    print(user_drive_database.retrieveDriveFromDB([verifyUserAccessToDB('{"user":"Joshua"}'), json.dumps({"name":"testdrive"}), returnUserInformation("Anthony"), returnUserInformation("Anthony")[6]]))
    
    for loginRequest in loginRequests:
        newLoginRequest = json.loads(loginRequest)
        if newLoginRequest['user'] in usersLoggedIn:
            print(verifyUserLogoutRequestandLogOut(json.dumps({newLoginRequest["user"]:usersLoggedIn[newLoginRequest["user"]]})))
    
    print(user_drive_database.addNewDriveToDatabase([verifyUserAccessToDB('{"user":"Anthony"}'), json.dumps({"name": "testdrive", "numberOfGames": 0, "totalDriveSize": 15, "driveSizeType": "tb", "totalDriveSizeRemaining":15}), returnUserInformation("Anthony")]))
    
    print(user_drive_database.removeDriveFromDB([(verifyUserAccessToDB('{"user":"Anthony"}')), json.dumps({"name":"testdrive"}), returnUserInformation("Anthony")]))
    
test()

#TODO: Not all intended functionality has been entered into this file. Additional functionality must be added
#       for blog posts. The functionality of this file as of December 23, 2020, is complete.
#TODO: Develop blog functionality into the application.