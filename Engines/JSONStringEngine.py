import json
import os

#Open file containing string
#Convert string into python readable code
#make modifications
#save changes to file
#close file

#TODO: Need to add a function that deletes a game drive every time a drive is removed from the database

def remove_user_entry(jsonFileName, jsonFileDirectory, user):
    jsonData = load_database_JSON(jsonFileName, jsonFileDirectory)
    if jsonData.get(user, False) == False:
        return -1
    else:
        del jsonData[user]
        save_database_JSON(jsonFileName, jsonFileDirectory, jsonData)
        return 0


def remove_user_database_entry(jsonFileName, jsonFileDirectory, user, databaseName):
    jsonData = load_database_JSON(jsonFileName, jsonFileDirectory)
    if jsonData.get(user, False) == False:
        return -1
    else:
        if jsonData[user].get(databaseName, False) == False:
            return -1
        else:
            del jsonData[user][databaseName]
            save_database_JSON(jsonFileName, jsonFileDirectory, jsonData)
            return 0


def retrieve_json_property(jsonFileName=str, jsonFileDirectory=str, tableLayoutName=str, tableLayoutPropertyName=str):
    jsonData = load_database_JSON(jsonFileName, jsonFileDirectory)
    if jsonData.get(tableLayoutName, False) == False:
        return -1
    else:
        if jsonData[tableLayoutName].get(tableLayoutPropertyName, False) == False:
            return -2
        else:
            return jsonData[tableLayoutName][tableLayoutPropertyName]


def retrieve_all_database_entries(jsonFileName=str, jsonFileDirectory=str, table=str):
    jsonData = load_database_JSON(jsonFileName, jsonFileDirectory)
    if jsonData.get(table, False) == False:
        return -1
    else:
        return jsonData[table]


def add_or_modify_user_database_entry(jsonFileName=str, jsonFileDirectory=str, user=str, databaseName=str,newData=dict):
    jsonData = load_database_JSON(jsonFileName, jsonFileDirectory)
    if jsonData.get(user, False) ==False:
        return -1
    else:
        if jsonData[user].get(databaseName, False) ==False:
            jsonData[user][databaseName] = newData
            save_database_JSON(jsonFileName, jsonFileDirectory, jsonData)
            return 0
        else:
            return -2


def add_or_modify_user_entry(jsonFileName=str, jsonFileDirectory=str, user=str, newData=dict):
    jsonData = load_database_JSON(jsonFileName, jsonFileDirectory)
    if jsonData.get(user, False) !=False:
        return -1
    else:
        jsonData[user] = newData
        save_database_JSON(jsonFileName, jsonFileDirectory, jsonData)
        return 0


def load_database_JSON(jsonFileName, jsonFileDirectory):
    with open (jsonFileDirectory+jsonFileName, 'r') as jsonFile:
        return json.load(jsonFile)


def save_database_JSON(jsonFileName, jsonFileDirectory, jsonDataToWrite):
    with open (jsonFileDirectory+jsonFileName, "w+") as jsonFile:
        json.dump(jsonDataToWrite, jsonFile, indent=4)
    return 0


def databaseDictionaryFormatter(userName, databaseDir, databasePurpose, tableNames):
    retDict = {
        str(userName)+"_s_"+str(databasePurpose)+".db":{
            "Database Type": databasePurpose,
            "Database Directory": databaseDir,
            "Database Tables": tableNames
        }
    }
    return retDict

#[
#   userName,
#   databaseDir,
#   databasePurpose,
#       {
#           table_name1: [header1, header2, header3, ..., headerN],
#           table_name2: [header1, header2, header3, ..., headerN],
#           table_name3: [header1, header2, header3, ..., headerN],
#           ...,
#           table_nameN: [header1, header2, header3, ..., headerN]
#       }
#]
#databaseDictionaryFormatter("Anthony", "./JSON Data/", "Games", [])
#add_or_modify_database_entry("database_info.json", "./JSON Data/", "Anthony", "Anthony_s_Games.db", databaseDictionaryFormatter("Anthony", "./JSON Data/", "Games", []))


#print(add_or_modify_user_entry("database_info.json", "./JSON Data/", "Joshua", dbentry))
#print(add_or_modify_user_entry("database_info.json", "./JSON Data/", "Joshua", dbentry))
#print(remove_database_entry("database_info.json", "./JSON Data/", "Joshua"))
#print(retrieve_all_database_entrys("database_info.json", "./JSON Data/","Anthony"))
#print(retrieve_database_entry("database_info.json", "./JSON Data/","Anthony", "Anthony_s_Drives.db"))
#jsonDataNow = load_database_JSON("database_info.json", "./JSON Data/")
#print(jsonDataNow.get("Joshua", False) != False)