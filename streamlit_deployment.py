import streamlit as st
import pandas as pd

df = pd.read_excel('data_untuk_visualisasi.xlsx', sheet_name = 'ALL')

# Streamlit App Title
st.title("Filter Data Table by Treatment Place")

# Sidebar for Filtering
st.sidebar.header("Filter Options")
treatment_places = st.sidebar.multiselect(
    "Select Treatment Places:",
    options=df['TreatmentPlace'].unique(),
    default=df['TreatmentPlace'].unique()
)

# Filter Data
filtered_df = df[df['TreatmentPlace'].isin(treatment_places)]

# Display Filtered Data
st.subheader("Filtered Data Table")
st.write(filtered_df)

# Display Total Records
st.text(f"Total Records: {len(filtered_df)}")
