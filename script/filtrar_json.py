import pandas as pd
import json

df = pd.read_excel(
    "/Users/enrique.marichal/Desktop/Pesca_en-Cuba/src/data/5.4-pib-aprecios-constantes.xls"
)

df.to_json("pib_const.json", indent=4)


df1 = pd.read_json("pib_const.json")

años = [x for x in range(2010, 2023)]

t = 0
a = {}
try:
    for i in df1:

        b = []
        for j in df1[i]:

            if not pd.isnull(j) and not isinstance(j, str):

                b.append(j)

        # a[años[t]]=b
        a[f"{i}"] = b
        t += 1
except:
    print("hola")

with open("pib_const_sin_nulo.json", "w") as file:
    json.dump(a, file, indent=4)
