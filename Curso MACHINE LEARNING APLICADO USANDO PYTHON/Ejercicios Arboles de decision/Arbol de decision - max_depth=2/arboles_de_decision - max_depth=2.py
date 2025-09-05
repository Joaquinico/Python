

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier #funcion para entrenar un arbol de decisiones
from sklearn.tree import export_graphviz
from sklearn.tree import plot_tree

from pydotplus import graph_from_dot_data 
import matplotlib.pyplot as plt

import pandas as pd

#Cargamos en X la longitud y anchura del pétalo, tal y como hemos hecho en secciones anteriores

#En y se vuelca la clasificación de cada lirio (0, 1, 2)

iris = load_iris()

#Convertir un objeto Bunch (load_iris) en un dataframe
# Convertir a DataFrame
#df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Opcional: agregar columna con las etiquetas
#df["target"] = iris.target

X=iris.data[:,2:] # : → toma todas las filas. 2: → toma las columnas desde la 2 en adelante (es decir, columnas 2 y 3 → "petal length (cm)" y "petal width (cm)").

y = iris.target

#Creamos un objeto arbol_clf con todos los atributos asociados a la construcción del DecisionTreeClassifier
arbol_clf=DecisionTreeClassifier(max_depth=2) # hemos fijado la profundidad de dicho árbol en 2 nodos, dado que indicamos max_depth = 2

arbol_clf.fit(X,y)# se contruye el arbol con x e y

arbol_data = export_graphviz(arbol_clf,out_file=None,feature_names=iris.feature_names[2:], class_names=iris.target_names,rounded=True,filled=True)

grafica = graph_from_dot_data(arbol_data)
grafica.write_png("arbol.png")

plt.figure(figsize=(12, 8)) # se crea la ventana para el grafico con el tamaño indicado
plot_tree(arbol_clf,
          feature_names=iris.feature_names,  # nombres de las variables
          class_names=iris.target_names,     # nombres de las clases
          filled=True,                       # colores para diferenciar
          rounded=True,                      # bordes redondeados
          fontsize=10)

plt.show()
