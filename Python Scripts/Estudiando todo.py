# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:35:44 2020

@author: Myre
"""
#34 print
#54 variables string
#76 Variables int (números enteros)
#115 variables float o decimales
#122 variables bool(True, False)
#155 metodos de strings
#180 LISTAS: colecciones ordenadas, no indexadas, mutables(podemos editar los elementos)
#a diferencia de las tuplas que son inmutables
#224 TUPLAS: Colecciones ordenadas, no indexadas,que SON INMUTABLES
#239 SETS: Colecciones no ordenadas, no indexadas, mutables, que no permiten elementos duplicados
#262 DICCIONARIOS: Colecciones no ordenadas, INDEXADAS, mutables, que no permiten elementos duplicados
#279 OPERADORES EN PYTHON
#361 SENTENCIAS IF, ELIF, ELSE
#413 Ciclo for
#471 Ciclo while
#508 regresion lineal MCO
#542 lIST COMPREHESION
#578 funciones lambda
#650 definir funciones
#740 funciones lambda otra vez pero aho rì bien entendido

"""
...........................................................
programo en python gaaaaaaaaaaaaaaaaaa
python 3 desde cero
-----------------------------------------------------------
"""
print ("asdasd")
print("debe llevar parentesis para no arrojar error")
# Para correr todo el código F5
# Para correr solo unas lineas en específico F9

"importar excel a python"
import pandas as pd
#es obligatorio poner el .xlsl
archivo = pd.read_excel("hoja.xlsx")
#si no hemos creado un proyecto, esto requeriría:
archivo2 = pd.read_excel("E:\\Joseph\\tutorial python\\proyecto 1\\hoja.xlsx")


"""Definicón y operación de variables en python"""

"spyther como interprete"
import math #librería para funciones y constantes matemáticas



"==========================================================================="
# Variables string
"==========================================================================="
variable_str = "La cartilla"
tutorial = "Python 3"
x = "la carta"

print (variable_str, tutorial, x) #"ver que es diferente resultado de poner , o +"
print (variable_str + tutorial+ x)
#para agregar un espacio con el signo +
print (variable_str + " " + tutorial + " " + x)
print (variable_str + " " + tutorial + " " + x + " " +"resultado de mult")
print (variable_str + " " + tutorial + " " + x + " " + str("mult"))

print(type(x))
type(x)
#type para pedir que tipo de variable es:
print(type(variable_str))
#comando len sirve para medir el tamaño de la variable
len(variable_str)
print(len(x))

"==========================================================================="
# Variables int (números enteros)
"==========================================================================="
variable_int = 1001
variable_int2 = 10
mult  = variable_int * variable_int2

"para elevar a potencia se usa doble asterisco"
variable_int2**2
variable_int2**20
variable_int2** (1/2) #la raiz requiere paréntesis, sino se pone a multiplicar

9**2

9** 1/2

x = 1/2
9**x

9**(0.5)
9**(-1)

"en todo caso, luego de importar la librería math, podemos usar math.sqrt()"
variable_int2**2/3
"""dividir se hace con un slash, pero con doble slash
obtienes solo numeros enteros"""
variable_int2//3
"usando math para multiplicar por pi"
variable_int2*math.pi
"ahora vamos a redondear mediante el comando round (valor, número de decimales)"
pi_10 = variable_int2*math.pi
pi_10 = round(pi_10, 2) #con esta estructura estas reescribiendo el valor de la variable

#print(len(variable_int)) "arrojará un erorr porque los numeros no son texto con unidades contables"
type (variable_int)
int2 = 10, 12, 11
"y = int2 * variable_int"
"print (y)"

"==========================================================================="
#variables float o decimales
"==========================================================================="
asd = 123.213
type(asd)
asd**1/2

"==========================================================================="
#variable bool 
"==========================================================================="
t = True #"1"
f = False #"0"

int(t)
print (t)

str ("asd")
#****************************************************************************
#IMPORTAR MÓDULOS / PAQUETES / LIBRERÍAS EN PYTHON
#****************************************************************************
"""A saber que python tiene funciones nativas, y para buscarlas
built in fuctions python"""

import math
#para acceder usamos math. + tabulacion

"ahora como ejemplo, importamos keras, que es una librería que no tenemos descargada"
import keras #cagao
import sklearn as skl
import pandas as pd

from sklearn.decomposition import PCA as pca



#****************************************************************************
#Métodos de strings nativos o cadenas de textos en Python 3
#****************************************************************************
#El python tiene funciones nativas o built-in
#https://www.w3schools.com/python/python_ref_string.asp

string1 = "La cartilla"
string2 = "123"
string3 = "Python 3 desde cero"

#Descriptivos o de análisis

string1.count("cartilla") #contar cuantas veces tenemos la palabra "cartilla"
string3.find("d") #desde donde empieza la letra que buscamos
string1.islower() #estamos preguntando si está todo en minúscula
string3.isupper() #preguntamos si está todo en mayúscula
string1.isnumeric() #este comando sirve para la minería de datos
string2.isnumeric() #nos avisa si hay valores numéricos

#Metodos de transformación
string1.upper() #nos lo devuelve en mayúsculas
string1.title() #le pone mayúscula solo al 
string1.replace("a", "e") #reemplaza la "a" por la "e"
string3.split(" ") #le pido que me lo separe por espacios
"nos muestra el resultado como una lista"

#****************************************************************************
#COLECCIONES / ARREGLOS BASICOS EN PYTHON
#****************************************************************************
"----------------------------------------------------------------------------"
#LISTAS: colecciones ordenadas, no indexadas, mutables(podemos editar los elementos)
#a diferencia de las tuplas que son inmutables
"----------------------------------------------------------------------------"
"""las listas son estructuras de datos muy versátiles porque pueden conteenr 
distintos tipos de elementos, podemos mezclar string, enteros, boleanos, floats,
otras listas, tuplas, sets o diccionarios ,incluso objetos mas complejos como
 dataframes de pandas"""
lista1 = [1,1,2,3,5, "la cartilla", (1), (1,2),(1,1,2,3,4), [True, False, False]]
#para acceder a los elementos de una lista, hay un indice, se cuentan desde el 0
#0, 1, 2, 3,... (indice positivo)
#o también puede ser de derecha a izquieda(indice negativo)
#..., -5, -4, -3, -2, -1  
lista1[4] #contando desde el cero, muestra al 5to valor
lista1[1: 8] #llamada del segundo al 8av valor, indices 1 al 7
lista1[3:] #llamada desde el cuarto elemento hasta el final
lista1[-2:]
lista1[:-4]
lista1[9][0] #el primer elemento de la decima lista
lista1[9][1:]
lista1[0] = 10 #reemplazamos el primer valor por 10
lista1[-1] = 88 #reemplazó todo el grupo de trues and falses, por 88
lista1[-1][0] = 2 #reemplazó solo uno de los valores de la lista
del(lista1) #equivalente al drop del stata
del(lista1[-1]) #eliminó solo el último elemento de la lista

del(lista1[9])
del(lista1[8])
del(lista1[7])
del(lista1[5])
sorted(lista1) #dropeamos todos los anteriores para poder ordenar, por defecto 
#de menor a mayor
"para cambiar el orden la lista"
lista1 = sorted(lista1)

"para ordenar de mayor a menor"
lista1 = sorted(lista1, reverse=True)
 
"para agregar un nuevo valor a la lista-----------------"
lista1.append(89)
lista1.append([True, False, "variable"])

#Metodos de listas nativos para python
#https://www.w3schools.com/python/python_ref_list.asp

"----------------------------------------------------------------------------"
#TUPLAS: Colecciones ordenadas, no indexadas,que SON INMUTABLES
"----------------------------------------------------------------------------"
#Métodos asociados a las tuplas
#https://www.w3schools.com/python/python_ref_tuple.asp

#tambien se construyen por defecto, sin paréntesis
tupla1 = (True, False, 1, 2, 3, (1,2), ["a","b", 1])
tupla1[1] #a pesar de que los parentesis son para definir tuplas, los llamados
#a sus variables se siguen haciendo con corchetes
tupla1[1] = 12 #estos dos comandos no son validos
del(tupla1[1]) #la tupla no admite cambios dentro de la misma
del(tupla1) #pero sí se puede borrar toda la tupla

"----------------------------------------------------------------------------"
#SETS: Colecciones no ordenadas, no indexadas, mutables, que no permiten elementos duplicados
"----------------------------------------------------------------------------"
#Métodos asociados a los sets
#https://www.w3schools.com/python/python_ref_set.asp
#usa corchetes {}
#no admite listas ()
#no admite tuplas []
set1 = {1,2,3,4, "la cartilla", 1,2, True, False} 
#El True no aparece porque es es lo mismo que 1

"para agregar UN nuevo valor al set-----------------"
set1.add("python")
set1.add(67) #este permite agregar strings e int

"para agregar VARIOS nuevos valores al set-----------------"
set1.update(["a","c", "d", True, False, 123]) #este no permite agregar ints, 
#pero sí tuplas y strings, y dentro de las tuplas deben ir los ints

"para remover elementos del set"
set1.discard("la cartilla") #ya no existe número de orden, y hay que expresar 
#completamente el valor que hay que ser eliminado

set1.intersection("set2") #te muestra los elementos en común
set1.difference("set2") #te muestra las diferencias
set1.union("set2") #junta los 2 sets y sin repeticiones
"----------------------------------------------------------------------------"
#DICCIONARIOS: Colecciones no ordenadas, INDEXADAS, mutables, que no permiten elementos duplicados
"----------------------------------------------------------------------------"
#Métodos asociados a diccionarios
#https://www.w3schools.com/python/python_ref_dictionary.asp
carro = {"marca": ["ford", "volwsgaen"], 
         "modelo":["mustang", "escarabajo"], 
         "año": ["1964", "2014"]}

carro["marca"]
carro["stock price"] = "250" #añade como si fuera pandas
carro.update({"color":"rojo"}) #añade de otra forma
carro.pop("stock price") #corta el elemento del diccionario
carro

carro.get("modelo") #el get se usa para que no te de error si es que la key no existe
carro.get("llantas") #no genera error
carro.keys() #nos muestra los índices, en formato "dict keys" hay que castear
#para poder trabajar con esta información
keys = list(carro.keys())
keys #ahora sí podemos trabajar como estabamos viendo

carro.values() #te muestra todos los valores(no indices)
valores = list(carro.values()) #castearlo a lista es otra buena práxis

carro.items() #te muestra todo

lista_marcas = ["ford","audi","jaguar"]
carro2 = {"marcas": lista_marcas}
carro3 = {"marcas": ["ford","audi","jaguar"]}
carro2.update({"colores":["rojo", "negro", "plata"]})
#update también sirve para juntar un diccionario con otro
#llave repetida te reemplaza la llave anterior
#=============================================================================
"----------------------------------------------------------------------------"
#OPERADORES EN PYTHON
"----------------------------------------------------------------------------"
#=============================================================================
"link de los operadores"
#https://www.w3schools.com/python/python_operators.asp

#Operadores aritméticos
#=============================================================================

10%3 #modulo % significa residuo de una divisón

x = 10
x//3 #valor entero de la división
x**2 #exponente

#Operadores de asignación
#=============================================================================
y = "La cartilla"
x+=5 #es lo mismo que poner x = x+ 5
x = x+ 5
x -= 10
x/= 5
x += "python" #no se puede agregar string al float
y += " python"

#Operadores de comparación (<>, y otros)
#=============================================================================
x == y #preguntamos, x es igual y?
x == 10
y == y
x!= y #preguntamos si x es DIFERENTE de y
True != False
10.515  > 2  #preguntamos si es mayor
len(y) #preguntamos por el número de caracteres que compone a la variable
#solo funciona para string
len(y) > x #puede compararse con otra variable
10>=10

#Operadores lógicos en python
#=============================================================================
x>5 and x>=10 #True
x>5 and x>10 #False
x>5 or x>10 #True
x>5
not(x>5 and x>=10) #not(True)

#Operadores de identidad
#=============================================================================

x is x #x es el mismo tipo de variable que x?
x is variable_int2 #x es el mismo tipo de variable que variable_int2?


#Operadores de pertenencia
#=============================================================================
x = 10, 11, 12
10 in x #pregunta si 10 está en la lista o vector x
10 not in x #pregunta si no está en
"la" in y #pregunta si hay "la" dentro de y = la cartilla

#=============================================================================
"----------------------------------------------------------------------------"
#SENTENCIAS IF, ELIF, ELSE
"----------------------------------------------------------------------------"
#=============================================================================
#=============================================================================
 
#comando imput sirve para intriducir valor en la consola, con el nombre número
#y automaticamente cree una variable
numero = input("introduzca un número: ") #por defecto crea strings
numero = int(input("introduzca un número: ")) #con el int, creará un numero entero
numero = float(input("introduzca un número: ")) #con el float creará decimal


numero = input("introduzca un número: ")
if numero == 5:
  print("kk")


#usaremos el modulo para saber si es par o impar
"============================================================================"
numero = int(input("introduzca un número: "))
#para indicar que hemos terminado la sentencia "if" se pone al final dos puntos :
if numero%2 == 0:
    print("El número introducido es par")
"else = sino cumple la enterior condición, entonces :"    
else:
    print("El número introducido es impar")
"============================================================================"

"============================================================================"
numero = int(input("introduzca un número: "))
if numero%2 == 0:
    print("El número introducido es par")
    if numero <= 20:
        print("El número es menor igual a 20")
    else:
        print("El número es mayor a 20")

else:
    print("El número introducido es impar")
    if numero <= 20:
        print("El número es menor igual a 20")
    else:
        print("El número es mayor a 20")
"============================================================================"

"============================================================================"
numero = int(input("introduzca un número: "))
if numero%2 == 0:
    print("El número introducido es par")
    if numero <= 20:
        print("El número es menor igual a 20")
    else:
        print("El número es mayor a 20")

else:
    print("El número introducido es impar")
    if numero < 20:
        print("El número es menor a 20")
#si las condiciones anteriores no eran ciertas, entonces intente esta condición        
    elif numero >20 and numero <= 30:
        print("El número es mayor a 20 y menor o igual a 30")
    else:
        print("El número es meyor a 30")
"============================================================================"

if numero > 30:
    numero  = numero**2
   
string = "la"
if len(string) >4:
    print(string) #la tabulación es importante para que python sepa hasta donde 
#va la condicional
else: 
    print ("el numero de caracteres es pequeño")

#=============================================================================
"----------------------------------------------------------------------------"
#CICLO FOR (bucle, lo Único que determina el número de iteraciones de algún proceso
#es el número de veces que decidas hacer algo)
"----------------------------------------------------------------------------"
#=============================================================================

#debemos partir de un objeto iterable, listas, tuplas, sets y diccionarios
#strings tambien son iterables porque están compuestos por caracteres
#otro objeto iterable es el rango

rango = range(10,20,2) #inicio, final, step(de cuanto en cuanto)
#LIMITE SUPERIOR DEL RANGO NO ES INCLUSIVO, EL RANGO ES DE 10 A 19

for elementitos in rango:
    print(elementitos)
#claramente estamos indicando el momento de la parada


for ix, elementitos in enumerate(rango):       #ix es indice
    print ("indice: " + str(ix) + ", elemento: " + str(elementitos))

"----------------------------------------------------------------------------"
rango = range(10,25,2)
rango2 = [2,4,5,6,7,8,10,122]
for ix, elemento in enumerate(rango):       #ix es indice
    #print ("indice: " + str(ix) + ", elemento: " + str(elementitos))
    print ("indice: " + str(ix) + ", elemento: " + str(elemento) + ", mult: " + str(elemento*rango2[ix]))
"----------------------------------------------------------------------------"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(2, 30, 3):
  print(x)

#ANIDANDO CICLOS FOR
lista = [["la","cartilla"],("python", "3", "desde cero")]
for x in lista:
    #print (x)
    for elemento2 in x:
        print(elemento2)

lista = [["la","cartilla"],("python", "3", "desde cero")]
for elemento in lista:
    #print (elemento)
    for zoom_elemento in elemento:
        if len(zoom_elemento) >3:
            print(zoom_elemento)

detalles = []
for ix in range(len(lista)):
    for elemento, lista[ix]:
        detalles.append([lista[ix], elemento, len(elemento)])
"volver a estudiar los ciclos for"

#=============================================================================
"----------------------------------------------------------------------------"
#CICLO WHILE
"----------------------------------------------------------------------------"
#=============================================================================
#Ciclo for se usa para un cantidad de repeticiones ya anteriormente definida
#Con while defines una condición para realizar un número de iteraciones desconocido
numero_usuario = int(input("Ingrese un número mayor a 50: "))

while numero_usuario <= 50:
    numero_usuario = int(input("Número errado, por favor ingrese otro :"))
print("Gracias, su número es correcto :v ")

help(ifelse)
#esta es otra forma de printear lo mismo
numero_usuario = int(input("Ingrese un número mayor a 50: "))
while numero_usuario <= 50:
    numero_usuario = int(input("Número errado, por favor ingrese otro :"))
else:
    print("Gracias, su número es correcto :v ")

numero = 1
while numero<10:
    print("El número es menor a 10")
    numero+=1
    
    
numero = 2
while numero<100000000000000:
    print(numero)
    numero+=1    
    if numero >100:
        print("el numero ya es mayor a 100")
        break
    


#=============================================================================
"----------------------------------------------------------------------------"
#REGRESIÓN LINEAL Y MÍNIMOS CUADRADOS ORDINARIOS
"----------------------------------------------------------------------------"
#=============================================================================

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
boston = load_boston()

print(boston.DESCR)

X = boston.data[:,5]
#print(X)
Y = boston.target
#print(Y)

X = np.array(boston.data[:,5])
Y = np.array(boston.target)
plt.scatter(X, Y, alpha= 0.3)


#Añadimos columna de 1s para el término independiente.
X = np.array([np.ones(506), X]).T
#print(X)
B = np.linalg.inv(X.T @ X) @ X.T @ Y
B
plt.plot([4,9], [B[0]+B[1]*4, B[0]+ B[1] * 9], c = "green")
plt.show()


#=============================================================================
"----------------------------------------------------------------------------"
#LIST COMPREHENSION EN PYTHON
"----------------------------------------------------------------------------"
#=============================================================================

pares = []
for numero in range(100):
    if numero%2==0:  #% significa modulo o residuo de una división
        pares.append(numero) #si el numero es par, se agrega a la lista "pares"

pares_lc = [numero for numero in range(100) if numero%2==0]

pares_dc = {"id: " + str(numero):numero for numero in range(100)  if numero%2==0}

generador = (numero for numero in range(100) if numero%2==0)
generador2 = list(generador)

import numpy as np #numpy es una biblioteca de funcione matemáticas de alto 
#nivel, se utiliza como soperte para vectores y matrices en muchas otras librerías
#como pandas, etc
parabola = np.array([[x,x**2]for x in range(-10,10,1)])
"np.array()es para convertir a matrices"

import matplotlib.pyplot as plt #librería para gráficos
plt.plot(parabola[:,0],parabola[:,1]) #[:,0] significa coger todos los elementos 
#de la columna "0", [:,1]significa coger todos los elementos de la columna 

"tokenización"

frases = ["La cartilla", "Curso de python", "list comprehension"]
tokens = [palabra.split(" ") for palabra in frases]
#split es una función de los strings significa separar frase o elemento string
#por un caracter en específico, en este caso el espacio entre plabras


#=============================================================================
"----------------------------------------------------------------------------"
#FUNCIONES LAMBDA EN PYTHON
"----------------------------------------------------------------------------"
#=============================================================================
"""Funciones anónimas
Funciones cortas que no requieren usar el prefijo def, adicionalmente no requieren 
de la asignación de un nombre específico (por eso son anónimas) pueden tomar múltiples
argumentos, pero solo reciben una expresión, de manera que únicamente se pueden
utilizar para simplificar el código cuando tenemos operaciones lógicas relativamente 
sencillas que queremos comprimir"""

mensaje = lambda numero: "el número ingresado es: " + str(numero)
mensaje(123)

binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2
binomio_cuadrado(21, 3)

""""Encontrar todos los números de 3 digitos en los que la suma de cada dígito 
al cubo es igual al nùmero"""

def cubos(numero):
    str_numero = str(numero)
    cubos = (int(valor)**3 for valor in str_numero)
    return sum(cubos)

valores_buscados = []
for numero in range (100,1000):
    if numero == cubos(numero):
        valores_buscados.append(numero)
        

"--------------------------------------------------------------------------"
suma_cubos = lambda numero: sum(int(digito**3) for digito in str(numero))
numeros_buscados = 

"-------------------------------"
#Ciclos For
"-------------------------------"
"""Los bucles en cualquier lenguaje son estructuras de control que nos sirven 
para aplicar funciones lógicas un cierto número de veces"""
#Para eso, debemos partir de una variable u objeto que sea iterable
#listas, tuplas, sets, diccionrios ()objetos iterables
#tambien los strings
#rango, otro objeto iterable

rango = range(1, 50, 4) #range se utiliza para crear rangos
for elementos in rango:
    print(elementos)

"Para acceder al indice del rango"
rango = range(1, 50, 4) #range se utiliza para crear rangos
for elementos in rango:
    print(elementos)

rango2 = [2,4,6,8,10]
for ix,elemento in enumerate(rango2):
    print("índice: " + str(ix) + ", elemento:" + str(elementos) + str(rango2(ix)))


"-------------------------------"
#Funciones de python
"-------------------------------"

def cuadradogaa(numero):
    valor_funcion = numero**2
    return valor_funcion

def raizcuadradagaa(numero):
    return numero**(1/2)

cuadradogaa(12)
print(raizcuadradagaa(18))

def utilidad_neta(ingresos_brutos,egresos,tasa_impuestos=0):
    uti = (ingresos_brutos-egresos)*(1-tasa_impuestos)
    return uti

utilidad_neta(3000,500)

#vamos a definir una parábola, ingresando el min y max nos va a plotear un grafico

import matplotlib.pyplot as plt
def paravola(minimo,maximo,step):
    x=[]
    y=[]
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**2)
        
    plt.plot(x,y)
    return x,y

valoresx, valoresy = paravola(-70, 78, 70)

#Argumentos arbitrarios en funciones

def tipo_datos(*datos):
    tipos_datos = []
    for valor in datos:
        tipos_datos.append(type(valor)._name_) "doble guion bajo a cada lado"
    return tipos_datos

tipos_datos = tipo_datos(1,10,5,0.3,True, "la cartilla")

def utilidad_neta(**valores):
    uti = (valores["ingresos_brutos"]-valores["egresos"])*(1-valores["tasa_impuestos"])
    return uti

"input"
#utilidad_neta(egresos=300,ingresos_brutos=1000,tasa_impuestos=0.1,otro=0)

import matplotlib.pyplot as plt
def cubica(minimo,maximo,step):
    x=[]
    y=[]
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**3)
        
    plt.plot(x,y)
    return x,y

valorex, valoresy =

def obtener_grafica(minimo, maximo, step, tipo_funcion):
    if tipo_funcion ==1.:
        return paravola(minimo,maximo,step)
    elif tipo_funcion==2:
        return cubica(minimo,maximo,step)
    else:
        return print("El tipo de funcion ingresada es incorrecta")

valores_grafica = obtener_grafica(-10,50,2,1)

x,y = obtener_grafica(-10,5,2,1)
https://www.w3schools.com/python/python_functions.asp

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

"generando la sucesión de fibonacci"
#forma iterativa
def fiib(n):
    a= 0
    b= 1
    for k in range(n):
        c = a + b
        a = b
        b = c
    return b
for x in range(1,20):
    print(fiib(x))
#de froma recursiva
def fib_r(n):
    if n < 2:
        return n
    return fib_r(n-1) + fib_r(n-2)
for x in range(1,20):
    print(fib_r(x))
    
"-----------------------------------------------------------------"
#funciones lambda
"-----------------------------------------------------------------"
"no requieren def ni nombre especifico"
mensaje = lambda numero: "el numero ingresado es: " + str(numero)
mensaje(9)   
binomio = lambda a,b: a**2 + 2*a*b + b**2
binomio(2,5)
"encontrar numeros de 3 digitos cuya suma al cubo de los elemntos, de el mismo"
"---------------------------------------------------------------------------"
def cubos(numero):
    "lo convertimos primero en string para acceder a cada uno de los elementos"
    str_numero = str(numero)
    cubos = (int(valor)**3 for valor in str_numero)
    return sum(cubos)
valores_buscados = []
for numero in range(100,1000):
    if numero == cubos(numero):
        valores_buscados.append(numero)
print(valores_buscados)
"---------------------------------------------------------------------------"
#con funcion lambda
suma_cubos = lambda numero: sum(int(str(x))**3 for x in str(numero))
suma_cubos(370)
valorcitos = []
for numero in range(100,1000):
    if numero == suma_cubos(numero):
        valorcitos.append(numero)
print (valorcitos)
"---------------------------------------------------------------------------"
#ahora ciclo for con list comprehension
suma_cubos = lambda numero: sum(int(str(x))**3 for x in str(numero))
#suma_cubos(370)
numeros_buscados = [numero for numero in range(1,1000000) if numero == suma_cubos(numero)]
print (numeros_buscados)

import pandas as pd
from pandas_datareader import data as pdr
import pyfolio
pip install pandas-datareader

import math

def senh(x):
    Y = 0.5*((math.e**x)-(math.e**-x))
    return Y
    
senh(50)


def cuadradogaa(numero):
    valor_funcion = numero**2
    return valor_funcion