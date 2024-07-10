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

"""pib = pd.read_json("./data/pib_const.json")
pib = pib.drop([0]).drop([1])
pib.columns = [x for x in range(1996, 2023)]
pib.index = [
    "Agricultura, ganadería y silvicultura ",
    " Pesca",
    " Explotación de minas y canteras",
    " Industria azucarera",
    "Industrias manufactureras (excepto Industria  azucarera)",
    " Suministro de electricidad, gas y agua",
    " Construcción",
    " Comercio; reparación de efectos personales",
    " Hoteles y restaurantes",
    "Transportes, almacenamiento y comunicaciones",
    " Intermediación financiera",
    " Servicios empresariales, actividades inmobiliarias  y de alquiler",
    " Administración pública, defensa; seguridad social",
    " Ciencia e innovación tecnológica",
    " Educación",
    " Salud pública y asistencia social",
    " Cultura y deporte",
    "Otras actividades de servicios comunales, de asociaciones y personales",
    " Derechos de importación",
]
print(pib.head(5))"""
