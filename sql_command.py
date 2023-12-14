import mysql.connector
import pandas as pd

def createUserAccount(userName, userPass):
    mydb = mysql.connector.connect(
        host="140.113.68.114",
        port="3306",
        user="manager",
        password="toServer111550009",
        database="db_final"
    )
    mycursor = mydb.cursor()
    sql_command = "select count(username) from user_data where username = %s;"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    cnt = int(results[0][0])
    if cnt != 0:
        print("This username has been used\nPlease choose another one.")
        mycursor.close()
        mydb.close()
        return
    sql_command = "select max(userid) from user_data"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    try:
        cnt = int(results[0][0])
    except:
        cnt = 0
    newid = str(cnt + 1);
    mytup = (newid, userName, userPass)
    sql_command = "insert into user_data values (%s, %s, %s)"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    # check
    sql_command = "select * from user_data"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    for x in results:
        print(x)
    mycursor.close()
    mydb.close()

def deleteUserAccount(userName, userPass):
    mydb = mysql.connector.connect(
        host="140.113.68.114",
        port="3306",
        user="manager",
        password="toServer111550009",
        database="db_final"
    )
    mycursor = mydb.cursor()
    sql_command = "select userid, userpassword from user_data where username = %s"
    mytup = (userName, )
    mycursor.execute(sql_command, mytup)
    results = mycursor.fetchall()
    mycursor.reset()
    if len(results) == 0:
        print("Account does not exist.\nPlease try again.")
        mycursor.close()
        mydb.close()
        return
    upass = str(results[0][1])
    uid = int(results[0][0])
    if upass != userPass:
        print("Your password is incorrect.\nPlease try again.")
        mycursor.close()
        mydb.close()
        return
    mytup = (uid, )
    sql_command = "delete from user_data where userid = %s"
    mycursor.execute(sql_command, mytup)
    mydb.commit()
    mycursor.reset()
    # check
    sql_command = "select * from user_data"
    mycursor.execute(sql_command)
    results = mycursor.fetchall()
    mycursor.reset()
    for x in results:
        print(x)
    mycursor.close()
    mydb.close()

