import streamlit as st
import pandas as pd

from viz import horarios

puntos_carga = pd.read_csv("puntos-comunas.csv", index_col=0, encoding="utf-8")

st.write("Acá puedes ver puntos de carga para 3 comunas")
st.write(puntos_carga)

st.write("Para ver la información de Horarios de Carga por Comuna, presiona el siguiente botón")
boton_carga = st.button("Ver Horarios de Carga por Comuna")


if boton_carga:
    resultado_horarios = horarios()
    st.table(resultado_horarios)

    boton_carga_ocultar = st.button("Ocultar Ver Horarios de Carga por Comuna")
    if boton_carga_ocultar:
        boton_carga = None