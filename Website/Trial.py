# TRial

import streamlit as st
import pandas as pd
import numpy as np

#add an import to Hydralit
from hydralit import HydraHeadApp
from hydralit import HydraApp
#create a wrapper class
class MySampleApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):
        #Method 1
        pf = pd.read_csv(r"C:\Users\vedan\Desktop\BE_Project\Website\data\patient_form.csv")
        st.write(pf)
        with st.form(key='form1'):
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
                pf.to_csv(r"C:\Users\vedan\Desktop\BE_Project\Website\data\patient_form.csv", index=False)
                st.write(pf)


if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!
    st.set_page_config(page_title ="DermCare", page_icon="🥇",layout='wide',initial_sidebar_state='collapsed')
    app = HydraApp()
    #add all your application classes here
    app.add_app("Sample App",icon="🔊", app=MySampleApp())

    #run the whole lot
    app.run()

app = HydraApp()
#add all your application classes here
#app.add_app("Home Page",icon="🔊", app=dboard())
#app.add_app("Home Remedies and Diet",icon="🔊", app=medication())
#app.add_app("Predict Disease",icon="🔊", app=predict())
app.add_app("Patient Form",icon="🔊", app=form())
#app.add_app("Profile",icon="🔊", app=Profile())

#run the whole lot
app.run()





