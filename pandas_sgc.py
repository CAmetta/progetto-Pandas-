
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pandas SGC", layout="wide")

st.title("Applicazione Pandas SGC")
st.subheader("Calcolo IVA")

df = pd.DataFrame({
    "prezzo": [10, 20, 30]
})

def applica_iva(x):
    return x * 1.22

df["con_iva"] = df["prezzo"].apply(applica_iva)

st.dataframe(df, use_container_width=True)

st.success("Calcolo IVA completato!")


  

