import json
import pandas as pd


with open('./data/barcos.json','r') as p:
    barcos = json.load(p)

barcos_df = pd.DataFrame(barcos)

for i in barcos_df['products']:
    for j in i:
        print(j['localizationName'])
        
    