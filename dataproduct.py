import streamlit as st
import plotly.graph_objects as go
import streamlit_analytics
import folium
import telebot
import streamlit.components.v1 as components
import time
import os

from dotenv import load_dotenv
from streamlit_folium import st_folium
from streamlit_feedback import streamlit_feedback
from streamlit_option_menu import option_menu

# locales
from charts.graficas_plotly import *
from auxiliar.auxiliar import *
from auxiliar.arreglos import graficar_mypimes_total_pastel, graficar_pastel_mypime

st.set_page_config(
    page_title="Data Product",
    page_icon="🦈",
    layout="wide",
)
st.logo("data/logo/6156312.jpeg")
load_dotenv()
with streamlit_analytics.track(unsafe_password=st.secrets.pesca, verbose=True):

    def principal():
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
                sobre su localización y las principales zonas de pesca que operan""",
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

    def economico():
        st.markdown(
            """<h1 class = 'titulos'>Captura de diferentes especies en Cuba</h1> <style>
                .titulos{
                font-size: 40px;
                text-align: center;
                }
            </style>""",
            unsafe_allow_html=True,
        )
        opciones = st.selectbox(
            "Seleccione una especie",
            [
                "Captura total",
                "todos a la vez",
                "Pargo",
                "Cherna",
                "Túnidos",
                "Bonito",
                "Biajaiba",
                "Machuelo",
                "Rabirubia",
                "Raya",
                "Carpa",
                "Tencas",
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
            help="Selecione una opción para las captura realizadas desde el 2001 hasta 2022",
        )
        if opciones == "Captura total":
            mostrar_grafica_sin(peces_sum_line)
        elif opciones == "todos a la vez":
            if st.checkbox("leyenda"):
                mostrar_grafica(fish)
            else:
                mostrar_grafica_sin(fish)
        elif opciones == "Pargo":
            mostrar_grafica_sin(pargo)
        elif opciones == "Cherna":
            mostrar_grafica_sin(Cherna)
        elif opciones == "Túnidos":
            mostrar_grafica_sin(tunidos)
        elif opciones == "Bonito":
            mostrar_grafica_sin(bonitos)
        elif opciones == "Biajaiba":
            mostrar_grafica_sin(biajaiba)
        elif opciones == "Machuelo":
            mostrar_grafica_sin(machuelo)
        elif opciones == "Rabirubia":
            mostrar_grafica_sin(rabirubia)
        elif opciones == "Raya":
            mostrar_grafica_sin(raya)
        elif opciones == "Carpa":
            mostrar_grafica_sin(carpa)
        elif opciones == "Tencas":
            mostrar_grafica_sin(tenca)
        elif opciones == "Tilapia":
            mostrar_grafica_sin(tilapia)
        elif opciones == "Claria":
            mostrar_grafica_sin(claria)
        elif opciones == "Cobo":
            mostrar_grafica_sin(cobo)
        elif opciones == "Ostión":
            mostrar_grafica_sin(ostion)
        elif opciones == "Almeja":
            mostrar_grafica_sin(almeja)
        elif opciones == "Langosta":
            mostrar_grafica_sin(langosta)
        elif opciones == "Camaron de mar":
            mostrar_grafica_sin(camaron_de_mar)
        elif opciones == "Camaronicultura":
            mostrar_grafica_sin(camaronicultura)
        elif opciones == "Morallas":
            mostrar_grafica_sin(moralla)

        st.title("Exportaciones e Importaciones")

        mostrar_grafica_sin(toneladas_global_total_line)

        epo = st.checkbox("Exportaciones")
        if epo:
            precios = st.checkbox("Precios y Toneladas CUCI")
            leg = st.checkbox(
                "Mostrar leyendas (Exportaciones)",
                help="En movil, usar el modo horizontal",
            )

            if precios:
                st.subheader(
                    "Exportaciones de Productos seleccionados en la Clasificación Uniforme para el Comercio Internacioal (CUCI)"
                )

                if leg:
                    mostrar_grafica(miles_peso_line)
                else:
                    mostrar_grafica_sin(miles_peso_line)

                ton = st.selectbox(
                    "Toneladas de los Diferentes productos",
                    [
                        "Pescado y marisco fresco y congelado",
                        "Pescado y marisco en conserva",
                    ],
                )
                if ton == "Pescado y marisco en conserva":
                    mostrar_grafica_sin(toneladas_bar1)
                else:
                    mostrar_grafica_sin(toneladas_bar)
                correla = st.checkbox("Correlación precio-volumen")
                if correla and ton == "Pescado y marisco en conserva":
                    st.markdown(
                        """<h3 class = 'corr1'> Precio-Volumen de Pescado y marisco en conserva</h3>
                            <style>
                            .corr1{
                                text-aling:center;
                            }
                            </style>
                            """,
                        unsafe_allow_html=True,
                    )

                    st.text(
                        "Los valores cercanos a 1 significan que estan directamente relacionados"
                    )
                    st.text(
                        "Los valores cercanos a -1 significan que estan inversamente relacionados"
                    )
                    st.pyplot(matriz1)

                elif correla and "Pescado y marisco fresco y congelado":
                    st.markdown(
                        """<h3 class = 'corr'> Precio-Volumen de Pescado y marisco fresco y congelado </h3>
                            <style>
                            .corr{
                                text-aling:center;
                            }
                            </style>
                            """,
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        "Los valores cercanos a 1 significan que estan directamente relacionados"
                    )
                    st.markdown(
                        "Los valores cercanos a -1 significan que estan inversamente relacionados"
                    )
                    st.pyplot(matriz)
            if leg:
                mostrar_grafica(grupos_exp_line)
            else:
                mostrar_grafica_sin(grupos_exp_line)

        impo = st.checkbox("Importaciones")

        if impo:
            leg1 = st.checkbox(
                "Mostrar leyendas (Importaciones)",
                help="En movil, usar el modo horizontal",
            )
            if leg1:
                mostrar_grafica(miles_peso_impo_line)
            else:
                mostrar_grafica_sin(miles_peso_impo_line)
            opp = st.selectbox(
                "Toneladas de los Diferentes productos",
                [
                    "Pescado y marisco fresco y congelado",
                    "Otros pescados, preparados o en conserva",
                ],
            )
            if opp == "Pescado y marisco fresco y congelado":
                mostrar_grafica_sin(toneladas_impo_bar)
                st.markdown(
                    "Los valores cercanos a 1 significan que estan directamente relacionados"
                )
                st.markdown(
                    "Los valores cercanos a -1 significan que estan inversamente relacionados"
                )
                st.pyplot(matriz2)
            else:
                mostrar_grafica_sin(toneladas_impo_bar1)
                st.markdown(
                    "Los valores cercanos a 1 significan que estan directamente relacionados"
                )
                st.markdown(
                    "Los valores cercanos a -1 significan que estan inversamente relacionados"
                )
                st.pyplot(matriz3)

        with st.expander("PIB-precios constantes y corrientes"):
            mostrar_pib()

        feed = st.chat_input("Sugerencias")

        if feed:
            recivir_feedback(feed)

    def leyes():
        st.markdown(
            """<h1 class = 'titulos'>¿Cómo han cambiado las leyes con respecto a la pesca en Cuba?</h1> <style>
                .titulos{
                font-size: 40px;
                text-align: center;
                }
            </style>""",
            unsafe_allow_html=True,
        )
        ly = st.selectbox(
            "",
            [
                "cantidad de Resoluciones por año",
                "sobre pesca ilegal",
                "sobre prohibición",
                "sobre periodos de pesca",
                "sobre autorizacion",
                "sobre arte de pesca",
                "otros",
            ],
        )
        if "cantidad de Resoluciones por año" == ly:
            mostrar_grafica_sin(leyes_annos)

        elif "sobre pesca ilegal" == ly:
            mostrar(leyes_ilegal)

        elif "sobre prohibición" == ly:
            mostrar_grafica_sin(leyes_prohi)

        elif "sobre periodos de pesca" == ly:
            mostrar_grafica_sin(leyes_periodo)

        elif "sobre autorizacion" == ly:
            mostrar_grafica_sin(leyes_auto)

        elif "sobre arte de pesca" == ly:
            mostrar_grafica_sin(leyes_arte)
        elif "otros" == ly:
            mostrar_grafica_sin(leyes_otros)

        mostrar_leyes(ly)

        with open("analytics.html", "r") as file:
            html = file.read()

        components.html(html)

        feed = st.chat_input("Sugerencias")
        if feed:
            recivir_feedback(feed)

    def mapas():
        st.markdown(
            """<h1 class = 'mapas'>Empresas de Pesca en Cuba</h1> <style>
                .mapas{
                font-size: 40px;
                text-align: center;
                }
            </style>""",
            unsafe_allow_html=True,
        )
        option = st.selectbox(
            "",
            [
                "Mypimes",
                "EpiGram",
                "PESCAGRAM",
                "EPICAI",
                "EPICIEN",
                "Pesca Caribe",
                "GEIP",
            ],
        )

        if option == "Mypimes":
            o = st.selectbox("", mypimesdf.index)
            if o == "Pinar del Rio":
                mostrar_grafica_sin(p16)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 0, mypimesdf))
            if o == "Artemisa":
                mostrar_grafica_sin(p1)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 1, mypimesdf))
            if o == "La Habana":
                mostrar_grafica_sin(p2)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 2, mypimesdf))
            if o == "Mayabeque":
                mostrar_grafica_sin(p3)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 3, mypimesdf))
            if o == "Matanzas":
                mostrar_grafica_sin(p4)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 4, mypimesdf))
            if o == "Villa Clara":
                mostrar_grafica_sin(p5)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 5, mypimesdf))
            if o == "Cienfuegos":
                mostrar_grafica_sin(p6)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 6, mypimesdf))
            if o == "Santi Spiritus":
                mostrar_grafica_sin(p7)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 7, mypimesdf))
            if o == "Ciego de Ávila":
                mostrar_grafica_sin(p8)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 8, mypimesdf))
            if o == "Camagüey":
                mostrar_grafica_sin(p9)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 9, mypimesdf))
            if o == "Las Tunas":
                mostrar_grafica_sin(p10)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 10, mypimesdf))
            if o == "Holguín":
                mostrar_grafica_sin(p11)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 11, mypimesdf))
            if o == "Granma":
                mostrar_grafica_sin(p12)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 12, mypimesdf))
            if o == "Santiago de Cuba":
                mostrar_grafica_sin(p13)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 13, mypimesdf))
            if o == "Guantánamo":
                mostrar_grafica_sin(p14)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 14, mypimesdf))
            if o == "La Isla de la Juventud":
                mostrar_grafica_sin(p15)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 15, mypimesdf))
            prov = st.button("Totales")
            if prov:
                mostrar_grafica_sin(mypimesdf_bar)
                mostrar_grafica(graficar_mypimes_total_pastel(mypimesdf))
        elif option == "EpiGram":
            st.subheader("EpiGram")
            st_folium(m, width=700, height=700)

        elif option == "PESCAGRAM":
            st.subheader("PESCAGRAM")
            st_folium(m1, width=700, height=700)

        elif option == "EPICAI":
            st.subheader("EPICAI")
            st_folium(m2, width=700, height=700)

        elif option == "EPICIEN":
            st.subheader("EPICIEN")
            st_folium(m3, width=700, height=700)

        elif option == "Pesca Caribe":
            st.subheader("Pesca Caribe")
            st_folium(m4, width=700, height=700)

        elif option == "GEIP":
            st.subheader("Grupo Empresarial de La Industria Pesquera (GEIP)")
            st_folium(m5, width=700, height=700)

        feed = st.chat_input("Sugerencias")
        if feed:
            recivir_feedback(feed)

    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Económico", "Empresas", "Leyes"],
        icons=[
            "house",
            "currency-dollar",
            "building",
            "clipboard",
        ],
        default_index=0,
        orientation="horizontal",
    )

    if selected == "Inicio":
        principal()
    elif selected == "Económico":
        economico()
    elif selected == "Empresas":
        mapas()
    elif selected == "Leyes":
        leyes()
