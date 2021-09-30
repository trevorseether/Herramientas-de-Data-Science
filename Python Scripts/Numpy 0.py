# =============================================================================
# Numpy 
# =============================================================================

#%% Primeros pasos
# Informacion acerca de numpy
import numpy as np 

# Contemos la cantidad de metodos o funciones del modulo 
len(dir(np))

listNumpy = dir(np)

np.__config__
np.__dir__()
print(np.__doc__)
np.__file__
np.__version__
np.__mkl_version__
# math kernel library 

#%% Creacion de arrays de numpy 
# generemos una lista con elementos aleatorios :

import random as rnd
lst = []
# generacion de 100 numeros aleatorios en [14,20]
for indice in range(100):
    lst.append(rnd.randint(14, 20))

type(lst)
len(lst)

vector = np.array(lst)
type(vector)
dir(vector)

help(vector.trace)

#%% Creacion de array a partir de un archivo de datos 

nombres = open("NombresBabys.txt", 'r')
# Creamos una variable para almacenar la informacion que se encuentra en el 
# archivo de datos
ListNames = []
for line in nombres:
    ListNames.append(line.strip().split(','))
nombres.close()
ListNames = ListNames[0]
len(ListNames)

ListNames[0][2:-1] # elementos desde el 3ero hasta el penultimo
ListNames[1][2:-1]  # elementos desde el 3ero hasta el penultimo
ListNames[666][2:-1]  # elementos desde el 3ero hasta el penultimo
ListNames[-1][2:-1]  # elementos desde el 3ero hasta el penultimo

# Creacion de una lista para Nombres limpiando la data 
Nombres = []
for i in range(0, len(ListNames)):
    Nombres.append(ListNames[i][2:-1])
    
Nombres[0:5]
Nombres[995:1000]
Nombres[-1]

# En vista de que el ultimo elemento tiene aun una doble comilla
# hay que limpiar
Nombres[-1] = Nombres[-1][0:-1]

# Verifiquemos 
Nombres[0:10]
Nombres[-9:]

# En vista de esto ultimo, ya tengo una lista limpia , creamos un ndarray
vectorNombres = np.array(Nombres)
type(vectorNombres)
dir(vectorNombres)

#%% Algunos metodos (propiedades) del objeto de tipo numpy.ndarray
vectorNombres.shape
vectorNombres.ndim
vectorNombres.size
vectorNombres.dtype
vectorNombres.itemsize


# Factores de vectorNombres.size
# Creacion de una pequeña funcion para calcular los factores primos de un 
# numero natural 
def prime_factor(n):
    i = 2 
    factor = []
    while i*i <= n :
        if n %i :
            i = i +1 
        else:
            n //= i 
            factor.append(i)
    if n>1  :
        factor.append(n)
    return factor

# Deseo clcular los factores de vectorNombres.size
factores = prime_factor(vectorNombres.size)
prime_factor(prime_factor(vectorNombres.size)[1])


# Para construir matrices , a partir de vectores basicamente lo que hacemos 
# es una redimension del objeto : metodo reshape
MatNombres = vectorNombres.reshape(factores[0], factores[1])
type(MatNombres)
dir(MatNombres)

# Algunos metodos o propiedades
MatNombres.shape

# Numro de filas
MatNombres.shape[0]

# Numero de columnas
MatNombres.shape[1]

MatNombres.ndim # fila-columna

MatNombres.size

MatNombres.dtype

MatNombres.itemsize


#%%

Lista2 = ListNames.copy()

dir(np.ndarray)

help(np.ndarray.dtype)

help(np.ndarray.itemsize)






