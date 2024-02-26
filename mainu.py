import streamlit as st
import pandas as pd

# Sidebar menu
st.sidebar.title("Menu")
selected_page = st.sidebar.radio("", [ "About Us", "Contact"])

if selected_page == "About Us":
    st.title("About Us")
    st.write(f"This address book application was created by {name}.")
elif selected_page == "Contact":
    st.title("Contact")
    st.write("For support, please email support@example.com.")
