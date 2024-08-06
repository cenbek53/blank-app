import streamlit as st
import pandas as pd
import numpy as np

def home():
    st.write("sss")

def customer():
    st.title("Customer")    
    df = pd.DataFrame(
        np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    st.table(df)

def contacts():
    st.write("ss")

def projects():
    st.write("ss")

def machinery():
    st.write("ss")

pg = st.navigation([st.Page(home, title="Home", icon=None), 
                    st.Page(customer, title="Customer", icon=None), 
                    st.Page(contacts, title="Contacts", icon=None), 
                    st.Page(projects, title="Projects", icon=None), 
                    st.Page(machinery,title="Machinery", icon=None)])
pg.run()
