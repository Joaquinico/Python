'''
📝 Tarea 5 (Opcional): Tu primer modelo de regresión 

📌 Instrucciones:
1.     Crea un modelo de regresión lineal con scikit-learn. Puedes usar un dataset como el de predicción de precios de viviendas (load_boston) o inventar uno simple.
2.     Ajusta el modelo y representa la línea de regresión.
3.     Comenta si crees que el modelo tiene un buen ajuste o no.

'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


archivo_datos = r"C:\Users\Usuario\OneDrive\Python\000Curso Machine Learning - Python\Librerias_Machine_learning\Modelos de regresion\Tarea 5 - regresion lineal\dataset_regresion_materias.csv"
df_datos = pd.read_csv(archivo_datos)
print(df_datos.head)

X = df_datos [['Horas_Estudio']]
y = df_datos['Rendimiento']

#nube de puntos de los datos
plt.scatter(X,y)
plt.xlabel("Horas de estudio")
plt.ylabel("Rendimiento")

lr = LinearRegression().fit(X,y)

ajuste_de_X=np.arange(1,100,10)

ajuste_de_X=np.transpose([ajuste_de_X])

y_pred = lr.predict(ajuste_de_X)

plt.plot(ajuste_de_X,y_pred,label="Ajuste lineal",linestyle='--',color='Red')
plt.legend()
plt.grid(True)

 #creamos curva con PolynomialFeatures a 4
 
curva = PolynomialFeatures(degree=4)

X_curva = curva.fit_transform(X)

pr0 =LinearRegression().fit(X_curva, y)

y_curva=pr0.predict(curva.fit_transform(ajuste_de_X))

plt.plot(ajuste_de_X,y_curva,label="Ajuste polinomico a 4",color='yellow')
plt.legend()
plt.grid(True)


#Evalucion de la precision del modelo LINEAL
y_tr_pred = lr.predict(X)
r2 = r2_score(y, y_tr_pred)
mse = mean_squared_error(y, y_tr_pred)

print("\033[1;31m"+f"Coeficiente de determinación modelo lineal: {r2:.2f}" + "\033[0;m")
print("\033[1;31m"+f"Error cuadrático medio modelo lineal: {mse:.2f}"+ "\033[0;m")
print('\n')


#Evalucion de la precision del modelo Polinomico
y_tra_pred = pr0.predict(X_curva)
r2_poly = r2_score(y, y_tra_pred)
mse_poly = mean_squared_error(y, y_tra_pred)

print("\033[1;33m"+f"Coeficiente de determinación polinomico a 4: {r2_poly:.2f}"+"\033[0;m")
print("\033[1;33m"+f"Error cuadrático medio modelo polinomico a 4: {mse_poly:.2f}"+"\033[0;m")

plt.show()

