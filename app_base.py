import streamlit as st
import mysql.connector
from mysql.connector import errorcode

#UCID = str(input("Please enter your NJIT UCID: "))
#pwd = str(input("Please enter your NJIT Database password: "))
UCID = "vg472"
pwd = "nagaValli@2023"

config = {
  'user': '%s' %UCID,
  'password': '%s' %pwd,
  'host': 'mysql01.arcs.njit.edu',
  'database': '%s' %UCID,
  'raise_on_warnings': True
}

try:
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
