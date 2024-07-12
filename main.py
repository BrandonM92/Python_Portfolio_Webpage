import streamlit as st
import pandas as pd

# Define the layout with two columns
col1, col2 = st.columns([1, 3])  # Adjust the widths as needed

# Column 1: Display an image
with col1:
    # This code block is where you put content on the left side column
    st.image(image="images/photo.png", caption="Programmer", use_column_width=True)

# Column 2: Display information about Brandon Mathews
with col2:
    # This code block is where you put content on the right side column"""
    st.title("Brandon Mathews")
    content = """
    I'm Brandon, an Aspiring IT professional with a focus on Python and Application Development. 
    I graduated in 2024 with a Bachelor's Degree in Information Technology and obtained a certification 
    in Data Analysis with Google (via Coursera). I am consistently increasing my skills and learning 
    various ways to not only tackle project ideas but also look for ways to make them easier and more efficient.

    I have mainly worked on small personal projects ranging from:
    - Python Programs (Web Scrapers, Automation, API-use)
    - Web Development (Javascript, HTML, CSS)
    - Game Development (C#, 2D & 3D Unity)
    - Data Analysis (SQL, R, Tableau, BigQuery)
    
    """
    st.markdown(content)  # Markdown lets us add html to the webpage.

contact_message = """
    On this webpage, you will find applications I developed in Python. 
    If you wish to contact me, all contact information can be found on the contact page. 
"""
st.markdown(contact_message)

col3, empty_col,  col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write("EDIT AS YOU FINISH!")



with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write("EDIT AS YOU FINISH!")



