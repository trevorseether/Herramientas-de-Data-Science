#%% modulo matplotlib

import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,1]
plt.plot(x,y)

import numpy as np

#%% grafico 1
# construyamos una variables independiente
x = np.linspace(0,10,30)
y = np.sin(x)
plt.plot(x,y)
plt.show()

#%% Grafico 2
x = np.linspace(0,10,30)
y = np.sin(np.sqrt(x))
plt.plot(x,y , '-o')
plt.show()


#%% Grafico 3
x = np.linspace(0,10,30)
y = np.sin(np.sqrt(x))
plt.plot(x,y , '-o')
plt.ylim(-2,2)
plt.xlim(-5,15)
plt.show()


#%%Grafico 4
x = np.linspace(0,10,30)
y = np.sin(np.sqrt(x))
plt.plot(x,y , '-o')
plt.ylim(-2,2)
plt.xlim(-5,15)
plt.xlabel("Variable INdependiente")
plt.ylabel("Variable Dependiente")
plt.title("Funcion de ejemplo")
plt.show()

#%% Grafico 5


x = np.linspace(0,10,30)
y = np.sin(np.sqrt(x))
plt.plot(x,y , '-o')
plt.ylim(-2,2)
plt.xlim(-5,15)
plt.axhline(y= -0.5 ,ls = '--', c = 'r')
plt.xlabel("Variable INdependiente")
plt.ylabel("Variable Dependiente")
plt.title("Funcion de ejemplo")
plt.show()

#%% Grafica 6 

t = np.linspace(-np.pi , np.pi, 50)
y = np.sin(t)
plt.plot(t,y)
plt.axvspan(xmin = -np.pi*0.5,  xmax = np.pi*0.5, alpha = 0.2, facecolor = 'r')
plt.axhspan(ymin = -0.75, ymax = 0.5, facecolor = 'b', alpha= 0.2)
plt.axvline(x = 0, ls = '--', c = 'r')
plt.show()




















