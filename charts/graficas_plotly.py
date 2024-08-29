import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
import folium
import matplotlib.pyplot as plt
import seaborn as sns
from auxiliar.arreglos import *

# economico
with open("./data/exportaciones_por_mercancias.json", "r") as file:
    df = json.load(file)
index = [
    x for x in df["Unnamed: 2"] if x.lstrip() != "Cantidad" and x.lstrip() != "Valor"
]

exp = llenar(df)

# arreglar primera parte (productos alimenticios y animales vivos) de exportacion
toneladas = []
miles_peso = []


miles_peso, toneladas = separar(exp, True)
miles_peso = pd.DataFrame(miles_peso)
miles_peso = miles_peso.T
miles_peso.columns = [x for x in range(1998, 2023)]
miles_peso = miles_peso.drop(index=[0, 1, 2, 3, 6, 7, 12, 17, 19, 20])
miles_peso.index = [
    "Pescado y marisco fresco y congelado",
    "Pescado y marisco en conserva",
    "Papas",
    "Pimientos",
    "Cítricos",
    "Conservas de frutas y vegetales",
    "Azúcar",
    "Melaza de caña",
    "Caramelos",
    "Miel natural",
    "Manteca, grasa o aceite de cacao",
]
miles_peso_ = miles_peso.T

miles_peso_line = px.line(
    miles_peso_[
        ["Pescado y marisco fresco y congelado", "Pescado y marisco en conserva"]
    ],
    title="Precios de CUCI",
)
miles_peso_line.update_layout(xaxis_title="años", yaxis_title="Millones de pesos (MP)")

toneladas_ = pd.DataFrame(toneladas)
toneladas_ = toneladas_.T
toneladas_.columns = [x for x in range(1998, 2023)]
toneladas_.index = [
    "Pescado y marisco fresco y congelado",
    "Pescado y marisco en conserva",
    "Papas",
    "Pimientos",
    "Cítricos",
    "Conservas de frutas y vegetales",
    "Azúcar",
    "Melaza de caña",
    "Caramelos",
    "Miel natural",
    "Manteca, grasa o aceite de cacao",
]
toneladas_bar = px.bar(
    toneladas_.T["Pescado y marisco fresco y congelado"], title="Toneladas Exportadas"
)
toneladas_bar.update_layout(xaxis_title="años", yaxis_title="Cantidad en Toneladas(T)")

toneladas_bar1 = px.bar(
    toneladas_.T["Pescado y marisco en conserva"], title="Toneladas Exportadas"
)
toneladas_bar1.update_layout(xaxis_title="años", yaxis_title="Cantidad en Toneladas(T)")

toneladas_total = np.sum(
    pd.concat(
        [
            toneladas_.T["Pescado y marisco en conserva"],
            toneladas_.T["Pescado y marisco fresco y congelado"],
        ],
        axis=1,
    ).T
)
# toneladas_total_line = px.line(toneladas_total, title="total de toneladas exportadas")

# por grupos, exportacion
with open("./data/exportaciones_por_grupos.json", "r") as yeison:
    grupos_exp = json.load(yeison)


grupos_exp_real = arreglar(grupos_exp)

grupos_exp_real = pd.DataFrame(grupos_exp_real)
grupos_exp_real = grupos_exp_real.T.drop([1985, 1986, 1987])

grupos_exp_real.index = [x for x in range(1989, 2023)]
grupos_exp_real = grupos_exp_real.T
grupos_auxiliar = grupos_exp_real.copy()


grupos_exp_real.index = [
    "Productos agropecuarios",
    "Productos de la Pesca",
    "Productos de la industria azucarera",
    "Productos de la minería",
    "Productos de la industria del tabaco",
    "Otros productos",
]
with open("./data/predi.json", "r") as pepe:
    data_new = json.load(pepe)
data_new_df = pd.DataFrame(data_new)

grupos_exp_real = grupos_exp_real.drop(index="Otros productos")
data_new_df.index = [2023]

grupos_exp_real1 = pd.concat([grupos_exp_real, data_new_df.T], axis=1)

grupos_exp_line = px.line(
    grupos_exp_real1.T, title="Exportaciones de mercancías por grupos de productos"
)
grupos_exp_line.update_layout(xaxis_title="años", yaxis_title="millones de pesos(MP)")

# correlaciones  exportaciones
concatenacion = pd.concat(
    [
        miles_peso.T["Pescado y marisco fresco y congelado"],
        toneladas_.T["Pescado y marisco fresco y congelado"],
    ],
    axis=1,
)
concatenacion.columns = ["Precio", "cantidad(T)"]
corr = concatenacion.corr()
matriz = plt.figure(figsize=(4, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)

concatenacion1 = pd.concat(
    [
        miles_peso.T["Pescado y marisco en conserva"],
        toneladas_.T["Pescado y marisco en conserva"],
    ],
    axis=1,
)
concatenacion1.columns = ["Precio", "cantidad(T)"]
corr1 = concatenacion1.corr()
matriz1 = plt.figure(figsize=(4, 4))
sns.heatmap(corr1, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)


# importaciones
with open("./data/importaciones.json", "r") as f:
    importaciones = json.load(f)
imp = llenar(importaciones)
imp_real = {}
for i in imp:
    if i == "names":
        imp_real["hola"] = imp[i]
    imp_real[i] = imp[i]


miles_peso_impo, toneladas_impo = separar(imp_real, False)

miles_peso_impo = pd.DataFrame(miles_peso_impo).T.drop(index=[0, 1, 6, 11, 14])
miles_peso_impo.columns = [x for x in range(1998, 2023)]
miles_peso_impo.index = [
    "Carne de ganado bovino, congelada deshuesada",
    "Carne de ganado porcino, congelada",
    "Carne y despojos comestibles de las aves",
    "Carne y despojos de carne, preparados o en conserva,",
    "Leche condensada",
    "Leche en polvo",
    "Mantequilla",
    "Queso y cuajada",
    "Pescado y marisco fresco y congelado",
    "Otros pescados, preparados o en conserva",
    "Trigo y morcajo o tranquillón sin moler",
    "Arroz consumo",
    "Cebada sin moler",
]
miles_peso_impo = miles_peso_impo.T
miles_peso_impo_line = px.line(
    miles_peso_impo[
        [
            "Pescado y marisco fresco y congelado",
            "Otros pescados, preparados o en conserva",
        ]
    ]
)

# barras importacion
toneladas_impo_ = pd.DataFrame(toneladas_impo).T.drop(index=13)
toneladas_impo_.columns = [x for x in range(1998, 2023)]
toneladas_impo_.index = [
    "Carne de ganado bovino, congelada deshuesada",
    "Carne de ganado porcino, congelada",
    "Carne y despojos comestibles de las aves",
    "Carne y despojos de carne, preparados o en conserva,",
    "Leche condensada",
    "Leche en polvo",
    "Mantequilla",
    "Queso y cuajada",
    "Pescado y marisco fresco y congelado",
    "Otros pescados, preparados o en conserva",
    "Trigo y morcajo o tranquillón sin moler",
    "Arroz consumo",
    "Cebada sin moler",
]
toneladas_impo_bar = px.bar(toneladas_impo_.T["Pescado y marisco fresco y congelado"])

toneladas_impo_bar1 = px.bar(
    toneladas_impo_.T["Otros pescados, preparados o en conserva"]
)

toneladas_impo_total = np.sum(
    pd.concat(
        [
            toneladas_impo_.T["Otros pescados, preparados o en conserva"],
            toneladas_impo_.T["Pescado y marisco fresco y congelado"],
        ],
        axis=1,
    ).T
)
toneladas_global_total = pd.concat([toneladas_impo_total, toneladas_total], axis=1)
toneladas_global_total.columns = ["importaciones", "exportaciones"]
toneladas_global_total_line = px.line(
    toneladas_global_total, title="Total de exportacioes e importaciones"
)

# correlaciones importaciones
concatenacion2 = pd.concat(
    [
        miles_peso_impo["Pescado y marisco fresco y congelado"],
        toneladas_impo_.T["Pescado y marisco fresco y congelado"],
    ],
    axis=1,
)
concatenacion2.columns = ["Precio", "Toneladas"]
corr2 = concatenacion2.corr()
matriz2 = plt.figure(figsize=(4, 4))
sns.heatmap(corr2, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)


concatenacion3 = pd.concat(
    [
        miles_peso_impo["Otros pescados, preparados o en conserva"],
        toneladas_impo_.T["Otros pescados, preparados o en conserva"],
    ],
    axis=1,
)
concatenacion3.columns = ["Precio", "Toneladas"]
corr3 = concatenacion3.corr()
matriz3 = plt.figure(figsize=(4, 4))
sns.heatmap(corr3, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)

# peces
peces = pd.read_json("./data/grupos_de_especies.json")

peces.columns = [x for x in range(2001, 2023)]
peces = peces.drop([0]).drop([1]).drop([2])
peces.index = [
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
    "Camarón de Mar",
    "Camaronicultura",
    "Moralla",
]

peces = peces.T

pescados_predict = pd.read_json("./data/predi_pez.json")
pescados_predict.index = [2023]
fish = px.line(
    pd.concat([peces, pescados_predict]), title="capturas de peces en toneladas"
)
fish.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)
peces_concat = pd.concat([peces.T, pescados_predict.T], axis=1)
peces_sum_line = px.line(np.sum(peces_concat), title="Total de capturas de especies")
peces_sum_line.update_layout(xaxis_title="años", yaxis_title="toneladas")

pargo = obtener_grafica_pez(peces, "Pargo", pescados_predict)
Cherna = obtener_grafica_pez(peces, "Cherna", pescados_predict)
tunidos = obtener_grafica_pez(peces, "Túnidos", pescados_predict)
bonitos = obtener_grafica_pez(peces, "Bonito", pescados_predict)
biajaiba = obtener_grafica_pez(peces, "Biajaiba", pescados_predict)
machuelo = obtener_grafica_pez(peces, "Machuelo", pescados_predict)
rabirubia = obtener_grafica_pez(peces, "Rabirubia", pescados_predict)
raya = obtener_grafica_pez(peces, "Raya", pescados_predict)
carpa = obtener_grafica_pez(peces, "Carpa", pescados_predict)
tenca = obtener_grafica_pez(peces, "Tenca", pescados_predict)
tilapia = obtener_grafica_pez(peces, "Tilapia", pescados_predict)
claria = obtener_grafica_pez(peces, "Claria", pescados_predict)
cobo = obtener_grafica_pez(peces, "Cobo", pescados_predict)
ostion = obtener_grafica_pez(peces, "Ostión", pescados_predict)
almeja = obtener_grafica_pez(peces, "Almeja", pescados_predict)
langosta = obtener_grafica_pez(peces, "Langosta", pescados_predict)
camaron_de_mar = obtener_grafica_pez(peces, "Camarón de Mar", pescados_predict)
camaronicultura = obtener_grafica_pez(peces, "Camaronicultura", pescados_predict)
moralla = obtener_grafica_pez(peces, "Moralla", pescados_predict)


with open("data/mypimes.json", "r") as f:
    mypimes = json.load(f)

mypimesdf = pd.DataFrame(mypimes)
mypimesdf.columns = [
    "alojamiento de servicios de comida",
    "Agricultura,Pesca,Ganaderia y Silvicultura",
    "Comercio",
    "Industrias manufactureras",
    "información y comunicaciones",
    "Transporte y Almacenamiento",
    "Construcción",
    "Resto de Actividades",
]

mypimesdf = mypimesdf.drop([0])
mypimesdf.index = [
    "Pinar del Rio",
    "Artemisa",
    "La Habana",
    "Mayabeque",
    "Matanzas",
    "Villa Clara",
    "Cienfuegos",
    "Santi Spiritus",
    "Ciego de Ávila",
    "Camagüey",
    "Las Tunas",
    "Holguín",
    "Granma",
    "Santiago de Cuba",
    "Guantánamo",
    "La Isla de la Juventud",
]


p15 = px.bar(mypimesdf.T["Pinar del Rio"])
p15.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")


def graficar_pastel_mypime(prov, num):

    def verificar_prov(num):
        for i, j in enumerate(list(mypimesdf.index)):
            if i == num:
                return j

    prov_real = verificar_prov(num)
    mypimesdf_pr = mypimesdf.loc[prov_real]
    pesca_mypimes = mypimesdf_pr["Agricultura,Pesca,Ganaderia y Silvicultura"]
    mypimesdf_pr_sum = np.sum(mypimesdf_pr) - pesca_mypimes
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Agricultura,Pesca,Ganaderia y Silvicultura", "total"],
                values=[pesca_mypimes, mypimesdf_pr_sum],
                hole=0.1,
                marker=dict(line=dict(color="black", width=0.3)),
            )
        ]
    )
    fig.update_layout(title=f"{prov_real}")
    return fig


p1 = obtener_grafica_barra_pyme(mypimesdf.T, "Artemisa")
p2 = obtener_grafica_barra_pyme(mypimesdf.T, "La Habana")
p3 = obtener_grafica_barra_pyme(mypimesdf.T, "Mayabeque")
p4 = obtener_grafica_barra_pyme(mypimesdf.T, "Matanzas")
p5 = obtener_grafica_barra_pyme(mypimesdf.T, "Villa Clara")
p6 = obtener_grafica_barra_pyme(mypimesdf.T, "Cienfuegos")
p7 = obtener_grafica_barra_pyme(mypimesdf.T, "Santi Spiritus")
p8 = obtener_grafica_barra_pyme(mypimesdf.T, "Ciego de Ávila")
p9 = obtener_grafica_barra_pyme(mypimesdf.T, "Camagüey")
p10 = obtener_grafica_barra_pyme(mypimesdf.T, "Las Tunas")
p11 = obtener_grafica_barra_pyme(mypimesdf.T, "Holguín")
p12 = obtener_grafica_barra_pyme(mypimesdf.T, "Granma")
p13 = obtener_grafica_barra_pyme(mypimesdf.T, "Santiago de Cuba")
p14 = obtener_grafica_barra_pyme(mypimesdf.T, "Guantánamo")
p15 = obtener_grafica_barra_pyme(mypimesdf.T, "La Isla de la Juventud")
p16 = obtener_grafica_barra_pyme(mypimesdf.T, "Pinar del Rio")
mypimesdf_bar = px.bar(np.sum(mypimesdf), title="total de mypimes en Cuba")


# leyes
artes_pesca = pd.read_csv("data/artes_de_pesca.csv")
autorizacion = pd.read_csv("data/autorizacion.csv")
pesca_ilegal = pd.read_csv("data/pesca_ilegal.csv")
periodos = pd.read_csv("data/periodo_de_pesca.csv")
prohibicion = pd.read_csv("data/prohibicion_de_pesca.csv")
pesca = pd.read_csv("data/pesca.csv")

merge = pd.concat(
    [artes_pesca, autorizacion, pesca, pesca_ilegal, prohibicion, periodos]
)
merge.index = [x for x in range(1, len(merge) + 1)]
a = merge["Año"].unique()


def contar(df, target):
    cont = 0
    for i in df:
        if i == target:
            cont += 1
    return [cont]


def llenar_dict(df, aux):
    dic = {}
    for i in df:
        dic[f"{i}"] = contar(aux, i)
    return dic


dic = llenar_dict(a, merge["Año"])
years = list(dic.keys())
values = [value[0] for value in dic.values()]

dic1 = llenar_dict(autorizacion["Año"].unique(), autorizacion["Año"])
values1 = [value1[0] for value1 in dic1.values()]
years1 = list(dic1.keys())

dic2 = llenar_dict(pesca_ilegal["Año"].unique(), pesca_ilegal["Año"])
values2 = [values2[0] for values2 in dic2.values()]
years2 = list(dic2.keys())

dic3 = llenar_dict(prohibicion["Año"].unique(), prohibicion["Año"])
values3 = [values3[0] for values3 in dic3.values()]
years3 = list(dic3.keys())


dic4 = llenar_dict(periodos["Año"].unique(), periodos["Año"])
values4 = [values4[0] for values4 in dic4.values()]
years4 = list(dic4.keys())

dic5 = llenar_dict(artes_pesca["Año"].unique(), artes_pesca["Año"])
values5 = [values5[0] for values5 in dic5.values()]
years5 = list(dic5.keys())

dic6 = llenar_dict(pesca["Año"].unique(), pesca["Año"])
values6 = [values6[0] for values6 in dic6.values()]
years6 = list(dic6.keys())


leyes_annos = go.Figure(data=[go.Bar(x=years, y=values)])
leyes_auto = go.Figure(data=[go.Bar(x=years1, y=values1)])
leyes_ilegal = go.Figure(data=[go.Bar(x=years2, y=values2)])
leyes_prohi = go.Figure(data=[go.Bar(x=years3, y=values3)])
leyes_periodo = go.Figure(data=[go.Bar(x=years4, y=values4)])
leyes_arte = go.Figure(data=[go.Bar(x=years5, y=values5)])
leyes_otros = go.Figure(data=[go.Bar(x=years6, y=values6)])


# mapas
m = obtener_mapa(20.329436, -77.153311)
m1 = obtener_mapa(20.329436, -77.153311)
m2 = obtener_mapa(22.526927, -79.467644)
m3 = obtener_mapa(22.169549, -80.480796)
m4 = obtener_mapa(23.161990, -82.290785)
m5 = obtener_mapa(23.119680, -82.354357)
