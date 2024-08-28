import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
import folium
import matplotlib.pyplot as plt
import seaborn as sns


# economico
with open("./data/exportaciones_por_mercancias.json", "r") as file:
    df = json.load(file)
index = [
    x for x in df["Unnamed: 2"] if x.lstrip() != "Cantidad" and x.lstrip() != "Valor"
]


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


exp = llenar(df)

# arreglar primera parte (productos alimenticios y animales vivos) de exportacion
toneladas = []
miles_peso = []


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
print(grupos_exp_real1)
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

pargo = px.line(
    pd.concat([peces["Pargo"], pescados_predict.T.loc["Pargo"]]),
    title="Capturas de Pargo en Toneladas",
)
pargo.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

Cherna = px.line(
    pd.concat([peces["Cherna"], pescados_predict.T.loc["Cherna"]]),
    title="Capturas de Cherna en Toneladas",
)
Cherna.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

tunidos = px.line(
    pd.concat([peces["Túnidos"], pescados_predict.T.loc["Túnidos"]]),
    title="Capturas de Túnidos en Toneladas",
)
tunidos.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

bonitos = px.line(
    pd.concat([peces["Bonito"], pescados_predict.T.loc["Bonito"]]),
    title="Capturas de Bonito en Toneladas",
)
bonitos.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

biajaiba = px.line(
    pd.concat([peces["Biajaiba"], pescados_predict.T.loc["Biajaiba"]]),
    title="Capturas de Biajaiba en Toneladas",
)
biajaiba.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

machuelo = px.line(
    pd.concat([peces["Machuelo"], pescados_predict.T.loc["Machuelo"]]),
    title="Capturas de Machuelo en Toneladas",
)
machuelo.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

rabirubia = px.line(
    pd.concat([peces["Rabirubia"], pescados_predict.T.loc["Rabirubia"]]),
    title="Capturas de Rabirubia en Toneladas",
)
rabirubia.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

raya = px.line(
    pd.concat([peces["Raya"], pescados_predict.T.loc["Raya"]]),
    title="Capturas de Raya en Toneladas",
)
raya.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

carpa = px.line(
    pd.concat([peces["Carpa"], pescados_predict.T.loc["Carpa"]]),
    title="Capturas de Carpa en Toneladas",
)
carpa.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

tenca = px.line(
    pd.concat([peces["Tenca"], pescados_predict.T.loc["Tenca"]]),
    title="Capturas de Tenca en Toneladas",
)
tenca.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

tilapia = px.line(
    pd.concat([peces["Tilapia"], pescados_predict.T.loc["Tilapia"]]),
    title="Capturas de Tilapia en Toneladas",
)
tilapia.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

claria = px.line(
    pd.concat([peces["Claria"], pescados_predict.T.loc["Claria"]]),
    title="Capturas de Claria en Toneladas",
)
claria.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

cobo = px.line(
    pd.concat([peces["Cobo"], pescados_predict.T.loc["Cobo"]]),
    title="Capturas de Cobo en Toneladas",
)
cobo.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

ostion = px.line(
    pd.concat([peces["Ostión"], pescados_predict.T.loc["Ostión"]]),
    title="Capturas de Ostión en Toneladas",
)
ostion.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

almeja = px.line(
    pd.concat([peces["Almeja"], pescados_predict.T.loc["Almeja"]]),
    title="Capturas de Almeja en Toneladas",
)
almeja.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

langosta = px.line(
    pd.concat([peces["Langosta"], pescados_predict.T.loc["Langosta"]]),
    title="Capturas de Langosta en Toneladas",
)
langosta.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

camaron_de_mar = px.line(
    pd.concat([peces["Camarón de Mar"], pescados_predict.T.loc["Camarón de Mar"]]),
    title="Capturas de Camarón de Mar en Toneladas",
)
camaron_de_mar.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

camaronicultura = px.line(
    pd.concat([peces["Camaronicultura"], pescados_predict.T.loc["Camaronicultura"]]),
    title="Capturas de Camaronicultura en Toneladas",
)
camaronicultura.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)

moralla = px.line(
    pd.concat([peces["Moralla"], pescados_predict.T.loc["Moralla"]]),
    title="Capturas de Moralla en Toneladas",
)
moralla.update_layout(
    showlegend=False, xaxis_title="años", yaxis_title="captura en toneladas(T)"
)


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
            )
        ]
    )
    fig.update_layout(title=f"{prov_real}")
    return fig


p1 = px.bar(mypimesdf.T["Artemisa"])
p1.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p2 = px.bar(mypimesdf.T["La Habana"])
p2.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p3 = px.bar(mypimesdf.T["Mayabeque"])
p3.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p4 = px.bar(mypimesdf.T["Matanzas"])
p4.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p5 = px.bar(mypimesdf.T["Villa Clara"])
p5.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p6 = px.bar(mypimesdf.T["Cienfuegos"])
p6.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p7 = px.bar(mypimesdf.T["Santi Spiritus"])
p7.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p8 = px.bar(mypimesdf.T["Ciego de Ávila"])
p8.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p9 = px.bar(mypimesdf.T["Camagüey"])
p9.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p10 = px.bar(mypimesdf.T["Las Tunas"])
p10.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p11 = px.bar(mypimesdf.T["Holguín"])
p11.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p12 = px.bar(mypimesdf.T["Granma"])
p12.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p13 = px.bar(mypimesdf.T["Santiago de Cuba"])
p13.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p14 = px.bar(mypimesdf.T["Guantánamo"])
p14.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p15 = px.bar(mypimesdf.T["La Isla de la Juventud"])
p15.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

p16 = px.bar(mypimesdf.T["Pinar del Rio"])
p16.update_layout(xaxis_title="Empresas", yaxis_title="Cantidad")

mypimesdf_bar = px.bar(np.sum(mypimesdf), title="total de mypimes en Cuba")


def graficar_mypimes_total_pastel():

    sum_pesca_pyme = np.sum(mypimesdf["Agricultura,Pesca,Ganaderia y Silvicultura"])
    total_pymes = sum(np.sum(mypimesdf)) - sum_pesca_pyme
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Agricultura,Pesca,Ganaderia y Silvicultura", "total"],
                values=[sum_pesca_pyme, total_pymes],
            )
        ]
    )
    fig.update_layout(title="Porciento de mypimes de Pesca vs el total")

    return fig


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
m = folium.Map(location=[20.329436, -77.153311])
m.add_child(folium.Marker(location=[20.329436, -77.153311]))


m1 = folium.Map(location=[20.329436, -77.153311])
m1.add_child(folium.Marker(location=[20.329436, -77.153311]))


m2 = folium.Map(location=[22.526927, -79.467644])
m2.add_child(folium.Marker(location=[22.526927, -79.467644]))

m3 = folium.Map(location=[22.169549, -80.480796])
m3.add_child(folium.Marker(location=[22.169549, -80.480796]))


m4 = folium.Map(location=[23.161990, -82.290785])
m4.add_child(folium.Marker(location=[23.161990, -82.290785]))


m5 = folium.Map(location=[23.119680, -82.354357])
m5.add_child(folium.Marker(location=[23.119680, -82.354357]))
