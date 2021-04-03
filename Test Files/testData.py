import __init__
from Engines import userVerificationEngine, JSONStringEngine

#database names
databaseNameForUsers = "userLoginInfo.db"
#database layouts
userLoginInfoTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "UserLoginInfo")
driveDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Drives")
gameDatabaseTBLayout = JSONStringEngine.retrieve_all_database_entries("database_info.json", "./JSON Data/", "Games")


#initial things that are required to be run when the server starts go here
#DatabaseController.database_initialization(databaseNameForUsers, userLoginInfoTBLayout)

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
        "Username":"Tdeves1",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"userVerificationEngine.create_drive_entry(*jsonData['args'])",
        "for":"User",
        "args":["Tdeves1.db", driveDatabaseTBLayout, driveInfo[0]]
    },
    {
        "Username":"Bold",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Bold.db", driveDatabaseTBLayout, driveInfo[1]]
    },
    {
        "Username":"Frozen07",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Frozen07.db", driveDatabaseTBLayout, driveInfo[2]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[3]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[4]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[5]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[6]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[7]]
    },
    {
        "Username":"Fantasy89",
        "ID":"0",
        "Login":"0",
        "AccessLevel":"Root",
        "function required":"driveDatabaseController.create_drive_entry(*jsonData['args'])",
        "for":"drive",
        "args":["Fantasy89.db", driveDatabaseTBLayout, driveInfo[8]]
    }
]


users = [
    {
        "Username":"Fantasy89",
        "Password":"abc123",
        "Email":"test1@test.com",
        "ID":"1",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Color",
        "AnswerQ1":"Purple",
        "SecurityQ2":"Hot",
        "AnswerQ2":"YEA",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"Tdeves1",
        "Password":"abc123",
        "Email":"test2@test.com",
        "ID":"2",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Fruit",
        "AnswerQ1":"Apple",
        "SecurityQ2":"Cold",
        "AnswerQ2":"Nah",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"goldeneye5671",
        "Password":"abc123",
        "Email":"test3@test.com",
        "ID":"3",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Veggie",
        "AnswerQ1":"Tomato",
        "SecurityQ2":"Music",
        "AnswerQ2":"Piano",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"geye5671",
        "Password":"abc123",
        "Email":"test4@test.com",
        "ID":"4",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Pet",
        "AnswerQ1":"Rabbit",
        "SecurityQ2":"Food",
        "AnswerQ2":"Meatballs",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"Bold",
        "Password":"abc123",
        "Email":"test5@test.com",
        "ID":"5",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Music",
        "AnswerQ1":"Alternative",
        "SecurityQ2":"Friend",
        "AnswerQ2":"I love the homies",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"TonyMAC",
        "Password":"abc123",
        "Email":"test6@test.com",
        "ID":"6",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Book",
        "AnswerQ1":"The Hungry Games",
        "SecurityQ2":"Console",
        "AnswerQ2":"Amiga",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"TonyPC",
        "Password":"abc123",
        "Email":"test7@test.com",
        "ID":"7",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Hyper",
        "AnswerQ1":"Nah dude",
        "SecurityQ2":"Pet",
        "AnswerQ2":"Dog",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"TonyiOS",
        "Password":"abc123",
        "Email":"test8@test.com",
        "ID":"8",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Console",
        "AnswerQ1":"Switch",
        "SecurityQ2":"Android",
        "AnswerQ2":"Hell na",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"TonyAndroid",
        "Password":"abc123",
        "Email":"test9@test.com",
        "ID":"9",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Color",
        "AnswerQ1":"Blue",
        "SecurityQ2":"State",
        "AnswerQ2":"NY",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"TimApple",
        "Password":"abc123",
        "Email":"test10@test.com",
        "ID":"10",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Fruit",
        "AnswerQ1":"Apple",
        "SecurityQ2":"Game",
        "AnswerQ2":"Bioshok: Infaninte",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"TheDankestPods",
        "Password":"abc123",
        "Email":"test11@test.com",
        "ID":"11",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Veggie",
        "AnswerQ1":"Artichoke",
        "SecurityQ2":"Streamer",
        "AnswerQ2":"Nope",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"FrozenBuds",
        "Password":"abc123",
        "Email":"test12@test.com",
        "ID":"12",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"iOS",
        "AnswerQ1":"NO",
        "SecurityQ2":"Social",
        "AnswerQ2":"Twitter",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"AvitarMaster",
        "Password":"abc123",
        "Email":"test13@test.com",
        "ID":"13",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Android",
        "AnswerQ1":"...maybe",
        "SecurityQ2":"Veggie",
        "AnswerQ2":"Cucumber",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"dank_meme_god",
        "Password":"abc123",
        "Email":"test14@test.com",
        "ID":"14",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Music",
        "AnswerQ1":"Pop",
        "SecurityQ2":"Fruit",
        "AnswerQ2":"Tomato",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"CommandMan",
        "Password":"abc123",
        "Email":"test15@test.com",
        "ID":"15",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Color",
        "AnswerQ1":"Green",
        "SecurityQ2":"Friend",
        "AnswerQ2":"Meh...maybe...",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"OneNastyBoi",
        "Password":"abc123",
        "Email":"test16@test.com",
        "ID":"16",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Fruit",
        "AnswerQ1":"Moldy Orange",
        "SecurityQ2":"state",
        "AnswerQ2":"CA",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"MadGuy",
        "Password":"abc123",
        "Email":"test17@test.com",
        "ID":"17",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Music",
        "AnswerQ1":"Clasic Rock",
        "SecurityQ2":"Color",
        "AnswerQ2":"teal",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"SadGuy",
        "Password":"abc123",
        "Email":"test18@test.com",
        "ID":"18",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Book",
        "AnswerQ1":"Im catching fire now!",
        "SecurityQ2":"Cat",
        "AnswerQ2":"Allergic",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"ShyGuy",
        "Password":"abc123",
        "Email":"test19@test.com",
        "ID":"19",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Hobby",
        "AnswerQ1":"Singing",
        "SecurityQ2":"Car",
        "AnswerQ2":"Audi",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"MarioMario",
        "Password":"abc123",
        "Email":"test120@test.com",
        "ID":"120",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Pet",
        "AnswerQ1":"Mouse",
        "SecurityQ2":"Hobby",
        "AnswerQ2":"Racing",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"Luigi Mario",
        "Password":"abc123",
        "Email":"test121@test.com",
        "ID":"121",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"PC",
        "AnswerQ1":"Nah",
        "SecurityQ2":"Hobby",
        "AnswerQ2":"Dancing",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"H20Delerious",
        "Password":"abc123",
        "Email":"test122@test.com",
        "ID":"122",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Apple",
        "AnswerQ1":"Yeah bro",
        "SecurityQ2":"Hobby",
        "AnswerQ2":"Writting Books",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"VannossGaming",
        "Password":"abc123",
        "Email":"test124@test.com",
        "ID":"123",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Friend",
        "AnswerQ1":"I have none",
        "SecurityQ2":"PC",
        "AnswerQ2":"base",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"iwantausername",
        "Password":"abc123",
        "Email":"test125@test.com",
        "ID":"124",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Color",
        "AnswerQ1":"Brown",
        "SecurityQ2":"PC",
        "AnswerQ2":"laptop",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"ohforcryingoutloudgivemeausername",
        "Password":"abc123",
        "Email":"test131@test.com",
        "ID":"125",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Veggie",
        "AnswerQ1":"Lettuce",
        "SecurityQ2":"Apple",
        "AnswerQ2":"No",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"Zeldom",
        "Password":"abc123",
        "Email":"test130@test.com",
        "ID":"126",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Shinny",
        "AnswerQ1":"Swoard",
        "SecurityQ2":"Apple",
        "AnswerQ2":"No",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"gameranks",
        "Password":"abc123",
        "Email":"test126@test.com",
        "ID":"127",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Car",
        "AnswerQ1":"VW",
        "SecurityQ2":"Apple",
        "AnswerQ2":"No",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"Stonks",
        "Password":"abc123",
        "Email":"test127@test.com",
        "ID":"128",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Music",
        "AnswerQ1":"Jazz",
        "SecurityQ2":"Car",
        "AnswerQ2":"No",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"Optimus",
        "Password":"abc123",
        "Email":"test128@test.com",
        "ID":"129",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Warm",
        "AnswerQ1":"NO!",
        "SecurityQ2":"Car",
        "AnswerQ2":"No",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
    {
        "Username":"OptimusPrime",
        "Password":"abc123",
        "Email":"test129@test.com",
        "ID":"1230",
        "Login":"0",
        "AccessLevel":"Basic",
        "SecurityQ1":"Cold",
        "AnswerQ1":"maybe...",
        "SecurityQ2":"Car",
        "AnswerQ2":"No",
        "SecurityQ3":"",
        "AnswerQ3":""
    },
]


listOfRandInts = []

for item in users:
    print(userVerificationEngine.verify_user_creation(item))
    # print(userVerificationEngine.verify_password_reset({usr:item[usr], eml:item[eml]}))
    # item["Authority"] = userVerificationEngine.initiate_password_reset(item)
    # item["NewPassword"] = "ZYX987"
    # item[psw] = "ZYX987"
    # userVerificationEngine.update_password(item)
    values = userVerificationEngine.verify_user_login(item)
    if type(values) ==list:
        item[rndID] = values[1]
        item[login] = int(values[0])
    #     print(userVerificationEngine.verify_user_logout(item)) 
    #     print(userVerificationEngine.delete_account(userVerificationEngine.conf, item[usr]))
    # else:
    #     print(values)
# print(users)


# print(userVerificationEngine.verify_password_reset({"Username":"OptimusPrime","Email":"test129@test.com"}))
# canIReset = userVerificationEngine.initiate_password_reset({"Username":"OptimusPrime","Email":"test129@test.com", a1:"maybe...",a2:"No",a3:""})
# userVerificationEngine.update_password({"Authority":canIReset, usr:"OptimusPrime", psw:"abc123456789"})
#print(userVerificationEngine.update_password())
