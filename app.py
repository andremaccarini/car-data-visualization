import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os


file_path = os.path.join('Data', 'vehicles.csv')
car_data = pd.read_csv(file_path)

hist_button = st.checkbox('Show Histogram')
if hist_button:
    st.write("Creating histogram for the data set...")
    st.write("This may take a few seconds.")
    fig = px.histogram(car_data, x='odometer', title='Histogram of Odometer Usage')

    st.plotly_chart(fig, use_container_width=True)
    st.write("Histogram created successfully!")

scatter_button = st.checkbox('Show Scatter Plot')
if scatter_button:
    st.write("Creating scatter plot for the data set...")
    st.write("This may take a few seconds.")
    fig = px.scatter(car_data, x='odometer', title='Dispersion of Odometer Usage')
    st.plotly_chart(fig, use_container_width=True)
    st.write("Scatter plot created successfully!")