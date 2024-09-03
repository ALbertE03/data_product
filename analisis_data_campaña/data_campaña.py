import pandas as pd
import numpy
import matplotlib.pyplot as plt


Audience_overview = pd.read_csv(
    "./data_campaña/Audience_overview_-_alberte03.github.io.csv"
)

Device_software = pd.read_csv(
    "./data_campaña/Devices__software_-_alberte03.github.io-2.csv"
)
Device_software_ = pd.read_csv(
    "./data_campaña/Devices__software_-_alberte03.github.io.csv"
)
Engagement = pd.read_csv("./data_campaña/Engagement_-_alberte03.github.io-2.csv")
Engagement_ = pd.read_csv("./data_campaña/Engagement_-_alberte03.github.io.csv")
locations = pd.read_csv("./data_campaña/Locations_-_alberte03.github.io-2.csv")
locations_ = pd.read_csv("./data_campaña/Locations_-_alberte03.github.io.csv")
session_log = pd.read_csv("./data_campaña/Session_log_-_alberte03.github.io.csv")


def obtener_dia(fecha):
    return fecha.split("-")[-1]


dias_llenos = []
for i in Audience_overview["Date (group by day) "]:
    aux = obtener_dia(i)
    if aux[0] == "0":
        dias_llenos.append(int(aux[1]))
        continue
    dias_llenos.append(int(aux))


dias = [x for x in range(1, 32)]
dias_llenos[-1] = 31
visitantes = Audience_overview["Visitors"]
junto = []
for i, j in enumerate(dias_llenos):
    junto.append((j, visitantes[i]))


def buscar_index(lista, num):
    c = 0
    for i in lista:
        if i == num:
            return c
        c += 1
    return -1


total = []
for i in dias:
    if i in [x[0] for x in junto]:
        index = buscar_index([x[0] for x in junto], i)
        total.append((i, junto[index][1]))
        continue
    total.append((i, 0))


returning = Audience_overview["% of returning visitors"]


def porciento_(porciento, todo):
    for i in range(1, todo + 1):

        if (i / todo) == porciento:
            return i
    return -1


porciento = []
for i, j in enumerate(visitantes):
    if returning[i] == 0.0:
        continue

    t = porciento_(returning[i], j)

    porciento.append(t)


porciento[4] = 1 if porciento[4] == -1 else porciento[4]


fig = plt.subplots(figsize=(10, 5))
plt.plot([x[0] for x in total], [x[1] for x in total])
plt.ylabel("cantidad de visitantes")
plt.xlabel("Dias")
plt.title("1 de agosto a 1 de septiembre")
plt.grid(which="major")
plt.xticks([x[0] for x in total])
plt.show()

print(sum([x[1] for x in total]) - sum(porciento))
