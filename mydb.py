#install mysql on computer
#pip install mysql
#pip install mysql-connector
#pip install mysql-conector-python

import mysql.connector

dataBase =  mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd= 'password123'
    )

#prpepare cursor object 
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL done")