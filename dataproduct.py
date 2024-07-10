import streamlit as st
from charts.graficas_plotly import *


def principal():
    st.title("¿Le gusta comer alimentos de mar?")
    opciones = st.selectbox(
        "",
        [
            "",
            "Pargo",
            "Cherna",
            "Túnidos",
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
        st.plotly_chart(pargo)
    if opciones == "Cherna":
        st.plotly_chart(Cherna)
    if opciones == "Túnidos":
        st.plotly_chart(tunidos)
    if opciones == "Bonito":
        st.plotly_chart(bonitos)
    if opciones == "Biajaiba":
        st.plotly_chart(biajaiba)
    if opciones == "Machuelo":
        st.plotly_chart(machuelo)
    if opciones == "Rabirubia":
        st.plotly_chart(rabirubia)
    if opciones == "Raya":
        st.plotly_chart(raya)
    if opciones == "Carpa":
        st.plotly_chart(carpa)
    if opciones == "Tenca":
        st.plotly_chart(tenca)
    if opciones == "Tilapia":
        st.plotly_chart(tilapia)
    if opciones == "Claria":
        st.plotly_chart(claria)
    if opciones == "Cobo":
        st.plotly_chart(cobo)
    if opciones == "Ostión":
        st.plotly_chart(ostion)
    if opciones == "Almeja":
        st.plotly_chart(almeja)
    if opciones == "Langosta":
        st.plotly_chart(langosta)
    if opciones == "Camaron de mar":
        st.plotly_chart(camaron_de_mar)
    if opciones == "Camaronicultura":
        st.plotly_chart(camaronicultura)
    if opciones == "Morallas":
        st.plotly_chart(moralla)

def pagina2():
    pass


pages = {
    "Inicio": principal,
    "Económico": pagina2,
}

selection = st.sidebar.radio("Ir a", list(pages.keys()))
pages[selection]()