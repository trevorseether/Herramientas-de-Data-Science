# -*- coding: utf-8 -*-
# modulo matplotlib

import matplotlib.pyplot as plt

x = [6, 2.3, 3]
y = [2, 4, 1]

plt.plot(x,y)

import numpy as np

#construimos variables independientes
x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x,y)
plt.show()

x = np.linspace(0, 10, 30)
y = np.sin(np.sqrt(x))
plt.plot(x,y, "-o")
plt.ylim(-2, 2)
plt.xlim(-5, 15)
plt.show()


x = np.linspace(0, 10, 30)
y = np.sin(np.sqrt(x))
plt.plot(x,y, "-o")
plt.ylim(-2, 2)
plt.xlim(-5, 15)
plt.xlabel("Variable Independiente")
plt.ylabel("Variable Dependiente")
plt.title("Función de ejemplo")
plt.show()


x = np.linspace(0, 10, 30)
y = np.sin(np.sqrt(x))
plt.plot(x,y, "-o")
plt.ylim(-2, 2)
plt.xlim(-5, 15)
plt.axhline(y = 0.5, xmin = 3, xmax = 7)
plt.xlabel("Variable Independiente")
plt.ylabel("Variable Dependiente")
plt.title("Función de ejemplo")
plt.show()

t = np.linspace(-np.pi , np.pi, 50)
y = np.sin(t)
plt.plot(t, y)
plt.axvspan(xmin = -np.pi*0.5, xmax = np.pi*0.5, alpha = 0.2, facecolor = "r")
plt.axhspan(ymin = -0.75, ymax = 0.5, facecolor = "b", alpha = 0.2)
plt.show()










