import streamlit as st
import pandas as pd

cleandf=pd.read_csv('clean_dataset.csv', index_col=False)
df=pd.read_csv('final_data (1).csv',index_col=False)
df['customer_id']=cleandf['customer_unique_id']
st.title("Сегментация клиентов")

client_id = st.selectbox(
    "Выберите клиента",
    sorted(df['customer_id'].unique())
)

risk = df[df["customer_id"] == client_id]["cluster"].values[0]

st.progress(risk/8)