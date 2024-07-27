import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
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

#peces
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



with open('data/mypimes.json','r')as f:
    mypimes=json.load(f)

mypimesdf= pd.DataFrame(mypimes)
mypimesdf.columns=['alojamiento de servicios de comida','Agricultura,Pesca,Ganaderia y Silvicultura','Comercio','Industrias manufactureras','información y comunicaciones','Transporte y Almacenamiento','Construcción','Resto de Actividades']

mypimesdf=mypimesdf.drop([0])
mypimesdf.index=['Pinar del Rio',"Artemisa","La Habana","Mayabeque","Matanzas","Villa Clara","Cienfuegos","Santi Spiritus","Ciego de Ávila","Camagüey","Las Tunas","Holguín","Granma","Santiago de Cuba","Guantánamo","La Isla de la Juventud"]


p=px.bar(mypimesdf.T['Pinar del Rio'])
p1=px.bar(mypimesdf.T['Artemisa'])
p2=px.bar(mypimesdf.T['La Habana'])
p3=px.bar(mypimesdf.T['Mayabeque'])
p4=px.bar(mypimesdf.T['Matanzas'])
p5=px.bar(mypimesdf.T['Villa Clara'])
p6=px.bar(mypimesdf.T['Cienfuegos'])
p7=px.bar(mypimesdf.T['Santi Spiritus'])
p8=px.bar(mypimesdf.T['Ciego de Ávila'])
p9=px.bar(mypimesdf.T['Camagüey'])
p10=px.bar(mypimesdf.T['Las Tunas'])
p11=px.bar(mypimesdf.T['Granma'])
p12=px.bar(mypimesdf.T['Santiago de Cuba'])
p13=px.bar(mypimesdf.T['Guantánamo'])
p14=px.bar(mypimesdf.T['La Isla de la Juventud'])


#leyes
artes_pesca = pd.read_csv('data/artes_de_pesca.csv')
autorizacion = pd.read_csv('data/autorizacion.csv')
pesca_ilegal = pd.read_csv('data/pesca_ilegal.csv')
periodos = pd.read_csv('data/periodo_de_pesca.csv')
prohibicion  = pd.read_csv('data/prohibicion_de_pesca.csv')
pesca = pd.read_csv("data/pesca.csv")

merge = pd.concat([artes_pesca,autorizacion,pesca,pesca_ilegal,prohibicion,periodos])

a=merge['Año'].unique()
def contar(df,target):
    cont = 0 
    for i in df:
        if  i == target:
            cont+=1
    return [cont]
    
def llenar_dict(df,aux):
    dic={}
    for i in df:
        dic[f'{i}'] = contar(aux,i)
    return dic

    
dic= llenar_dict(a,merge['Año'])
years = list(dic.keys())
values = [value[0] for value in dic.values()]

dic1= llenar_dict(autorizacion['Año'].unique(),autorizacion['Año'])
values1 = [value1[0] for value1 in  dic1.values()]
years1 = list(dic1.keys())

dic2 = llenar_dict(pesca_ilegal['Año'].unique(),pesca_ilegal['Año'])
values2 = [values2[0] for values2 in dic2.values()]
years2 = list(dic2.keys())

dic3 = llenar_dict(prohibicion['Año'].unique(),prohibicion['Año'])
values3 = [values3[0] for values3 in dic3.values()]
years3 = list(dic3.keys())


dic4 = llenar_dict(periodos['Año'].unique(),periodos['Año'])
values4 = [values4[0] for values4 in dic4.values()]
years4 = list(dic4.keys())

dic5 = llenar_dict(artes_pesca['Año'].unique(),artes_pesca['Año'])
values5 = [values5[0] for values5 in dic5.values()]
years5 = list(dic5.keys())

dic6 = llenar_dict(pesca['Año'].unique(),pesca['Año'])
values6 = [values6[0] for values6 in dic6.values()]
years6 = list(dic6.keys())


leyes_annos = go.Figure(data=[go.Bar(x=years, y=values)])
leyes_auto = go.Figure(data = [go.Bar(x=years1, y = values1)])
leyes_ilegal = go.Figure(data = [go.Bar(x= years2, y= values2)])
leyes_prohi = go.Figure(data = [go.Bar(x= years3, y= values3)])
leyes_periodo = go.Figure(data = [go.Bar(x= years4, y= values4)])
leyes_arte = go.Figure(data = [go.Bar(x= years5, y= values5)])
leyes_otros = go.Figure(data = [go.Bar(x= years6, y= values6)])


#mapas

fig = go.Figure(go.Scattermapbox(lat=[20.329436],lon=[-77.153311],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EpiGram']))
fig.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=20.329436,lon=-77.153311),zoom=13))
pio.write_html(fig,file="mapa.html")

fig1 = go.Figure(go.Scattermapbox(lat=[20.329436],lon=[-77.153311],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['PescaGram']))
fig1.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=20.329436,lon=-77.153311),zoom=13))
pio.write_html(fig1,file="mapa1.html")

fig2 = go.Figure(go.Scattermapbox(lat=[22.526927],lon=[-79.467644],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EPICAI']))
fig2.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=22.526927,lon=-79.467644),zoom=13))
pio.write_html(fig2,file="mapa2.html")

fig3 = go.Figure(go.Scattermapbox(lat=[22.169549],lon=[-80.480796],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['EPICIEN']))
fig3.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=22.169549,lon=-80.480796),zoom=13))
pio.write_html(fig3,file="mapa3.html")

fig4 = go.Figure(go.Scattermapbox(lat=[23.161990],lon=[-82.290785],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['Pesca Caribe']))
fig4.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=23.161990,lon=-82.290785),zoom=13))
pio.write_html(fig4,file="mapa4.html")

fig5 = go.Figure(go.Scattermapbox(lat=[23.119680],lon=[-82.354357],mode='markers',marker=go.scattermapbox.Marker(size=14),text=['GEIP']))
fig5.update_layout(mapbox_style='open-street-map',mapbox=dict(center=go.layout.mapbox.Center(lat=23.119680,lon=-82.354357),zoom=13))
pio.write_html(fig5,file="mapa5.html")