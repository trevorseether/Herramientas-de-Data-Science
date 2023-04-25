# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:37:47 2023

@author: sanmiguel38
"""
#############################
#   reporte para sentinel   #
#############################
#ESTE ES EL REPORTE QUE NOS PASA DENISSE

#%% módulos necesarios
import pandas as pd
import os
import pyodbc
#import numpy as np

#%%
#añadiendo nro de fincore al reporte de sentinel
conn = pyodbc.connect('DRIVER=SQL Server;SERVER=(local);UID=sa;Trusted_Connection=Yes;APP=Microsoft Office 2016;WSID=SM-DATOS')


########################################################
###  donde dice @fechacorte se debe poner el mes  ######
########################################################

#extraemos una tabla con el NumerodeCredito18 y ponemos fecha de hace 2 meses (para que jale datos de 2 periodos)
df_fincore = pd.read_sql_query('''declare @fechacorte datetime
set @fechacorte = '20230331' 

select NumerodeCredito18, Nro_Fincore from anexos_riesgos2..Anx06_preliminar

where FechaCorte1 = @fechacorte
''', conn)

#%%
#ALTERNATIVO SOLO POR SI ESTE REPORTE LLEGA ANTES QUE EL ANX06
#necesitamos un excel del anexo06 que tenga dos columnas, el nro de crédito18 y el nro_fincore
#lo podemos obtener a partir del ampliado que nos pasa Cesar y no tiene ningún error


os.chdir("C:\\Users\\sanmiguel38\\Desktop\\sentinel\\FEBRERO")
#ALTERNATIVO SOLO POR FEBRERO
df_fincore = pd.read_excel('CRED 18 FINCORE.xlsx',
                           dtype={'Numero de Crédito 18/': object, 
                                  'fincore': object})

df_fincore = df_fincore.rename(columns={'Numero de Crédito 18/': 'NumerodeCredito18'})
df_fincore = df_fincore.rename(columns={'fincore': 'Nro_Fincore'})


#%%

#eliminamos las filas duplicadas
df_fincore = df_fincore.drop_duplicates(subset=['NumerodeCredito18'], keep='first')

#%%
#eliminando posibles espacios en las columnas de los códigos
df_fincore['NumerodeCredito18'] = df_fincore['NumerodeCredito18'].str.strip()
df_fincore['Nro_Fincore'] = df_fincore['Nro_Fincore'].str.strip()

#%%

#importamos el archivo sentinel bruto, que nos manda Denisse
os.chdir("C:\\Users\\sanmiguel38\\Desktop\\sentinel\\2023 MARZO") #aqui se cambia la ubicación

df_sentinel=pd.read_excel("SM_0323 - SENTINEL-EXPERIAN CART VIGENTE Y VENCIDA - MARZO-23.xlsx",    # aqui se cambia el nombre del archivo si es necesario
                  dtype={
'''Fecha del
Periodo
(*)''': object, 
'''Codigo
Entidad
(*)''': object,
'''Tipo
Documento
Identidad (*)''': object,
'''N° Documento
Identidad (*)  DNI o RUC''' : object,
'''Tipo Persona (*)''': object,
'''Modalidad de Credito (*)''': object})

df_sentinel.dropna(subset=['Cod. Prestamo', 
                   '''N° Documento
Identidad (*)  DNI o RUC''',
                   'Razon Social (*)',
                   'Apellido Paterno (*)'], inplace=True, how='all')

#%% avales
# en la misma ubicación que tenemos el archivo en bruto, debemos poner los avales
# estos avales los sacamos del Fincore con los siguientes botones:
# REPORTES / CREDITO /PRESTAMOS OTORGADOS / REGISTRO DE AVALES Y-O GARANTÍAS 
ruta = "Rpt_Avales.xlsx"
df1=pd.read_excel(ruta,
                  dtype={'''Nro Docto
Aval''': object,
                            '''Nro Docto
Socio''': object,
'Numero':object},
                     skiprows=8)

df1.columns

#%%
#realizamos la suma horizontal
#primero para MN

mask = df_sentinel['MN Deuda Directa Cobranza Judicial (*)'] > 0
df_sentinel.loc[mask, 'MN Deuda Directa Cobranza Judicial (*)']    = \
    df_sentinel.loc[mask, 'MN Deuda Directa Cobranza Judicial (*)'] + \
    df_sentinel.loc[mask, 'MN Deuda Directa Vencida > 30 (*)']      + \
    df_sentinel.loc[mask, 'MN Deuda Directa Venvida < = 30 (*)']    + \
    df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']
df_sentinel.loc[mask, 'MN Deuda Directa Vencida > 30 (*)']    = 0
df_sentinel.loc[mask, 'MN Deuda Directa Venvida < = 30 (*)']  = 0
df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']    = 0
df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']         = 0

    
mask = df_sentinel['MN Deuda Directa Vencida > 30 (*)'] > 0
df_sentinel.loc[mask, 'MN Deuda Directa Vencida > 30 (*)']    = \
    df_sentinel.loc[mask, 'MN Deuda Directa Vencida > 30 (*)']      + \
    df_sentinel.loc[mask, 'MN Deuda Directa Venvida < = 30 (*)']    + \
    df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)'] 
df_sentinel.loc[mask, 'MN Deuda Directa Venvida < = 30 (*)']  = 0
df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']    = 0
df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']         = 0

mask = df_sentinel['MN Deuda Directa Venvida < = 30 (*)'] > 0
df_sentinel.loc[mask, 'MN Deuda Directa Venvida < = 30 (*)']       = \
    df_sentinel.loc[mask, 'MN Deuda Directa Venvida < = 30 (*)']    + \
    df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']
df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']    = 0
df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']         = 0
    
mask = df_sentinel['MN Deuda Directa Refinanciada (*)'] > 0
df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']         = \
    df_sentinel.loc[mask, 'MN Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']    
df_sentinel.loc[mask, 'MN Deuda Directa Vigente (*)']         = 0
    
#%%
#realizamos la suma horizontal para ME
mask = df_sentinel['ME Deuda Directa Cobranza Judicial (*)'] > 0
df_sentinel.loc[mask, 'ME Deuda Directa Cobranza Judicial (*)']    = \
    df_sentinel.loc[mask, 'ME Deuda Directa Cobranza Judicial (*)'] + \
    df_sentinel.loc[mask, 'ME Deuda Directa Vencida > 30 (*)']      + \
    df_sentinel.loc[mask, 'ME Deuda Directa Venvida < = 30 (*)']    + \
    df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']
df_sentinel.loc[mask, 'ME Deuda Directa Vencida > 30 (*)']    = 0
df_sentinel.loc[mask, 'ME Deuda Directa Venvida < = 30 (*)']  = 0
df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']    = 0
df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']         = 0
    
mask = df_sentinel['ME Deuda Directa Vencida > 30 (*)'] > 0
df_sentinel.loc[mask, 'ME Deuda Directa Vencida > 30 (*)']    = \
    df_sentinel.loc[mask, 'ME Deuda Directa Vencida > 30 (*)']      + \
    df_sentinel.loc[mask, 'ME Deuda Directa Venvida < = 30 (*)']    + \
    df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)'] 
df_sentinel.loc[mask, 'ME Deuda Directa Venvida < = 30 (*)']  = 0
df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']    = 0
df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']         = 0

mask = df_sentinel['ME Deuda Directa Venvida < = 30 (*)'] > 0
df_sentinel.loc[mask, 'ME Deuda Directa Venvida < = 30 (*)']       = \
    df_sentinel.loc[mask, 'ME Deuda Directa Venvida < = 30 (*)']    + \
    df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']
df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']    = 0
df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']         = 0
    
mask = df_sentinel['ME Deuda Directa Refinanciada (*)'] > 0
df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']         = \
    df_sentinel.loc[mask, 'ME Deuda Directa Refinanciada (*)']      + \
    df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']    
df_sentinel.loc[mask, 'ME Deuda Directa Vigente (*)']         = 0
    

#%%
# colocamos todos los valores en la columna de MN,
# y ponemos ceros en las columnas ME
df_sentinel['MN Deuda Directa Cobranza Judicial (*)'] = df_sentinel['MN Deuda Directa Cobranza Judicial (*)'] + \
    df_sentinel['ME Deuda Directa Cobranza Judicial (*)']
df_sentinel['ME Deuda Directa Cobranza Judicial (*)'] = 0

df_sentinel['MN Deuda Directa Vencida > 30 (*)'] = df_sentinel['MN Deuda Directa Vencida > 30 (*)'] + \
    df_sentinel['ME Deuda Directa Vencida > 30 (*)']
df_sentinel['ME Deuda Directa Vencida > 30 (*)'] = 0

df_sentinel['MN Deuda Directa Venvida < = 30 (*)'] = df_sentinel['MN Deuda Directa Venvida < = 30 (*)'] + \
    df_sentinel['ME Deuda Directa Venvida < = 30 (*)']
df_sentinel['ME Deuda Directa Venvida < = 30 (*)'] = 0

df_sentinel['MN Deuda Directa Refinanciada (*)'] = df_sentinel['MN Deuda Directa Refinanciada (*)'] + \
    df_sentinel['ME Deuda Directa Refinanciada (*)']
df_sentinel['ME Deuda Directa Refinanciada (*)'] = 0

df_sentinel['MN Deuda Directa Vigente (*)'] = df_sentinel['MN Deuda Directa Vigente (*)'] + \
    df_sentinel['ME Deuda Directa Vigente (*)']
df_sentinel['ME Deuda Directa Vigente (*)'] = 0

#%%
# ponemos ceros a las columnas donde van los montos de los avales
df_sentinel['MN Deuda Indirecta (avales,cartas fianza,credito) (*)'] = 0
df_sentinel['MN Deuda Avalada (*)'] = 0

#%%
#para concatenar las columnas, nos quedamos con un archivo que solo servirá para el merge

#aqui estamos creando una columna que va a tener el nombre del aval + el numero del crédito,
#servirá para quedarnos con los valores únicos, ya que se repiten los avales en algunos casos
df1['concatenacion'] = df1['Aval'].apply(str) + ' ' + df1['Numero'].apply(str)

#creamos un nuevo dataframe solo con estas columnas
df1_filtrado = df1[['''Nro Docto
Aval''','Aval', 'Numero','''Nro Docto
Socio''', 'concatenacion']]

#le cambiamos de nombre a dos columnas
df1_filtrado = df1_filtrado.rename(columns={'''Nro Docto
Aval''': 'Dni - Asociado - indirecta2'})
df1_filtrado = df1_filtrado.rename(columns={'''Nro Docto
Socio''': 'dni socio'})

#eliminamos las filas duplicadas en función de la columna 'concatenación'
valores_unicos = df1_filtrado.drop_duplicates(subset='concatenacion', keep='first')

#creamos la columna fincore en función del nro de crédito en la columna 'Numero',
#la cual tiene texto en el siguiente formado: '01-00079529' y nos quedaremos con '00079529'
valores_unicos.loc[:, 'fincore'] = valores_unicos['Numero'].str.split('-').str[1]

#eliminamos las filas donde haya NAN en las columnas 'Dni - Asociado - indirecta2' y 'Aval'
valores_unicos = valores_unicos.dropna(subset=['Dni - Asociado - indirecta2', 'Aval'])

#valores_unicos['fincore']

#%% merge que servirá para poner numero de fincore al reporte de sentinel (solo tiene credito18)
'aqui está el problema'
'aqui está el gran problema'

#tenemos una columna que tiene esta estrucutra de datos '00000007-00099116'
#lo que hacemos es quedarnos con la segunda parte, que corresponde con el nro de crédito
df_sentinel.loc[:, 'credito18'] = df_sentinel['Cod. Prestamo'].str.split('-').str[1]

#aqui le quitamos posibles espacios vacíos en el nombre
df_sentinel['credito18'] = df_sentinel['credito18'].str.strip()

#ahora que tenemos el número de crédito 18, le hacemos un merge con la columna fincore
df_sentinel_fincore = df_sentinel.merge(df_fincore, ##########################################################
                         left_on=['credito18'], 
                         right_on=['NumerodeCredito18']
                         ,how='left')

#df_sentinel_fincore.columns
#df_sentinel_fincore.to_excel('333.xlsx', index=False)

#PARA VER ALGUNAS COSAS
#df_fincore[df_fincore['NumerodeCredito18'] == '004663']

#%%

#codigo para verificar que haya habido un match completo
df_sentinel_fincore.loc[df_sentinel_fincore['Nro_Fincore'].isna()]
#si sale Empty DataFrame significa que hizo el match correctamente

#%%
'todo bien actualmente'
#hacemos un merge que solo nos dejará con la tabla de avales
df_resultado = df_sentinel_fincore.merge(valores_unicos, 
                         left_on=['Nro_Fincore'], 
                         right_on=['fincore']
                         ,how='inner')

#%%
#
#
#ESTA ES LA PARTE EN LA QUE ARREGLAMOS EL DNI DEL AVAL, CREO QUE AQUÍ TAMBIÉN DEBERÍAMOS PONER
#LOS DATOS PERSONALES DE LOS AVALES CUANDO TENGAMOS ESE REPORTE
#
#
df_resultado['''N° Documento
Identidad (*)  DNI o RUC'''] = df_resultado['Dni - Asociado - indirecta2']


#%%
#'creación de excels para hacer una revisada'
#df_resultado.to_excel('111.xlsx', index=False)
#valores_unicos.to_excel('222.xlsx', index=False) #aqui no hay problema
#df_sentinel_fincore.to_excel('333.xlsx', index=False)
#%%
#a esta tabla de avales le ponemos 3 en 'Tipo Persona (*)'
df_resultado['Tipo Persona (*)'] = '3'

#df_resultado = df_resultado.drop_duplicates(subset=['Cod. Prestamo', '''N° Documento
#Identidad (*)  DNI o RUC'''], keep='first')



#%%
#colocamos el monto de la deuda en la columna 'MN Deuda Avalada (*)'
df_resultado['MN Deuda Avalada (*)'] = df_resultado['MN Deuda Directa Vigente (*)'] + \
                                       df_resultado['MN Deuda Directa Refinanciada (*)'] + \
                                       df_resultado['MN Deuda Directa Venvida < = 30 (*)'] + \
                                       df_resultado['MN Deuda Directa Vencida > 30 (*)'] + \
                                       df_resultado['MN Deuda Directa Cobranza Judicial (*)']
df_resultado['MN Deuda Directa Vigente (*)']           = 0
df_resultado['MN Deuda Directa Refinanciada (*)']      = 0
df_resultado['MN Deuda Directa Venvida < = 30 (*)']    = 0
df_resultado['MN Deuda Directa Vencida > 30 (*)']      = 0
df_resultado['MN Deuda Directa Cobranza Judicial (*)'] = 0


#%% ordenando
columnas = ['Fecha del\nPeriodo\n(*)', 'Codigo\nEntidad\n(*)', 'Cod. Prestamo',
       'Tipo\nDocumento\nIdentidad (*)',
       'N° Documento\nIdentidad (*)  DNI o RUC', 'Razon Social (*)',
       'Apellido Paterno (*)', 'Apellido Materno (*)', 'Nombres (*)',
       'Tipo Persona (*)', 'Modalidad de Credito (*)',
       'MN Deuda Directa Vigente (*)', 'MN Deuda Directa Refinanciada (*)',
       'MN Deuda Directa Venvida < = 30 (*)',
       'MN Deuda Directa Vencida > 30 (*)',
       'MN Deuda Directa Cobranza Judicial (*)',
       'MN Deuda Indirecta (avales,cartas fianza,credito) (*)',
       'MN Deuda Avalada (*)', 'MN Linea de Credito (*)',
       'MN Creditos Cartigados (*)', 'ME Deuda Directa Vigente (*)',
       'ME Deuda Directa Refinanciada (*)',
       'ME Deuda Directa Venvida < = 30 (*)',
       'ME Deuda Directa Vencida > 30 (*)',
       'ME Deuda Directa Cobranza Judicial (*)',
       'ME Deuda Indirecta (avales,cartas fianza,credito) (*)',
       'ME Deuda Avalada (*)', 'ME Linea de Credito (*)',
       'ME Creditos Cartigados (*)', 'Calificación(*)',
       'N° de Días Vencidos o Morosos ( * )', 'Dirección', 'Distrito',
       'Provincia', 'Departamento', 'Telefono', 'Estado',
       'Fecha de Vencimiento (*)']

df_avales = df_resultado[columnas]

df_sentinel = df_sentinel[columnas]

#%%
# ahora vamos a asignar el monto de la columna 'MN Deuda Avalada (*)' al reporte original

df_avales_copia = df_avales.copy()
df_avales_copia = df_avales_copia.drop_duplicates(subset='Cod. Prestamo', keep='first')
df_avales_reducido = df_avales_copia[['Cod. Prestamo', 'MN Deuda Avalada (*)']]
df_avales_reducido = df_avales_reducido.rename(columns={'Cod. Prestamo': 
                                                        'Cod. Prestamo_avales'})
df_avales_reducido = df_avales_reducido.rename(columns={'MN Deuda Avalada (*)': 
                                                        'MN Deuda Avalada (*)_avales'})


#hacemos el merge para asignar esa columna al otro
df_sentinel_avales = df_sentinel.merge(df_avales_reducido, ##########################################################
                         left_on=['Cod. Prestamo'], 
                         right_on=['Cod. Prestamo_avales']
                         ,how='left')

df_sentinel_avales['MN Deuda Avalada (*)_avales'].fillna(0, inplace=True)
df_sentinel_avales['MN Deuda Avalada (*)'] = df_sentinel_avales['MN Deuda Avalada (*)_avales']

#%%
#antes de la unión, eliminamos posibles espacios en blanco porque los he detectado

'este código lo he comentado porque por alguna razón eliminaba el dni :c'
#df_sentinel_avales['''N° Documento
#Identidad (*)  DNI o RUC'''] = df_sentinel_avales['''N° Documento
#Identidad (*)  DNI o RUC'''].str.strip()


df_avales['''N° Documento
Identidad (*)  DNI o RUC'''] = df_avales['''N° Documento
Identidad (*)  DNI o RUC'''].str.strip()

#%%

'aqui tenemos que modificar la columna de los avales de la MN Deuda Avalada (*), porque aquí debe ir todo, incluyendo los saldos castigados'

df_avales['MN Deuda Avalada (*)'] = df_avales['MN Deuda Avalada (*)']  + df_avales['MN Creditos Cartigados (*)']
df_avales['MN Creditos Cartigados (*)'] = 0

#%%
'hasta aquí ya está todo lo numérico, solo falta reemplazar los datos personales de los avales'

#%%
#unimos todo

reporte = pd.concat([df_sentinel_avales,df_avales], ignore_index=True)

#%%
#hay dos columnas al final que debemos eliminar
reporte.drop(["Cod. Prestamo_avales"], axis=1, inplace=True)
reporte.drop(["MN Deuda Avalada (*)_avales"], axis=1, inplace=True)

#%%
#Arreglando la columna final de fechas de vencimiento:

# Convertir la columna 'Fecha de Vencimiento (*)' a objetos de fecha
reporte['Fecha de Vencimiento (*)'] = pd.to_datetime(reporte['Fecha de Vencimiento (*)'])

# Aplicar formato de fecha específico
reporte['Fecha de Vencimiento (*)'] = reporte['Fecha de Vencimiento (*)'].dt.strftime('%d/%m/%Y')

#%%

try:
    ruta = "sentinel.xlsx"
    os.remove(ruta)
except FileNotFoundError:
    pass


reporte.to_excel('sentinel.xlsx', index=False)


