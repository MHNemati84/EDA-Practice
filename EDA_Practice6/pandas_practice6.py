# Imports
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Exploratory Data Analaysis')
st.subheader('EDA using Streamlit')

upload = st.file_uploader("Upload your dataset(in CSV format)")

# 1. Checking the head and tail of the dataset
if upload:
    data = pd.read_csv(upload)
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())


# 2. Checking the datatype of each column
if upload:
    if st.checkbox('Datatype of columns'):
        st.write(data.dtypes)

# 3. Checking the shape of the dataset
if upload:
    shape = st.radio(label='Number of rows or columns? ', options=('Rows', 'Columns'))
    if shape == 'Rows':
        st.write(data.shape[0])
    elif shape == 'Columns':
        st.write(data.shape[1])

# 4. Finding the null values in the dataset

if upload:
    if st.checkbox("Missing values? "):
        test = data.isnull().values.any()
        if test == True:
            st.warning("Missing value exists")
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
            st.success("No Missing Values")


# 5. Handling duplicate values in the dataset

if upload:
    if st.checkbox('Check for Duplicates: '):
        if data.duplicated().values.any():
            st.warning("Duplicate rows in dataset")
            drop_choice = st.radio("Do you want to drop duplicates?", \
                                   options=('Yes','No'))
            if drop_choice == 'Yes':
                data.drop_duplicates(inplace=True)
                st.success("Duplicates removed successfuly")
            else:
                st.text("Ok")
        else:
            st.success("No Duplicates")

## 6. Get overall statistics about the dataset
if upload:
    if st.checkbox("Descriptive statistics"):
        st.write(data.describe())

