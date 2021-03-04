import __init__

import sqlite3
import os
from Engines import databaseStringEngine

def createDatabaseConnections(database_name, database_directory):
    connection = sqlite3.connect(database_directory + database_name)
    curs = connection.cursor()
    return [connection, curs]


def create_database(database_name, database_directory):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[0].commit()
    databaseConnections[1].close()

def delete_database(database_name, database_directory):
    os.remove(database_directory + database_name)


def create_table(database_name, database_directory, tableName, tableHeader_list):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.create_table(tableName, tableHeader_list))
    databaseConnections[0].commit()
    databaseConnections[1].close()


def delete_table(database_name, database_directory, tableName):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.delete_table(tableName))
    databaseConnections[0].commit()
    databaseConnections[1].close()


def insert_row(database_name, database_directory, tableName, tableHeader_list):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.insert_into_table(tableName, tableHeader_list))
    databaseConnections[0].commit()
    databaseConnections[1].close()


def delete_row(database_name, database_directory, tableName, selectCriteria_list):
    databaseConnections = createDatabaseConnections(database_name, database_directory)
    databaseConnections[1].execute(databaseStringEngine.delete_table_row(tableName, selectCriteria_list))
    databaseConnections[0].commit()
    databaseConnections[1].close()