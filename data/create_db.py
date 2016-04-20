#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('septweather_db')
print "Opened database successfully";

conn.execute('''CREATE TABLE FAVOURITES
        (ID        INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME  TEXT NOT NULL,
		 URL	TEXT NOT NULL);''')
print "Table created successfully";

conn.close()