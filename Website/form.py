import streamlit as st
import pandas as pd

def app():
    st.title("Patient Form")
    st.text("")
    #Method 1
    pf = pd.read_csv(r"Website/data/patient_form.csv")
    c1,c2 = st.columns([3,1])
    with c1.form(key='form1'):
        name = st.text_input("Full Name")
        dob = str(st.date_input("Date of Birth"))
        address = st.text_input("Address")
        age = st.text_input("Age in years")
        weight = st.text_input("Weight in kg")
        height = st.text_input("Height in ft")
        medicalcondition_1 = st.text_input("Blood Pressure")
        medicalcondition_2 = st.text_input("Diabetes")
        medicalcondition_3 = st.text_input("Alergy")
        medicalcondition_4 = st.text_input("Any other medical condition")
        submit_button = False
        submit_button = st.form_submit_button(label='Submit')
        print("Form 1 Submit Button")
        if submit_button == True:
            st.success("Hello {} you have submitted your persnoel details".format(name))
            new_data = {"Name": name, "Birth Date": dob, "Address": address, "Age":age, "Wieght": weight, "Height": height, "medicalcondition_1":medicalcondition_1, "medicalcondition_2":medicalcondition_2, "medicalcondition_3":medicalcondition_3, "medicalcondition_4":medicalcondition_4}
            pf = pf.append(new_data, ignore_index=True)
            pf.to_csv(r"Website/data/patient_form.csv", index=False)
            st.write(pf)
    
    st.title("")
    city = c1.text_input("Enter Your City")
    abc = "https://www.practo.com/"+ city + "/dermatologist"
    url = abc
    st.markdown("[Check doctors nearby](%s)" % url)