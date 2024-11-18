import streamlit as st
import pandas as pd

df = pd.read_excel('data_untuk_visualisasi.xlsx', sheet_name = 'ALL')

# Streamlit App Title
st.title("Filter Data Table by Treatment Place")

# Sidebar for Filtering
st.sidebar.header("Filter Options")
selected_treatment_place = st.sidebar.selectbox(
    "Select Treatment Place:",
    options=["All"] + df['TreatmentPlace'].unique().tolist()
)

# Apply Filter
if selected_treatment_place != "All":
    filtered_df = df[df['TreatmentPlace'] == selected_treatment_place]
else:
    filtered_df = df

# Display Filtered Data
st.subheader("Filtered Data Table")
st.write(filtered_df)

# Display Total Records
st.text(f"Total Records: {len(filtered_df)}")
