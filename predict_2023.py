from charts.graficas_plotly import miles_peso_, grupos_exp_real, peces
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
from charts.graficas_plotly import toneladas_, toneladas_impo_
import csv

#### usarlo en un jupyter notebook y separarlos en celdas.
##############################################################
# predecir el precio en millones de pesos del pescado en exportaciones (total)
##############################################################

años = np.array([x for x in range(1998, 2023)]).reshape(-1, 1)
sumap1 = miles_peso_.T.loc["Pescado y marisco fresco y congelado"]
sumap2 = miles_peso_.T.loc["Pescado y marisco en conserva"]
valores = np.array(sumap1 + sumap2)

degree = 3
poly_feature = PolynomialFeatures(degree=degree, include_bias=False)

x_poly = poly_feature.fit_transform(años)

model = LinearRegression()
model.fit(x_poly, valores)


y = model.predict(x_poly)
r2 = r2_score(valores, y)
print(f"r2_score: {r2:.2f}")

pre = np.array([[2023]])
x_future = poly_feature.transform(pre)
predict = model.predict(x_future)

aaa = list(y) + list(predict)
plt.scatter(años, valores)
plt.plot([x for x in range(1998, 2024)], aaa)
plt.show()

##############################################################
# predicción de grupos de exportaciones
##############################################################
##############################################################
# predecir exportació de Productos de Pesca
##############################################################

productos_pesca = np.array(grupos_exp_real.loc["Productos de la Pesca"])
annos = np.array([x for x in range(1989, 2023)]).reshape(-1, 1)

degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(annos)

modelo = LinearRegression()

modelo.fit(poly_x, productos_pesca)

p = modelo.predict(poly_x)
r2 = r2_score(productos_pesca, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict1 = modelo.predict(x_future1)
print(predict1)

aaa = list(p) + list(predict1)
plt.plot(annos, productos_pesca, ".")
plt.plot([x for x in range(1989, 2024)], aaa)
plt.show()


##############################################################
# predecir productos agropecuarios
##############################################################

productos_agropecuarios = np.array(grupos_exp_real.loc["Productos agropecuarios"])
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(annos)

modelo2 = LinearRegression()

modelo2.fit(poly_x, productos_agropecuarios)

p = modelo2.predict(poly_x)
r2 = r2_score(productos_agropecuarios, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict2 = modelo2.predict(x_future1)
print(predict2)
aaa = list(p) + list(predict2)
plt.plot(annos, productos_agropecuarios, ".")
plt.plot([x for x in range(1989, 2024)], aaa)
plt.show()

##############################################################
# predecir productos de la industria azucarera
##############################################################

productos_azucar = np.array(grupos_exp_real.loc["Productos de la industria azucarera"])
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(annos)

modelo3 = LinearRegression()

modelo3.fit(poly_x, productos_azucar)

p = modelo3.predict(poly_x)
r2 = r2_score(productos_azucar, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict3 = modelo3.predict(x_future1)
print(predict3)
aaa = list(p) + list(predict3)
plt.plot(annos, productos_azucar, ".")
plt.plot([x for x in range(1989, 2024)], aaa)
plt.show()


##############################################################
# predecir productos de la mineria
##############################################################
productos_mineria = np.array(grupos_exp_real.loc["Productos de la minería"])
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(annos)

modelo4 = LinearRegression()

modelo4.fit(poly_x, productos_mineria)

p = modelo4.predict(poly_x)
r2 = r2_score(productos_mineria, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict4 = modelo4.predict(x_future1)
print(predict4)
aaa = list(p) + list(predict4)
plt.plot(annos, productos_mineria, ".")
plt.plot([x for x in range(1989, 2024)], aaa)
plt.show()


##############################################################
# predecir productos del tabaco
##############################################################

productos_tabaco = np.array(grupos_exp_real.loc["Productos de la industria del tabaco"])
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(annos)

modelo5 = LinearRegression()

modelo5.fit(poly_x, productos_tabaco)

p = modelo5.predict(poly_x)
r2 = r2_score(productos_tabaco, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict5 = modelo5.predict(x_future1)
print(predict5)
aaa = list(p) + list(predict5)
plt.plot(annos, productos_tabaco, ".")
plt.plot([x for x in range(1989, 2024)], aaa)
plt.show()

r = list(predict1) + list(predict2) + list(predict3) + list(predict4) + list(predict5)
agrego = np.array(r).reshape(-1, 1)

actual = {
    "Productos de Pesca": agrego[0],
    "Productos agropecuarios": agrego[1],
    "Productos de la industria azucarera": agrego[2],
    "Productos de la mineria": agrego[3],
    "Productos del tabaco": agrego[4],
}
actual_df = pd.DataFrame(actual)


# peces
##############################################################
# predecir pargos
##############################################################
pargo = np.array(peces["Pargo"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 1
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo6 = LinearRegression()

modelo6.fit(poly_x, pargo)

p = modelo6.predict(poly_x)
r2 = r2_score(pargo, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict6 = modelo6.predict(x_future1)
print(predict6)
aaa = list(p) + list(predict6)
plt.plot(años_peces, pargo, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir cherna
##############################################################

cherna = np.array(peces["Cherna"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo7 = LinearRegression()

modelo7.fit(poly_x, cherna)

p = modelo7.predict(poly_x)
r2 = r2_score(cherna, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict7 = modelo7.predict(x_future1)
print(predict7)
aaa = list(p) + list(predict7)
plt.plot(años_peces, cherna, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir tunidos
##############################################################

tunidos = np.array(peces["Túnidos"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 5
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo8 = LinearRegression()

modelo8.fit(poly_x, tunidos)

p = modelo8.predict(poly_x)
r2 = r2_score(tunidos, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict8 = modelo8.predict(x_future1)
print(predict8)
aaa = list(p) + list(predict8)
plt.plot(años_peces, tunidos, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Bonito
##############################################################

Bonito = np.array(peces["Bonito"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo9 = LinearRegression()

modelo9.fit(poly_x, Bonito)

p = modelo9.predict(poly_x)
r2 = r2_score(Bonito, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict9 = modelo9.predict(x_future1)
print(predict9)
aaa = list(p) + list(predict9)
plt.plot(años_peces, Bonito, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Biajaiba
##############################################################

Biajaiba = np.array(peces["Biajaiba"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo10 = LinearRegression()

modelo10.fit(poly_x, Biajaiba)

p = modelo10.predict(poly_x)
r2 = r2_score(Biajaiba, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict10 = modelo10.predict(x_future1)

print(predict10)
aaa = list(p) + list(predict10)
plt.plot(años_peces, Biajaiba, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Machuelo
##############################################################

Machuelo = np.array(peces["Machuelo"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 4
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo11 = LinearRegression()

modelo11.fit(poly_x, Machuelo)

p = modelo11.predict(poly_x)
r2 = r2_score(Machuelo, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict11 = modelo11.predict(x_future1)

print(predict11)
aaa = list(p) + list(predict11)
plt.plot(años_peces, Machuelo, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Rabirubia
##############################################################

Rabirubia = np.array(peces["Rabirubia"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 1
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo12 = LinearRegression()

modelo12.fit(poly_x, Rabirubia)

p = modelo12.predict(poly_x)
r2 = r2_score(Rabirubia, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict12 = modelo12.predict(x_future1)

print(predict12)
aaa = list(p) + list(predict12)
plt.plot(años_peces, Rabirubia, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Raya
##############################################################

Raya = np.array(peces["Raya"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo13 = LinearRegression()

modelo13.fit(poly_x, Raya)

p = modelo13.predict(poly_x)
r2 = r2_score(Raya, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict13 = modelo13.predict(x_future1)

print(predict13)
aaa = list(p) + list(predict13)
plt.plot(años_peces, Raya, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()


##############################################################
# predecir Carpa
##############################################################

Carpa = np.array(peces["Carpa"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo14 = LinearRegression()

modelo14.fit(poly_x, Carpa)

p = modelo14.predict(poly_x)
r2 = r2_score(Carpa, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict14 = modelo14.predict(x_future1)

print(predict14)
aaa = list(p) + list(predict14)
plt.plot(años_peces, Carpa, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Tenca
##############################################################

Tenca = np.array(peces["Tenca"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo15 = LinearRegression()

modelo15.fit(poly_x, Tenca)

p = modelo15.predict(poly_x)
r2 = r2_score(Tenca, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict15 = modelo15.predict(x_future1)

print(predict15)
aaa = list(p) + list(predict15)
plt.plot(años_peces, Tenca, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Tilapia
##############################################################

Tilapia = np.array(peces["Tilapia"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo16 = LinearRegression()

modelo16.fit(poly_x, Tilapia)

p = modelo16.predict(poly_x)
r2 = r2_score(Tilapia, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict16 = modelo16.predict(x_future1)

print(predict16)
aaa = list(p) + list(predict16)
plt.plot(años_peces, Tilapia, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Claria
##############################################################

Claria = np.array(peces["Claria"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo17 = LinearRegression()

modelo17.fit(poly_x, Claria)

p = modelo17.predict(poly_x)
r2 = r2_score(Claria, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict17 = modelo17.predict(x_future1)

print(predict17)
aaa = list(p) + list(predict17)
plt.plot(años_peces, Claria, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Cobo
##############################################################

Cobo = np.array(peces["Cobo"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 1
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo18 = LinearRegression()

modelo18.fit(poly_x, Cobo)

p = modelo18.predict(poly_x)
r2 = r2_score(Cobo, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict18 = modelo18.predict(x_future1)

print(predict18)
aaa = list(p) + list(predict18)
plt.plot(años_peces, Cobo, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Ostión
##############################################################

Ostión = np.array(peces["Ostión"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo19 = LinearRegression()

modelo19.fit(poly_x, Ostión)

p = modelo19.predict(poly_x)
r2 = r2_score(Ostión, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict19 = modelo19.predict(x_future1)

print(predict19)
aaa = list(p) + list(predict19)
plt.plot(años_peces, Ostión, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Almeja
##############################################################

Almeja = np.array(peces["Almeja"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo20 = LinearRegression()

modelo20.fit(poly_x, Almeja)

p = modelo20.predict(poly_x)
r2 = r2_score(Almeja, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict20 = modelo20.predict(x_future1)

print(predict20)
aaa = list(p) + list(predict20)
plt.plot(años_peces, Almeja, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Langosta
##############################################################

Langosta = np.array(peces["Langosta"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo21 = LinearRegression()

modelo21.fit(poly_x, Langosta)

p = modelo21.predict(poly_x)
r2 = r2_score(Langosta, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict21 = modelo21.predict(x_future1)

print(predict21)
aaa = list(p) + list(predict21)
plt.plot(años_peces, Langosta, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Camarón de Mar
##############################################################

Camarón = np.array(peces["Camarón de Mar"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 4
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo22 = LinearRegression()

modelo22.fit(poly_x, Camarón)

p = modelo22.predict(poly_x)
r2 = r2_score(Camarón, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict22 = modelo22.predict(x_future1)

print(predict22)
aaa = list(p) + list(predict22)
plt.plot(años_peces, Camarón, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Camaronicultura
##############################################################

Camaronicultura = np.array(peces["Camaronicultura"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 3
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo23 = LinearRegression()

modelo23.fit(poly_x, Camaronicultura)

p = modelo23.predict(poly_x)
r2 = r2_score(Camaronicultura, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict23 = modelo23.predict(x_future1)

print(predict23)
aaa = list(p) + list(predict23)
plt.plot(años_peces, Camaronicultura, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

##############################################################
# predecir Moralla
##############################################################

Moralla = np.array(peces["Moralla"])
años_peces = np.array([x for x in range(2001, 2023)]).reshape(-1, 1)
degree = 2
poly = PolynomialFeatures(degree=degree, include_bias=False)
poly_x = poly.fit_transform(años_peces)

modelo24 = LinearRegression()

modelo24.fit(poly_x, Moralla)

p = modelo24.predict(poly_x)
r2 = r2_score(Moralla, p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future1 = poly.transform(pre1)
predict24 = modelo24.predict(x_future1)

print(predict24)
aaa = list(p) + list(predict24)
plt.plot(años_peces, Moralla, ".")
plt.plot([x for x in range(2001, 2024)], aaa)
plt.show()

#####################################################
# Exportaciones
#################################################3####
años25 = np.array([x for x in range(1998, 2023)]).reshape(-1, 1)

degree = 4
poly = PolynomialFeatures(degree=degree)
poly_x = poly.fit_transform(años25)

modelo25 = LinearRegression()
modelo25.fit(poly_x, toneladas_.T["Pescado y marisco fresco y congelado"])

p = modelo25.predict(poly_x)
r2 = r2_score(toneladas_.T["Pescado y marisco fresco y congelado"], p)
print(f"r2_score: {r2:.2f}")

pre = np.array([[2023]])
x_future25 = poly.transform(pre1)
predict25 = modelo25.predict(x_future25)
print(predict25)
aaa25 = list(p) + list(predict25)
plt.plot(años, toneladas_.T["Pescado y marisco fresco y congelado"], ".")
plt.plot([x for x in range(1998, 2024)], aaa25)
plt.show()


años26 = np.array([x for x in range(1998, 2023)]).reshape(-1, 1)
degree = 5
poly = PolynomialFeatures(degree=degree)
poly_x = poly.fit_transform(años26)

modelo26 = LinearRegression()
modelo26.fit(poly_x, toneladas_.T["Pescado y marisco en conserva"])

p = modelo26.predict(poly_x)
r2 = r2_score(toneladas_.T["Pescado y marisco en conserva"], p)
print(f"r2_score: {r2:.2f}")

pre1 = np.array([[2023]])
x_future26 = poly.transform(pre1)
predict26 = modelo26.predict(x_future26)
print(predict26)
aaa26 = list(p) + list(predict26)
plt.plot(años, toneladas_.T["Pescado y marisco en conserva"], ".")
plt.plot([x for x in range(1998, 2024)], aaa26)


exporta_predict = {
    "Pescado y marisco fresco y congelado": predict25,
    "Pescado y marisco en conserva": predict26,
}

exporta_predict


###########################################################
# Importaciones
###########################################################
años25 = np.array([x for x in range(1998, 2023)]).reshape(-1, 1)

degree = 4
poly = PolynomialFeatures(degree=degree)
poly_x = poly.fit_transform(años25)

modelo25 = LinearRegression()
modelo25.fit(poly_x, toneladas_impo_.T["Pescado y marisco fresco y congelado"])

p = modelo25.predict(poly_x)
r2 = r2_score(toneladas_impo_.T["Pescado y marisco fresco y congelado"], p)
print(f"r2_score: {r2:.2f}")

pre = np.array([[2023]])
x_future25 = poly.transform(pre1)
predict27 = modelo25.predict(x_future25)
print(predict27)
aaa25 = list(p) + list(predict27)
plt.plot(años, toneladas_impo_.T["Pescado y marisco fresco y congelado"], ".")
plt.plot([x for x in range(1998, 2024)], aaa25)
plt.show()


años25 = np.array([x for x in range(1998, 2023)]).reshape(-1, 1)

degree = 4
poly = PolynomialFeatures(degree=degree)
poly_x = poly.fit_transform(años25)

modelo25 = LinearRegression()
modelo25.fit(poly_x, toneladas_impo_.T["Otros pescados, preparados o en conserva"])

p = modelo25.predict(poly_x)
r2 = r2_score(toneladas_impo_.T["Otros pescados, preparados o en conserva"], p)
print(f"r2_score: {r2:.2f}")

pre = np.array([[2023]])
x_future25 = poly.transform(pre1)
predict28 = modelo25.predict(x_future25)
print(predict28)
aaa25 = list(p) + list(predict28)
plt.plot(años, toneladas_impo_.T["Otros pescados, preparados o en conserva"], ".")
plt.plot([x for x in range(1998, 2024)], aaa25)
plt.show()


importa_predict = {
    "Pescado y marisco fresco y congelado": predict27,
    "Pescado y marisco en conserva": predict28,
}

importa_predict


with open("data/exporta_predict.csv", "w", newline="", encoding="utf-8") as archivo:
    fieldname = list(exporta_predict.keys())
    writer = csv.DictWriter(archivo, fieldnames=fieldname)
    writer.writeheader()

    writer.writerow(exporta_predict)
    archivo.close()

with open("data/importa_predict.csv", "w", newline="", encoding="utf-8") as archivo1:
    fieldname = list(importa_predict.keys())
    writer = csv.DictWriter(archivo1, fieldnames=fieldname)
    writer.writeheader()

    writer.writerow(importa_predict)
    archivo.close()
