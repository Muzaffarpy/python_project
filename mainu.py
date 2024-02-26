
import streamlit as st
import pandas as pd

menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
        st.subheader("Home")
