'''
Al igual que sucedía en los problemas de regresión, lo habitual en el contexto de árboles es emplear, 
para el entrenamiento del algoritmo, un subconjunto de los elementos a clasificar, 
de modo que los restantes se pueden utilizar para las pruebas. 
En este caso, te animo a que utilices los procedimientos que ya conoces para obtener los datos de entrenamiento 
del conjunto iris y que generes el árbol sin fijar un nivel máximo de profundidad, aplicando como medida de impureza el coeficiente de Gini. 

Escribe el código necesario y obtén la gráfica de dicho árbol. ¿Qué profundidad final se alcanza y cómo son las últimas hojas?

Responde a la cuestión expuesta y, posteriormente, comprueba tu respuesta haciendo clic en el siguiente botón.

'''
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


Iris = load_iris()
print(type(Iris))
print(Iris.keys())

X = Iris.data
y = Iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)
arbol_clf = DecisionTreeClassifier(max_depth=None)
arbol_clf.fit(X_train,y_train)

# el grafico se genera en pantalla usando Matplotlib para la fig y skalearn.tree para la grafica
plt.figure(figsize=(16, 10)) # se crea la ventana para el grafico con el tamaño indicado
plot_tree(arbol_clf,
          feature_names=Iris.feature_names,  # nombres de las variables
          class_names=Iris.target_names,     # nombres de las clases
          filled=True,                       # colores para diferenciar
          rounded=True,                      # bordes redondeados
          fontsize=8)


plt.show()

# 5. Consultar la profundidad y número de hojas
print("Profundidad final del árbol:", arbol_clf.get_depth())
print("Número de hojas terminales:", arbol_clf.get_n_leaves())




