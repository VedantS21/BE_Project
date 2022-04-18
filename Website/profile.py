from secrets import choice
from struct import pack
# from turtle import home
import streamlit as st
import csv
import home
name = home.usrname_1 

def app():
    st.title("My Profile")
    st.write("")

    st.write(name)

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