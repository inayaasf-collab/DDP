import streamlit as st

st.title("Form Data Diri")
st.write("Silahkan isi data diri anda")
st.write("Made by Inayah")

with st.form("form_data_diri"):
    nama = st.text_input("Nama")
    alamat = st.text_input("Alamat")
    usia = st.number_input("Usia")
    submit = st.form_submit_button("Submit")