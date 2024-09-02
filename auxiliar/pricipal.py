from auxiliar.graficas_plotly import *
from auxiliar.auxiliar import postcast, historia, autores, recivir_feedback
import streamlit as st
from streamlit_extras.annotated_text import annotated_text
from annotated_text import annotation


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
    annotated_text(
        "En ",
        "la ",
        "pestaña ",
        annotation("Económico", color="#38cec6", border="1px blue"),
        " puede acceder a datos sobre las capturas en toneladas de diversas especies de peces. También econtrará comparativas y análisis sobre las relaciones entre Importaciones e Exportaciones en el sector pesquero. ",
    )
    annotated_text(
        "En ",
        annotation("Empresas", color="#38cec6", border="1px blue"),
        " se presenta un listado de las principales empresas pesqueras en Cuba, así como pequeñas y medianas empresas del sector. Además, se incluyen detalles sobre su localización.",
    )
    annotated_text(
        "En ",
        annotation("leyes", color="#38cec6", border="1px blue"),
        " se recopilan las acciones y regulaciones adoptadas por el gobierno de Cuba en relación con la pesca, proporcionando un panorama claro de las políticas implementdas en este ámbito.",
    )
    annotated_text(
        "En caso de alguna sugerencia o duda, nos lo puede hacer llegar utilizando los mensajes de ",
        annotation("sugerencias", color="#38cec6", border="1px blue"),
        ". Se encuentra al final de cada página. Gracias.",
    )
    st.divider()
    st.markdown(
        """<h4 class = 'sub'>Extras</h4> <style>
                    .sub{
                    font-size: 40px;
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
    st.write("")
    st.write("⬇️")
    if st.checkbox("¿Quiénes somos?"):
        autores()
