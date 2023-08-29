import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import os
import openpyxl



# Assuming you have already merged the data and created the merged_df dataframe

# Create a color palette for the bar chart
sns.set_palette("pastel")

# Sidebar - Semester Selection
st.sidebar.title("Dashboard Options")
selected_semester = st.sidebar.selectbox('Select Semester:', merged_df['code_presentation'].unique())

# Sidebar - Student Selection
selected_student_id = st.sidebar.selectbox('Select Student ID:', merged_df['id_student'].unique())

# Sidebar - Gender Selection
selected_gender = st.sidebar.radio('Select Gender:', ['M', 'F'])

# Filter the data based on selected semester, student id, and gender
filtered_df = merged_df[(merged_df['code_presentation'] == selected_semester) &
                        (merged_df['id_student'] == selected_student_id)]

if selected_gender != 'All':
    filtered_df = filtered_df[filtered_df['gender'] == selected_gender]

# Display the bar plot using Streamlit
st.title('Registration Status by Code Presentation')
st.write(f'Selected Semester: {selected_semester}')
st.write(f'Selected Student ID: {selected_student_id}')
st.write(f'Selected Gender: {selected_gender}')

# Create a bar plot with the chosen color palette
fig, ax = plt.subplots(figsize=(10, 6))
filtered_df['code_presentation'].value_counts().sort_index().plot(kind='bar', ax=ax)

plt.title('Number of Registrations')
plt.xlabel('Code Presentation (Semester)')
plt.ylabel('Number of Registrations')
plt.xticks(rotation=45)

st.pyplot(fig)

# Display the raw data table
st.subheader('Raw Data')
st.write(filtered_df)

# Display categorized data by code_module
st.subheader('Categorized Data by Code Module')
categorized_data = filtered_df.groupby('code_module').size().reset_index(name='count')
st.write(categorized_data)

# Display all data info table
st.subheader('All Data Info')
st.write(merged_df)

