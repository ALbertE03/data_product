import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
import folium
import matplotlib.pyplot as plt
import seaborn as sns


# arreglar el json de exportacion
def llenar(df):
    columns = ["names"] + [x for x in range(1998, 2023)]
    exp = {}
    for i, j in enumerate(df):
        contador = 0
        auxiliar = []
        for u in df[j]:
            if contador >= 3:
                auxiliar.append(u)
            contador += 1
        exp[str(columns[i])] = auxiliar
    return exp


def separar(exp, boolean):
    miles_peso1 = []
    toneladas1 = []
    if boolean:
        for j in exp:
            if j != "names":
                y = []
                o = []
                for t, u in enumerate(exp[j]):

                    if t < 32:

                        if (
                            t == 4
                            or t == 6
                            or t == 10
                            or t == 12
                            or t == 14
                            or t == 16
                            or t == 19
                            or t == 21
                            or t == 23
                            or t == 25
                            or t == 28
                        ):
                            if isinstance(u, str):
                                y.append(0)
                            else:
                                y.append(u)
                        elif isinstance(u, str):
                            o.append(0)
                        else:
                            o.append(u)

                miles_peso1.append(o)
                toneladas1.append(y)
        return miles_peso1, toneladas1

    for j in exp:
        if j != "names":
            y = []
            o = []
            for t, u in enumerate(exp[j]):
                if t < 32:
                    if (
                        t == 2
                        or t == 4
                        or t == 6
                        or t == 8
                        or t == 11
                        or t == 13
                        or t == 15
                        or t == 17
                        or t == 20
                        or t == 22
                        or t == 25
                        or t == 27
                        or t == 29
                        or t == 31
                        or t == 33
                    ):
                        if isinstance(u, str):
                            y.append(0)
                        else:
                            y.append(u)
                    elif isinstance(u, str):
                        o.append(0)
                    else:
                        o.append(u)
            miles_peso1.append(o)
            toneladas1.append(y)
    return miles_peso1, toneladas1


def arreglar(grupos_exp):
    grupos_exp_real = {}
    años = [x for x in range(1984, 2023)]
    for i, j in enumerate(grupos_exp):
        if i != 0:
            r = []
            for e, t in enumerate(grupos_exp[j]):
                if j == "Unnamed: 37":
                    if e == 0 or e == 1 or e == 2:
                        continue
                elif j == "Unnamed: 18":
                    if e == 0 or e == 1 or e == 2:
                        continue
                elif e == 0 or e == 1:
                    continue
                r.append(t)

            grupos_exp_real[años[i]] = r
    return grupos_exp_real


def obtener_grafica_pez(peces, pez, pescados_predict):
    fig = px.line(
        pd.concat([peces[pez], pescados_predict.T.loc[pez]]),
        title=f"Capturas de {pez} en Toneladas",
    )
    fig.update_layout(
        showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
    )
    return fig


def obtener_mapa(lati, long):
    fig = folium.Map(location=[lati, long])
    fig.add_child(folium.Marker(location=[lati, long]))
    return fig
