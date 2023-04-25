# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:31:51 2023

@author: sanmiguel38
"""

nombre = "Juan"
edad = 30
mensaje = "Hola, mi nombre es {} y tengo {} años".format(nombre, edad)
print(mensaje) # muestra "Hola, mi nombre es Juan y tengo 30 años"


nombre = "Juan"
edad = 30
mensaje = "Hola, mi nombre es %s y tengo %d años" % (nombre, edad)
print(mensaje) # muestra "Hola, mi nombre es Juan y tengo 30 años"

nombre = "Juan"
mensaje = f"Bienvenido, {nombre}!"
print(mensaje)  # muestra "Bienvenido, Juan!"

x = 10
y = 20
resultado = f"La suma de {x} y {y} es {x + y}"
print(resultado)  # muestra "La suma de 10 y 20 es 30"
