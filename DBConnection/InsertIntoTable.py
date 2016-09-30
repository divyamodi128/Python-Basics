import DBConnDemo

# db = DBConnDemo.ConnectDB()
sql = """insert into Emp(
        First_Name, Last_Name, Age, Sex, Income)
       VALUES ('%s', '%s', '%d', '%c', '%d')""" % \
      ('Mac', 'Mohan', 20, 'M', 2000)
# print sql
# cursor = db.cursor()

DBConnDemo.ExecuteUpdate(sql)
# disconnect from server
# db.close()