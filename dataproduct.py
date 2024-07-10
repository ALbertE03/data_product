import streamlit as st
from graficas_plotly import exportaciones, fish

st.title("¿Le gusta comer alimentos de mar?")
opciones = st.selectbox(
    "",
    [
        "",
        "Pargo",
        "Cherna",
        "Bonito",
        "Biajaiba",
        "Machuelo",
        "Rabirubia",
        "Raya",
        "Carpa",
        "Tenca",
        "Tilapia",
        "Claria",
        "Cobo",
        "Ostión",
        "Almeja",
        "Langosta",
        "Camaron de mar",
        "Camaronicultura",
        "Morallas",
    ],
)

if opciones == "Pargo":
    pass
if opciones == "Cherna":
    pass
if opciones == "Bonito":
    pass
if opciones == "Biajaiba":
    pass
if opciones == "Machuelo":
    pass
if opciones == "Rabirubia":
    pass
if opciones == "Raya":
    pass
if opciones == "Carpa":
    pass
if opciones == "Tenca":
    pass
if opciones == "Tilapia":
    pass
if opciones == "Claria":
    pass
if opciones == "Cobo":
    pass
if opciones == "Ostión":
    pass
if opciones == "Almeja":
    pass
if opciones == "Langosta":
    pass
if opciones == "Camaron de mar":
    pass
if opciones == "Camaronicultura":
    pass
if opciones == "Morallas":
    pass
st.plotly_chart(exportaciones)
st.plotly_chart(fish)
