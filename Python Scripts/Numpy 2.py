# -*- coding: utf-8 -*-

import numpy as np
help(np.linalg.solve)

A = np.array([[4,3,2], [-2,2,3], [3,-5,2]])
type(A)
dir(A)

b = np.array([25,10,-4])
# Representa un sistema de ecuaciones: Ax = b
# Si la matriz tiene un determinante diferente de cero, se puede hacer un 
# despeje como de 
np.linalg.matrix_rank(A)
#  si el rango de A es igual a 3, es de esperar que la determinante de A,
#  sea diferente de cero
X = np.linalg.inv(A).dot(b)

x1 = np.linalg.solve(A, b) # es lo mismo que pedir que resuelva Ax = b

# opción cuando las matrices no son cuadrados
# se usa mínimos cuadrados, np.linalg.lstsq
help(np.linalg.lstsq)

A = np.array([[1,2,1], [1,1,2], [2,1,1], [1,1,1]])
b = np.array([4,3,5,1])

# x0   + 2*x1  +  x2    = 4
# x0   + x1    +  2*x2  = 3
# 2*x0 + x1    +  x2    = 5
# x0   + x1    +  x2    = 1


x, res, rank, s = np.linalg.lstsq(A, b)
# x es el resultado
# res es el resto
# rank, tamaño del vector resultado?
# s

#%% carga de datos 

"Base de datos"
# C:\Users\Merly\Desktop\data
# C:\Users\Merly\Desktop\TSLA_28062010-13092020

# con magic comandas
# modifiquemos nuestro directorio de trabajo

# no es código de pytohn
%cd "C:\Users\Merly\Desktop" # como en stata 
%pwd # para ver cual es nuestro directorio actual

#%% ahora sí cargando los datos uwu

help(np.loadtxt) # numpy tiene su función para abrir código

data = np.loadtxt("data.csv", delimiter = ",", usecols = (6, 7))
type(data) # el formato es numpy.ndarray
# ultima columna, número de acciones negociadas, lo demás son precios(cierre, apertura, etc)
#primera columna:
c = data[:,0]

#segunda columna:
d = data[:,1]

# promedio de los valores de la variable c (precio)
PrecioPromedio = np.mean(c)

#procediendo a redondear el número anterior
PrecioPromedio = np.round(np.mean(c), decimals = 2)

# Numpy tiene función averge, que permite calcular promedios ponderados

help(np.average)

# calcular promedio ponderado de los valores de c, 
# con pesos en la variable d

# esto tiene el nomn de Promedio ponderado por volumen
prom_pond = np.average(c, weights = d)

# promedio ponderado por el tiempo
t = np.arange(len(c))
prom_pond_t = np.average(c , weights= t)

print(PrecioPromedio)
print(np.round((prom_pond), decimals = 2))
print(prom_pond_t)

#%% la segunda columna si la cargamos, va a ser caracteres
# no lo va a reconocer como fecha

# usaremos el argumento converters para "parsear" los datos de la segunda
# columna a datos de tipo "datetime"

import datetime as dt
def datestr2num(s):
    return dt.datetime.strptime(s, "%d-%m-%Y").date()

ejefecha = datestr2num("20-09-2020")
type(ejefecha)
dir(ejefecha)

ejefecha.day
ejefecha.month
ejefecha.weekday()
ejefecha.year
ejefecha.isoweekday()

# llaves alt + 123 125
fechas, precio = np.loadtxt("data.csv", delimiter = ",",
                            dtype = str,
                            usecols = (1,6),
                            converters = {1:datestr2num},
                            unpack = True)
                            
#%% Vamos a usar pandas para cargar los datos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tesla = pd.read_csv("TSLA_28062010-13092020.csv")
type(tesla)
dir(tesla)

tesla.head()
tesla.tail(n=3)
help(tesla.head)
tesla.info()

#gráfico 1
plt.plot(tesla["Open"])
plt.shoy()

# calculo el vector de diferencias
retornos = np.diff(tesla.Open)
#gráfico 2
plt.plot(retornos)
plt.shoy()

#%% generamos 2 ventanas para dos gráficos

plt.figure(1)
plt.plot(tesla.Open)
plt.tittle("Precios de apertura")

plt.figure(2)
plt.plot(retornos)
plt.tittle("Retornos del precio de apretura")

plt.figure(3)
plt.plot(np.log(retornos))
plt.tittle("Logaritmo de los retornos")
plt.show()

#%% metodo de biseccion
# luego esplicacion grafica , implementemos el algoritmo para calcular
# raices de funciones no lineales

def biseccion(f, a,b , N):
    if(f(a)*f(b) >= 0):
        print("Elmetodo expicado falla")
        print("[a,b] no es el adecuado")
        return None
    a_n = a
    b_n = b
    # empieza la parte repetitiva
    for n in range(1,N+1):
        m_n = (a_n+b_n)/2
        f_m_n = f(m_n)
        if (f(a_n) * f_m_n <0 ):
            a_n =a_n
            b_n = m_n
        elif (f(b_n) * f_m_n <0):
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0.0:
            print("Solucion exacta")
            return m_n
        else:
            print("El metodo de biseccion a fallado")
            return None 
    return (a_n+b_n)/2

#%% Pruebas del metodo en cuestion
# ejemplo 1
f = lambda x : x**2 -x-1
biseccion(f, 0, 10 , 5)

# ejemplo 2 
def func(z):
    return z*z*z -z*z +2
biseccion(func,-200, 300, 50)

# Ejemplo 3 
import math as m 
def fz(t):
    return m.exp(t)*(3.2*m.sin(t) - 0.5*m.cos(t))
biseccion(fz, 0, 10 , 20)

import matplotlib.pyplot as plt
import numpy as np
fz_vect = np.vectorize(fz)
t = np.linspace(0, 10, 120)
y = fz_vect(t)
plt.plot(t, y)
# Grafiquemos una recta horizontal 
plt.hlines(y = 0 , xmin = 0 , xmax =10 , colors = 'red')
plt.show()


# del grafico  puedo inferir que una raiz esta en [6.4,6.5]
biseccion(fz, 6.4, 6.5 , 20)
biseccion(fz, 3.1, 3.5 , 20)

#%% metodo de la secante
    
def secant(f,a,b,N):
    if (f(a)*f(b) >= 0):
        print("el método falla")
        return None
    a_n = a
    b_n = b
    #parte iterativa
    for n in range(1, N+1):
        m_n = a_n - f(a_n) * (b_n - a_n)/(f(b_n) - f(a_n))
        if f(a_n)*f(m_n) < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0.0:
            print("solucion exacta")
            return m_n
        else:
            print("El metodo de la secante falla")
            return None
    return a_n -f(a_n) * (b_n - a_n)/(f(b_n) - f(a_n))

#%% ejemplos 
import math as m 
def fz(t):
    return m.exp(t)*(3.2*m.sin(t) - 0.5*m.cos(t))
secant(fz, 6, 7 , 20)        



#%% scipy

import scipy as scp
x = dir(scp.linalg)

A = scp.linalg.hadamard(4)

#%% scipy 
import scipy as scp
import numpy as np

import matplotlib.pyplot as plt

help(scp.linalg)
dir(scp.linalg)
help(scp.linalg.hadamard)

A = scp.linalg.hadamard(4)

#%% submodulo de intepolacion

# construyamos datos experimentales : a la funcion seno 
# le vamos a agregar un ruido

t = np.linspace(0,1,10)
noise = (np.random.random(10)*2 -1)*1e-1
measures = np.sin(2*np.pi*t) + noise
# interp1d : interpolacion lineal 
linear_interp= scp.interpolate.interp1d(t,measures)
type(linear_interp)
dir(linear_interp)
linear_interp.axis
linear_interp.bounds_error
linear_interp.x

interpolation_time = np.linspace(0,1,50)
linear_results = linear_interp(interpolation_time)


# construyamos una interpolacion cubica
cubic_interp = scp.interpolate.interp1d(t, measures, kind = 'cubic')
cubic_results = cubic_interp(interpolation_time)


# grafiquemos 
plt.figure(figsize = (16,9))
plt.plot(t, measures, '*g' , label = "Data")
plt.plot(interpolation_time, linear_results, '--b' , label ='Interp. Lineal')
plt.plot(interpolation_time, cubic_results,'-r' , label = 'Interp. Cubica')
plt.legend()
plt.show()

help(scp.interpolate.interp1d)
help(scp.interpolate.interp2d)

#%% modulo de interpolación

# cosntruimos datos experimentales: a la función seno
# le vamos a agregar ruido

t = np.linspace(0,1,10)
noise = (np.random.random(10)*2-1)*1e-1
measures = np.sin(2*np.pi*t) + noise

#interp1d : interpolación lineal
linear_interp = scp.interpolate.interp1d(t, measures)
type(linear_interp)
dir(linear_interp)
linear_interp.axis
linear_interp.bounds_error
linear_interp.x


interpolation_time = np.linspace(0, 1, 50)
linear_results = linear_interp(interpolation_time)

# construimos una interpolación cúbica
cubic_interp = scp.interpolate.interp1d(t, measures, kind = "cubic")
cubic_results = cubic_interp(interpolation_time)


# grafiquemos
plt.figure(figsize = (16, 9))
plt.plot(t, measures, "*g", label = "Data")
plt.plot(interpolation_time, linear_results, "--b", label = "Interpolación lineal")
plt.plot(interpolation_time, cubic_results, "-r", label = "Interpolación cúbica")
plt.legend()
plt.show()


scp.__version__















