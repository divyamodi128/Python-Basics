import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "EmployeeDetails")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS Emp")

sql = """create table Emp (
        First_Name char(20) not null,
        Last_Name char(20) not null,
        Age int,
        Sex char(1),
        Income float)"""

cursor.execute(sql)
#db.close()