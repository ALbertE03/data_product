import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go


with open("./data/pib_corriente.json", "r") as jsonfile:
    pib_corriente = json.load(jsonfile)

pib_corriente_aux = {}

for i in pib_corriente:
    pepe = []
    for t, j in enumerate(pib_corriente[i]):
        if t <= 20:
            if j != 0 and t != 0:
                pepe.append(j)

    pib_corriente_aux[i] = pepe


pib_corriente_df = pd.DataFrame(pib_corriente_aux)

totales_pib = pib_corriente_df.iloc[0]

pib_corriente_df = pib_corriente_df.drop(index=0)

pib_corriente_df.index = [
    "Agricultura, ganadería y silvicultura ",
    "Pesca",
    " Explotación de minas y canteras",
    " Industria azucarera",
    " Industrias manufactureras (excepto Industria  azucarera)",
    " Suministro de electricidad, gas y agua",
    " Construcción",
    " Comercio; reparación de efectos personales",
    " Hoteles y restaurantes",
    " Transportes, almacenamiento y comunicaciones",
    " Intermediación financiera",
    " Servicios empresariales, actividades inmobiliarias  y de alquiler",
    "Administración pública, defensa; seguridad social",
    " Ciencia e innovación tecnológica",
    " Educación",
    " Salud pública y asistencia social",
    " Cultura y deporte",
    " Otras act de servicios comunales, de asociaciones y personales",
    " Derechos de importación",
]

fig1 = px.line(
    pib_corriente_df.loc["Pesca"].T,
    title="Evolución del pib de la pesca a precios corrientes",
)
fig1.update_layout(yaxis_title="millones de pesos", xaxis_title="años")


def auto(año, df):
    fig = go.Figure(
        data=[
            go.Bar(
                x=list(df.index),
                y=df[año],
                text=df[año],
                textposition="auto",
                marker_color="skyblue",
            )
        ]
    )
    fig.add_hline(
        y=sum(df[año]) / len(df[año]),
        line_dash="dash",
        line_color="red",
        annotation_text="media",
    )
    fig.update_layout(
        title=f"PIB a precios corrientes {año}", yaxis_title="Millones de pesos"
    )
    return fig, sum(df[año]) / len(df[año])


def pastel(año):
    pesca = pib_corriente_df[str(año)].iloc[1]
    total = totales_pib[str(año)] - pesca
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["restantes", "pesca"],
                values=[total, pesca],
                hole=0.1,
                marker=dict(line=dict(color="black", width=0.1)),
            )
        ]
    )
    fig.update_layout(title=f"Porciento del pib en el año {año}")
    return fig
