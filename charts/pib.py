import pandas as pd 
import numpy as np 
import json
import plotly.express as px
import plotly.graph_objects as go



with open("./data/pib_corriente.json",'r') as jsonfile:
    pib_corriente = json.load(jsonfile)

pib_corriente_aux ={}

for i in pib_corriente:
    pepe = []
    for t,j in enumerate(pib_corriente[i]):
        if t<=20:
            if j !=0 and t!=0 :
                pepe.append(j)
        
        
    pib_corriente_aux[i] = pepe


pib_corriente_df = pd.DataFrame(pib_corriente_aux)

totales_pib = pib_corriente_df.iloc[0]

pib_corriente_df = pib_corriente_df.drop(index=0)

pib_corriente_df.index = ['Agricultura, ganadería y silvicultura ','Pesca',' Explotación de minas y canteras',' Industria azucarera',
' Industrias manufactureras (excepto Industria  azucarera)',' Suministro de electricidad, gas y agua',' Construcción',' Comercio; reparación de efectos personales',
' Hoteles y restaurantes',' Transportes, almacenamiento y comunicaciones',' Intermediación financiera',' Servicios empresariales, actividades inmobiliarias  y de alquiler',
'Administración pública, defensa; seguridad social',' Ciencia e innovación tecnológica',' Educación',' Salud pública y asistencia social',' Cultura y deporte',
' Otras act de servicios comunales, de asociaciones y personales',' Derechos de importación'
]

def pastel(leyenda,año,df):
    
    return go.Figure(data=[go.Pie(labels=leyenda,values=df[año])])