''' 
objetivos: - calcular la suma de un conjunto de números correlativos
          - calcular la suma de un conjunto de números usando progresion aritmetica para comprobar la eficiencia sobre la suma convencional

Resultado: tiempo usado para el calculo convencional: 0:00:02.023689
           Resultado de la suma de los primeros 50000000 numeros: 1250000025000000
           
           tiempo usado para el calculo con progresion aritmetica: 0:00:00.000002
           total de la suma de los primeros 50000000 numero: 12500002500000.0

'''

from datetime import datetime

def suma_convencional(num):
    inicio = datetime.now()
    resultado=0
    for n in range(num+1):
        resultado+=n
    return inicio, resultado


def suma_progresion_aritmetica(num):
    inicio = datetime.now()
    resultado_con_pro_arit = (num * (num+1)) / 2
    return inicio, resultado_con_pro_arit

primeros_n_num = 50000000
t_inicio, resultado = suma_convencional(primeros_n_num)
t_final = datetime.now()

t_inicio_con_pro, resultado_con_pro = suma_progresion_aritmetica(5000000)
t_fin_con_pro = datetime.now()

print(f'tiempo usado para el calculo convencional: {t_final - t_inicio}')
print(f'Resultado de la suma de los primeros {primeros_n_num} numeros: {resultado}')


print(f'tiempo usado para el calculo con progresion aritmetica: {t_fin_con_pro - t_inicio_con_pro}')
print(f'total de la suma de los primeros {primeros_n_num} numero: {resultado_con_pro}')
