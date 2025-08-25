'''
1. Genera, en primer lugar, el código necesario para determinar el elemento n-ésimo de la sucesión de Fibonacci. 
Trata de emplear, para ello, una función que devuelva el valor correspondiente en caso de que n sea 0 o 1 y que, en otro caso, 
proporcione la suma de los términos precedentes, llamándose a sí misma hasta alcanzar los dos primeros términos. 
2. medir su eficiencia.
   
    
Otra fórmula que permite calcular el elemento n-ésimo de la sucesión de Fibonacci es la siguiente, con el uso de la fórmula de Binet, 
que hace uso de la proporción aurea:
1. Genera el código necesario para determinar el elemento n-ésimo de la sucesión de Fibonacci a través de este segundo enfoque.
Recuerda que, para calcular raíces cuadradas en Python, necesitas la función sqrt de la librería math; por ejemplo, print(sqrt(4)) 
da como salida el valor 2. Ten en cuenta, además, que la potenciación se representa en Python con 2 asteriscos.
2. ¿Cuál de estos dos algoritmos crees, a priori, que será más eficiente? Justifica tu respuesta.
3. Computa el tiempo invertido por cada uno de estos algoritmos en el cálculo del elemento 40 de la sucesión de Fibonacci. 

    Introduce la posicion de la serie de Fibonacci que quieres calcular: 45
el valor del 45º elemento de la serie de fibonacci es : 1134903170
El tiempo empleado en el calculo es de: 0:03:29.725328
formula para hallar el enesimo numero de la serie usando recursividad: fn = fn-1 + fn-2 (considerando f0 = 0)


Valor de fi (Proporcion aurea) = 1.618033988749895
el valor del 45º elemento de la serie de fibonacci calculado con la formula de Binet es : 1134903170.00
El tiempo empleado en el calculo usando la formual de Binet es de: 0:00:00.000303
formula de Binet usada para el calculo: ((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n)) / math.sqrt(5)

'''
from datetime import datetime
import math

def calculo_fibonacci(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculo_fibonacci(n-1) + calculo_fibonacci(n-2)
    

def Calculo_n_fibonacci_Binet(n):
    
    fi = (1 + math.sqrt(5)) / 2
    print(f'Valor de fi (Proporcion aurea) = {fi}')

    fn = ((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n)) / math.sqrt(5)

    return round(fn)


def calculo_fibonacci_sin_recursividad(n):
        if n<2:
            return n
        else:
            prim_elem=0
            seg_elem=1
            contador=1
            suma=0
        while(contador<=n):
            contador+=1
            prim_elem=seg_elem
            seg_elem=suma
            suma=prim_elem+seg_elem
        return suma

n = int(input("Introduce la posicion de la serie de Fibonacci que quieres calcular: "))

''' Calculo usando funcion recursiva con al formula del calculo de fn de Fibonacci'''
t_inicial = datetime.now()
print(f'el valor del {n}º elemento de la serie de fibonacci es : {calculo_fibonacci(n)}')
t_final = datetime.now()
print(f'El tiempo empleado en el calculo es de: {t_final-t_inicial}')
print('formula para hallar el enesimo numero de la serie usando recursividad: fn = fn-1 + fn-2 (considerando f0 = 0)')
print('\n') 

''' callculo Usando la formula de Binet'''
t_inicial_con_binet = datetime.now()
print(f'el valor del {n}º elemento de la serie de fibonacci calculado con la formula de Binet es : {Calculo_n_fibonacci_Binet(n)}')#:.2f} solo dos decimales
t_final_con_binet = datetime.now()
print(f'El tiempo empleado en el calculo usando la formual de Binet es de: {t_final_con_binet-t_inicial_con_binet}')
print('formula de Binet usada para el calculo: ((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n)) / math.sqrt(5)')
print('\n')

''' calculo del enesimo elemento de fibonacci sin recursividad ni formula de Binet'''
t_inicial_sin_recur_sin_Binet = datetime.now()
print(f'el elemento {n} de la serie de Fibonacci es {calculo_fibonacci_sin_recursividad(n)}' )
t_final_sin_recur_sin_Binet = datetime.now()
print(f'El tiempo empleado en el calculo sin recursividad ni Binet es: {t_final_sin_recur_sin_Binet-t_inicial_sin_recur_sin_Binet}')
