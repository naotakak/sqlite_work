'''
Naotaka Kinoshita
SoftDev1 pd 7
HW09 -- No Treble
2017-10-16
'''

import csv, sqlite3

##set database name
database = "things.db"

db = sqlite3.connect(database)
c = db.cursor()

##create both tables
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

##open peeps.csv file and read
reader = csv.DictReader(open("peeps.csv"))
for row in reader:
    print row
    ##populate table
    c.execute("INSERT INTO peeps VALUES ('" + row['name'] + "'," + row['age'] + "," + row['id'] + ")")

##open courses.csv file and read
reader = csv.DictReader(open("courses.csv"))
for row in reader:
    print row
    ##populate table
    c.execute("INSERT INTO courses VALUES ('" + row['code'] + "'," + row['mark'] + "," + row['id'] + ")")

##save and close database
db.commit()
db.close()
