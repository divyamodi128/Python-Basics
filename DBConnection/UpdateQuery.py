import DBConnDemo

sql = "update Emp set Income = 5000 where Age = '%d'" % (40)

DBConnDemo.ExecuteUpdate(sql)