from secrets import choice
from struct import pack
# from turtle import home
import streamlit as st
import csv

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


def app():
    st.title("My Profile")
    st.write("")

    st.write(usname)

    col1,col2,col3 = st.columns(3)
    # name = col1.text_input("Enter your name")
    patient_data = []
    with open(r"Website/data/patient_form.csv") as file:
        read = csv.reader(file)
        for row in read:
            patient_data.append(row)    
    col_1 = [x[0] for x in patient_data]
    if name in col_1:
        for x in range(0,len(patient_data)):
            if name == patient_data[x][0]:
                col1,col2 = st.columns(2)
                col1.subheader("Name: "+name)
                col1.subheader("Date of Birth: " + patient_data[x][1])
                col1.subheader("Address: "+patient_data[x][2])
                col2.subheader("Age: "+patient_data[x][3])
                col2.subheader("Weight: "+patient_data[x][4])
                col2.subheader("Height: "+patient_data[x][5])
                col2.subheader("Blood Pressure: "+patient_data[x][6])
                col1.subheader("Diabetes: "+patient_data[x][7])
                col1.subheader("Alergy: "+patient_data[x][8])
                col2.subheader("Any other medical condition: "+patient_data[x][9])
                # st.write(patient_data[x])
                continue
    else:
        st.error("Patient data not found")