import DBConnDemo

sql = "select * from Emp where Income > '%d'" % (1000)

DBConnDemo.Execute(sql)