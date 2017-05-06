import sqlite3 as sql
import sys

sqlFile = 'data.db'
connection = sql.connect(sqlFile)
c = connection.cursor()
c.execute('''CREATE TABLE data(type varchar(1), year varchar(2), 
	month varchar(2), day varchar(2), hour varchar(2), min varchar(2), sec varchar(2))''')

connection.close()