''' Elabora un sencillo programa para descargar del fichero cotiz_GRIF.csv 
las cotizaciones mínimas en cada sesión (vuélcalas a una variable denominada minimos) y 
muéstralas a través de la consola para comprobar que lo has realizado correctamente.'''

import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 

# Cargo el archivo CSV para leer su contenido usando la libreria Pandas. al abrirlo se convierte en un dataframe
coti = pd.read_csv('cotiz_GRIF.csv')
print(f'Encabezados del fichero: {coti.columns}')

# abro el archivo CSV para leer su contenido usando la libreria CSV
with open('cotiz_GRIF.csv') as f:
    lectura = csv.reader(f, delimiter=';')
    encabezados = next(lectura)
    fecha = []
    minimos = []
    maximos = []
    for fila in lectura:
        v_fila_fecha = datetime.strptime(fila[0], '%d/%m/%Y')
        v_fila = float(fila[7])
        v_fila_max = float(fila[6])
        fecha.append(v_fila_fecha)
        minimos.append(v_fila)
        maximos.append(v_fila_max)

print(maximos)
print(minimos)


# Generando la grafica

plt.style.use('seaborn-v0_8') # define el estilo de la grafica
fig,ax = plt.subplots() # crea y define el tamaño de la ventana del grafico
ax.plot(fecha, maximos, c='blue', marker='o', label='maximos')
ax.plot(fecha, minimos, c='red', marker='o', label = 'minimos')

plt.fill_between(fecha, maximos, minimos,facecolor='grey',alpha=0.5) # rellena el espacio entre las dos lineas de la grafica

ax.legend()

plt.title('Valores maximos y minimos de cotizacion')
plt.ylabel('Valor en euros')
plt.xlabel('Fecha de los datos')



ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
fig.text(0.75,0.01, f'Creado el: {ahora}',
         color='blue')

plt.show()



