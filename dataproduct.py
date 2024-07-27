import streamlit as st
from charts.graficas_plotly import *
import plotly.graph_objects as go
import plotly.io as pio

def mostrar(a):
    st.write(a)

def mostrar_grafica(graf):
    st.plotly_chart(graf)

def warning(a):
    st.warning(a)

st.set_page_config(
    page_title="Data Product",
    page_icon=":shark:",
    layout="centered",
    initial_sidebar_state="expanded",
)

def principal():
    st.markdown("""<h1 class = 'titulo'>La Pesca en Cuba</h1> <style>
    .titulo{
      font-size: 60px;
      text-align: center;
    }
    
  </style>""",unsafe_allow_html=True)
    
    st.write("""<p style='text-aling:center;'>En Económico puede encontrar .... dalia termina esto<p> """,unsafe_allow_html=True)
    st.write("""En Empresas se encuentran las principales empresas de pesca en Cuba, junto a las pequeñas y medianas empresas""",unsafe_allow_html=True)
    st.write("En leyes y Resoluciones se encuentran las acciones que ah tomado el gobierno de Cuba con respecto a la Pesca",unsafe_allow_html=True)


def economico():
    st.title("Captura de diferentes especies")
    opciones = st.selectbox(
        "",
        [
            "Selecione una especie",
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
        ],help="Selecione una opción para ver las captura realizadas desde el 2001 hasta 2022"
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

def leyes():
    st.title('¿Cómo han cambiado las leyes con respecto a la pesca en Cuba?')
    ly = st.selectbox("",['Selecione una opción','cantidad de Resoluciones por año','sobre pesca ilegal','sobre prohibición','sobre periodos de pesca','sobre autorizacion','sobre arte de pesca','otros'])
    if 'cantidad de Resoluciones por año' == ly:
        mostrar_grafica(leyes_annos)
        
    if 'sobre pesca ilegal' == ly:
        mostrar(leyes_ilegal)
    if 'sobre prohibición' == ly:
        mostrar(leyes_prohi)
    if 'sobre periodos de pesca' == ly:
        mostrar(leyes_periodo)
    if 'sobre autorizacion' == ly:
        mostrar_grafica(leyes_auto)

    if "sobre arte de pesca" == ly:
        mostrar_grafica(leyes_arte)
    if  'otros' == ly:
        mostrar_grafica(leyes_otros)
    
    
    if st.checkbox("Mostrar las resoluciones"):
        st.markdown("Selecione un estado")
        check = st.checkbox("derogadas")
        check1 =st.checkbox("Modificadas")
        check2 = st.checkbox("Vigentes")
        if check and check1 and check2:
            warning("Seleccione solo una; una ley no puede estar en tres estados a la vez")

        elif check1 and check :
                warning("Seleccione solo una; una ley no puede estar en dos estados a la vez")

        elif check1 and check2 :
                warning("Seleccione solo una; una ley no puede estar en dos estados a la vez")

        elif check and check2 :
                warning("Seleccione solo una; una ley no puede estar en dos estados a la vez")

        elif check2:
            if 'cantidad de Resoluciones por año' == ly:
                st.subheader("Resoluciones Vigentes")
                mostrar(merge[merge['Estado']== 'Vigente'])
                mostrar(str(len(merge[merge['Estado']== 'Vigente']))+' Vigentes')
            elif 'sobre pesca ilegal' == ly:
                st.subheader("Resoluciones Vigentes respecto a la pesca ilegal")
                mostrar(pesca_ilegal[pesca_ilegal['Estado']=='Vigente'])
                mostrar(str(len(pesca_ilegal[pesca_ilegal['Estado']=='Vigente']))+' Vigentes')

            elif 'sobre prohibición' == ly :
                st.subheader("Resoluciones Vigentes en cuanto a prohibiciones")
                mostrar(pesca_ilegal[pesca_ilegal['Estado']=='Vigente'])
                mostrar(str(len(pesca_ilegal[pesca_ilegal['Estado']=='Vigente']))+' Vigentes')

            elif 'sobre periodos de pesca' == ly:
                st.subheader("Resoluciones Vigentes con respecto a los periodos de pescas")
                mostrar(periodos[periodos['Estado']=='Vigente'])
                mostrar(str(len(periodos[periodos['Estado']=='Vigente']))+' Vigentes')

            elif 'sobre autorizacion' == ly:
                st.subheader("Resoluciones Vigentes con respecto a autorizaciones")
                mostrar(autorizacion[autorizacion['Estado']=='Vigente'])
                mostrar(str(len(autorizacion[autorizacion['Estado']=='Vigente']))+' Vigentes')

            elif "sobre arte de pesca" == ly:
                st.subheader("Resoluciones Vigentes con respecto a artes de pesca")
                mostrar(artes_pesca[artes_pesca['Estado']=='Vigente'])
                mostrar(str(len(artes_pesca[artes_pesca['Estado']=='Vigente']))+' Vigentes')

            elif 'otros' == ly:
                st.subheader("Otras resoluciones Vigentes")
                mostrar(pesca[pesca['Estado']=='Vigente'])
                mostrar(str(len(pesca[pesca['Estado']=='Vigente']))+' Vigentes')

        elif  check1:
            if 'cantidad de Resoluciones por año' == ly:
                st.subheader("Resoluciones Modificadas")
                mostrar(merge[(merge['Estado']== 'Modificada')|(merge['Estado']== "Copia corregida")])
                mostrar(str(len(merge[(merge['Estado']== 'Modificada')|(merge['Estado']== "Copia corregida")]))+" Modificadas")

            elif 'sobre pesca ilegal' == ly:
                st.subheader("Resoluciones Modificadas con respecto a la pesca ilegal")
                mostrar(pesca_ilegal[(pesca_ilegal['Estado']=='Modificada')|(pesca_ilegal['Estado']=="Copia corregida")])
                mostrar(str(len(pesca_ilegal[(pesca_ilegal['Estado']=='Modificada')|(pesca_ilegal['Estado']=="Copia corregida")]))+" Modificadas")

            elif 'sobre prohibición' == ly :
                st.subheader("Resoluciones Modificadas en cuanto a prohibiciones")
                mostrar(pesca_ilegal[(pesca_ilegal['Estado']=='Modificada')|(pesca_ilegal['Estado']=="Copia corregida")])
                mostrar(str(len(pesca_ilegal[(pesca_ilegal['Estado']=='Modificada')|(pesca_ilegal['Estado']=="Copia corregida")]))+" Modificadas")

            elif 'sobre periodos de pesca' == ly:
                st.subheader("Resoluciones Modificadas con respecto a los periodos de pescas")
                mostrar(periodos[(periodos['Estado']=='Modificada')|(periodos['Estado']=="Copia corregida")])
                mostrar(str(len(periodos[(periodos['Estado']=='Modificada')|(periodos['Estado']=="Copia corregida")]))+" Modificadas")

            elif 'sobre autorizacion' == ly:
                st.subheader("Resoluciones Modificadas con respecto a autorizaciones")
                mostrar(autorizacion[(autorizacion['Estado']=='Modificada')|(autorizacion['Estado']=="Copia corregida")])
                mostrar(str(len(autorizacion[(autorizacion['Estado']=='Modificada')|(autorizacion['Estado']=="Copia corregida")]))+" Modificadas")

            elif "sobre arte de pesca" == ly:
                st.subheader("Resoluciones Modificadas con respecto a artes de pesca")
                mostrar(artes_pesca[(artes_pesca['Estado']=='Modificada')|(artes_pesca['Estado']=="Copia corregida")])
                mostrar(str(len(artes_pesca[(artes_pesca['Estado']=='Modificada')|(artes_pesca['Estado']=="Copia corregida")]))+" Modificadas")

            elif 'otros' == ly:
                st.subheader("Otras resoluciones modificadas")
                mostrar(pesca[(pesca['Estado']=='Modificada')|(pesca['Estado']=="Copia corregida")])
                mostrar(str(len(pesca[(pesca['Estado']=='Modificada')|(pesca['Estado']=="Copia corregida")]))+" Modificadas")

        elif check:
            if 'cantidad de Resoluciones por año' == ly:
                st.subheader("Resoluciones Derogadas")
                mostrar(merge[merge['Estado']=='Derogada'])
                mostrar( str(len(merge[merge['Estado']=='Derogada']))+ " Derogadas")

            elif 'sobre pesca ilegal' == ly:
                st.subheader("Resoluciones Derogadas sobre pesca ilegal")
                mostrar(pesca_ilegal[pesca_ilegal['Estado']=='Derogada'])
                mostrar(str(len(pesca_ilegal[pesca_ilegal['Estado']=='Derogada']))+ ' Derogadas')

            elif 'sobre prohibición' == ly :
                st.subheader("Resoluciones Derogadas sobre prohibición")
                mostrar(prohibicion[prohibicion['Estado']=='Derogada'])
                mostrar(str(len(prohibicion[prohibicion['Estado']=='Derogada']))+ ' Derogadas')

            elif 'sobre periodos de pesca' == ly:
                st.subheader("Resoluciones Derogadas sobre los periodos de pesca")
                mostrar(periodos[periodos['Estado']=='Derogada'])
                mostrar(str(len(periodos[periodos['Estado']=='Derogada']))+ ' Derogadas')

            elif 'sobre autorizacion' == ly:
                st.subheader("Resoluciones Derogadas sobre autorizaciones")
                mostrar(autorizacion[autorizacion['Estado']=='Derogada'])
                mostrar( str(len(autorizacion[autorizacion['Estado']=='Derogada']))+' Derogadas')
                
                
            elif "sobre arte de pesca" == ly:
                st.subheader("Resoluciones Derogadas sobre artes de pesca")
                mostrar(artes_pesca[artes_pesca['Estado']=='Derogada'])
                mostrar(str(len(artes_pesca[artes_pesca['Estado']=='Derogada']))+ ' Derogadas')
            
            elif 'otros' == ly:
                st.subheader("Resoluciones Derogadas sobre artes de pesca")
                mostrar(pesca[pesca['Estado']=='Derogada'])
                mostrar( str(len(pesca[pesca['Estado']=='Derogada']))+' Derogadas')

        elif  'cantidad de Resoluciones por año' == ly:
            st.subheader('Todas las Resoluciones sobre Pesca en Cuba')
            mostrar(merge)
            mostrar("total: "+str(len(merge)))
        
        elif 'sobre pesca ilegal' == ly:
            st.subheader("Resoluciones sobre la pesca ilegal")
            mostrar(pesca_ilegal)
            mostrar("total: "+str(len(pesca_ilegal)))

        elif 'sobre prohibición' == ly :
            st.subheader("Resoluciones sobre prohibiciones en la pesca")
            prohibicion
            mostrar("total: "+str(len(prohibicion)))

        elif 'sobre periodos de pesca' == ly:
            st.subheader("Resoluciones sobre los periodos de pesca")
            periodos
            mostrar("total: "+str(len(periodos)))

        elif 'sobre autorizacion' == ly:
            st.subheader('Resoluciones sobre autorizaciones en la pesca')
            mostrar(autorizacion)
            mostrar("total: "+str(len(autorizacion)))
            
        elif "sobre arte de pesca" == ly:
            st.subheader("Resoluciones sobre el arte de la pesca")
            artes_pesca
            mostrar("total: "+str(len(artes_pesca)))
        elif  'otros' == ly:
            st.subheader("Resoluciones sobre pesca")
            pesca
            mostrar("total: "+str(len(pesca)))

    
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
    "Empresas": mapas,
    'leyes y Resoluciones':leyes
}

selection = st.sidebar.radio("Ir a", list(pages.keys()))
pages[selection]()