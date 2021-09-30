import math
#help(mt)

math.sin(50)
#COMANDO dir TE MUESTRA LOS METODOS DE UNA LIBRERÍA


#--------------------------------------------------------------
#ESTRUCTURAS DE DATOS BÁSICAS EN PYTHON
#--------------------------------------------------------------
"............................................................................."
#LISTAS: colecciones ordenadas, no indexadas, mutables(Homólogo a vector)
"............................................................................."

"ASÍ COMO PARA DEFINIR UN STRING SIEMPRE USAMOS COMILLAS"
"PARA UNA LISTA SIEMPRE USAREMOS CORCHETES"
"CADA ELEMENTO DEBE ESTAR SEPARADO POR COMAS"
"""DENTRO DE UNA LISTA PODEMOS MEZCLAR DIFERENTES TIPOS DE VARIABLES, STRING,
ENTEROS, BOOLEANOS, FLOATS, DATAFRAMES, OTRAS LISTAS, TUPLAS, SETS, DICCIONARIOS ETC ETC"""
lista1 = [3, 1, 2, "Alexandra", [True, False, True]] #dar click en el explorador de variables
"hacer referencia a un objeto de la lista"
#INDICES:             0     1    2     3   4    ......
#INDICES NEGATIVOS:   .......     -4    -3    -2    -1
lista1[3]
lista1[-1]
"Para acceder a más de un elemento, hacemos slicing"
lista1[0:3] #limite superior de las listas no es inclusivo
#hacemos referencia a una posición posterior
lista1[2:]
lista1[-2:]
lista1[:-0]
lista1[2] = 55
lista1[4][2]
lista1[4][1:]
del(lista1[2:])

sorted(lista1) #va a arrojar error
del(lista1[3:])
sorted(lista1)
#reasignación
#sorted(lista1) = lista1 
#error

lista1 = sorted(lista1)
sorted(lista1, reverse = True)
fg = [3, 33, 21]
fg = sorted(fg, reverse = True)


#Agregar un nevo valor a la lista (.append)
lista1[3] = 5 #no se puede agregar si el indice no existe

lista1.append(x)

lista1.append([33, 34, 50, True, "joven"])

"............................................................................."
#TUPLAS: colecciones ordenadas, no indexadas, INMUTABLES
"............................................................................."
"Muy similar a las listas, pero no se pueden modificar sus elementos"
"ASÍ COMO LOS CORCHETES DEFINEN A LAS LISTAS, LOS PARÉNTESIS DEFINEN A LAS TUPLAS"
tupla1 = (True, False, 1, 2, [33, 45], (1), (0, "True"))
tupla1[3]
tupla1[0] = False
del(tupla1[-1])
tupla1.append([33, 34, 50,  True, "joven"]) #no tiene atributo append

"............................................................................."
#SETS:colecciones NO ordenadas, no indexadas, mutables, QUE NO ADMITEN DUPLICADOS
"............................................................................."
"no permiten elementos duplicados a diferencia de las listas y tuplas"
"se definen por llaves { o }"
"no tienen indice, se llama a sus elemtnos por el nombre"
set1 = {1, 5, 6, 8, 8, 9}
set1[1]  #no funciona
set1.add(4) #agregar un solo elemento
set1.update([1, 2, 3, 4, 5])
set1.discard(1) 

"............................................................................."
#DICCIONARIOS:colecciones NO ordenadas, INDEXADOS, mutables, QUE NO ADMITEN DUPLICADOS
"............................................................................."
"están compuestos por pares indices o keys, y también se definen por llaves"
carro = {"marca":"ford", "modelo":"mustang", "año":"1969"}
type(carro)
carro.get("modelo")
carro.keys() #para saber qué indices o keys tenemos
carro. values() #para ver los elementos dentro del diccionario
carro.update({"color":"rojo"})

lista_marcas= ["ford", "audi", "cheverolet"]
carro2 = {"MARCAS": lista_marcas}
carro2.update({"color": ["rojito", "verdecito", "amarillito"] })

"----------------------------------------------------------------------------"
dir(fg)

metfg = dir(fg) # ahora podemos ver todos los métodos que se le pueden aplicar a 
#las listas
type(metfg) #es lista :o

help(list.append)
help(list.sort) #aquí podemos detallar un poco cada método

x = []

x = ()
dir(x)
mt.sqrt(9)

import sympy
#%%






















