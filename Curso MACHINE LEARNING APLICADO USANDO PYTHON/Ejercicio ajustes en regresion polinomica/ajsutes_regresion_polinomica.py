'''
1. cargar datos para x e y
2. entrenar un modelo de regresion lineal simple
3. graficar

'''

import numpy as np
import pandas as pd
import random

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Carga de datos
X = np.array([258.0,270.0,294.0,320.0,342.0,368.0,396.0,446.0,480.0,586.0,700.0])
y = np.array([236.4,234.4,252.8,298.6,314.2,342.2,360.8,368.0,391.2,390.8,450.0])

#nube de puntos de los datos
plt.scatter(X,y)
plt.xlabel("Datos de X")
plt.ylabel("Datos de Y")



#necesario hacer transpose antes de pasar los datos al modelo para que sea un array en 2D y no sea 1D
X=np.transpose([X])

# se entrena un modelo de regresion lineal
#Este modelo calcula la línea de mejor ajuste que minimiza 
# la suma de los cuadrados de los errores entre los valores reales de y y los valores predichos por el modelo.
lr = LinearRegression().fit(X,y)

ajuste_de_X=np.arange(250,720,10)

ajuste_de_X=np.transpose([ajuste_de_X])

y_lin_pred = lr.predict(ajuste_de_X)
plt.plot(ajuste_de_X,y_lin_pred,label="Ajuste lineal",linestyle='--',color='green')

#creamos los ajsutes de la curva con PolynomialFeatures a 0 (en realidad sera una recta)
Horizontal = PolynomialFeatures(degree=0) #Cuando el grado es 0, PolynomialFeatures ignora los valores de X y crea una nueva matriz donde cada elemento es simplemente un 1.

X_horizontal = Horizontal.fit_transform(X)

pr0 =LinearRegression().fit(X_horizontal, y)

y_horizontal_ajuste=pr0.predict(Horizontal.fit_transform(ajuste_de_X))

# plt.scatter(X,y)

plt.plot(ajuste_de_X,y_horizontal_ajuste,label="Ajuste horizontal a 0",color='yellow')

# plt.legend(loc='lower right')


#creamos los ajsutes de la curva con PolynomialFeatures a 2
cuadratico = PolynomialFeatures(degree=2)

X_cuadra = cuadratico.fit_transform(X)

pr2 =LinearRegression().fit(X_cuadra, y)

y_cuadratico_pred=pr2.predict(cuadratico.fit_transform(ajuste_de_X))

#plt.scatter(X,y)

plt.plot(ajuste_de_X,y_cuadratico_pred,label="Ajuste horizontal a 2",color='Red')

#plt.legend(loc='lower right')

#Valor nuevo a predecir con degree a 2
X_nuevo_valor = ([[1200]])

y_predic = lr.predict(X_nuevo_valor)

print(f"el nuevo valor de Y predicho en base a X = 1200 con degree 2 es : {y_predic[0]:.2f}")
print('\n')

#creamos los ajsutes de la curva con PolynomialFeatures a 4
cuatro = PolynomialFeatures(degree=4)
X_cuatro = cuatro.fit_transform(X)

pr4 =LinearRegression().fit(X_cuatro, y)

y_cuatro_ajuste=pr4.predict(cuatro.fit_transform(ajuste_de_X))

#plt.scatter(X,y)

plt.plot(ajuste_de_X,y_cuatro_ajuste, label="Ajuste horizontal a 4",color='Orange')

#plt.legend(loc='lower right')

#creamos los ajsutes de la curva con PolynomialFeatures a 9
noveno = PolynomialFeatures(degree=9)
X_noveno = noveno.fit_transform(X)

pr9 =LinearRegression().fit(X_noveno, y)

y_noveno_pred=pr9.predict(noveno.fit_transform(ajuste_de_X))

plt.scatter(X,y)

plt.plot(ajuste_de_X,y_noveno_pred,label="Ajuste horizontal a 9",color='Green')

plt.legend(loc='lower right')

#Valor nuevo a predecir con degree a 9
X_nuevo_valor = ([[1200]])

y_predic = lr.predict(X_nuevo_valor)

print(f"el nuevo valor de Y predicho en base a X = 1200 con degree 9 es : {y_predic[0]:.2f}")

#Errores cuadráticos medios y coeficientes de determinación
y_hor_ajuste=pr0.predict(X_horizontal)

y_line_pred=lr.predict(X)

y_cuadratico_pred=pr2.predict(X_cuadra)

y_cuatro_pred=pr4.predict(X_cuatro)

y_noveno_pred=pr9.predict(X_noveno)

print("Errores cuadráticos medios")

print("Error cuadrático medio del modelo constante:", round(mean_squared_error(y,y_hor_ajuste),4))

print("Error cuadrático medio del modelo lineal:",round(mean_squared_error(y,y_line_pred),4))

print("Error cuadrático medio del modelo cuadrático:",round(mean_squared_error(y,y_cuadratico_pred),4))

print("Error cuadrático medio del modelo a la cuarta:",round(mean_squared_error(y,y_cuatro_pred),4))

print("Error cuadrático medio del modelo a la novena:", round(mean_squared_error(y,y_noveno_pred),4))

print ("Coeficientes de determinación")

print("Coeficiente de determinación del modelo constante:",round(r2_score(y,y_hor_ajuste),4))

print("Coeficiente de determinación del modelo lineal:",round(r2_score(y,y_line_pred),4))

print("Coeficiente de determinación del modelo cuadrático:",round(r2_score(y, y_cuadratico_pred),4))

print("Coeficiente de determinación del modelo a la cuarta:",round(r2_score(y,y_cuatro_pred),4))

print("Coeficiente de determinación del modelo a la novena:",round(r2_score(y,y_noveno_pred),4))


plt.show()