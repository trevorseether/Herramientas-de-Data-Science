# -*- coding: utf-8 "

"Gráfico circular"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches

#%% Ejemplo 1

items = ["Samsung", "Huawei", "Apple", "LG"]
proportions = [4, 2, 3, 5]
colors = ["r", "y", "g", "b"]
plt.pie(proportions, labels = items, colors = colors)
plt.legend(items, loc = "best")
plt.show()

#%%%

items = ["Samsung", "Huawei", "Apple", "LG"]
proportions = [4, 2, 3, 5]
colors = ["r", "y", "g", "b"]
plt.pie(proportions, labels = items, colors = colors,
        startangle = 90, shadow = True, explode = (0.1, 0.3, 0.1, 0.2))
plt.legend(items, loc = "best")
plt.show()

#%%
items = ["Samsung", "Huawei", "Apple", "LG"]
proportions = [4, 2, 3, 5]
colors = ["r", "y", "g", "b"]
plt.pie(proportions, labels = items, colors = colors,
        startangle = 90, shadow = True, explode = (0.1, 0.3, 0.1, 0.2),
        radius = 3.8)
plt.legend(items, loc = "best")
plt.show()

#%%
items = ["Samsung", "Huawei", "Apple", "LG"]
proportions = [4, 2, 3, 5]
colors = ["r", "y", "g", "b"]
plt.pie(proportions, labels = items, colors = colors,
        startangle = 90, shadow = True, explode = (0.1, 0.3, 0.1, 0.2),
        radius = 0.8, autopct = "%1.3f%%")
plt.legend(items, loc = "best")
plt.show()

#%%

items = ["Samsung", "Huawei", "Apple", "LG"]
proportions = [4, 2, 3, 5]
colors = ["r", "y", "g", "b"]
plt.pie(proportions, labels = items, 
        colors = colors,
        startangle = 90, 
        shadow = True, 
        explode = (0.1, 0.3, 0.1, 0.2),
        radius = 0.8, 
        autopct = "%1.3f%%")
plt.legend(items, loc = "best",
           bbox_to_anchor = (1.075, 1.025))
plt.title("Mercado de smartfones", size = 14, y = 1.1)
plt.show()

#%%
items = ["Samsung", "Huawei", "Apple", "LG"]
proportions = [4, 2, 3, 5]
colors = ["r", "y", "g", "b"] # se puede poner los códigos de los colores https://htmlcolorcodes.com/es/
plt.pie(proportions, labels = items, 
        colors = colors,
        startangle = 90, 
        shadow = True, 
        explode = (0.1, 0.3, 0.1, 0.2),
        radius = 0.8, 
        autopct = "%1.3f%%")
plt.legend(items, loc = "upper right",
           bbox_to_anchor = (1.4, 1.025)) #ubicación de el cuadro de legenda
plt.title("Mercado de smartfones", size = 14, y = 1.1)
plt.show()

#%% diagrama de barras

help(plt.bar)
 #bar oara barras verticales
x_units = [1, 2, 3, 4]
y_units = [10, 24, 36, 48]
tick_label = ["XBIT", "VNA", "INVA", "BMAB"]
colors = ["r", "g", "b", "y"]
plt.bar(x_units, y_units, 
        width  =1.2,
        tick_label = tick_label,
        color = colors)
plt.xlabel("Eje X")
plt.xlabel("Eje Y")
plt.title("gRÁFICO DE BARRAS")
plt.show()
     
     
     
#barh para barras horizontales  
x_units = [1, 2, 3, 4]
y_units = [10, 24, 36, 48]
tick_label = ["XBIT", "VNA", "INVA", "BMAB"]
colors = ["r", "g", "b", "y"]
plt.barh(x_units, y_units, 
        height  =0.8,
        tick_label = tick_label,
        color = colors)
plt.xlabel("Eje X")
plt.xlabel("Eje Y")
plt.title("gRÁFICO DE BARRAS")
plt.show()

#%%
# Histograma
#generación de edades aleatorias
ages = np.random.randint(0, 80, 22000)
rango_age = (0,80)
bins = 20
plt.hist(ages, bins, rango_age,
         color = "blue",
         histtype = "bar",
         rwidth = 0.5)
plt.show() 
#%% 
#generación de edades aleatorias
ages = np.random.normal(45,10, 200500)
rango_age = (0,80)
bins = 20
plt.hist(ages, bins, rango_age,
         color = "blue",
         histtype = "bar",
         rwidth = 0.5)
plt.show() 
   #%%
  
ages = np.random.normal(45,10, 200500)
rango_age = (0,80)
bins = 50
plt.hist(ages, 
         bins = bins,
         color = "blue",
         histtype = "bar")
plt.show() 
     
#%%

h1 = np.random.normal(0, 0.8, 1000)
h2 = np.random.normal(-3, 1.2, 1000)
h3 = np.random.normal(4, 0.5, 1000)

kwargs = dict(bins = 40, alpha = 0.5)
plt.hist(h1, **kwargs)
plt.hist(h2, **kwargs)     
plt.hist(h3, **kwargs)
plt.axvline(x = np.mean(h1))
plt.show()

#%%

h1 = np.random.normal(0, 0.8, 1000)
h2 = np.random.normal(-3, 1.2, 1000)
h3 = np.random.normal(4, 0.5, 1000)

kwargs = dict(bins = 40, alpha = 0.5) #aquí están empaquedos los argumentos

plt.hist(h1, **kwargs, color = "g")
plt.hist(h2, **kwargs, color = "r")     
plt.hist(h3, **kwargs, color = "y")
plt.axvline(x = np.mean(h1), c = "g")
plt.axvline(x = np.mean(h2), c = "r")
plt.axvline(x = np.mean(h3), c = "y")
plt.text(x = -6, y = 60, s = "Normales")
plt.show()

#es como poner los argumentos así

h1 = np.random.normal(0, 0.8, 1000)
h2 = np.random.normal(-3, 1.2, 1000)
h3 = np.random.normal(4, 0.5, 1000)


plt.hist(h1, bins = 40, alpha = 0.5, color = "g")
plt.hist(h2, bins = 40, alpha = 0.5, color = "r")     
plt.hist(h3, bins = 40, alpha = 0.5, color = "y")
plt.axvline(x = np.mean(h1), c = "g")
plt.axvline(x = np.mean(h2), c = "r")
plt.axvline(x = np.mean(h3), c = "y")
plt.text(x = -6, y = 60, s = "Normales")
plt.show()

# Mediante métodos de objetos POO
vectorndarray.argmax()

# Mediante 1 función max del módulo numpy: programación estructurada
np.argmax(vecndarray)




