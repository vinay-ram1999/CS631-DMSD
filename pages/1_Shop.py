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

st.title("eComputerStore")

st.sidebar.header("Menu")
section = st.sidebar.radio("Title", ["Products", "Offers"], label_visibility="collapsed")

if section == "Products":
    DB.get_products()

if section == "Offers":
    DB.get_offers()