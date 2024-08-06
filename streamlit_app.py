import streamlit as st

def home():
    st.write("sss")

def customer():
    st.write("ss")

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
