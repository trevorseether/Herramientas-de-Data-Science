# -*- coding: utf-8 -*-
#%% Algebra lineal
# platear un problema de optimización en modelo de álgebra lineal

"Para definir espacio vectorial"
#espacio diferente al vacío
# y 2 operaciones

# A != vacio
# + : A X A > A
# * : R X A > A
# A = matrices M de tamaños 2x2,  + suma de matrices, * producto por escalar
# producto interno: función que oéra sobre 2 elementos en un espacio vectorial,
# cuyo resultado cae en los números reales
# Ortogonalidad, la multiplicación de los vectotres da cero, o algo así
# norma de un vectore es el producto interno de un vector consigo mismo
# a partir de estos conceptos defino una base ortogonal: gram-schmidt

#%%

# =============================================================================
# Primos pasos con NUMPY
# Definiendo objetos vectoriales
# Tipo de datos: type
# Métidos: dir
# También hay que usar help
# =============================================================================
import numpy as np
# ndarray vectores de numpy
dir(np)
listaNumpy = dir(np)
type(listaNumpy)
dir(listaNumpy)
help(np.version)

# Definir vector de numpy

numpy_vector = np.array([1, 2, 3])
type(numpy_vector)
dir(numpy_vector)[0:5] # es una lista por lo tanto se puede acceder a sus componentes

# para definir un objeto vectorial en 2 dimensiones
numpy_matrix = np.array([[234,234,214],[12,24,25]]) # cada corchete es una fila
type(numpy_matrix)
dir(numpy_matrix)

# 3D. array
numpy_3d = np.array([[[1,2,3], [4,5,6]], [[5,3,1], [2,4,6] ]])
type(numpy_3d)
dir(numpy_3d)

help(numpy_3d.shape)
help(np.ndarray.shape)
numpy_vector.shape #nos muestra el tamaño de cada dimensión
numpy_3d.shape #nos muestra el tamaño de cada dimension

# empezamos generando lista de números aleatorios: 50 elementos
list1 = []
import random as rd
for i in range(0,50):
    list1.append(rd.triangular())

list1_np = np.array(list1)

# empaquetamos lo anterior en una función
def makeNP(n):
    """
    parameters
    
    n : int
        tamaño/longitud del vector a generar
        
    return:
        
    ndarray
    """
    import random as rd
    lst = []
    for i in range(0,n):
        lst.append(rd.triangular())
    return np.array(lst)

# creación del vector con el makeNP
    
u = makeNP(1000)
v = makeNP(500)

# Otras funciones para definir vetores

help(np.linspace) # números igulmente intervalados
a = np.linspace(-10, 10, 500) #inferior, superior, número de elementos
b = np.linspace(-np.pi, np.pi, 100)

c = range(12, 24) #desde 12 hasta 24
#no permite ver los elementos a menos que usemon un for
for i in c:
    print(i)
type(c) #variable iteradora

d = np.arange(0, 20, 3) #del 0 al 20 de 3 en 3
help(np.arange)

#sub módulo random de numpy
e = np.random.normal(1, 5, 10)
help(np.random.normal) # media, distribución estandar, 

# simulando algunas notas
notas = np.random.normal(8, 14, (63, 5))

# generando matriz de 3 dimensiones
f = np.random.rand(3,3,2)

#se puede especificar un ndarray con tipo de dato

vec1 = np.array([2,3,4.5]) #float de 64 bits
vec2 = np.array([2,3,4.5], dtype = "float32") #ahora es un float de 32 bits
vec3 = np.arange(0, 4, dtype= "float16") # float de 16 bits
help(np.zeros)
vec4 = np.zeros((4,4), dtype = "complex64") 
# leer :
     # http://www.jldelafuenteoconnor.es/Libro2017_NV_10-8_SP.pdf
     #  capitulo 1 entra al examen

# comparamos el espacio en memoria ram ocupado por una lista
# y con un objeto ndarray

s = range(1000)
import sys
sys.getsizeof(s)*len(s) # resultado en bites

t = np.arange(1000)
t.size*t.itemsize #este pesa menos bites

#los objetos de tipo ndarray operan de manera vectorizada
vec5 = np.random.randint(14,20,5) # 5 elemeentos entre 14 y 19
vec6 = np.random.randint(1,13,5)
vec5.shape
vec6.shape

print(vec5 + vec6)
print(vec5 - vec6)
print(vec5 * vec6)
print(vec5 / vec6)
print(np.sqrt(vec5))

mat1 = np.random.randint(14, 20, (4,4)) #aleatorios del 14 al 19, matriz de 4x4
help(np.random.randint)

# "Dualidad" entre las funciones de numpy y métodos que se aplican a un objeto
# de tipo ndarray. (n dimensional)
np.mean(vec5)
np.median(vec5)
np.var(vec5)
np.std(vec5)

# generamos matriz de números aleatorios
help(np.random.triangular)
mat2 = np.random.triangular(left = 12, #generando distribución normal
                            mode = 13.5, #genera números aleatorios con decimales
                            right = 20,
                            size = (4,4))

mat2 = np.round(mat2, decimals = 0) #se queda con la parte entera
mat2.dtype #pero sigue siendo float
mat2 = np.array(mat2, dtype = "int16")
mat2.dtype #ahora sí son números enteros

mat3 = np.random.triangular(left = 12, #generando distribución normal
                            mode = 13.5, #genera números aleatorios con decimales
                            right = 20,
                            size = (4,4))

mat3 = np.array(mat3, dtype = "int16") #este funciona para quedarse solo con enteros
mat3.dtype #ahora sí son números enteros

# Calculamos la media de mat2 usando np.mean para estudiar el argumento axis
np.mean(mat2)

np.mean(mat2, axis = 0) #media de cada columnas
# np.mean(mat2[:,0]) verificando el cálculo para cada columna

np.mean(mat2, axis = 1) #media para cada filas

# vemos ayuda de la mediana
help(np.median)

# Elementos NA
mat4 = np.random.triangular(12, 13.8, 19, (2,2))
vec7 = np.array([-1,0,1])/0
mat4[0,1] = vec7[1]
np.mean(mat4, axis = 0)

help(np.nanmean) #media que ignora los valores errores
np.nanmean(mat4, axis = 0)


#%% Sub módulo de algebra lineal

mat5 = mat1.copy() #sin el copy, va a enlazar ambas matrices
mat5[0,0] = 20

help(mat1.copy)

mat6 = mat2.copy()

# rango de una matriz
np.linalg.matrix_rank(mat5)
help(np.linalg.matrix_rank)

# determinante d euna matriz
np.linalg.det(mat5)

# traza de una matriz
np.trace(mat5) #suma de los elementos que pertenecen a la diagonal principal

# potencias de matrices: producto matricial
np.linalg.matrix_power(mat5, 3)

#no es lo mismo que esto porque es cada elemento al cubo
mat5**3

# Lista de metodos que pertenecen al álgebra lineal
x = dir(np.linalg)

help(np.linalg.eigh)
help(np.linalg.eig)

#verificamos el cálculo
A = np.array([[0, 1, -1], [1, 1, 0], [-1, 0, 1]])
np.linalg.eig(A)
# A*lambda = lambda*v

B = np.array([[1, -2j],[2j, 5]])
B.dtype

# QUÉ OCURRE SI UTILIZO EIG PARA B
np.linalg.eig(B)
np.linalg.eigh(B) #aparentemente no hay difernecia

#generamos una matriz de 10**4 x 10**4
mat7 = np.random.triangular(21,25,32, (10**2, 10**2))
mat7.size*mat7.itemsize #está pesando 800 megabytes

autoval, autovec = np.linalg.eig(mat7)

























