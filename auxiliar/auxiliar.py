import telebot
import os
import time
import streamlit as st

from streamlit_feedback import streamlit_feedback
from auxiliar.pib_const import *
from auxiliar.pib_corriente import *
from auxiliar.graficas_plotly import (
    merge,
    leyes_annos,
    leyes_auto,
    leyes_ilegal,
    leyes_prohi,
    leyes_periodo,
    leyes_arte,
    leyes_otros,
    autorizacion,
    artes_pesca,
    pesca_ilegal,
    periodos,
    prohibicion,
    pesca,
)


def postcast():
    st.markdown(
        """<h1 class = 'redes'>Redes de Pesca Cubanas</h1> <style>
                .redes{
                font-size: 60px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.write(
        """Bienvenidos a nuestro podcast Redes de Pesca Cubanas en el cual te invimitamos a sumergirte en las aguas de nuestro país 
            y conocer sobre el maravilloso arte de la pesca en nuestro primer episodio 'Economía de Pesca' 
            conversaremos sobre el impacto económico del sector pesquero en nuestra Isla, 
            sin más, los exorto a que se adentren y conozcan nuestro podcast."""
    )
    st.markdown("#### Capítulo 1:")
    st.audio(
        "AUDIO-2024-08-21-21-32-12.m4a",
    )

    streamlit_feedback("thumbs")

    st.write("👇 podrán encontar los demás capitulos.")
    if st.button("Más Capítulos"):
        with st.spinner("El proceso puede tardar unos segundos..."):
            time.sleep(5)

            st.warning("Proximamente disponible...")


def recivir_feedback(feedback):

    token = st.secrets.token
    bot = telebot.TeleBot(token)
    chat_id = st.secrets.chat_id
    try:
        bot.send_message(chat_id=chat_id, text=feedback)
        st.success("Recibido ✅, si es posible será agregado. Gracias")
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


def historia():

    st.markdown(
        """<h1 class = 'hist'>Aguas de Esperanza </h1> <style>
                .hist{
                font-size: 30px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<h3 class = 'hist1'>La Historia y el Futuro  de la pesca en Cuba</h3> <style>
                .hist1{
                font-size: 25px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )

    st.write(
        """
               La pesca en Cuba ha pasado de ser una actividad floreciente a enfrentar 
               serios desafíos debido a la sobreexplotación, la contaminación y el cambio 
               climático. En los años 60 y 70, las capturas aumentaron significativamente, 
               impulsadas por políticas gubernamentales que promovían la explotación de los 
               recursos marinos. Sin embargo, a partir de los años 80, la tasa de crecimiento 
               de las capturas comenzó a disminuir, y en los 90, varias pesquerías importantes 
               entraron en decadencia. De 1990 a 2023, la producción de pescados y mariscos se 
               redujo de 188000 a 31933.07 toneladas. Durante los años 1960, 1961 y 1962 las 
               importaciones de productos pesqueros en Cuba sufrieron una drástica disminución 
               como consecuencia de la reorientación que estaba tomando el comercio exterior. 
               En esos años las principales importaciones fueron el bacalao seco y la sardina 
               enlatada.
               A partir del año 1963 se observa una fuerte recuperación de las importaciones 
               debido al convenio que se firmó con la Unión Soviética, en virtud del cual se 
               inició la entrega en puertos cubanos de pescado fresco, como merluza, Saida y 
               Pikcha por parte de la flota soviética que operaba en las proximidades del 
               territorio cubano, como también bacalao seco o en salmuera y sardinas para ser 
               elaborado posteriormente en industrias cubanas.
               Durante el año 1964 las importaciones estuvieron compuestas por 10.721 toneladas 
               de pescado congelado, 13.330 toneladas de bacalao y 8.350 de sardinas en lata, que 
               costaron al país la suma de 14 millones de dólares.
               En términos de comercio, el valor de las importaciones de productos pesqueros siempre 
               ha superado al de las exportaciones, con un saldo negativo creciente desde \$1.314.000 
               en 1960 hasta \$12.702.000 en 1964. Esta tendencia desfavorable se explica por la 
               eliminación que ha tenido la colocación de los productos cubanos en los mercados 
               americanos. Las importaciones de pescados se vieron incrementadas por la presencia de la 
               flota pesquera soviética del Atlántico en Cuba y su aumento sirvió para solucionar las 
               deficiencias de abastecimientos de productos alimenticios en el país. El principal rubro 
               de exportación en Cuba era la langosta y los niveles más altos de ventas al exterior se 
               alcanzaron en 1959 y 1960. Con posterioridad a estos años, las exportaciones han sufrido 
               una violenta contracción por la pérdida de los mercados tradicionales.
               En el año 1965 se observó una recuperación de las exportaciones, gracias a la apertura 
               de nuevos mercados como los de Canadá y Francia, para la venta de langostas en lata. 
               El total de las exportaciones pesqueras alcanzaron a $3.385.000 en 1965, dentro de los 
               cuales el 71% corresponde al valor de la langosta.
               Para revertir esta situación, es crucial implementar medidas de gestión sostenible que 
               incluyan la regulación del esfuerzo pesquero, la protección de los hábitats marinos y l
               a reducción de la contaminación. Uno de los más grandes desafíos que afronta la pesca en 
               Cuba es la sobrepesca y la contaminación. De acuerdo con el VI Informe Nacional al Convenio 
               sobre la Diversidad Biológica (CDB) de la Isla, las actividades excesivas de captura suponen 
               una fuerte presión sobre los ecosistemas marinos y reducen drásticamente las poblaciones de 
               peces, invertebrados y plantas acuáticas. A ello también han contribuido las operaciones de 
               pesca ilegal y las prácticas nocivas de captura. Así para el 2018, el 74,4% de los recursos 
               pesqueros cubanos estaban sobreexplotados y el 5,2% colapsados. Además, la contaminación de los 
               acuíferos y la presencia de especies invasoras han contribuido a la degradación de los 
               ecosistemas marinos. De acuerdo con el Informe de Cuba al CDB, el país requiere identificar a 
               las especies de peces más vulnerables en las zonas de pesca y establecer límites de captura, 
               evaluar el empleo de las artes de pesca masiva y el cumplimiento de las disposiciones al respecto, 
               fortalecer los mecanismos para el control de la pesca no estatal y para la regulación de los recursos 
               marinos, implementar medidas para reducir las presiones antropogénicas sobre los arrecifes de coral, así 
               como crear acciones de rehabilitación y conservación para estos últimos. El documento reconoce que las acciones 
               para la prevención de ilegalidades resultan insuficientes.
               En este sentido, en 2019 el país aprobó la Ley de Pesca y su Reglamento, publicados en la Gaceta Oficial No. 11 
               Ordinaria de 7 de febrero de 2020 con el objetivo de “establecer las regulaciones para el adecuado ordenamiento, 
               administración y control de la pesca, en función de la conservación y el aprovechamiento racional de los recursos 
               hidrobiológicos."""
    )


def autores():
    st.markdown(
        """<h1 class = 'uni'>Universidad de la Habana🏛️</h1> <style>
                .uni{
                font-size: 60px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'facu'>Facultad: MATCOM </h2> <style>
                .facu{
                font-size: 45px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h2 class = 'carr'>Carrera: Ciencia de Datos</h2> <style>
                .carr{
                font-size: 35px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h5 class = 'name1'>Alberto E Marichal Fonseca: primer año</h5> <style>
                .name1{
                font-size: 25px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """<h5 class = 'name1'>Dalia Castro Valdes: primer año</h5> <style>
                .name1{
                font-size: 25px;
                text-align: center;
                }
            </style>""",
        unsafe_allow_html=True,
    )


def mostrar_pib():
    st.subheader("PIB-precios constantes")
    mostrar_grafica_sin(fig)
    slider1 = st.slider("selecione un año", 2005, 2022)
    st.info("linea roja representa la media en cada año")
    mostrar(f"La media del {slider1} es: {auto1(slider1, pib_const_aux_df)[1]}")
    mostrar_grafica_sin(auto1(slider1, pib_const_aux_df)[0])
    mostrar_grafica(pastel1(slider1))

    st.divider()

    st.subheader("PIB-precios corrientes")
    st.info(
        "a partir del 2021 se nota un aumento drástico debido a la Tarea Ordenamieto"
    )
    mostrar_grafica_sin(fig1)

    slider = st.slider("selecione un año", 2010, 2022)
    st.info("linea roja representa la media en cada año")
    mostrar(f"La media del {slider} es: {auto(str(slider), pib_corriente_df)[1]}")
    mostrar_grafica_sin(auto(str(slider), pib_corriente_df)[0])
    paste = pastel(slider)
    mostrar_grafica(paste)


def mostrar_leyes(f):
    ly = f
    st.markdown("Selecione un estado")
    check = st.checkbox("derogadas")
    check1 = st.checkbox("Modificadas")
    check2 = st.checkbox("Vigentes")

    if check and check1 and check2:
        warning("Seleccione solo una; una ley no puede estar en tres estados a la vez")

    elif check1 and check:
        warning("Seleccione solo una; una ley no puede estar en dos estados a la vez")

    elif check1 and check2:
        warning("Seleccione solo una; una ley no puede estar en dos estados a la vez")

    elif check and check2:
        warning("Seleccione solo una; una ley no puede estar en dos estados a la vez")

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
                str(len(prohibicion[prohibicion["Estado"] == "Vigente"])) + " Vigentes"
            )

        elif "sobre periodos de pesca" == ly:
            st.subheader("Resoluciones Vigentes con respecto a los periodos de pescas")
            mostrar(periodos[periodos["Estado"] == "Vigente"])
            mostrar(str(len(periodos[periodos["Estado"] == "Vigente"])) + " Vigentes")

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
                str(len(artes_pesca[artes_pesca["Estado"] == "Vigente"])) + " Vigentes"
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
            st.subheader("Resoluciones Modificadas con respecto a la pesca ilegal")
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
            st.subheader("Resoluciones Modificadas con respecto a autorizaciones")
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
            st.subheader("Resoluciones Modificadas con respecto a artes de pesca")
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
            mostrar(str(len(merge[merge["Estado"] == "Derogada"])) + " Derogadas")

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
            mostrar(str(len(periodos[periodos["Estado"] == "Derogada"])) + " Derogadas")

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
            mostrar(str(len(pesca[pesca["Estado"] == "Derogada"])) + " Derogadas")

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
