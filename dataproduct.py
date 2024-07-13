import streamlit as st
from charts.graficas_plotly import *
import plotly.graph_objects as go
import plotly.io as pio

st.set_page_config(
    page_title="Data Product",
    page_icon=":fish:",
)

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

def economico():
    pass

def mapas():
    st.title("Empresas de Pesca en Cuba")
    option=st.selectbox("",['Mypimes','EpiGram','PESCAGRAM','EPICAI',"EPICIEN",'Pesca Caribe',"GEIP"])

    #fig = go.Figure(go.Scattermapbox(lat=[20.329436],lon=[-77.153311],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
    #fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=20.329436,lon=-77.153311),zoom=13))
    #pio.write_html(fig,file="mapa.html")

    #fig = go.Figure(go.Scattermapbox(lat=[20.329436],lon=[-77.153311],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
    #fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=20.329436,lon=-77.153311),zoom=13))
    #pio.write_html(fig,file="mapa1.html")

    #fig = go.Figure(go.Scattermapbox(lat=[22.526927],lon=[-79.467644],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
    #fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=22.526927,lon=-79.467644),zoom=13))
    #pio.write_html(fig,file="mapa2.html")

    #fig = go.Figure(go.Scattermapbox(lat=[22.169549],lon=[-80.480796],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
    #fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=22.169549,lon=-80.480796),zoom=13))
    #pio.write_html(fig,file="mapa3.html")

    #fig = go.Figure(go.Scattermapbox(lat=[23.161990],lon=[-82.290785],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
    #fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=23.161990,lon=-82.290785),zoom=13))
    #pio.write_html(fig,file="mapa4.html")

    #fig = go.Figure(go.Scattermapbox(lat=[23.119680],lon=[-82.354357],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
    #fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=23.119680,lon=-82.354357),zoom=13))
    #pio.write_html(fig,file="mapa5.html")

    if option == 'Mypimes':
        o=st.selectbox("",mypimesdf.index)
        if o =='Pinar del Rio':
            st.plotly_chart(p)
        if o == "Artemisa":
            st.plotly_chart(p1)
        if o == 'La Habana':
            st.plotly_chart(p2)
        if o== "Mayabeque":
            st.plotly_chart(p3)
        if o =="Matanzas":
            st.plotly_chart(p4)
        if o == "Villa Clara":
            st.plotly_chart(p5)
        if o =="Cienfuegos":
            st.plotly_chart(p6)
        if  o =="Santi Spiritus":
            st.plotly_chart(p7)
        if o =="Ciego de Ávila":
            st.plotly_chart(p8)
        if o =="Camagüey":
            st.plotly_chart(p9)
        if o =="Las Tunas":
            st.plotly_chart(p10)
        if o =="Holguín":
            st.plotly_chart(p11)
        if o =="Santiago de Cuba":
            st.plotly_chart(p12)
        if o =="Guantánamo":
            st.plotly_chart(p13)
        if o =="La Isla de la Juventud":  
            st.plotly_chart(p14)
            
    if option == "EpiGram":
        st.subheader("EpiGram")
        with open("mapa1.html",'r') as f:
            html =f.read()
        st.components.v1.html(html,height=500)

    if option == "PESCAGRAM":
        st.subheader("PESCAGRAM")
        with open("mapa.html",'r') as f:
            html =f.read()
        st.components.v1.html(html,height=500)

    if option == "EPICAI":
        st.subheader("EPICAI")
        with open("mapa2.html",'r') as f:
            html =f.read()
        st.components.v1.html(html,height=500)
    
    if option == "EPICIEN":
        st.subheader("EPICIEN")
        with open("mapa3.html",'r') as f:
            html =f.read()
        st.components.v1.html(html,height=500)
    
    if option == "Pesca Caribe":
        st.subheader("Pesca Caribe")
        with open("mapa4.html",'r') as f:
            html =f.read()
        st.components.v1.html(html,height=500)

    if option == "GEIP":
        st.subheader("Grupo Empresarial de La Industria Pesquera (GEIP)")
        with open("mapa5.html",'r') as f:
            html =f.read()
        st.components.v1.html(html,height=500)

pages = {
    "Inicio": principal,
    "Económico": economico,
    "Localización e investigación": mapas
}

selection = st.sidebar.radio("Ir a", list(pages.keys()))
pages[selection]()