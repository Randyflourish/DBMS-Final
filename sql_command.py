import mysql.connector

# Note: Please use string as all arguments' type

mydb = mysql.connector.connect(
    host="localhost",
    user="manager",
    password="toServer111550009",
    database="db_final"
)
mycursor = mydb.cursor()

# (id): new list id
def createFList(uid, listname):
    global mydb, mycursor
    mytup = (listname, uid)
    sql_command = "insert into flist_conn_data (listname, userid) values (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "select last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = int(results[0][0])
    return id

def deleteFList(listid):
    global mydb, mycursor
    mytup = (listid, )
    sql_command = "delete from flist_data where listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "delete from flist_conn_data where listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

def deleteUserFLists(uid):
    global mydb, mycursor
    mytup = (uid, )
    sql_command = "select listid from flist_conn_data where userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        try:
            lid = int(col[0])
            mytup = (lid, )
            sql_command = "delete from flist_data where listid = %s"
            mycursor.execute(sql_command, mytup)
            mydb.commit()
            mycursor.reset()
        except:
            break
    mytup = (uid, )
    sql_command = "delete from flist_conn_data where userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

# -1: account has been used (id): new account id
def createUserAccount(userName, userPass):
    global mydb, mycursor
    sql_command = "select count(username) from user_data where username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = int(results[0][0])
    if cnt != 0:
        print("This username has been used\nPlease choose another one.")
        return -1
    mytup = (userName, userPass)
    sql_command = "insert into user_data (username, userpassword) values (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "select last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = int(results[0][0])
    return id

# -1: account does not exist 0: password fail 1: success
def deleteUserAccount(uid, userPass):
    global mydb, mycursor
    sql_command = "select * from user_data where userid = %s"
    mytup = (uid, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        password = str(results[0][2])
    except:
        print("Account does not exist.\nPlease try again.")
        return -1
    if userPass != password:
        print("Password Incorrect.\nPlease try again.")
        return 0
    deleteUserFLists(uid)
    mytup = (uid, )
    sql_command = "delete from user_data where userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: account does not exist 0: password fail (id): login
def login(userName, userPass):
    global mydb, mycursor
    sql_command = "select * from user_data where username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        id = int(results[0][0])
        password = str(results[0][2])
    except:
        print("Account does not exist.\nPlease try again.")
        return -1
    if userPass == password:
        print("Success.\n")
        return id
    else:
        print("Password Incorrect.\nPlease try again.")
        return 0

"""
testing data
createUserAccount("A","0800000123")
deleteUserAccount("1","0800000123")
createFList(str(uid),"MHY")
"""
