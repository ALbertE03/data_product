import streamlit as st
from charts.graficas_plotly import *
import plotly.graph_objects as go
import streamlit_analytics
import folium
from streamlit_folium import st_folium
from streamlit_feedback import streamlit_feedback
import telebot
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from charts.pib_corriente import *
from charts.pib_const import *

st.set_page_config(
    page_title="Data Product",
    page_icon="🦈",
    layout="wide",
)

with streamlit_analytics.track(unsafe_password="Pesca1234", verbose=True):

    def recivir_feedback(feedback):
        token = "7235089424:AAFG69LRNuLCYOFCdnLDuPMQiKxLo7AOj98"
        bot = telebot.TeleBot(token)

        chat_id = "1883265786"
        try:
            bot.send_message(chat_id=chat_id, text=feedback)
            st.success("Recibido ✅")

        except Exception as e:
            st.error(f"Error al enviar el mensaje: {e}")

    def mostrar(a):
        st.write(a)

    def mostrar_grafica(graf):
        graf.update_layout(showlegend=True)
        st.plotly_chart(graf, use_container_width=True)

    def mostrar_grafica_sin(g):
        g.update_layout(showlegend=False)
        st.plotly_chart(g, use_container_width=True)

    def warning(a):
        st.warning(a)

    def principal():

        st.markdown(
            """<h1 class = 'titulo'>La Pesca en Cuba</h1> <style>
                .titulo{
                font-size: 60px;
                text-align: center;
                }
            </style>""",
            unsafe_allow_html=True,
        )

        st.write(
            """<p style='text-aling:center;'>En Económico puede encontrar las capturas en toneladas de los diferentes peces, además, 
                la comparativa y relaciones entre Importaciones e Exportaciones.<p> """,
            unsafe_allow_html=True,
        )
        st.write(
            """En Empresas se encuentran las principales empresas de pesca en Cuba, 
                junto a las pequeñas y medianas empresas, sus localizaciones y las principales zonas de pesca.""",
            unsafe_allow_html=True,
        )
        st.write(
            "En leyes y Resoluciones se encuentran las acciones que ah tomado el gobierno de Cuba con respecto a la Pesca.",
            unsafe_allow_html=True,
        )

        st.subheader("Dejar suguerencias")
        feed = st.text_area("", help="Si es posible su pedido será añadido")
        if st.button("Enviar"):
            if feed:
                recivir_feedback(feed)

    def economico():

        st.title("Captura de diferentes especies en Cuba")
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
        if opciones == "Selecione una especie":
            mostrar_grafica_sin(peces_sum_line)
        if opciones == "Pargo":
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

        pibruto = st.checkbox("PIB-precios corrientes")
        if pibruto:
            st.info(
                "a partir del 2021 se nota un aumento drástico debido a la Tarea Ordenamieto"
            )
            mostrar_grafica_sin(fig1)

            slider = st.slider("selecione un año", 2010, 2022)
            st.info("linea roja representa la media en cada año")
            mostrar_grafica_sin(auto(str(slider), pib_corriente_df))
            paste = pastel(slider)
            mostrar_grafica(paste)

        pibrutoC = st.checkbox("PIB-precios constantes")
        if pibrutoC:
            st.info(
                "a partir del 2021 se nota un aumento drástico debido a la Tarea Ordenamieto"
            )
            mostrar_grafica_sin(fig)
            slider1 = st.slider("selecione un año", 2005, 2022)
            st.info("linea roja representa la media en cada año")
            mostrar_grafica_sin(auto1(slider1, pib_const_aux_df))
            mostrar_grafica(pastel1(slider1))

        st.subheader("Dejar suguerencias")
        feed = st.text_area("", help="Si es posible su pedido será añadido")
        if st.button("Enviar"):
            if feed:
                recivir_feedback(feed)

    def leyes():
        st.title("¿Cómo han cambiado las leyes con respecto a la pesca en Cuba?")
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

        if "sobre pesca ilegal" == ly:
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

        if st.checkbox("Mostrar las resoluciones"):
            st.markdown("Selecione un estado")
            check = st.checkbox("derogadas")
            check1 = st.checkbox("Modificadas")
            check2 = st.checkbox("Vigentes")

            if check and check1 and check2:
                warning(
                    "Seleccione solo una; una ley no puede estar en tres estados a la vez"
                )

            elif check1 and check:
                warning(
                    "Seleccione solo una; una ley no puede estar en dos estados a la vez"
                )

            elif check1 and check2:
                warning(
                    "Seleccione solo una; una ley no puede estar en dos estados a la vez"
                )

            elif check and check2:
                warning(
                    "Seleccione solo una; una ley no puede estar en dos estados a la vez"
                )

            elif check2:
                if "cantidad de Resoluciones por año" == ly:
                    st.subheader("Resoluciones Vigentes")
                    mostrar(merge[merge["Estado"] == "Vigente"])
                    mostrar(str(len(merge[merge["Estado"] == "Vigente"])) + " Vigentes")

                elif "sobre pesca ilegal" == ly:
                    st.subheader("Resoluciones Vigentes respecto a la pesca ilegal")
                    mostrar(pesca_ilegal[pesca_ilegal["Estado"] == "Vigente"])
                    mostrar(
                        str(len(pesca_ilegal[pesca_ilegal["Estado"] == "Vigente"]))
                        + " Vigentes"
                    )

                elif "sobre prohibición" == ly:
                    st.subheader("Resoluciones Vigentes en cuanto a prohibiciones")
                    mostrar(prohibicion[prohibicion["Estado"] == "Vigente"])
                    mostrar(
                        str(len(prohibicion[prohibicion["Estado"] == "Vigente"]))
                        + " Vigentes"
                    )

                elif "sobre periodos de pesca" == ly:
                    st.subheader(
                        "Resoluciones Vigentes con respecto a los periodos de pescas"
                    )
                    mostrar(periodos[periodos["Estado"] == "Vigente"])
                    mostrar(
                        str(len(periodos[periodos["Estado"] == "Vigente"]))
                        + " Vigentes"
                    )

                elif "sobre autorizacion" == ly:
                    st.subheader("Resoluciones Vigentes con respecto a autorizaciones")
                    mostrar(autorizacion[autorizacion["Estado"] == "Vigente"])
                    mostrar(
                        str(len(autorizacion[autorizacion["Estado"] == "Vigente"]))
                        + " Vigentes"
                    )

                elif "sobre arte de pesca" == ly:
                    st.subheader("Resoluciones Vigentes con respecto a artes de pesca")
                    mostrar(artes_pesca[artes_pesca["Estado"] == "Vigente"])
                    mostrar(
                        str(len(artes_pesca[artes_pesca["Estado"] == "Vigente"]))
                        + " Vigentes"
                    )

                elif "otros" == ly:
                    st.subheader("Otras resoluciones Vigentes")
                    mostrar(pesca[pesca["Estado"] == "Vigente"])
                    mostrar(str(len(pesca[pesca["Estado"] == "Vigente"])) + " Vigentes")

            elif check1:
                if "cantidad de Resoluciones por año" == ly:
                    st.subheader("Resoluciones Modificadas")
                    mostrar(
                        merge[
                            (merge["Estado"] == "Modificada")
                            | (merge["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                merge[
                                    (merge["Estado"] == "Modificada")
                                    | (merge["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

                elif "sobre pesca ilegal" == ly:
                    st.subheader(
                        "Resoluciones Modificadas con respecto a la pesca ilegal"
                    )
                    mostrar(
                        pesca_ilegal[
                            (pesca_ilegal["Estado"] == "Modificada")
                            | (pesca_ilegal["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                pesca_ilegal[
                                    (pesca_ilegal["Estado"] == "Modificada")
                                    | (pesca_ilegal["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

                elif "sobre prohibición" == ly:
                    st.subheader("Resoluciones Modificadas en cuanto a prohibiciones")
                    mostrar(
                        prohibicion[
                            (prohibicion["Estado"] == "Modificada")
                            | (prohibicion["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                prohibicion[
                                    (prohibicion["Estado"] == "Modificada")
                                    | (prohibicion["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

                elif "sobre periodos de pesca" == ly:
                    st.subheader(
                        "Resoluciones Modificadas con respecto a los periodos de pescas"
                    )
                    mostrar(
                        periodos[
                            (periodos["Estado"] == "Modificada")
                            | (periodos["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                periodos[
                                    (periodos["Estado"] == "Modificada")
                                    | (periodos["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

                elif "sobre autorizacion" == ly:
                    st.subheader(
                        "Resoluciones Modificadas con respecto a autorizaciones"
                    )
                    mostrar(
                        autorizacion[
                            (autorizacion["Estado"] == "Modificada")
                            | (autorizacion["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                autorizacion[
                                    (autorizacion["Estado"] == "Modificada")
                                    | (autorizacion["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

                elif "sobre arte de pesca" == ly:
                    st.subheader(
                        "Resoluciones Modificadas con respecto a artes de pesca"
                    )
                    mostrar(
                        artes_pesca[
                            (artes_pesca["Estado"] == "Modificada")
                            | (artes_pesca["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                artes_pesca[
                                    (artes_pesca["Estado"] == "Modificada")
                                    | (artes_pesca["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

                elif "otros" == ly:
                    st.subheader("Otras resoluciones modificadas")
                    mostrar(
                        pesca[
                            (pesca["Estado"] == "Modificada")
                            | (pesca["Estado"] == "Copia corregida")
                        ]
                    )
                    mostrar(
                        str(
                            len(
                                pesca[
                                    (pesca["Estado"] == "Modificada")
                                    | (pesca["Estado"] == "Copia corregida")
                                ]
                            )
                        )
                        + " Modificadas"
                    )

            elif check:
                if "cantidad de Resoluciones por año" == ly:
                    st.subheader("Resoluciones Derogadas")
                    mostrar(merge[merge["Estado"] == "Derogada"])
                    mostrar(
                        str(len(merge[merge["Estado"] == "Derogada"])) + " Derogadas"
                    )

                elif "sobre pesca ilegal" == ly:
                    st.subheader("Resoluciones Derogadas sobre pesca ilegal")
                    mostrar(pesca_ilegal[pesca_ilegal["Estado"] == "Derogada"])
                    mostrar(
                        str(len(pesca_ilegal[pesca_ilegal["Estado"] == "Derogada"]))
                        + " Derogadas"
                    )

                elif "sobre prohibición" == ly:
                    st.subheader("Resoluciones Derogadas sobre prohibición")
                    mostrar(prohibicion[prohibicion["Estado"] == "Derogada"])
                    mostrar(
                        str(len(prohibicion[prohibicion["Estado"] == "Derogada"]))
                        + " Derogadas"
                    )

                elif "sobre periodos de pesca" == ly:
                    st.subheader("Resoluciones Derogadas sobre los periodos de pesca")
                    mostrar(periodos[periodos["Estado"] == "Derogada"])
                    mostrar(
                        str(len(periodos[periodos["Estado"] == "Derogada"]))
                        + " Derogadas"
                    )

                elif "sobre autorizacion" == ly:
                    st.subheader("Resoluciones Derogadas sobre autorizaciones")
                    mostrar(autorizacion[autorizacion["Estado"] == "Derogada"])
                    mostrar(
                        str(len(autorizacion[autorizacion["Estado"] == "Derogada"]))
                        + " Derogadas"
                    )

                elif "sobre arte de pesca" == ly:
                    st.subheader("Resoluciones Derogadas sobre artes de pesca")
                    mostrar(artes_pesca[artes_pesca["Estado"] == "Derogada"])
                    mostrar(
                        str(len(artes_pesca[artes_pesca["Estado"] == "Derogada"]))
                        + " Derogadas"
                    )

                elif "otros" == ly:
                    st.subheader("Resoluciones Derogadas sobre artes de pesca")
                    mostrar(pesca[pesca["Estado"] == "Derogada"])
                    mostrar(
                        str(len(pesca[pesca["Estado"] == "Derogada"])) + " Derogadas"
                    )

            elif "cantidad de Resoluciones por año" == ly:
                st.subheader("Todas las Resoluciones sobre Pesca en Cuba")
                mostrar(merge)
                mostrar("total: " + str(len(merge)))

            elif "sobre pesca ilegal" == ly:
                st.subheader("Resoluciones sobre la pesca ilegal")
                mostrar(pesca_ilegal)
                mostrar("total: " + str(len(pesca_ilegal)))

            elif "sobre prohibición" == ly:
                st.subheader("Resoluciones sobre prohibiciones en la pesca")
                mostrar(prohibicion)
                mostrar("total: " + str(len(prohibicion)))

            elif "sobre periodos de pesca" == ly:
                st.subheader("Resoluciones sobre los periodos de pesca")
                mostrar(periodos)
                mostrar("total: " + str(len(periodos)))

            elif "sobre autorizacion" == ly:
                st.subheader("Resoluciones sobre autorizaciones en la pesca")
                mostrar(autorizacion)
                mostrar("total: " + str(len(autorizacion)))

            elif "sobre arte de pesca" == ly:
                st.subheader("Resoluciones sobre el arte de la pesca")
                mostrar(artes_pesca)
                mostrar("total: " + str(len(artes_pesca)))

            elif "otros" == ly:
                st.subheader("Resoluciones sobre pesca")
                mostrar(pesca)
                mostrar("total: " + str(len(pesca)))

        with open("analytics.html", "r") as file:
            html = file.read()

        components.html(html)
        st.subheader("Dejar suguerencias")
        feed = st.text_area("", help="Si es posible su pedido será añadido")
        if st.button("Enviar"):
            if feed:
                recivir_feedback(feed)

    def mapas():
        st.title("Empresas de Pesca en Cuba")

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
                mostrar_grafica_sin(graficar_pastel_mypime(o, 0))
            if o == "Artemisa":
                mostrar_grafica_sin(p1)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 1))
            if o == "La Habana":
                mostrar_grafica_sin(p2)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 2))
            if o == "Mayabeque":
                mostrar_grafica_sin(p3)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 3))
            if o == "Matanzas":
                mostrar_grafica_sin(p4)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 4))
            if o == "Villa Clara":
                mostrar_grafica_sin(p5)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 5))
            if o == "Cienfuegos":
                mostrar_grafica_sin(p6)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 6))
            if o == "Santi Spiritus":
                mostrar_grafica_sin(p7)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 7))
            if o == "Ciego de Ávila":
                mostrar_grafica_sin(p8)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 8))
            if o == "Camagüey":
                mostrar_grafica_sin(p9)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 9))
            if o == "Las Tunas":
                mostrar_grafica_sin(p10)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 10))
            if o == "Holguín":
                mostrar_grafica_sin(p11)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 11))
            if o == "Granma":
                mostrar_grafica_sin(p12)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 12))
            if o == "Santiago de Cuba":
                mostrar_grafica_sin(p13)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 13))
            if o == "Guantánamo":
                mostrar_grafica_sin(p14)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 14))
            if o == "La Isla de la Juventud":
                mostrar_grafica_sin(p15)
                mostrar_grafica_sin(graficar_pastel_mypime(o, 15))

            prov = st.checkbox("Totales")
            if prov:
                mostrar_grafica_sin(mypimesdf_bar)
        if option == "EpiGram":
            st.subheader("EpiGram")
            st_folium(m, width=700, height=700)

        if option == "PESCAGRAM":
            st.subheader("PESCAGRAM")
            st_folium(m1, width=700, height=700)

        if option == "EPICAI":
            st.subheader("EPICAI")
            st_folium(m2, width=700, height=700)

        if option == "EPICIEN":
            st.subheader("EPICIEN")
            st_folium(m3, width=700, height=700)

        if option == "Pesca Caribe":
            st.subheader("Pesca Caribe")
            st_folium(m4, width=700, height=700)

        if option == "GEIP":
            st.subheader("Grupo Empresarial de La Industria Pesquera (GEIP)")
            st_folium(m5, width=700, height=700)

        st.subheader("Dejar suguerencias")
        feed = st.text_area("", help="Si es posible su pedido será añadido")
        if st.button("Enviar"):
            if feed:
                recivir_feedback(feed)

    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Económico", "Empresas", "Leyes"],
        icons=["house", "currency-dollar", "building", "clipboard"],
        default_index=0,
        orientation="horizontal",
    )

    if selected == "Inicio":
        principal()
    if selected == "Económico":
        economico()
    if selected == "Empresas":
        mapas()
    if selected == "Leyes":
        leyes()
