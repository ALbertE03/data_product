import pandas as pd 
import numpy as np 
import json
import plotly.express as px
import plotly.graph_objects as go


with open ("./data/pib_const.json",'r') as file:
    pib_const = json.load(file)

pib_const_aux = {}
totales_pib1 = []
annos = [x for x in range(2005,2023)]
for t,i in enumerate(pib_const):
    p = []
    for r,j in enumerate(pib_const[i]):
        if r == 1:
            totales_pib1.append(j)
        if r != 0 and r!= 1:
            p.append(j)
    pib_const_aux[annos[t]] = p  
print(totales_pib1)
pib_const_aux_df = pd.DataFrame(pib_const_aux)
pib_const_aux_df.index = ['Agricultura, ganadería y silvicultura ','Pesca',' Explotación de minas y canteras',' Industria azucarera',
' Industrias manufactureras (excepto Industria  azucarera)',' Suministro de electricidad, gas y agua',' Construcción',' Comercio; reparación de efectos personales',
' Hoteles y restaurantes',' Transportes, almacenamiento y comunicaciones',' Intermediación financiera',' Servicios empresariales, actividades inmobiliarias  y de alquiler',
'Administración pública, defensa; seguridad social',' Ciencia e innovación tecnológica',' Educación',' Salud pública y asistencia social',' Cultura y deporte',
' Otras act de servicios comunales, de asociaciones y personales',' Derechos de importación'
]

pesca_pib_const = pib_const_aux_df.loc['Pesca']

fig = px.line(pesca_pib_const.T,title = "Evolución del pib de la pesca a precios constantes")
fig.update_layout(yaxis_title = "millones de pesos",xaxis_title = 'años')


def auto1(año,df):
    
    fig = go.Figure(data = [go.Bar(x = list(df.index),y = df[año],text = df[año],textposition = 'auto',marker_color = 'skyblue')])
    fig.add_hline(y = sum(df[año]) / len(df[año]),line_dash = 'dash',line_color = 'red', annotation_text = "media")
    fig.update_layout(title = f"PIB a precios constantes: {año}", yaxis_title = 'Millones de pesos')
    return fig,sum(df[año]) / len(df[año])

def contar_año(año):
    contador = 0
    for i in [x for x in range(2005,2023)]:
        if i == año:
            return contador
        contador += 1
    
def pastel1(año):
    pesca = pib_const_aux_df[año].iloc[1]
    co = contar_año(año)
    total = totales_pib1[co] - pesca
    fig = go.Figure(data = [go.Pie(labels = ['total','pesca'],values = [total,pesca])])
    fig.update_layout(title = f'Porciento del pib de año: {año}')
    return fig
