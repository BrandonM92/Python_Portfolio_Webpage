import streamlit as st
from email_utility import send_email

st.header("Contact Information")

st.markdown("""
    \nLinkedIn: https://www.linkedin.com/in/brandon-mathews-1b2268201/
    \nGitHub: https://github.com/BrandonM92 
    
""")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    subject = st.text_input("Subject")
    message = st.text_area("Enter Your Message")
    message = message + "\n" + user_email
    button = st.form_submit_button("Send Email")

    if button:
        send_email(message=message,subject=subject)
        st.info("Your email was sent successfully")

