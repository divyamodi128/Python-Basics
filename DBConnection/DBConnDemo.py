import MySQLdb

def ConnectDB():
    db = MySQLdb.connect("localhost", "root", "root", "EmployeeDetails")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print "Database version : %s" % data
    # db.close()
    return db

def ExecuteUpdate(sql):
    db = ConnectDB()
    cursor = db.cursor()
    try:
        # Execute the SQL command
        cursor.execute(sql)
        print sql
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    finally:
        db.close()

def Execute(sql):
    db = ConnectDB()
    cursor = db.cursor()
    # try:
    cursor.execute(sql)
    print sql

    print cursor.rowcount
    rs1 = cursor.fetchone()
    # print rs1
    # for row in rs1:
    print "%s %s %d %c %f" % (rs1[0], rs1[1], rs1[2], rs1[3], rs1[4])

    rs2 = cursor.fetchall()
    for row in rs2:
        print "%s %s %d %c %.2f" % (row[0], row[1], row[2], row[3], row[4])

    # except:
    #     print "Error: unable to fecth data"
    # finally:
    db.close()


