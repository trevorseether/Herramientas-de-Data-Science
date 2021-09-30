# -*- coding: utf-8 -*-
#%% Gráficos con sympy
# Vamos a hacer uso del concepto de submódulos

from sympy import symbols
from sympy.plotting import plot
import math as m

help(symbols)
help(plot)

x = symbols("x")
plot(x*x)

p1 = plot(x**3)
p2 = plot(x)
p3 = plot(m.sin(x)) #error

import sympy as sp
p3 = plot(sp.sin(x))

#%reset
#%% Otros gráficos y opciones

import sympy
from sympy.plotting import plot

x = sympy.symbols("x")
#Generamos un gráfico modificando el dominio
plot(sympy.sin(x**2), (x, -sympy.pi, sympy.pi))

# Dos funciones con el mismo dominio
plot((sympy.sin(x))/x), sympy.cos(sympy.sqrt(x)), (x, -4, 4)

#Graficar dos funciones, cada una con su respectivo dominio

plot((sympy.sin(x), (x, -6, 6)), (sympy.cos(x**2), (x, -3, 3)))

#%% Graficando función con su correspondiente derivada
#cada una con color diferente

import sympy as sp
from sympy.plotting import plot


#Creamos variable independiente como una variable simbólica

x = sp.symbols("x")

#Creamos la variable dependiente

f = sp.exp(x) * sp.sin(2*x)
p1 = f
p2 = sp.diff(f, x)

#Debemeos hacer un plot de ambas funciones
p = plot(p1, p2, (x, 6, 10), show = True)

type(p)

p[0].line_color = "green"
p[1].line_color = "r"

p.show()

#%reset

#%% 


# Funciones Gamma Incompletas
import sympy as sp
sp.init_printing()
 
#dir(sp)
#help(sp.uppergamma)
 
print(sp.uppergamma.__doc__)
 
x = sp.Symbol("x")
 
f = sp.uppergamma(3, x)
f
 
p1 = f
p2 = sp.diff(f, x)
 
 #Graficar la función f y su derivada en dominios diferentes
 #Eligiendo el color para cada uno
p = plot((p1, (x, 1, 5)), (p2, (x , 0, 2)), show = True)



#%% Ploteo en 3D
 
 #Superficies
 
#%reset
 
from sympy import symbols, sqrt, ln, pi
from sympy.plotting import plot3d
x,y = symbols(("x", "y"))
 
 #primera superficie
 
plot3d(x*y, (x, -5, 5), (y, -5, 5))
 
plot3d(15/ ((sqrt(x) + sqrt(y) + 10)**3), (x, -15, 15), (y, -20, 20))
 
plot3d(15/ ((sqrt(x) + sqrt(y) + 10)**3), (x, -15, 15), (y, -20, 20),
         nb_of_points_x = 200,
         nb_of_points_y = 200)

 
plot3d(ln(x) + ln(y), (x, 1, 15), (y, 1, 20))
 
 #Veamos el uso de parámetros para las funciones
h,k = 10, 10
plot3d(-0.5 * (x-h)**2 - -0.5*(y-k)**2 , (x, -5*pi, 5*pi), (y, -5*pi, 5*pi))
 
 #%% Subplots
 
 #%reset
 
from sympy import symbols, sin
from sympy.plotting import plot, plot3d, PlotGrid
x,y = symbols(("x", "y"))
p1 = plot(x, x**2, x**3, (x, -5, 5), show = True)
p2 = plot((x**2, (x, -6, 6)), (x, (x, -5, 5)), show = False)
p3 = plot3d(x**y, (x, -5, 5), (y, -5, 5), show = True)
p4 = plot(sin(x**2), (x, 0, 2), show = False)
p = PlotGrid(2, 2, p1, p2, p3, p4)
 
 
 
 
 
 
 
 
 
 




