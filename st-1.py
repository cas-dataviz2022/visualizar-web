import streamlit as st
import pandas as pd

st.write("Mi primera Visualización de Datos Web:")
st.write("Una tabla de datos sencilla:")
st.write(pd.DataFrame({
    'Lugares': [1, 2, 3, 4],
    'Cantidades': [10, 20, 30, 40]
}))
