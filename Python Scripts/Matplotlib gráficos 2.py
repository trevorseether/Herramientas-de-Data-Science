# -*- coding: utf-8 -*-
# =============================================================================
# Matplotlib (gráficas 2d)
# Numpy
# =============================================================================
#%%
import matplotlib.pyplot as plt
import numpy as np

#%%Ejemplo 1
# Definamos la variable independiente

x = np.linspace(-5, 15, 120)

# Para cualquier objeto de python
type(x)
dir(x)
help(x.tofile)

# Definamos variables dependientes

y1 = np.sin(x**(1/7))
y2 = np.exp(-x**2)

plt.plot(x, y1, x, y2)
plt.axvline(x = 0, c = "r") #rayita roja
plt.axvspan(xmin = 0, xmax = 15, alpha = 0.2) #sombreado, alpha es transparencia
plt.show()

#%% Ejemplo2 

y3 = np.sin(x)
plt.plot(x, y3)
 # Hagamos algunas anotacones de texto en una determianada coordenada:
plt.text(x = np.pi, y = 0, s = "y=0", c = "r")
plt.text(x = np.pi, y = 0, s = "ejemplooo", c = "r")
#%% Ejemplo 3

#Colocar una flecha para señalar el punto más alto
plt.plot(x, y3)
plt.annotate("Max1", xy = (np.pi/2, 1),
             xytext = (np.pi/2 +1, 1),
             c = "r",
             arrowprops = dict(arrowstyle = "->", 
            connectionstyle = "arc3",
            color = "r"))

plt.plot(x, y3)
plt.annotate("Max2", xy = (np.pi*2.5, 1),
             xytext = (np.pi*2.5 +1, 1),
             c = "g",
             arrowprops = dict(arrowstyle = "->", 
            connectionstyle = "arc3",
            color = "g"))

plt.show()

#%% Mostrar dos funciones con su leyenda

plt.plot(x, y1, label = "Función y1")
plt.plot(x, np.sin(y2), label = "Función y2")
plt.legend(loc = "center right", frameon = False)
plt.show()

#%%

plt.plot(x, y1, label = "Función y1")
plt.plot(x, np.sin(y2), label = "Función y2")
plt.legend(loc = "lower center", frameon = False, ncol = 2)
plt.ylim(-0.3, 1.2)
plt.show()

#%%

plt.plot(x, y1)
plt.plot(x, np.sin(y2))
plt.legend(["Funcion"])
plt.ylim(-0.3, 1.2)
plt.show()

#%% tamaños y colores para graficar otras dimensiones
#generamos 4 variables
#2 dependientes y 2 independientes

x1 = np.random.rand(100)
y4 = np.random.rand(100)
colors = np.random.rand(100)
size = 100*np.random.rand(100)

plt.scatter(x1, y4, c = colors, s = size, alpha = 0.5, cmap = "viridis")
plt.colorbar()
plt.show()

#%% Caracteres matemáticos en los labels o donde sea

#Modificar ciertas propiedades de compilación propias de latex
#plt.rc("text", usetex = True)
#plt.rc("font", family = "serif")
x2 = ["análsisi real", "análisis numérico", "procesos estocásticos"]
y1 = [95, 88, 45]
plt.plot(x2, y1, label = "Sargent")

y2 = [67, 45, 56]
plt.plot(x2, y2, label = "Romer")

y3 = [27, 67, 90]
plt.plot(x2, y3, label = "Lucas")

plt.xlabel("Cursos")
plt.ylabel(r"Indicador: $/chi$")
plt.title("3 Funciones - 1 Gráfico")
plt.leyend()
plt.show()















