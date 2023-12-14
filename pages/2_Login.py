import sys
import path
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)
from app_base import *

DB = DBLink()

st.set_page_config(page_title="Login",
                   page_icon=":shopping_trolley:",
                   layout="wide",
                   menu_items = {"About": "Source: https://github.com/vinay-ram1999/CS631-DMSD",
                                 "Report a Bug": "mailto:vinayramgazula@gmail.com"})

st.title("Login")

with st.expander("About", expanded=True):
    st.markdown("If you are already a customer at eComputerStore please login using your customer ID.")

DB.login_prompt()

if hasattr(DB, "_logged_in") and DB._logged_in:
    DB.welcome()

    tab1, tab2, tab3, tab4 = st.tabs(["Info", "Cart", "My Orders", "Logout"])

    with tab1:
        DB.get_info()
        if st.checkbox("Show saved cards", value=True):
            DB.get_cards()
        if st.checkbox("Show saved shipping addresses", value=True):
            DB.get_address()

    with tab2:
        DB.get_cart()
        
        col1, col2 = st.columns(2)

        BID = col1.number_input("Basket ID:")
        cid = col1.number_input("Customer ID:")
        SAName = col1.text_input("Shipping Address:")
        TDate = col2.date_input("Date:", value="today")
        CCNumber = col2.number_input("Card Number:")
        TTag = col2.text_input("Tag:", value = "Not Delivered")

        if st.checkbox("BUY", value=True):
            #cmd = "INSERT INTO TRANSACTION VALUES(%d, %d, \"%s\", \"%s\", %d, \"%s\");" %(BID,cid,SAName,TDate,CCNumber,TTag)
            #DB.insert(cmd)
            st.warning("Not implemented yet!")

    with tab3:
        DB.get_orders()
    
    with tab4:
        if st.button("Logout"):
          DB.logout()



