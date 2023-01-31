import pandas as pd
import streamlit as st
import glob


imput_analyse_bedrijven = st.sidebar.text_input("vul hier een map in waar excelbestanden instaan :", "C:/Users/info/OneDrive/Documenten/ARNE/program/excel_calc/")
excel_files = glob.glob(str(imput_analyse_bedrijven) + "*.xlsx")

aandelen_calc_list = [pd.read_excel(filename) for filename in excel_files]


st.title("test")
if(st.button('tabel met bestanden')):
    st.text("Ready")

    st.dataframe(aandelen_calc_list)

