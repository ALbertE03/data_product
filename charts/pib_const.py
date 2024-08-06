import pandas as pd 
import numpy as np 
import json
import plotly.express as px
import plotly.graph_objects as go


with open ("./data/pib_const.json",'r') as file:
    pib_const = json.load(file)

pib_const_aux={}
annos = [x for x in range(2005,2023)]
for t,i in enumerate(pib_const):
    p=[]
    for r,j in enumerate(pib_const[i]):
        if r !=0 and r!=1:
            p.append(j)
    pib_const_aux[annos[t]]=p  

pib_const_aux_df =pd.DataFrame(pib_const_aux)
pib_const_aux_df.index=['Agricultura, ganadería y silvicultura ','Pesca',' Explotación de minas y canteras',' Industria azucarera',
' Industrias manufactureras (excepto Industria  azucarera)',' Suministro de electricidad, gas y agua',' Construcción',' Comercio; reparación de efectos personales',
' Hoteles y restaurantes',' Transportes, almacenamiento y comunicaciones',' Intermediación financiera',' Servicios empresariales, actividades inmobiliarias  y de alquiler',
'Administración pública, defensa; seguridad social',' Ciencia e innovación tecnológica',' Educación',' Salud pública y asistencia social',' Cultura y deporte',
' Otras act de servicios comunales, de asociaciones y personales',' Derechos de importación'
]

pesca_pib_const = pib_const_aux_df.loc['Pesca']

print(pesca_pib_const)
fig = px.line(pesca_pib_const.T,title="Evolución del pib de la pesca a precios constantes")
