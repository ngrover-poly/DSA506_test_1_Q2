import pandas as pd
import numpy as np
import streamlit as st

students = pd.read_csv('university_student_dashboard_data.csv')

# KPIs
st.title('University Students Dashboard')
st.metric('Total Applications', students['Applications'].sum())
st.metric('Total Admissions', students['Admitted'].sum())
st.metric('Total Enrollment', students['Enrolled'].sum())


# Sidebar Filters
st.sidebar.header('Filters')
term_filter = st.sidebar.selectbox('Select Term', ['All'] + list(students['Term'].unique()))

if term_filter != 'All':
    students = students[students['Term'] == term_filter]

year = st.slider("Select Year:", int(students["Year"].min()), int(students["Year"].max()), int(students["Year"].min()))
