import sqlite3
import json
import random
import os

userDBDir = "./Database Files/userLoginInfo/userLoginInfo.db"
user_game_info_dir = "./Database Files/usersGameInfo/"
userLoginInfoTableName = "loginInfo"
userLoginInfoTableHeaders = ['uname', 'pword', 'email', 'dir', 'acc_lev']
#expected layout of this var:
#{uname: [dir, acc_lev, uniqueIdentifier(should be saved as a cookie through the browser, uniquely generated and checked to grant data access)]}
usersLoggedIn = {}

#because this is used many times it doesn't make sense to open and close this constantly. Just leave it open untill a server hault is called and close the database.
userLoginInfoConnection = sqlite3.connect(userDBDir)
userLoginInfoCursor = userLoginInfoConnection.cursor()

#when creating table the function is only expecting a length of 4 for the list of headers
def initializeUserLoginInfoDB(dir, listOfHeaders, userLoginInfoTblName):
    if len(listOfHeaders) == 5:
        userLoginInfoConnection = sqlite3.connect(userDBDir)
        userLoginInfoCursor = userLoginInfoConnection.cursor()
        userLoginInfoCursor.execute("""CREATE TABLE IF NOT EXISTS """ + userLoginInfoTblName + """(""" + userLoginInfoTableHeaders[0] + ", " + userLoginInfoTableHeaders[1] + ", " + userLoginInfoTableHeaders[2] + ", " + userLoginInfoTableHeaders[3] + ", " + userLoginInfoTableHeaders[4] + """)""")
        return "Table initialized successfully"
    else:
        return "Error on table creation. The length of listOfHeaders is " + listOfHeaders.length + "and not the expected value of 4"


#JSON data expected in the following format:
#{user: uname, pass: pword}
#the information will be hashed. No unhashed data will be stored on the server.
#the data that will be sent will already be hashed
#if the uname/pword does not match anything in the database then an error JSON
#string will be sent in the following format:
#{errorcode: -1, desc: "uname/pasword either doesn't exist or information entered is incorrect"}
def verifyUserInformationandLogin(json_data):
    userLoginInfoRecieved = json.loads(json_data)
    userLoginInfoRecievedFromDB = userLoginInfoCursor.execute("SELECT * FROM " + userLoginInfoTableName + " WHERE " + userLoginInfoTableHeaders[0] + " = ?", (userLoginInfoRecieved["user"],)).fetchall()
    if -1 < len(userLoginInfoRecievedFromDB) < 1:
        return '{"errorcode": -1, "desc": "uname does not exist or information is incorrect"}'
    elif len(userLoginInfoRecievedFromDB) > 1:
        return '{"errorcode": -1, "desc": "duplicate uname found in database. Database Check needed"}'
    else:
        recievedUserInfo = list(userLoginInfoRecievedFromDB[0])
        if recievedUserInfo[1] == userLoginInfoRecieved["pass"]:
            randomIdentifier = random.randint(1, 100000000)
            usersLoggedIn[recievedUserInfo[0]] = [*recievedUserInfo, randomIdentifier]
            return json.dumps({recievedUserInfo[0]: [*recievedUserInfo, randomIdentifier]})
        else:
            return '{"errorcode": -1, "desc": "pword does not exist or information is incorrect"}'


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
def verifyCriteriaAndCreateUser(json_data):
    #needs a unique username and email. Accesslv will be a number. 0 represents a normal user and 1 represents a user with privleged access. Numbers can be added as program progresses
    userLoginInfoRecieved = json.loads(json_data)
    usersWithUsernameAndemail = userLoginInfoCursor.execute("SELECT * FROM " + userLoginInfoTableName + " WHERE " + userLoginInfoTableHeaders[0] + " = ? OR " + userLoginInfoTableHeaders[2] + " = ?", (userLoginInfoRecieved["user"], userLoginInfoRecieved["email"])).fetchall()
    if len(usersWithUsernameAndemail) > 0:
        checkingUserOut = list(usersWithUsernameAndemail[0])
        if checkingUserOut[0] == userLoginInfoRecieved["user"] and checkingUserOut[2] == userLoginInfoRecieved["email"]:
            return '{"errorcode":"-1", "desc":"username and email already in use"}'
        elif checkingUserOut[0] == userLoginInfoRecieved["user"] and checkingUserOut[1] != userLoginInfoRecieved["email"]:
            return '{"errorcode":"-1", "desc":"username already in use"}'
        elif checkingUserOut[0] != userLoginInfoRecieved["user"] and checkingUserOut[2] == userLoginInfoRecieved["email"]:
            return '{"errorcode":"-1", "desc":"email already in use"}'
        else:
             return '{"errorcode":"-1", "desc":"unknown error. Please contact support"}'
    else:
        userLoginInfoCursor.execute("INSERT INTO " + userLoginInfoTableName + " VALUES (?,?,?,?,?)", (userLoginInfoRecieved["user"], userLoginInfoRecieved["pword"], userLoginInfoRecieved["email"], "./userDriveInfo/" + userLoginInfoRecieved["user"], 0))
        sqlite3.connect(user_game_info_dir+userLoginInfoRecieved["user"])
        userLoginInfoConnection.commit()
        return '{success: "user created successfully"}'

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
                        userLoginInfoCursor.execute('DELETE FROM ' + userLoginInfoTableName + ' WHERE uname = ? AND email = ? AND dir = ?', (userLoginInfoRecieved["user"], userLoginInfoRecieved["email"], checkingUserOut[3]))
                        userLoginInfoConnection.commit()
                        os.remove(user_game_info_dir+userLoginInfoRecieved["user"])
            #log the user out/
            #delete the user from the database/
            #delete the database file created when the user was created/
            #delete any posts that the user may have posted on the blog ( cannot do yet blog not implemented yet)
        else:
            return '{"errorcode":"-1", "desc": "Internal error. Please contact support."}'
            # Return an error that there has been an internal error and the user must contact support to proceed
    else:
        return '{"errorcode":"-1", "desc":"The user does not exist"}'




#def setUserParameters(uname, dir, accsess_lev)

#format of the json data:
#{uname: uname, }
def verifyUserAccessToDB(json_data):
    userLoginInfoRecieved = json.loads(json_data)
    userLoginInfoFromDB = userLoginInfoCursor.execute("SELECT * FROM " + userLoginInfoTableName + " WHERE " + userLoginInfoTableHeaders[0] + " = ? OR " + userLoginInfoTableHeaders[2] + " = ?", (userLoginInfoRecieved["user"], userLoginInfoRecieved["email"])).fetchall()
    if 0 < len(userLoginInfoRecieved) < 2:
        checkingUserOut = list(userLoginInfoFromDB)
        if checkingUserOut[4] == 0:
            return '{"accesslevel":"basic"}'
        elif checkingUserOut[4] == 1:
            return '{"accesslevel":"advanced"}'
        elif checkingUserOut[4] == 2:
            return '{"accesslevel":"administraitor"}'
        else:
            return '{"errorcode":"-1", "desc":"accesslevel var out of range"}'


initializeUserLoginInfoDB(userDBDir, userLoginInfoTableHeaders, userLoginInfoTableName)
loginRequests = ['{"user": "Anthony", "pass": "1234a"}', '{"user": "Joshua", "pass": "12345a"}', '{"user": "Maria", "pass": "123456a"}', '{"user": "Antonia", "pass": "1234567a"}']
userCreateReq = ['{"user": "Anthony", "pword":"1234a", "email":"test1@test.com"}', '{"user": "Joshua", "pword":"12345a", "email":"test2@test.com"}', '{"user": "Maria", "pword":"123456a", "email":"test3@test.com"}', '{"user": "Antonia", "pword":"1234567a", "email":"test4@test.com"}']

for userToMake in userCreateReq:
    print(verifyCriteriaAndCreateUser(userToMake))
for loginRequest in loginRequests:
    print(verifyUserInformationandLogin(loginRequest))
#   {user: uname, email: email, randID: number}
#print('{"user":"Anthony", "email":"test1@test.com", "randID": "'+str(usersLoggedIn['Anthony'][5])+'"}')
#verifyAndDestroyUser('{"user":"Anthony", "email":"test1@test.com", "randID": "'+str(usersLoggedIn['Anthony'][5])+'"}')
#verifyAndDestroyUser('{"user":"Maria", "email":"test3@test.com", "randID": "'+str(usersLoggedIn['Maria'][5])+'"}')
#verifyAndDestroyUser('{"user":"Joshua", "email":"test2@test.com", "randID": "'+str(usersLoggedIn['Joshua'][5])+'"}')
#verifyAndDestroyUser('{"user":"Antonia", "email":"test4@test.com", "randID": "'+str(usersLoggedIn['Antonia'][5])+'"}')
#verifyAndDestroyUser('{"user":"Anthony", "email":"test1@test.com", "randID": "123456789"}')
