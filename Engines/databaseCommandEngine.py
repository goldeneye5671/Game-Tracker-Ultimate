import __init__

import sqlite3
import os
from Engines import databaseStringEngine

def createDatabaseConnections(database_name=str, database_directory=str):
    connection = sqlite3.connect(database_directory + database_name)
    curs = connection.cursor()
    return [connection, curs]


def create_database(database_name=str, database_directory=str):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[0].commit()
    databaseConnections[1].close()

def delete_database(database_name=str, database_directory=str):
    os.remove(database_directory + database_name)


def create_table(database_name=str, database_directory=str, tableName=str, tableHeader_list=list):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.create_table(tableName, tableHeader_list))
    databaseConnections[0].commit()
    databaseConnections[1].close()


def delete_table(database_name=str, database_directory=str, tableName=str):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.delete_table(tableName))
    databaseConnections[0].commit()
    databaseConnections[1].close()



def retrieve_table(database_name=str, database_directory=str, tableName=str):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    selectCriteriaQuerry = databaseConnections[1].execute(databaseStringEngine.select_entire_table(tableName)).fetchall()
    databaseConnections[1].close()
    return selectCriteriaQuerry



def insert_row(database_name=str, database_directory=str, tableName=str, tableHeader_list=list, insertionValues_list=list):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.insert_into_table(tableName, tableHeader_list), tuple(insertionValues_list))
    databaseConnections[0].commit()
    databaseConnections[1].close()


def delete_row(database_name=str, database_directory=str, tableName=str, selectCriteria_list=list):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.delete_table_row(tableName, selectCriteria_list))
    databaseConnections[0].commit()
    databaseConnections[1].close()


def retrieve_row(database_name=str, database_directory=str, tableName=str, selectCriteria_dict=dict):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    selectCriteriaQuerry = databaseConnections[1].execute(databaseStringEngine.select_table(tableName, "*", list(selectCriteria_dict.keys())), tuple(selectCriteria_dict.values())).fetchall()
    databaseConnections[1].close()
    return selectCriteriaQuerry

def retrieve_row_or(database_name=str, database_directory=str, tableName=str, selectCriteria_dict=dict):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    selectCriteriaQuerry = databaseConnections[1].execute(databaseStringEngine.select_table_or(tableName, "*", list(selectCriteria_dict.keys())), tuple(selectCriteria_dict.values())).fetchall()
    databaseConnections[1].close()
    return selectCriteriaQuerry

def retrieve_all_table_names(database_name=str, database_directory=str):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    retrievedData=databaseConnections[1].execute("""SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name""").fetchall()
    retVal=[]
    for item in retrievedData:
        retVal.append(item[0])
    return retVal


def update_table_at_spot(): return None
