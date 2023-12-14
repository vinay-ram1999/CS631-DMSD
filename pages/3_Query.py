import path
import sys
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)
from app_base import *

DB = DBLink()

st.set_page_config(page_title="Query",
                   page_icon=":shopping_trolley:",
                   layout="wide",
                   menu_items = {"About": "Source: https://github.com/vinay-ram1999/CS631-DMSD",
                                 "Report a Bug": "mailto:gazulavinayram@gmail.com"})

st.title("Query")

with st.expander("About", expanded=True):
    st.markdown("In this section you can explore the eComputerStore database using SQL commands.")

#st.sidebar.title('Menu')
st.sidebar.header("Menu")
section = st.sidebar.radio("Title", ["Schema", "Query"], label_visibility="collapsed")

if section == "Schema":
    st.image('./pages/docs/DB_schema.png', caption='The schema that is used to build the eComputerStore database.', use_column_width=True)

if section == "Query":
    txt = st.text_area("Enter the query:", value="SELECT * FROM CUSTOMER;", height=250)
    if txt:
        if st.button("RUN", type="primary"):
            df = DB.query(txt)
            st.dataframe(df, use_container_width=True)
    else:
        st.warning("Please enter a query.")

"""if section == "Update":
    txt = st.text_area("Enter the query:", value=" ", height=250)
    if txt:
        if st.button("RUN", type="primary"):
            df = DB.insert(txt)
            st.dataframe(df, use_container_width=True)
    else:
        st.warning("Please enter a query.")"""