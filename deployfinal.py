#!/usr/bin/env python
# coding: utf-8

# In[2]:
import pandas as pd
import streamlit as st 
import sklearn
import base64
from sklearn.tree import  DecisionTreeClassifier
from pickle import dump
from pickle import load

#change page name and icon
col1 = st.beta_columns(2)

names = "<div><span class='red_heading'>Fraud Analytics</span></div>"
col1.markdown(names, unsafe_allow_html=True)
import streamlit as st
st.image("Excelr.jpeg")

# In[2]:


st.title('Model Deployment:Decision Tree')


# In[ ]:




def user_input_features():
    st.sidebar.header('User Input Parameters')

    age_display = ("0 to 17","18 to 29","30 to 49","50 to 69","70 or Older")
    options1 = list(range(len(age_display)))

    surg_display = ("Medical","Surgical")
    options2 = list(range(len(surg_display)))

    emerg_display = ("Yes","No")
    options3 = list(range(len(emerg_display)))

    adm_display = ("Elective","Emergency","New Born","Not Available","Trauma","Urgent")
    options4 = list(range(len(adm_display)))

    care_display = ("Another Type","Cancer Center","Court/Law Enforcement","Critical Access","Expired","Facility","Federal","Home/Self care","HHS","Hosp-Medicare","Hospice-Home","Hospice-Medical","Inpatient","Left-Advice","MedicAid-Nursing","Medicare-Long Term","Psychiatric","Short-term","Skilled")
    options5 = list(range(len(care_display)))

    
    data = {'Area_Service':Area_Service,
            'Age':Age,
            'Gender':Gender,
            'Cultural_group':Cultural_group,
            'Ethnicity':ethnicity,
            'Days_spend_hsptl':Days_spend_hsptl,
            'Admission_type':Admission_type,
            'Home or self care':Home_or_selfcare,
            'ccs_diagnosis_code':ccs_diagnosis_code,
            'ccs_procedure_code':ccs_procedure_code,
            'Code_illness':Code_illness,
            'Mortality risk':Mortality_risk,
            'Surg_Description':Surg_Description,
            'Emergency dept_yes/No':Emergency_dept,
            'Tot_charg':Tot_charg,
            'Tot_cost':Tot_cost,
            'Payment_Typology':Payment_Typology 
            }

    features = pd.DataFrame(data,index = [0])
    return features
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# In[ ]:


# load the model from disk
loaded_model = load(open('DecisionTree_Model.sav', 'rb'))


# In[ ]:


prediction = loaded_model.predict(df)


# In[ ]:


st.latex('Result: Genuine' if prediction==1 else 'Result: Fraud')



# In[ ]:
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

st.header("**Presented by Group 5:**")
st.markdown("**ANANYA,VISHWANATH,MURALI KRISHNA,BHASKAR A,DALTON,PUNITH KUMAR**")
                                                                   

