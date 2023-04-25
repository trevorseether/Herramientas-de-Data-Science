# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:18:16 2023

@author: sanmiguel38
"""
from datetime import datetime
import pandas as pd
import calendar
import os
import pyodbc
#%%

fecha_txt = 'Marzo - 2023' #escribir el mes que estamos haciendo

os.chdir('C:\\Users\\sanmiguel38\\Desktop\\ratios\\2023 MARZO')

#%%


def parse_date(date_str):
    try:
        # Intentar parsear como fecha con formato DD/MM/YYYY HH:MM:SS
        return datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    except ValueError:
        # Si falla, intentar parsear como fecha con formato DD/MM/YYYY
        return datetime.strptime(date_str, '%d/%m/%Y')
    except ValueError:
        # Si falla, intentar parsear como fecha con formato DD-MM-YYYY HH:MM:SS
        return datetime.strptime(date_str, '%d-%m-%Y %H:%M:%S')
    except ValueError:
        # Si falla, intentar parsear como fecha con formato DD-MM-YYYY HH:MM:SS
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        #si hay un '-' solo dejar -
        if date_str == '-':
            return date_str
    except ValueError:
        #si hay un 'NULL' solo dejar -
        if date_str == 'NULL':
            return date_str

#%%

df = pd.read_excel('Ratios - Cronogramas de creditos vigentes al 31-Marzo-23 - No incl castigados.xlsx',
                   skiprows= 0,
                   dtype = {'NroPrestamo Fincore': object}
                   ,parse_dates=['Fecha Vencimiento' #ojo que podría estar mal esta fecha
                                ])

df['NroPrestamo Fincore'] = df['NroPrestamo Fincore'].str.strip()
df = df.rename(columns={"Fecha Vencimiento": "FechaVencimiento"})
df = df.rename(columns={"Moneda Prestamo": "MonedaPrestamo"})

#%%
'nos quedamos solamente con '
df_filtrado = df.query('FechaVencimiento >= "2023-01-01"')

''' ejemplo d un equivalente a Like, para el query
df_filtrado = df.query('FechaVencimiento >= "2023-01-01" and MonedaPrestamo.str.contains("US")')
'''

#%% nos quedamos solo con aquellos cuyo nro de fincore esté vigente en el anexo06

# esta consulta nos devuelve el nro de fincore del anexo más reciente
# si queremos otro mes tendríamos que modificar la query
conn = pyodbc.connect('DRIVER=SQL Server;SERVER=(local);UID=sa;Trusted_Connection=Yes;APP=Microsoft Office 2016;WSID=SM-DATOS')
nro_fincore_vigentes = pd.read_sql_query('''
SELECT Nro_Fincore 
FROM anexos_riesgos2..Anx06_preliminar
WHERE FechaCorte1 = (
  SELECT MAX(FechaCorte1)
  FROM anexos_riesgos2..Anx06_preliminar
)
                                           ''', conn)

#%%
#procedemos a filtrar los datos

fincores = nro_fincore_vigentes['Nro_Fincore'].tolist()
df_filtrado_2 = df_filtrado[df_filtrado['NroPrestamo Fincore'].isin(fincores)]

#para chequear si es que no hacen ningún match
#print(nro_fincore_vigentes['Nro_Fincore'].tolist())
#print(df_filtrado['NroPrestamo Fincore'])


#%% creando columnas adicionales

df_filtrado['Mes'] = df_filtrado['FechaVencimiento'].dt.month
df_filtrado['Año'] = df_filtrado['FechaVencimiento'].dt.year
df_filtrado['Mes_Texto'] = df_filtrado['FechaVencimiento'].dt.strftime('%B')
df_filtrado['Mes_año'] = df_filtrado['FechaVencimiento'].dt.to_period('M')
df_filtrado['Fecha_Agrupada'] = df_filtrado['Año'].astype(str) + '/' + df_filtrado['Mes_Texto']

#%%
'tabla pivote'
df_filtrado
df_filtrado['Fecha_Agrupada'] = pd.to_datetime(df_filtrado['Fecha_Agrupada'], format='%Y/%B')
pivot_table = df_filtrado.pivot_table(columns='MonedaPrestamo',
                                      values=['Capital','Interes'], 
                                      index=['Fecha_Agrupada'], 
                                      
                                      aggfunc='sum'
                                      )

#%%
pivot_table = pivot_table.reset_index()

pivot_table.columns

#%%

#agregando la columna de años
pivot_table['Años'] = pivot_table['Fecha_Agrupada'].dt.year

#agregando la columna de meses
meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 
         7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

pivot_table['Meses'] = pivot_table['Fecha_Agrupada'].dt.month.map(meses)

#%% dataframe
#ordenamiento por si acaso
pivot_table = pivot_table.sort_values(by='Fecha_Agrupada', ascending=True)

dataframe_final = pivot_table[['Años', 'Meses']]

dataframe_final.loc[:, ('SOLES', 'Capital')] = pivot_table.loc[:, ('Capital', 'S/')]
dataframe_final.loc[:, ('SOLES', 'Interés')] = pivot_table.loc[:, ('Interes', 'S/')]

dataframe_final.loc[:, ('DOLARES', 'Capital')] = pivot_table.loc[:, ('Capital', 'US$')]
dataframe_final.loc[:, ('DOLARES', 'Interés')] = pivot_table.loc[:, ('Interes', 'US$')]

#%%

'CREACIÓN DEL EXCEL'
#primero creamos un excel auxiliar para poner bien las columnas :'v
nombre = "temporal.xlsx"
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

dataframe_final.to_excel(nombre,
                      index=True)

df = pd.read_excel('temporal.xlsx')
df = df.drop(df.columns[0], axis=1)
df = df.drop(1, axis=0)

try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

reporte = 'Ratios - Cronogramas ' + fecha_txt + '.xlsx'

try:
    ruta = reporte
    os.remove(ruta)
except FileNotFoundError:
    pass

df.to_excel(reporte,
                      index=False)

