import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Randylour0123",
    database="db_final"
)

mycursor = mydb.cursor()

mydb.commit()
mycursor.reset()
mycursor.close()
mydb.close()
