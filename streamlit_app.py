import streamlit as st

def page1():
    st.write("sss")

def page2():
    st.write("ss)

pg = st.navigation([st.Page(page1), st.Page(page2)])
pg.run()
