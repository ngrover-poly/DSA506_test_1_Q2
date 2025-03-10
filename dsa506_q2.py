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
school_filter = st.sidebar.selectbox('Select School',['All'] + ['Arts', 'Business', 'Engineering', 'Science'])

def handle_input(df, school_filter): 
    match school_filter:
        case 'Arts':
            return df[df['Arts Enrolled'] == school_filter]
        case 'Business':
            return df[df['Business Enrolled'] == school_filter]
        case 'Engineering':
            return df[df['Engineering Enrolled'] == school_filter]
        case 'Science':
            return df[df['Science Enrolled'] == school_filter]
        case  _:
            return df 
            
students = handle_input(filtered_students, school_filter)

year = st.slider("Select Year:", int(students["Year"].min()), int(students["Year"].max()), int(students["Year"].min()))
