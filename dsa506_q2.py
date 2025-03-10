import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

students = pd.read_csv('university_student_dashboard_data.csv')
filtered_students = None
filtered_students1 = None

# Sidebar Filters
st.sidebar.header('Filters')
term_filter = st.sidebar.selectbox('Select Term', ['All'] + list(students['Term'].unique()))
filtered_students1 = students[students['Term'] == term_filter]

# Other filters
year = st.slider("Select Year:", int(students["Year"].min()), int(students["Year"].max()), value=None)

if term_filter == 'All' and year is None:
    filtered_students = students
elif term_filter != 'All' and year is None:
    filtered_students = students[students['Term'] == term_filter]
elif term_filter == 'All' and year is not None:
    filtered_students = students[students['Year'] == year]
else:
    filtered_students = students[(students['Term'] == term_filter) & (students['Year'] == year)]

# KPIs
st.title('University Students Dashboard')
st.metric('Total Applications Since 2015', students['Applications'].sum())
st.metric('Filtered Applications', filtered_students['Applications'].sum())
st.metric('Total Admissions Since 2015', students['Admitted'].sum())
st.metric('Filtered Admissions', filtered_students['Admitted'].sum())
st.metric('Total Enrollment Since 2015', students['Enrolled'].sum())
st.metric('Filtered Enrollment', filtered_students['Enrolled'].sum())

# Charts
st.subheader('Charts (filtered by term)')
fig = px.line(filtered_students1, x='Year', y='Retention Rate (%)', title='Retention Rates')
fig1 = px.line(filtered_students1, x='Year', y='Student Satisfaction (%)', title='Student Satisfaction')

st.plotly_chart(fig)
st.plotly_chart(fig1)

chart1, chart2, chart3, chart4 = st.columns((4))
with chart1:
    st.subheader('Arts Enrollment By Year')
    fig2 = px.bar(filtered_students1, x='Year', y='Arts Enrolled', title='Arts Enrollment by Year')
    st.plotly_chart(fig2,use_container_width=True)

with chart2:
    st.subheader('Business Enrollment By Year')
    fig3 = px.bar(filtered_students1, x='Year', y='Business Enrolled', title='Business Enrollment by Year')
    st.plotly_chart(fig3,use_container_width=True)

with chart3:
    st.subheader('Engineering Enrollment By Year')
    fig4 = px.bar(filtered_students1, x='Year', y='Engineering Enrolled', title='Engineering Enrollment by Year')
    st.plotly_chart(fig4,use_container_width=True)

with chart4:
    st.subheader('Science Enrollment By Year')
    fig5 = px.bar(filtered_students1, x='Year', y='Science Enrolled', title='Science Enrollment by Year')
    st.plotly_chart(fig5,use_container_width=True)
