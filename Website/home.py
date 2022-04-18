from PIL import Image
import numpy as np
import csv
import streamlit as st
import Dashboard, form, medication, Predict, profile
import pandas as pd
import streamlit as st
st.set_page_config(page_title ="DermCare", page_icon="🥇",layout='wide')
with open(r"Website/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# look nice from the start
global proceed
global usname
# proceed = False


PAGES = {
"Home Page" : Dashboard,
"Predict Disease": Predict,
"Home Remedies & Diet": medication,
"Patient Form" : form,
"My Profile": profile

}
selection = st.sidebar.radio("Navigation", list(PAGES.keys()))
page = PAGES[selection]
page.app()
