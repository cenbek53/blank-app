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

pg = st.navigation([st.Page(home), st.Page(customer), st.Page(contacts), st.Page(projects), st.Page(machinery)])
pg.run()
