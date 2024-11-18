import streamlit as st
import pandas as pd

# Membaca data dari file Excel
df = pd.read_excel('data_untuk_visualisasi.xlsx', sheet_name='ALL')

# Menghapus baris yang memiliki NaN pada kolom 'Nama Item Garda Medika'
df = df.dropna(subset=['Nama Item Garda Medika'])

# Mengkonversi 'Amount Bill' menjadi numerik dan menggantikan yang tidak bisa dikonversi menjadi NaN
df['Amount Bill'] = pd.to_numeric(df['Amount Bill'], errors='coerce')

# Mengisi NaN yang mungkin ada pada 'Amount Bill' dengan 0 (atau bisa diganti dengan nilai lain)
df['Amount Bill'] = df['Amount Bill'].fillna(0)

# Pastikan kolom 'Amount Bill' memiliki tipe data numerik (float)
df['Amount Bill'] = df['Amount Bill'].astype(float)

# Streamlit App Title
st.title("Data Obat di Tiap Rumah Sakit")

# Sidebar Navigation
page = st.sidebar.selectbox("Choose Page:", ["Filter Data", "Grouped Data"])

# Page 1: Filter Data
if page == "Filter Data":
    st.header("Filter Data Table by Treatment Place")

    # Sidebar for Filtering
    selected_treatment_place = st.sidebar.selectbox(
        "Select Treatment Place:",
        options=["All"] + df['TreatmentPlace'].unique().tolist()
    )

   # Apply Filter
    if selected_treatment_place != "All":
        filtered_df = df[df['TreatmentPlace'] == selected_treatment_place]
    else:
        filtered_df = df

    # Pilih hanya kolom yang diinginkan
    filtered_df = filtered_df[['Nama Item Garda Medika', 'Satuan', 'Qty', 'Amount Bill']]

    # Display Filtered Data
    st.subheader("Filtered Data Table")
    st.write(filtered_df)

    # Display Total Records
    st.text(f"Total Records: {len(filtered_df)}")

# Page 2: Grouped Data
elif page == "Grouped Data":
    st.header("Grouped Data Table")

    # Filter by Treatment Place
    selected_treatment_place = st.sidebar.selectbox(
        "Filter by Treatment Place:",
        options=["All"] + df['TreatmentPlace'].unique().tolist()
    )

    # Apply Filter for Grouping
    if selected_treatment_place != "All":
        filtered_group_df = df[df['TreatmentPlace'] == selected_treatment_place]
    else:
        filtered_group_df = df

    # Group by 'Nama Item Garda Medika'
    grouped_df = filtered_group_df.groupby('Nama Item Garda Medika').agg(
        Total_Amount_Bill=('Amount Bill', 'sum'),
        Total_Rows=('ClaimNo', 'count')
    ).reset_index()

    # Display Grouped Data
    st.subheader(f"Grouped Data by 'Nama Item Garda Medika' (Filtered by {selected_treatment_place})")
    st.write(grouped_df)
