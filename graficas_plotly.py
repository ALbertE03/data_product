import pandas as pd
import plotly.express as px
import json

df = pd.read_json("./data/exportaciones.json")
df.index = [x for x in range(1998, 2023)]
df.columns = [x for x in range(1, 83)]
data = pd.DataFrame(
    {
        "animales vivos": df[3],
        "productos lácteos": df[4],
        "moluscos y crustáceos": df[5],
        "mariscos congelados": df[7],
        "mariscos en conserva": df[9],
        "legumbres y frutas": df[10],
        "citrícos": df[12],
        "azúcares": df[15],
        "miel natural": df[18],
        "cafe, té, cacao": df[19],
        "manteca": df[21],
        "bebidas alcholicas": df[26],
        "tabaco": df[27],
    }
)
exportaciones = px.line(data, title="exportaciones de productos en millones de pesos")
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
fish = px.line(peces, title="capturas de peces en toneladas")
pargo = px.line(peces["Pargo"], title="Capturas de Pargo en Toneladas")
Cherna = px.line(peces["Cherna"], title="Capturas de Cherna en Toneladas")
tunidos = px.line(peces["Túnidos"], title="Capturas de Túnidos en Toneladas")
bonitos = px.line(peces["Bonito"], title="Capturas de Bonito en Toneladas")
biajaiba = px.line(peces["Biajaiba"], title="Capturas de Biajaiba en Toneladas")
machuelo = px.line(peces["Machuelo"], title="Capturas de Machuelo en Toneladas")
rabirubia = px.line(peces["Rabirubia"], title="Capturas de Rabirubia en Toneladas")
raya = px.line(peces["Raya"], title="Capturas de Raya en Toneladas")
carpa = px.line(peces["Carpa"], title="Capturas de Carpa en Toneladas")
tenca = px.line(peces["Tenca"], title="Capturas de Tenca en Toneladas")
tilapia = px.line(peces["Tilapia"], title="Capturas de Tilapia en Toneladas")
claria = px.line(peces["Claria"], title="Capturas de Claria en Toneladas")
cobo = px.line(peces["Cobo"], title="Capturas de Cobo en Toneladas")
ostion = px.line(peces["Ostión"], title="Capturas de Ostión en Toneladas")
almeja = px.line(peces["Almeja"], title="Capturas de Almeja en Toneladas")
langosta = px.line(peces["Langosta"], title="Capturas de Langosta en Toneladas")
camaron_de_mar = px.line(
    peces["Camarón de Mar"], title="Capturas de Camarón de Mar en Toneladas"
)
camaronicultura = px.line(
    peces["Camaronicultura"], title="Capturas de Camaronicultura en Toneladas"
)
moralla = px.line(peces["Moralla"], title="Capturas de Moralla en Toneladas")
