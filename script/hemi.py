import requests
import pandas as pd 
import json


a=[]
for x in range(1,71):
  
    url = f"https://www.clickandboat.com/api/v6/products?page={x}&distance=300&latitude=39.513946&longitude=1.401413&types%5B%5D=Sailboat&types%5B%5D=Catamaran&types%5B%5D=Gulet&types%5B%5D=Sail%20Yacht&types%5B%5D=Motorboat&types%5B%5D=RIB&types%5B%5D=Jet%20Ski&types%5B%5D=Houseboat&types%5B%5D=Without%20license&types%5B%5D=Motor%20Yacht&abVariations%5BrankingAlgo%5D=A&_locale=es"

    payload = {}
    headers = {
    'Cookie': 'vulid=1CEBmx7mmomgBZBwuU3dfn.3268cfff503cf7e7308764634cfc332d8271f51dd849f7e0965ce67e29f71b38'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    a.append(response.json())

with open ('barcos.json','w') as file:
    json.dump(a,file,indent=4)


with open ('barcos.json','r') as barcos:
    data =  json.load(barcos)


df= pd.DataFrame(data)
print(df)
    
            

