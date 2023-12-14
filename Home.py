from app_base import *

st.set_page_config(page_title="eComputerStore",
                   page_icon=":shopping_trolley:",
                   layout="wide",
                   menu_items = {"About": "Source: https://github.com/vinay-ram1999/CS631-DMSD",
                                 "Report a Bug": "mailto:vinayramgazula@gmail.com"})

st.title("eComputerStore")

with st.expander("About", expanded=True):
    st.markdown("This is an interactive dashboard built to access the eComputerStore database")
