import streamlit as st

def Home():
    st.write("sss")

def Customer():
    st.write("ss")

def Contacts():
    st.write("ss")

def Projects():
    st.write("ss")

def Machinery():
    st.write("ss")

pg = st.navigation([st.Page(Home), st.Page(Customer), st.Page(Contacts), st.Page(Projects), st.Page(Machinery)])
pg.run()
