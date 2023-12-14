import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import errorcode

class DBLink(object):
  def __init__(self, UCID=st.secrets.db_username, pwd=st.secrets.db_password, host="mysql01.arcs.njit.edu") -> None:
    self.config = {'user': '%s' %UCID, 
                   'password': '%s' %pwd, 
                   'host': '%s' %host, 
                   'database': '%s' %UCID, 
                   'raise_on_warnings': True}
    self._alias = None
    return
  
  @property
  def connection(self):
    try:
      cnx = mysql.connector.connect(**self.config)
      return cnx
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        st.error("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        st.error("Database does not exist")
      else:
        st.error(err)

  def check_CID(self):
    if st.session_state.CID:
      CID = st.session_state.CID
      df = self.query("SELECT CID FROM CUSTOMER WHERE CID = \"%s\";" %CID)
      if df.empty:
        self._logged_in = False
        st.warning("Incorrect CID. Please try again.")
      else:
        self._logged_in = True

  def get_alias(self):
    CID = st.session_state.CID
    df = self.query("SELECT * FROM CUSTOMER WHERE CID = \"%s\";" %CID)
    df = df.to_dict("index")[0]
    self._alias = df
    return

  def login_prompt(self):
    st.text_input("Enter CID:", value="10013", key="CID")
    if st.button("Login", type="primary"):
      self.check_CID()

  def logout(self):
    delattr(self, "_logged_in")

  def welcome(self):
    st.success("Login successful.")
    self.get_alias()


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
      st.error(err)

  def insert(self, cmd):
    cnx = self.connection
    try:
      cursor = cnx.cursor(dictionary=True)
      cursor.execute(cmd, multi=True)
      return
    except Exception as err:
      st.error(err)
  
  def get_products(self):
    ptypes_df = self.query("SELECT DISTINCT(PType) FROM PRODUCT;")
    ptypes = ptypes_df["PType"].sort_values().values.tolist()
    PType = st.selectbox("Select the product type to view available products", ["All"] + ptypes)
    if PType == "All":
      products_df = self.query("SELECT * FROM PRODUCT;")
      st.dataframe(products_df, use_container_width=True)
    else:
      products_df = self.query("SELECT * FROM PRODUCT WHERE PType = \"%s\";" %PType)
      st.dataframe(products_df, use_container_width=True)
    return
  
  def get_offers(self):
    ptypes_df = self.query("SELECT DISTINCT(PType) FROM PRODUCT NATURAL JOIN OFFER_PRODUCT;")
    ptypes = ptypes_df["PType"].sort_values().values.tolist()
    PType = st.selectbox("Select the product type to view available products", ["All"] + ptypes)
    if PType == "All":
      products_df = self.query("SELECT * FROM PRODUCT NATURAL JOIN OFFER_PRODUCT;")
      st.dataframe(products_df, use_container_width=True)
    else:
      products_df = self.query("SELECT * FROM PRODUCT NATURAL JOIN OFFER_PRODUCT WHERE PType = \"%s\";" %PType)
      st.dataframe(products_df, use_container_width=True)
    return
  
  def get_info(self):
    st.table(self._alias)
    return
  
  def get_cards(self):
    CID = st.session_state.CID
    cards_df = self.query("SELECT * FROM CREDIT_CARD JOIN CUSTOMER ON CREDIT_CARD.StoredCardCID = CUSTOMER.CID WHERE CREDIT_CARD.StoredCardCID = \"%s\";" %CID)
    st.dataframe(cards_df, use_container_width=True)
    return
  
  def get_address(self):
    CID = st.session_state.CID
    address_df = self.query("SELECT * FROM SHIPPING_ADDRESS WHERE CID = \"%s\";" %CID)
    st.dataframe(address_df, use_container_width=True)
    return
  
  def get_cart(self):
    CID = st.session_state.CID
    carts_df = self.query("SELECT * FROM PRODUCT NATURAL JOIN APPEARS_IN NATURAL JOIN BASKET WHERE CID = \"%s\" AND BID NOT IN (SELECT BID FROM TRANSACTION);" %CID)
    st.dataframe(carts_df, use_container_width=True)
    return
  
  def get_orders(self):
    CID = st.session_state.CID
    orders_df = self.query("SELECT * FROM TRANSACTION WHERE CID = \"%s\";" %CID)
    st.dataframe(orders_df, use_container_width=True)
    return
  
  def buy(self):
    CID = st.session_state.CID
    col1, col2 = st.columns(2)

    BID = col1.number_input("Basket ID:")
    cid = col1.number_input("Customer ID:", value=int(CID))
    SAName = col2.text_input("Shipping Address:")
    TDate = col2.date_input("Date:", value="today")
    CCNumber = col1.number_input("Card Number:")
    TTag = col2.text_input("Tag:", value = "Not Delivered")

    self.insert("INSERT INTO TRANSACTION VALUES(%d, %d, %s, %s, %d, %s);" %(BID,cid,SAName,TDate,CCNumber,TTag))
    return
