# -*- coding: utf-8 -*-
#%% LIBRERÍA PANDAS,
#SOFTWARE LIBRE DE CÓDIGO ABIERTO

#dos estructuras de datos, data frame y series,
#este módulo fue contruido en base a numpy

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random as rnd
import math as m

# Pandas proporciona dos estructuras de datos: Series, DataFrame
# ------------- 
# SERIES
# -------------
# Array etiquetado de una dimensión, capaz de contener datos de cualquier tipo
# La etiqueta del único eje se llama INDEX, analógicamente es una columna de excel
s = pd.Series(np.random.randn(4), name = "Retornos diarios")
s
type(s)
# pandas.core.series.Series
dir(s)
help(s.to_excel)

#Operaciones vectorizadas
s
s*100
E_s = np.exp(s) #la exponencial de cada uno de los componentes
Abs_s = np.abs(s)  #valores absolutos
print(s)
print(E_s)
print(Abs_s)

s.describe() #nos da un conjunto de indicadores estadísticos:
"""cuantos elementos son, media, desviacion estandar,
mínimo, primer cuartil, segundo cuartil, tercer cuartil, máximo"""

# 1era componenete
s[0]
s[1:3] #segunda y tercera componenete

# El manejo de indices es bastante flexible
s.index = ["AMZN", "APPL", "MSFT", "GOOG"]
s

# Comportamiento similar a un diccionario
s["AMZN"]

s["AMZN"] = np.pi**2
s

#tambien podemos preguntar si el elemento está en la serie

"AAPL" in s #el resultado es True o False

#%%

# =============================================================================
# Cargamos datos
# =============================================================================

# pwt9.1

pwt91 = pd.read_excel("pwt91.xlsx", sheet_name = "Data") #los sheets son la hoja de cálculo en excel

# se puede setear una de las columnas como índice
pwt91 = pd.read_excel("pwt91.xlsx", sheet_name = "Data", index_col = 0) 


# Cargamos otro dato: ticker_data.csv

portafolio1 = pd.read_csv("ticker_data.csv", index_col = "Date",
                          parse_dates = True) #debemos agregar el parse_dates por las fechas
type(portafolio1)
dir(portafolio1)

#%% Obteniendo información de los dataframes

# Información de las columnas del objeto de tipo DataFrame
type(pwt91.columns)
pwt91.columns[0:5] 

pwt91.index
pwt91.info()

#  notación de l a PCO
pwt91.i_cig

# notación vectorial
pwt91["i_cig"]

# porcentaje de datos faltantes
pwt91.isnull().sum()/len(pwt91)*100

# ordenando las columnas por número de elementos faltantes:
pwt91.isnull().sum().sort_values(ascending = False) #de mayor a menor 

# dropna, considerar aquellas columnas que tienen un máximo número de N.A.
help(pwt91.dropna)
# luego de leer me interesan los argumentos de axis y thresh
pwt912 = pwt91.dropna(axis = "columns", thresh = 5000) #elimina columnas con 5000NA o menos

# Información del portafolio 1
portafolio1.head() #los primeros 5 elementos
portafolio1.tail(n = 10) # los últimos 10 elementos de mi portafolio
portafolio1.info()
portafolio1.dtypes

# veamos lo relacionado al conjunto de índices de la variable portafolio1
portafolio1.loc["2013-01"] #información de todo enero

portafolio1.loc["2013-11"] #información de noviembre

# otra forma
portafolio1.loc["November, 2013"]
portafolio1.loc["2013-Nov"]
portafolio1.loc["2013-11"]

portafolio1.loc["2013-jul-15"].describe()

dir(portafolio1.loc["2013"])

portafolio1.loc["2013"]. count()

# rango de fechas
portafolio1.loc["2013-01-01" : "2013-06-15"]

#%% Food_Preference
df = pd.read_csv("https://raw.githubusercontent.com/robintux/Datasets4StackOverFlowQuestions/master/Food_Preference.csv",
                 index_col = 0,
                 parse_dates = True) #parse dates es para que reconozca las fechas

df.head()
df.info()

df.index[1]
type(df.index[1])
help(df.index[1].day)

df.index[1].day
df.index[1].day_name()
df.index[1].month
df.index[1].min
df.index[1].minute
df.index[1].month_name()
df.index[1].hour
df.index[1].second

# se pueden crear nuevas variables con la info de timestamp(datetime)
df["Año"] = df.index.year #le agregamos una nueva columna de solo el año
df["Mes"] = df.index.month_name()
df["Día"] = df.index.day
df["Hora"] = df.index.hour
df["minuto"] = df.index.minute
df["segundo"] = df.index.second
df["NomDía"] = df.index.day_name()

# metodo resample: controlamos la conversión de la frecuencia
# resumen mensual para portafolio 1
portafolio1.resample("M").mean() #promedio
df.resample("D").mean() #promedio por día

#%% tópicos de visualización

#conseguir datos
sns.get_dataset_names()

anagramas = sns.load_dataset("anagrams")
anscombee = sns.load_dataset("anscombe")
cerebro = sns.load_dataset("brain_networks")
choqueasautos = sns.load_dataset("car_crashes")
titanic = sns.load_dataset("titanic")
tips =  sns.load_dataset("tips")
iris = sns.load_dataset("iris")
vuelos = sns.load_dataset("flights")

#%% visualización: matplotlib + seaborn

# conjuntos de estilos de matplotlib y seaborn
# para visualizar nuestros datos
plt.style.available # nos muestra estilos disponibles

# graficos de distribución
#  distplot : perteneciente a seaborn

# veamos algunos graficos del dataframetips
tips.columns
# seteamos / configuramos que estilo(theme) vamos a usar
plt.style.use("ggplot")
sns.distplot(tips["total_bill"])
plt.show()

plt.style.use("classic")
sns.distplot(tips["total_bill"])
plt.show()

plt.style.use("tableau-colorblind10")
sns.distplot(tips["total_bill"], bins = 30,
             kde = True) #kde es la linea de la distribución
plt.show()

#%% joinplot
plt.style.use("tableau-colorblind10")
sns.jointplot(x = "total_bill", y= "tip", data = tips)
plt.show()

plt.style.use("seaborn-whitegrid")
sns.jointplot(x = "total_bill", y= "tip", data = tips,
              kind = "hex")
plt.show()

plt.style.use("tableau-colorblind10")
sns.jointplot(x = "total_bill", y= "tip", data = tips,
              kind = "kde")
plt.show()

plt.style.use("seaborn-whitegrid")
sns.jointplot(x = "total_bill", y= "tip", data = tips,
              kind = "reg")
plt.show()

#%% pairplot

sns.pairplot(tips) #matriz de graficos, sina rgumentos

sns.pairplot(tips, hue = "smoker")
plt.show()














































































































