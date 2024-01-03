import mysql.connector

# Note: Please use string as all arguments' type

mydb = mysql.connector.connect(
    host="localhost",
    user="manager",
    password="toServer111550009",
    database="db_final"
)
mycursor = mydb.cursor()

def createTagList():
    global mydb, mycursor
    genreslist = list()
    taglist = list()
    sql_command = "SELECT DISTINCT genres FROM steam_basic_data"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        genreslist = str(col[0]).split(';')
        for tag in genreslist:
            if tag not in taglist:
                taglist.append(tag)
    return taglist

def resetAI(tablename):
    global mydb, mycursor
    sql_command = "ALTER TABLE "+tablename+" AUTO_INCREMENT = 1"
    mycursor.execute(sql_command)
    mydb.commit()
    mycursor.reset()

# -1: name has been used, id: new list id
def createFList(uid, listname):
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    mytup = (listname, uid)
    sql_command = "SELECT COUNT(*) FROM flist_conn_data WHERE listname = %s AND userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    if int(results[0][0]) != 0:
        return -1
    sql_command = "INSERT INTO flist_conn_data (listname, userid) VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "SELECT last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = int(results[0][0])
    return id

# -1: no flist, list[name, id]: list of flist
def showFList(uid):
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    flistlist = list()
    mytup = (uid, )
    sql_command = "SELECT COUNT(*) FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    if int(results[0][0]) == 0:
        return -1
    sql_command = "SELECT listname, listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    for col in results:
        flistlist.append([str(col[0]), int(col[1])])
    return flistlist

def deleteFList(listid):
    global mydb, mycursor
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, )
    sql_command = "DELETE FROM flist_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "DELETE FROM flist_conn_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

def deleteUserFLists(uid):
    global mydb, mycursor
    mytup = (uid, )
    sql_command = "SELECT listid FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    for col in results:
        try:
            lid = int(col[0])
            mytup = (lid, )
            sql_command = "DELETE FROM flist_data WHERE listid = %s"
            mycursor.execute(sql_command, mytup)
            mydb.commit()
            mycursor.reset()
        except:
            break
    mytup = (uid, )
    sql_command = "DELETE FROM flist_conn_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()

# 0: already in this flist, 1: success
def insertAppIntoFList(appid, listid):
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, appid)
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    cnt = int(results[0][0])
    if cnt != 0:
        return 0
    sql_command = "INSERT INTO flist_data VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: no app, list[name, id]: list of app
def showAppFromFList(listid):
    global mydb, mycursor
    if type(listid) != str:
        listid = str(listid)
    flistlist = list()
    mytup = (listid, )
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    if int(results[0][0]) == 0:
        return -1
    sql_command = "SELECT sb.name, f.appid FROM\
        (SELECT steam_basic_data.name, steam_basic_data.appid FROM steam_basic_data) AS sb INNER JOIN\
        (SELECT appid FROM flist_data WHERE listid = %s) AS f ON f.appid = sb.appid"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    for col in results:
        flistlist.append([str(col[0]), int(col[1])])
    return flistlist

# 0: not in this flist, 1: success
def deleteAppFromFList(appid, listid):
    global mydb, mycursor
    if type(appid) != str:
        appid = str(appid)
    if type(listid) != str:
        listid = str(listid)
    mytup = (listid, appid)
    sql_command = "SELECT COUNT(*) FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    cnt = int(results[0][0])
    if cnt != 0:
        return 0
    sql_command = "DELETE FROM flist_data WHERE listid = %s AND appid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: account has been used, id: new account id
def createUserAccount(userName, userPass):
    global mydb, mycursor
    sql_command = "SELECT COUNT(username) FROM user_data WHERE username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = int(results[0][0])
    if cnt != 0:
        return -1
    mytup = (userName, userPass)
    sql_command = "INSERT INTO user_data (username, userpassword) VALUES (%s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    sql_command = "SELECT last_insert_id()"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    id = int(results[0][0])
    return id

# -1: account does not exist, 0: password fail, 1: success
def deleteUserAccount(uid, userPass):
    global mydb, mycursor
    if type(uid) != str:
        uid = str(uid)
    sql_command = "SELECT * FROM user_data WHERE userid = %s"
    mytup = (uid, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        password = str(results[0][2])
    except:
        return -1
    if userPass != password:
        return 0
    deleteUserFLists(uid)
    mytup = (uid, )
    sql_command = "DELETE FROM user_data WHERE userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    return 1

# -1: account does not exist, 0: password fail, id: login
def login(userName, userPass):
    global mydb, mycursor
    sql_command = "SELECT * FROM user_data WHERE username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        id = int(results[0][0])
        password = str(results[0][2])
    except:
        return -1
    if userPass != password:
        return 0
    return id

"""
testing code
uid = createUserAccount("A","0800000123")
lid = createFList(str(uid),"MHY")
insertAppIntoFList(1610, lid)
insertAppIntoFList(1670, lid)
flist = showFList(uid)
print(flist)
flist = showAppFromFList(lid)
print(flist)
deleteUserAccount(uid,"0800000123")
resetAI("user_data")
resetAI("flist_conn_data")
"""


uid = createUserAccount("A","0800000123")
lid = createFList(str(uid),"MHY")
insertAppIntoFList(1610, lid)
insertAppIntoFList(1670, lid)
flist = showFList(uid)
print(flist)
flist = showAppFromFList(lid)
print(flist)
lid = createFList(str(uid),"MHY2")
flist = showAppFromFList(lid)
print(flist)
flist = showFList(uid)
print(flist)
deleteUserAccount(uid,"0800000123")
resetAI("user_data")
resetAI("flist_conn_data")