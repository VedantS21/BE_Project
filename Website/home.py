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
def signin(uname,pword):
    a = b = ""
    data = []
    with open(r"Website/data/Login.csv") as file:
        read = csv.reader(file)
        for row in read:
            data.append(row)
    col_1 = [x[1] for x in data]
    col_2 = [x[2] for x in data]
    if uname in col_1:
        for x in range(0,len(data)):
            if uname == data[x][1]:
                a = data[x][1]
                continue
    else:
        st.sidebar.error("User Not Registered")

    if pword in col_2:
        for x in range(0,len(data)):
            if pword == data[x][2]:
                b = data[x][2]
                continue
    else:
        st.sidebar.error("Incorect Password")

    if a == uname and b == pword:
        st.sidebar.success("Login Successful")
    else:
        st.sidebar.error("Login Unsuccessful")
    return(str(a))

def register(n,usrname,psword):
    lg = pd.read_csv(r"Website/data/Login.csv")
    new_data = {"Name":n, "Username":usrname, "Password":psword}
    lg = lg.append(new_data, ignore_index=True)
    lg.to_csv(r"Website/data/Login.csv", index=False)
    st.success("User registered successfully")

choice = st.sidebar.selectbox("Sign Up", ("Login","Create Account","None"))

if choice == "Login":
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    submit1 = st.sidebar.button("Login")
    if submit1 == True:
        proceed = True
        usname = signin(username,password)
        st.write(type(usname))

elif choice == "Create Account":
    name = st.sidebar.text_input("Name")
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    submit2 = st.sidebar.button("Create Profile")
    if submit2 == True:
        register(name,username,password)
        proceed = False


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
