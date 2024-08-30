from auxiliar.graficas_plotly import *
from auxiliar.auxiliar import postcast, historia, autores, recivir_feedback
import streamlit as st


def mostrar_principal():
    st.markdown(
        """<h1 class = 'titulos'>La Pesca en Cuba</h1> <style>
                .titulos{
                font-size: 60px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h4 class = 'sub'>Como navegar:</h4> <style>
                .sub{
                font-size: 30px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )

    st.write(
        """En la pestaña Económico puede acceder a datos sobre las capturas en toneladas de diversas especies de peces. También
                econtrará comparativas y análisis sobre las relaciones entre Importaciones e Exportaciones en el sector pesquero. """,
    )
    st.write(
        """En Empresas se presenta un listado de las principales empresas pesqueras en Cuba,
                así como pequeñas y medianas empresas del sector. Además, se incluyen detalles 
                sobre su localización.""",
    )
    st.write(
        """En leyes se recopilan las acciones y regulaciones adoptadas por el gobierno de Cuba 
            en relación con la pesca, proporcionando un panorama claro de las políticas implementdas 
            en este ámbito. """,
    )
    st.divider()
    st.markdown(
        """<h4 class = 'sub'>Extras</h4> <style>
                .sub{
                font-size: 30px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.write("⬇️")
    if st.checkbox("sobre nuestro postcast"):
        postcast()
    st.write("⬇️")
    if st.checkbox("Historias de Pesca"):
        historia()
    st.write("⬇️")
    if st.checkbox("¿Quiénes somos?"):
        autores()
    feed = st.chat_input("Sugerencias")
    if feed:
        recivir_feedback(feed)
