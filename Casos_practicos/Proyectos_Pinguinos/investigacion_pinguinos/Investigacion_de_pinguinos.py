''' 
Caso práctico: investigación de pingüinos.
Genera el código necesario para realizar las siguientes cuestiones:

1. Carga los datos e imprime por pantalla los encabezados de las columnas existentes. - HECHO
2. Imprime las cinco primeras filas del fichero. - HECHO
3. Obtén el diagrama de correlación entre las variables ‘bill_length_mm’ y ‘bill_depth_mm’, considerando como variable discriminatoria ‘species’. 
Incorpora una rejilla para visualizar mejor los datos. - HECHO
4. Dibuja la matriz de correlaciones entre todas las variables existentes, discriminando de nuevo con ‘species’.

'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime
import csv

ahora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
fich_csv = 'penguins_mod.csv'

with open(fich_csv) as f:
    lector = csv.reader(f, delimiter=',')
    encabezados = next(lector)
    for fila in lector:
        print(fila)

df_penguins = pd.read_csv(fich_csv)
print(df_penguins.columns)
print(df_penguins.columns.values)
print(df_penguins.head())

fig,ax = plt.subplots()
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', data=df_penguins, hue='species')
fig.text(0.75, 0.01, f'Creado el {ahora}')


g = sns.pairplot(data=df_penguins, hue='species', height=2.5)

g.figure.text(0.84, 0.01, f'creado el {ahora}')




plt.grid(True)

plt.show()

