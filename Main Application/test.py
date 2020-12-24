import sqlite3

testconnection = sqlite3.connect("./Database Files/userDriveInfo/Anthony.db")
curs = testconnection.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS test(test, my)")