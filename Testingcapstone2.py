import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import os
import openpyxl

data1 = pd.read_csv('assessments.csv')
data2 = pd.read_csv('courses.csv')

import pandas as pd

# Load your data into a DataFrame (assuming your data is stored in a CSV file)
data3 = pd.read_csv('studentAssessment.csv')

# Calculate statistics
mean_score = data3['score'].mean()
median_score = data3['score'].median()
mode_score = data3['score'].mode()[0]  # mode() returns a Series, so we use [0] to get the first value

# Choose the statistic you want to use (mean, median, or mode)
chosen_statistic = mean_score

# Fill missing values in the 'score' column with the chosen statistic
data3['score'].fillna(chosen_statistic, inplace=True)

import pandas as pd

# Load your data into a DataFrame (assuming your data is stored in a CSV file)
data4 = pd.read_csv('studentInfo.csv')

# Calculate the mode of 'imd_band'
mode_imd_band = data4['imd_band'].mode()[0]  # mode() returns a Series, so we use [0] to get the first value

# Fill missing values in the 'imd_band' column with the mode
data4['imd_band'].fillna(mode_imd_band, inplace=True)


data5 = pd.read_csv('studentRegistration.csv')

merged_df = pd.merge(data1, data2, on=['code_module','code_presentation'])
merged_df = pd.merge(merged_df, data3, on='id_assessment')
merged_df = pd.merge(merged_df, data4, on=['code_module','code_presentation','id_student'])
merged_df = pd.merge(merged_df, data5, on=['code_module','code_presentation','id_student'])


# Assuming you have already merged the data and created the merged_df dataframe

# Create a color palette for the bar chart
sns.set_palette("pastel")

# Sidebar - Semester Selection
st.sidebar.title("Dashboard Options")

import streamlit as st
from PIL import Image

image = Image.open('UTMlogo.jpg')

st.image(image, caption='Universiti Teknologi Malaysia',width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


selected_semester = st.sidebar.selectbox('Select Semester:', merged_df['code_presentation'].unique())

# Sidebar - Student Selection
selected_student_id = st.sidebar.selectbox('Select Student ID:', merged_df['id_student'].unique())

# Sidebar - Gender Selection
selected_gender = st.sidebar.radio('Select Gender:', ['All','M', 'F'])

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

