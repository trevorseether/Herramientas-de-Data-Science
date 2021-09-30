# -*- coding: utf-8

# =============================================================================
# # Importación de PANDAS
# =============================================================================


import pandas as pd
#pip install requests
import requests

# Excel, cancer de mama
cancer_mama = pd.read_excel("breast_cancer.xlsx")
type(cancer_mama) #pandas.core.frame.DataFrame
#argumentos
# io : url a la localización del archivo, (repositorio local o sitio web)
# sheet_name : qué hoja del archivo queremos leer
# header : si el set de datos tiene encabezado de columna

# CSV (coma separated values), titanic y vino rojo
titanic = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
vino_rojo = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
                        sep = ";")
type(titanic) #pandas.core.frame.DataFrame
type(vino_rojo) #pandas.core.frame.DataFrame
# "sep" es para elegir el separador


# JSON - COVID
json_covid = requests.get("https://api.covid19api.com/summary").json()
type(json_covid) #DICCIONARIO
# CONVERTIRMOS DICCIONARIO A PANDA´S DATA FRAME
datos_coronavirus = pd.DataFrame.from_dict(json_covid["Countries"]) #nos pide la clave o "key"

datos_coronavirus.info()
# resumen de las variables, su tipo, y su peso en memoria

vino_rojo.describe()
# Nos sirve para calcular rápidamente algunas medidas de tendencia central y dispersion

# metodos que nos permiten obtener una muestra de nuestro dataframe
cancer_mama.head() #por defecto nos muestra las primeras 5 filas
cancer_mama.head(10) #pero se puede elegir otra cantidad

# para poder visualizar completamente las filas creamos una variable
sample_cancer = cancer_mama.head(10)

# podemos hacer lo mismo pero con tail, que nos muestralas últimas filas
sample_covid = datos_coronavirus.tail(9)

#%%

# =============================================================================
# Acceso a elementos de un DATAFRAME
# =============================================================================

# Shape del dataframe
vino_rojo.shape # nos muestra el número de filas y columnas

# Columnas del data frame
titanic.columns #nos muestra el nombre de las columnas

# Indices del dataframe
titanic.index
type(titanic.index) # tipo rango de indice de pandas dataframe

# Cómo seleccionar una columna
titanic["Name"] # las dos formas te permiten seleccionar una sola columnsa
titanic.Name # COLUMNA DE NOMRBES
nombres = titanic["Name"] # cuando tomamos una sola columna, se convierte en tipo SERIE
nombres_ = titanic.Name # cuando tomamos una sola columna, se convierte en tipo SERIE
type(nombres) # Serie de pandas
# En cambio si seleccionas más de una columna, sigue siendo dataframe

# tambien los datos del vector lo podemos convertir en otro tipo
nombres__ = list(titanic.Name)
nombres__

# Seleccionar varias columnas y reordenar un dataframe
# lista dentro de lista con los nombres de las columnas
# titanic = titanic[['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
       # 'Parents/Children Aboard', 'Fare']]
"Este es el orden predeterminado"
titanic = titanic[[ 'Sex', 'Age', 
                   'Siblings/Spouses Aboard',
                   'Parents/Children Aboard', 
                   'Fare', 'Survived', 'Pclass', 
                   'Name']]

# nos quedamos solo con algunos elementos en un nuevo dataframe
nombre_sexo = titanic[["Name", "Sex"]]

# COMO REASIGNAR LOS INDICES DE UN DATAFRAME
cancer_mama.index = cancer_mama["id"]

cancer_mama.drop(["id"],
                 axis = 1, #axis indica si es columna o fila
                 inplace = True) # esto se usa para que solo dropee id
# axis 1 indica que es columna

#FILTRADO DE COLUMNAS DE UN DATAFRAME
cols_cancer = list(cancer_mama.columns)
cols_cancer.remove("radius_mean")
cancer_mama = cancer_mama[cols_cancer]

# ACCEDER A VALORES ESPECIFICOS DE UN DATAFRAME

# USO DEL LOC
cancer_mama.loc[842302] # nos muestra toda la info según el indice,
# anteriormente convertimos al id en el índice

cancer_mama.loc[842302,"diagnosis"] #solo la info de diagnostico

#para pedir más de una info, debemos empaquetar los datos:

cancer_mama.loc[[842302, 842517]]

titanic_50 = titanic.loc[0:49]
titanic_50_ = titanic.head(50) # ambos son lo mismo

# USO DEL ILOC
datos_coronavirus.iloc[1,0] #segundo elemento, primera columna
datos_coronavirus.iloc[:20,:4] #20 primeras filas, 4 columnas
datos_coronavirus.iloc[-50:-1, -3:-1]

# FILTRANDO DATAFRAMES CON OPERADORES LÓGICOS
calidad_5 = vino_rojo["quality"] == 5 # true o false si es 5 o no
registros_calidad5 = vino_rojo[calidad_5] #se queda solo con la info que tiene calidad 5

calidad_5_6 = (vino_rojo["quality"]==5) | (vino_rojo["quality"]==6)
# | significa "o"
registros_calidad_56 = vino_rojo[calidad_5_6] #se queda solo con los de calidad 5 o 6

#%% 

# =============================================================================
# # Medidas derivadas y aplicación de funciones
# =============================================================================

# Medidas aritméticas para columna/variable/atributo/descriptores
vino_rojo.mean() #media de cada columna
vino_rojo.std() #desviaicón estandar
vino_rojo.median() #mediana

# Conteo de valores en una columna
vino_rojo["quality"].value_counts() #esto solo aplica para columnas, es decir series
titanic["Survived"].value_counts()
cancer_mama["diagnosis"].value_counts() #benigno o maligno

# Creando nuevas columnas derivadas
datos_coronavirus["Deathrate"] = 1 #hemos creado una columna nueva, llena de unos
datos_coronavirus["Deathrate"] = datos_coronavirus["TotalDeaths"] / datos_coronavirus["TotalConfirmed"]
datos_coronavirus.sort_values("Deathrate", ascending = False, inplace = True)

# Aplicando funciones a la medida sobre series(una columna)
titanic["SurvivedLabel"] = titanic["Survived"].map({0:"Murió",1:"Sobrevivió"})
titanic["SurvivedLabel"].value_counts() #contar

series_upper = lambda x: x.upper()
name_upper = titanic["Name"].map(series_upper) #a mayúsculas

name_upper = titanic["Name"].str.upper() #lo mismo pero con función base del python

# Aplicando funciones a la medida sobre dataframes(variascolumnas)
name_sex = titanic[["Name", "Sex"]].applymap(series_upper) #Mayúscula a las 2 columnas

df_lower = lambda x: x.lower() if type(x) == str else x
titanic = titanic.applymap(df_lower)





