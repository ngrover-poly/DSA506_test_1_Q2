import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

students = pd.read_csv('university_student_dashboard_data.csv')

import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

students = pd.read_csv('university_student_dashboard_data.csv')


# Sidebar Filters
st.sidebar.header('Filters')
term_filter = st.sidebar.selectbox('Select Term', ['All'] + list(students['Term'].unique()))

# Other filters
year = st.slider("Select Year:", int(students["Year"].min()), int(students["Year"].max()), int(students["Year"].min()))

if not term_filter and not year:
    filtered_students = students
elif term_filter and not year:
    filtered_students = students[students['Term'] == term_filter]
elif not term_filter and year:
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
st.subheader('Charts')
fig = px.line(students, x='Year', y='Retention Rate (%)', title='Retention Rates')
fig1 = px.line(students, x='Year', y='Student Satisfaction (%)', title='Satisfaction')

st.plotly_chart(fig)
st.plotly_chart(fig1)
