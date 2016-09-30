import DBConnDemo

sql = "delete from Emp WHERE Age = '%d'" % (20)

DBConnDemo.ExecuteUpdate(sql)