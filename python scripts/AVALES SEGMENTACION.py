# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:53:26 2023

@author: sanmiguel38
"""

import pandas as pd
import os
from datetime import datetime

import numpy as np

import pyodbc 

#%%

MES_NOMBRE = 'MARZO 2023'

os.chdir('C:\\Users\\sanmiguel38\\Desktop\\SEGMENTACIONES\\MARZO 2023') #aqui escoger la ubicación de los archivos

#%%
conn = pyodbc.connect('DRIVER=SQL Server;SERVER=(local);UID=sa;Trusted_Connection=Yes;APP=Microsoft Office 2016;WSID=SM-DATOS')

#donde dice @fechacorte se debe poner el mes
df = pd.read_sql_query('''declare @fechacorte datetime
set @fechacorte = '20230228' 


select NumerodeDocumento10 as 'DNI SOCIOS', 
Saldodecolocacionescreditosdirectos24 AS 'SALDO DE CARTERA',
Saldodecolocacionescreditosdirectos24-IngresosDiferidos42 AS 'SALDO DE CARTERA NETA',
TipodeCredito19 AS 'TIPO DE CREDITO',
Situacion_Credito AS 'SITUACION',
DiasdeMora33 AS 'DIAS DE ATRASO',
NumerodeCuotasProgramadas44 AS 'PLAZO TOTAL',
PeriododeGracia47 AS 'PLAZO DE GRACIA',
TipodePersona11 AS 'TIPO DE SOCIO',
'CREDITOS - DIRECTOS' as 'MODALIDAD CREDITICIA',
'' AS 'Dni - Asociado - indirecta',
ClasificaciondelDeudorconAlineamiento15 AS 'CLASIFICACION CREDITICIA'

from anexos_riesgos2..Anx06_preliminar
where FechaCorte1 = @fechacorte
and SaldosdeCreditosCastigados38 = 0''', conn)

#print(df)

#%%
'en caso de que pidan este reporte antes de subirlo a la base de datos, pero ya tenemos el excel'

nombre_anexo = 'Rpt_DeudoresSBS_Marzo 2023 finalizado.xlsx' #este es el reporte que YO he elaborado

df = pd.read_excel(nombre_anexo,
                   skiprows=1,
                   dtype = {'Número de Documento 10/':object,
                            'Tipo de Crédito 19/': object,
                            'Tipo de Persona 11/': object,
                            'Clasificación del Deudor con Alineamiento 15/': object})

df.dropna(subset=['Apellidos y Nombres / Razón Social 2/', 
                   'Fecha de Nacimiento 3/',
                   'Número de Documento 10/',
                   'Domicilio 12/',
                   'Numero de Crédito 18/'], inplace=True, how='all')

#%% renameamos y creamos las columnas necesarias
df = df.rename(columns={"Número de Documento 10/": "DNI SOCIOS"})
df = df.rename(columns={"Saldo de colocaciones (créditos directos) 24/": "SALDO DE CARTERA"})
df = df.rename(columns={"Ingresos Diferidos 42/": "IngresosDiferidos42"})
df['SALDO DE CARTERA NETA'] = df['SALDO DE CARTERA'] - df['IngresosDiferidos42']

df = df.rename(columns={"Tipo de Crédito 19/": "TIPO DE CREDITO"})
df = df.rename(columns={"Situacion TXT": "SITUACION"})
df = df.rename(columns={"Dias de Mora 33/": "DIAS DE ATRASO"})
df = df.rename(columns={"Número de Cuotas Programadas 44/": "PLAZO TOTAL"})
df = df.rename(columns={"Periodo de Gracia 47/": "PLAZO DE GRACIA"})
df = df.rename(columns={"Tipo de Persona 11/": "TIPO DE SOCIO"})
df = df.rename(columns={"Situacion TXT": "TIPO DE SOCIO"})
df['MODALIDAD CREDITICIA'] = 'CREDITOS - DIRECTOS'
df['Dni - Asociado - indirecta'] = ''
df = df.rename(columns={"Clasificación del Deudor con Alineamiento 15/": "CLASIFICACION CREDITICIA"})

#%%
#nos quedamos solo con las columnas necesarias

df = df[["DNI SOCIOS", "SALDO DE CARTERA", 'SALDO DE CARTERA NETA', 'TIPO DE CREDITO', "SITUACION", "DIAS DE ATRASO", "PLAZO TOTAL",
         "PLAZO DE GRACIA", "TIPO DE SOCIO", 'MODALIDAD CREDITICIA', 'Dni - Asociado - indirecta', "CLASIFICACION CREDITICIA"]]

df["DNI SOCIOS"] = df["DNI SOCIOS"].str.strip()

#%%
'AQUI SE LEE EL REPORTE DE AVALES'
#HAY QUE SACARLO DEL FINCORE
#RUTA:
#    'REPORTES/CREDITO/PRESTAMOS OTORGADOS/REGISTRO DE AVALES Y-O GARANTÍAS'

ruta = "Rpt_Avales.xlsx"
df1=pd.read_excel(ruta,
                  dtype={'''Nro Docto
Aval''': object,
                            '''Nro Docto
Socio''': object,
'Numero':object},
                     skiprows=8)

df1['''Nro Docto
Aval'''] = df1['''Nro Docto
Aval'''].str.strip()

#%%

#para concatenar las columnas, nos quedamos con un archivo que solo servirá para el merge

df1['concatenacion'] = df1['Aval'].apply(str) + ' ' + df1['Numero'].apply(str)

df1_filtrado = df1[['''Nro Docto
Aval''','Aval', 'Numero','''Nro Docto
Socio''', 'concatenacion']]

df1_filtrado = df1_filtrado.rename(columns={'''Nro Docto
Aval''': 'Dni - Asociado - indirecta2'})
df1_filtrado = df1_filtrado.rename(columns={'''Nro Docto
Socio''': 'dni socio'})

valores_unicos = df1_filtrado.drop_duplicates(subset='concatenacion', keep='first')


#%%
#merge

df_resultado = df.merge(valores_unicos, 
                         left_on=['DNI SOCIOS'], 
                         right_on=['dni socio']
                         ,how='inner')

df_resultado.columns
df_resultado['Dni - Asociado - indirecta2']

df_para_unir = df_resultado[['DNI SOCIOS', 
                             'SALDO DE CARTERA',
                             'SALDO DE CARTERA NETA',
                             'TIPO DE CREDITO',
                             'SITUACION',
                             'DIAS DE ATRASO',
                             'PLAZO TOTAL',
                             'PLAZO DE GRACIA',
                             'TIPO DE SOCIO',
                             'MODALIDAD CREDITICIA',
                             'Dni - Asociado - indirecta2',
                             'CLASIFICACION CREDITICIA']]

df_para_unir = df_para_unir.rename(columns={'Dni - Asociado - indirecta2': 'Dni - Asociado - indirecta'})

df_para_unir['MODALIDAD CREDITICIA'] = 'CREDITOS - INDIRECTOS'

#%%
#concatenar dataframes
avales = pd.concat([df,df_para_unir], ignore_index=True)

#%%
#este código es solo para crear un excel y revisarlo

nombre = 'SEGMENTACION '+ MES_NOMBRE + '.xlsx'
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

avales.to_excel(nombre,
                sheet_name=MES_NOMBRE,
                index=False)


