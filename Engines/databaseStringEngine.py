#What I want this file to do:
#   This file will create sql string commands to be used by other files.
#   This file is not intended to create querrys to the database, only to make strings to be used by querrys in other programs


def check(tableHeaders):
    if len(tableHeaders) == 0:
        return False
    else:
        for tableHeader in tableHeaders:
            if tableHeaders.count(tableHeader) > 1:
                return False
    return True


#What I want this to do:
#   I want this to create a table in a database with the name given and the table headers given
def create_table(tableName, tableHeaders):
    if check(tableHeaders):
        command='CREATE TABLE IF NOT EXISTS ' + str(tableName) + '('
        for i in range(0, len(tableHeaders)):
            command += str(tableHeaders[i])
            if i != len(tableHeaders)-1:
                command += ', '
        command += ')'
        return command
    else:
        return check(tableHeaders)


#What I want this to do:
#   I want this to delete a table in a database with the given name and table headers given
def delete_table_row(tableName, selectCriteria):
    if check(selectCriteria):
        command = 'DELETE FROM ' + tableName + ' WHERE '
        for i in range(0, len(selectCriteria)):
            command += (str(selectCriteria[i]) + ' = ?')
            if i != len(selectCriteria)-1:
                command += " AND "
        return command
    else:
        return check(selectCriteria)


def delete_table(tableName):
    command = 'DROP TABLE ' + tableName
    return command

#what I want this to do:
#   I want this to search a table in a database with the given table name and table headers and select the items in the table that match the criteria
#   
#   searchCriteria should be a list
#   [tableHeader,
#    anotherTableHeader,
#   ...]
#   The select terms should be organized from most sugnificant select criteria to least sugnificant select criteria
def select_table(tableName, selectType, selectCriteria):
    if check(selectCriteria):
        command = "SELECT " + str(selectType) + " FROM " + str(tableName) +" WHERE "
        for i in range(0, len(selectCriteria)):
            command += (str(selectCriteria[i]) + ' = ?')
            if i != len(selectCriteria)-1:
                command += " AND "
        return command
    else:
        return check(selectCriteria)


def select_table_or(tableName, selectType, selectCriteria):
    if check(selectCriteria):
        command = "SELECT " + str(selectType) + " FROM " + str(tableName) +" WHERE "
        for i in range(0, len(selectCriteria)):
            command += (str(selectCriteria[i]) + ' = ?')
            if i != len(selectCriteria)-1:
                command += " OR "
        return command
    else:
        return check(selectCriteria)


def select_entire_table(tableName):
    return "SELECT * FROM " + tableName

def insert_into_table(tableName, tableHeaders):
    if check(tableHeaders):
        command = 'INSERT INTO ' + tableName + '('
        for i in range (0, len(tableHeaders)):
            command += tableHeaders[i]
            if i != len(tableHeaders)-1:
                command += ', '
        command += ') VALUES ('
        for i in range (0, len(tableHeaders)):
            command += '?'
            if i != len(tableHeaders)-1:
                command += ','
        command += ')'
        return command


#print (insert_into_table("testTable", ["a", 'b', 'c']))
