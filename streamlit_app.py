from app_base import *

DB = DBLink()

st.set_page_config(page_title="eComputerStore DB",
                   page_icon="📊",
                   layout="wide",
                   menu_items = {"About": "Source: https://github.com/vinay-ram1999/CS631-DMSD",
                                 "Report a Bug": "mailto:vinayramgazula@gmail.com"})


st.title("eComputerStore DB")

with st.expander("About", expanded=True):
    st.markdown("This is an interactive dashboard built to access the eComputerStore database")

# sidebar arguments
st.sidebar.title('Menu')

section = st.sidebar.radio("", ["Query"], label_visibility="collapsed")

if section == "Query":
    txt = st.text_area("Enter your query:", value="SELECT * FROM CUSTOMER;")
    if txt:
        if st.button("RUN"):
            df = DB.query(txt)
            st.dataframe(df)
    else:
        st.warning("Please enter a query.")