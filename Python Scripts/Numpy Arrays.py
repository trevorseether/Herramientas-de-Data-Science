#%% sympy
import sympy
print(sympy.__version__)

#%% numpy

# =============================================================================
# Información acera de Numpy
# =============================================================================

import numpy as np
print(np.__version__)

#Contamos la cantidad de metodos del módulo
len(dir(np))

listNumpy = dir(np) #meter todos los métodos en una lista

np.__config__ #ruta donde se encuentra el archivo de configuracion de este módulo
np.__dir__() #otra forma de ver todas las funciones
print(np.__doc__) #documentación
np.__file__
np.__version__
np.__mkl_version__ #librería que utiliza para el álgebra lineal
# math kernel library está usando la version 2020.0 
# intel mkl es una librería de matemáticas de esa empresa

# =============================================================================
# Creación de arrays(vector) de numpy
# =============================================================================
#generamos una lista con elementos aleatorios

import random as rd

lst = []
#generación de 100 números aleatorios en [14, 20]
for indice in range(100):
    lst.append(rd.randint(14,20))

type(lst)
len(lst)

vector = np.array(lst) #módulo array recibe lista
type(vector)
len(dir(vector))

#%% creación de array a partir de un archivo de datos

nombres = open("NombresBabys.txt", "r")
#creación de una variable para almacenar el archivo
listnames = []
for line in nombres:
    listnames.append(line.strip().split(","))
nombres.close()
listnames = listnames[0]
len(listnames)

listnames[0][2: -1]
listnames[1][2: -1]

listnames[-1][]

#limpiar la información
Nombres = []
for i in range(0, len(listnames)):
    Nombres.append(listnames[i][2:-1])
    
Nombres[0:5]
Nombres[-5:-1]
#limpiar manualmente al último elemento
Nombres[-1] = Nombres[-1][0:-1]

#Verifiquemos
Nombres[0:10]
Nombres[-9:]

#Ya tenemos una lista limpia, creamos un array
vector_nombres = np.array(Nombres)
dir(vector_nombres)

# =============================================================================
# mÉTODOS DEL numpy.ndarray
# =============================================================================

vector_nombres.shape #numero de elementos
vector_nombres.ndim #dimension
vector_nombres.itemsize #cada uno de los elementos ocupa 60 bytes
vector_nombres.dtype
vector_nombres.size

#matriz, reformatear un objeto lineal

# Factores de vector_nombres

vector_nombres.size/7

#Creación de una pequeña función para calcular los factores primos de un número natural
def prime_factor(n):
    i=2
    factor = []
    while i*i <= n:
        if n%i :
            i = i+1
        else:
            n //= i
            factor.append(i)
    if n>1:
        factor.append(n)
    return factor

prime_factor(5626)
factores = prime_factor(vector_nombres.size)
prime_factor(prime_factor(vector_nombres.size)[1])

"""Para construir matrices a partr de los vectores basicamente
hacemos una redimensión del objeto: metodo reshape"""

mat_nombres = vector_nombres.reshape(factores[0], factores[1])
#anterior se ha creado una matriz de 47 * 38839 

type(mat_nombres)
dir(mat_nombres)

mat_nombres.shape #no da tupla (filas, columnas)

#Número de filas

mat_nombres.shape[0]

#Número de columnas

mat_nombres.shape[1]

mat_nombres.ndim #se encuentra en 2 dimensiones

mat_nombres.size

mat_nombres.dtype

mat_nombres.itemsize #cantidad de memoria que ocupa cada elemento (60 bytes)

#%%

lista2 = listnames.copy()

dir(np.ndarray)
help(np.ndarray.dtype)
help(np.ndarray.itemsize)

#%% matplotlib
import matplotlib
print(matplotlib.__version__)

#%% scipy
import scipy
print(scipy.__version__)



