import streamlit as st
import pandas


st.set_page_config(layout="wide")

company_desc = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum.
"""
team_header = "Our Team"

st.title("The Best Company")
st.write(company_desc)
st.subheader(team_header)

df = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.text(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.text(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.text(row["role"])
        st.image("images/" + row["image"])
