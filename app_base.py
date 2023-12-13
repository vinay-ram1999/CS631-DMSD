import sys
import numpy as np
import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import errorcode

class DBLink(object):
  def __init__(self, UCID=st.secrets.db_username, pwd=st.secrets.db_password, host="mysql01.arcs.njit.edu", db="vg472") -> None:
    self.config = {'user': '%s' %UCID, 
                   'password': '%s' %pwd, 
                   'host': '%s' %host, 
                   'database': '%s' %db, 
                   'raise_on_warnings': True}
    return
  
  @property
  def connection(self):
    try:
      cnx = mysql.connector.connect(**self.config)
      return cnx
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
  
  def query(self, cmd):
    cnx = self.connection
    try:
      cursor = cnx.cursor(dictionary=True)
      cursor.execute(cmd, multi=True)
      val_dict = cursor.fetchall()
      attr = cursor.column_names
      df = pd.DataFrame(columns=attr)
      for val in val_dict:
        df_val = pd.DataFrame(val, columns=list(val.keys()), index=[0])
        df = pd.concat([df, df_val], ignore_index=True)
      cnx.close()
      return df
    except Exception as err:
      print(err)
