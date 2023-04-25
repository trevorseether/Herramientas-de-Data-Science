# -*- coding: utf-8 -*-

"""
Created on Wed Feb  8 11:37:33 2023

@author: sanmiguel38
"""

import pandas as pd
import os
import datetime
import calendar
from datetime import datetime, timedelta
import pyodbc
import numpy as np

#%%

import datetime
import calendar

#%%
#PONER LA FECHA DE CORTE
fecha_corte = '2023-03-31'

#esta función nos permite obtener el número de días del mes de corte
def dias_en_mes(fecha):
    # Convertimos la fecha en formato de cadena a objeto datetime
    fecha_objeto = datetime.datetime.strptime(fecha, '%Y-%m-%d')
    
    # Obtenemos el número de días del mes utilizando el método monthrange del módulo calendar
    _, dias_en_el_mes = calendar.monthrange(fecha_objeto.year, fecha_objeto.month)
    
    # Retornamos el número de días en el mes
    return dias_en_el_mes

dias_corte = dias_en_mes(fecha_corte)

#%%
#función que transforma fechas en formato '18/01/2023 y devuelve 20230118'

'''
def convertir_formato_fecha(fecha):
    fecha = pd.to_datetime(fecha, format='%d/%m/%Y') #aqui podemos cambiar el 
    fecha = fecha.strftime('%Y%m%d')
    return fecha

#dataframe de ejemplo
df = pd.DataFrame({'Fecha': ['18/01/2023', '19/01/2023', '20/01/2023']})

#aplicación de ejemplo
df['Fecha'] = df['Fecha'].apply(convertir_formato_fecha)
'''

#%%

#UBICACIÓN DE LOS ARCHIVOS
os.chdir('C:\\Users\\sanmiguel38\\Desktop\\TRANSICION  ANEXO 6\\2023 marzo')

#%%


anexo_del_mes = "Rpt_DeudoresSBS Anexo06  - Marzo2023 - campos ampliados.xlsx"
df1=pd.read_excel(anexo_del_mes,
                 dtype={'Registro 1/': object, 
                        'Fecha de Nacimiento 3/': object,
                        'Código Socio 7/':object, 
                        'Número de Documento 10/': object,
                        'Relación Laboral con la Cooperativa 13/':object, 
                        'Código de Agencia 16/': object,
                        'Moneda del crédito 17/':object, 
                        'Numero de Crédito 18/': object,
                        'Tipo de Crédito 19/': object,
                        'Sub Tipo de Crédito 20/': object,
                        'Fecha de Desembolso 21/': object,
                        'Cuenta Contable 25/': object,
                        'Tipo de Producto 43/': object,
                        'Fecha de Vencimiento Origuinal del Credito 48/': object,
                        'Fecha de Vencimiento Actual del Crédito 49/': object,
                        '''Nro Prestamo 
Fincore''': object,
'Refinanciado TXT': object},
                     skiprows=2)

#eliminando las filas con NaN en las siguiente columnas al mismo tiempo:
df1.dropna(subset=['Apellidos y Nombres / Razón Social 2/', 
                   'Fecha de Nacimiento 3/',
                   'Número de Documento 10/',
                   'Domicilio 12/',
                   'Numero de Crédito 18/'], inplace=True, how='all')

#leyendo la lista de socios con cred < 100 soles
df_100=pd.read_excel(anexo_del_mes,
                 dtype={'Código Socio 7/':object},
                 skiprows=0,
                 sheet_name='socios con cred < 100 soles')

                        
anexo06 = df1.columns  ; socios_menor_100 = df_100.columns

del anexo_del_mes

x = df1.columns

#%%
#ahora vamos a leer el archivo donde Enrique manualmente elabora la clasificación de los refinanciados
#para leer bien este reporte primero debemos eliminar los otros meses del excel (ya que se repiten)

'eliminar #456' #si se desea reactivar esta celda

#456'este es el archivo de la calificación que añade Enrique manualmente'
#456########################################################################################################################
#456archivo_refinanciados = 'REFINANCIADOS RECLASIFICADOS 28 02 2023 (1).xlsx' #nombre del archivo de los refinanciados ####
#456########################################################################################################################

#456calif_ref = pd.read_excel(archivo_refinanciados,
#456                          skiprows=3,
#456                          dtype={'Nº de Crédito FINCORE': object, })

#456############################################################################################
#456mes_calif = 'Febrero' #aqui debemos poner el mes donde esté la calificación más reciente ###
#456############################################################################################

#456calif_ref[mes_calif] = calif_ref[mes_calif].astype(float)

#456calif_ref = calif_ref.rename(columns={mes_calif: 'calificacion especial'})
#456calif_ref = calif_ref.rename(columns={'Nº de Crédito FINCORE': 'fincore ref'})

#456calif_ref = calif_ref[['fincore ref','calificacion especial']]

#456calif_ref = calif_ref.dropna()

#456del archivo_refinanciados
#456del mes_calif

#de aqui esta tabla se usará después de aplicar la calificación con alineamiento de manera individual (linea )
                                        
#%%
'parseando datos de fechas'
                 
df1['Fecha de Nacimiento 3/'] = pd.to_datetime(df1['Fecha de Nacimiento 3/'], format='%Y%m%d')   
df1['Fecha de Desembolso 21/'] = pd.to_datetime(df1['Fecha de Desembolso 21/'], format='%Y%m%d')   
df1['Fecha de Vencimiento Origuinal del Credito 48/'] = pd.to_datetime(df1['Fecha de Vencimiento Origuinal del Credito 48/'], format='%Y%m%d')   
df1['Fecha de Vencimiento Actual del Crédito 49/'] = pd.to_datetime(df1['Fecha de Vencimiento Actual del Crédito 49/'], format='%Y%m%d')   
                       
#%%
#quitando posibles espacios vacíos en el nombre
df1['Código Socio 7/'] = df1['Código Socio 7/'].str.strip()

#%%
# resultado_1
# haciendo un merge en realidad innecesario pero es para comprobar la primera columna 
# 'Socios al menos con un cred < 100 soles
# amarillo =  cred <100
# rosado =  cred >= 100
# PROV.REQUERIDA A SER EVALUADA.'

df100_merge = df_100.copy()
df100_merge = df100_merge.rename(columns={"Código Socio 7/": "codigo de socio"})
df100_merge.drop_duplicates(subset='codigo de socio', inplace=True)
df100_merge = df100_merge["codigo de socio"]

df_resultado = df1.merge(df100_merge, 
                         left_on=["Código Socio 7/"], 
                         right_on=["codigo de socio"]
                         ,how='left')

df_resultado = df_resultado.rename(columns={"codigo de socio": "al menos 1 crédito < 100"})

dataframe = df_resultado.copy()

# del df_resultado
# df_resultado = dataframe 

#%%
'creando dataframe auxiliar con los refinanciados'

#lo ponemos todo en mayúsculas
df_resultado['Refinanciado TXT'] = df_resultado['Refinanciado TXT'].str.upper()
df_resultado['Refinanciado TXT'] = df_resultado['Refinanciado TXT'].astype(str)
print(df_resultado['Refinanciado TXT'].unique())

datos_refinanciados = df_resultado[df_resultado['Refinanciado TXT'] == 'REFINANCIADO']
datos_refinanciados = datos_refinanciados[['''Nro Prestamo 
Fincore''', 'Clasificación del Deudor 14/']]

datos_refinanciados = datos_refinanciados.rename(columns={'''Nro Prestamo 
Fincore''': 'fincore ref'})
datos_refinanciados = datos_refinanciados.rename(columns={'Clasificación del Deudor 14/': 'calificacion especial'})

calif_ref = datos_refinanciados.copy()

#%%

df_resultado['Refinanciado TXT'] = df_resultado['Refinanciado TXT'].str.strip()
df_resultado['''Nro Prestamo 
Fincore'''] = df_resultado['''Nro Prestamo 
Fincore'''].str.strip()

'hora de calcular la clasificación con alineamiento interno:'
###############################################
uit = 4950 #valor de la uit en el año 2023  ###
###############################################

#por si acaso convertirmo el tipo de dato a numero
df_resultado['Dias de Mora 33/'] = df_resultado['Dias de Mora 33/'].astype(int)
def alineamiento(df_resultado):
    if ('REFINANCIADO' not in df_resultado['Refinanciado TXT'] or 'Refinanciado' not in df_resultado['Refinanciado TXT']):
        if df_resultado['Tipo de Crédito 19/'] in ['06', '07', '08']:
            if df_resultado['Dias de Mora 33/'] <=15:
                return '0'
            elif df_resultado['Dias de Mora 33/'] <=60:
                return '1'
            elif df_resultado['Dias de Mora 33/'] <=120:
                return '2'
            elif df_resultado['Dias de Mora 33/'] <=365:
                return '3'
            elif df_resultado['Dias de Mora 33/'] >365:
                return '4'
        elif df_resultado['Tipo de Crédito 19/'] in ['09', '10', '11','12']:
            if df_resultado['Dias de Mora 33/'] <=8:
                return '0'
            elif df_resultado['Dias de Mora 33/'] <=30:
                return '1'
            elif df_resultado['Dias de Mora 33/'] <=60:
                return '2'
            elif df_resultado['Dias de Mora 33/'] <=120:
                return '3'
            elif df_resultado['Dias de Mora 33/'] >120:
                return '4'
        elif df_resultado['Tipo de Crédito 19/'] in ['13']:
            if df_resultado['Dias de Mora 33/'] <=30:
                return '0'
            elif df_resultado['Dias de Mora 33/'] <=60:
                return '1'
            elif df_resultado['Dias de Mora 33/'] <=120:
                return '2'
            elif df_resultado['Dias de Mora 33/'] <=365:
                return '3'
            elif df_resultado['Dias de Mora 33/'] >365:
                return '4'
    elif ('REFINANCIADO' in df_resultado['Refinanciado TXT'] or 'Refinanciado' in df_resultado['Refinanciado TXT']):
        return str(df_resultado.iloc[0]['Clasificación del Deudor 14/'])
    else:
        return 'revisar caso'

#aplicamos la función
df_resultado['alineamiento14 provisional'] = df_resultado.apply(alineamiento, axis=1)

#convertimos esa columna a numerica
df_resultado['alineamiento14 provisional'] = df_resultado['alineamiento14 provisional'].astype(float)

#este resultado se debería asignar a la columna 14/
df_resultado['Clasificación del Deudor 14/'] = df_resultado['alineamiento14 provisional']

df_resultado.to_excel('anx06 solo para ver el alinemaiento 14.xlsx',
                      index=False)



#%%
#HASTA AQUÍ HEMOS CREADO EL ALINEAMIENTO POR LA LÓGICA ESTABLECIDA
#FALTA PONERLE LA CLASIFICACIÓN MANUAL QUE ELABORA ENRIQUE A LOS CRÉDITOS REFINANCIADOS

calif_ref['fincore'] = calif_ref['fincore ref'].str.strip()

#hacemos un merge
df_resultado = df_resultado.merge(calif_ref, 
                          how='left', 
                          left_on=['''Nro Prestamo 
Fincore'''], 
                          right_on=['fincore ref'])
                                   
                       
fincores = df_resultado[['fincore ref', 'calificacion especial']].copy()                                   
fincores = fincores.dropna()
fincores = fincores['fincore ref'].tolist()
                                   
def asignacion_calif_refinanciados(df_resultado):
    if df_resultado['''Nro Prestamo 
Fincore'''] in fincores:
        return df_resultado['calificacion especial']
    else:
        return df_resultado['alineamiento14 provisional']

df_resultado['alineamiento 14 final'] = df_resultado.apply(asignacion_calif_refinanciados, axis=1)

df_resultado['alineamiento14 provisional'] = df_resultado['alineamiento 14 final']
df_resultado['Clasificación del Deudor 14/'] = df_resultado['alineamiento 14 final']   

#%%

'ALINEAMIENTO 15/'
#creamos un dataframe que tenga el máximo
alineamiento_provisional = df_resultado.groupby('Código Socio 7/')['alineamiento14 provisional'].max().reset_index()
alineamiento_provisional = alineamiento_provisional.rename(columns={'Código Socio 7/': "cod soc alin"})
alineamiento_provisional = alineamiento_provisional.rename(columns={'alineamiento14 provisional': "alineamiento maximo"})
#creamos un dataframe que tenga el total del saldo de cartera del socio
saldo_total = df_resultado.groupby('Código Socio 7/')['Saldo de colocaciones (créditos directos) 24/'].sum().reset_index()
saldo_total = saldo_total.rename(columns={'Código Socio 7/': "cod soc saldo"})
saldo_total = saldo_total.rename(columns={'Saldo de colocaciones (créditos directos) 24/': "saldo total"})
#hacemos dos merge
df_resultado = df_resultado.merge(alineamiento_provisional, 
                          how='left', 
                          left_on=['Código Socio 7/'], 
                          right_on=["cod soc alin"])

df_resultado = df_resultado.merge(saldo_total, 
                          how='left', 
                          left_on=['Código Socio 7/'], 
                          right_on=["cod soc saldo"])
#eliminamos columnas de más
df_resultado.drop(["cod soc alin"], axis=1, inplace=True)
df_resultado.drop(["cod soc saldo"], axis=1, inplace=True)

#calculamos qué porcentaje de 

def porcentaje_del_total(df_resultado):
    denominador = df_resultado["saldo total"]
    numerador = df_resultado['Saldo de colocaciones (créditos directos) 24/']
    # Verificar si el denominador es cero
    if denominador == 0:
        return 0
    else:
        return numerador / denominador
  
df_resultado['% del total'] = df_resultado.apply(porcentaje_del_total, axis=1)

#ahora vamos a marcar las que tengan un saldo menor a 1% del total 
def menor_1(df_resultado):
    '''
    
    "Resolución SBS Nº 11356-2008 
    Reglamento para la Evaluación y Clasificación del Deudor y la Exigencia de Provisiones"
    "5.2 CLASIFICACIÓN CREDITICIA DEL DEUDOR
           Criterios Generales"
    c) En caso que el deudor tenga varios créditos en la misma empresa, su clasificación será la correspondiente a la categoría de mayor riesgo:
    1. a menos que el saldo en dichos créditos sea menor a S/. 100.00 (Cien Nuevos Soles)
    2. o al uno por ciento (1%) del total de la deuda con la empresa (con un tope máximo de tres (3) Unidades Impositivas Tributarias (UIT)), el que resulte mayor.
     La empresa primero consolidará la clasificación correspondiente al deudor por modalidad de crédito aplicando el criterio señalado anteriormente; luego consolidará las distintas modalidades por tipo de crédito, aplicando el mismo criterio.

    '''
    if df_resultado['% del total'] < 0.01 and \
        df_resultado['Saldo de colocaciones (créditos directos) 24/'] \
        < (3*uit):
        return 'menor 1% & 3uit'
    else:
        return 'no'
  
df_resultado['menor 1 3uit'] = df_resultado.apply(menor_1, axis=1)

#marcamos los que tienen saldo de crédito menor a s/.100
def menor_100(df_resultado):

    if df_resultado['Saldo de colocaciones (créditos directos) 24/'] < 100:
        return 'menor 100'
    else:
        return 'no'
  
df_resultado['menor a 100'] = df_resultado.apply(menor_100, axis=1)

#filtramos aquellos que tengan montos menor a 100, o que sean menores al 1% del total del saldo de cartera sin superar 3 uit
alinemiento_filtrado = df_resultado.loc[~((df_resultado['menor 1 3uit'] == 'menor 1% & 3uit') | (df_resultado['menor a 100'] == 'menor 100'))]

#ahora sí creamos el mejor alineamiento para asignar el riesgo
alineamiento = alinemiento_filtrado.groupby('Código Socio 7/')['alineamiento14 provisional'].max().reset_index()
alineamiento = alineamiento.rename(columns={"Código Socio 7/": "socio"})
alineamiento = alineamiento.rename(columns={'alineamiento14 provisional': "alineamiento15 provisional final"})



#ahora si un merge
df_resultado = df_resultado.merge(alineamiento[['socio', "alineamiento15 provisional final"]], 
                          how='left', 
                          left_on=['Código Socio 7/'], 
                          right_on=['socio'])

df_resultado.drop(['socio'], axis=1, inplace=True)
'a esta altura, en teoría ya tenemos el alineamiento interno'
#es la columna "alineamiento15 provisional final"

#reemplazamos los nan por los valores en la columna 15
df_resultado.loc[df_resultado["alineamiento15 provisional final"].isna(), "alineamiento15 provisional final"] = df_resultado.loc[df_resultado["alineamiento15 provisional final"].isna(), 'Clasificación del Deudor con Alineamiento 15/']

#calificación original(para mantenerla)
df_resultado['Clasificación del Deudor con Alineamiento 15/ ORIGINAL'] = df_resultado['Clasificación del Deudor con Alineamiento 15/']

#este código habría que tenerlo, pero si queremos mantener el alineamiento 15 original le ponemos hashtag
df_resultado['Clasificación del Deudor con Alineamiento 15/'] = df_resultado["alineamiento15 provisional final"]

#habría que modificar una de las provisiones
#%% PROVISIONES
'función para elaborar las provisiones'

def provision_SA(df_resultado):
    '''
    entra el dataframe df_resultado
    ----------
    df_resultado : 
        va a calcular [Tasa de Provisión SA]

    Returns
    -------
    None.

    '''
    # tasa de provisión genérica
    if df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '06':
        return 0.0070
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '07':
        return 0.0070
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '08':
        return 0.0100
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '09':
        return 0.0100
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '10':
        return 0.0100
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '11':
        return 0.0100
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '12':
        return 0.0100
    elif df_resultado['Clasificación del Deudor 14/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '13':
        return 0.0070    ## tasa de provisión específica
    elif df_resultado['Saldo de Garantías Autoliquidables 35/'] > 0:
        return 0.0100

    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 1:
        return 0.0250  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 1:
        return 0.0500  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 2:
        return 0.1250  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 2:
        return 0.2500 
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 3:
        return 0.3000  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 3:
        return 0.6000 
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 4:
        return 0.6000  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor 14/'] == 4:
        return 1.0000
    else:
        return 'revisar caso'

df_resultado['Tasa de Provisión SA'] = df_resultado.apply(provision_SA, axis=1)

#%%%
def provision(df_resultado):
    '''
    entra el dataframe df_resultado
    ----------
    df_resultado : 
        va a calcular [Tasa de Provisión]

    Returns
    -------
    None.

    '''
    # tasa de provisión genérica
    if df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '06':
        return 0.0070
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '07':
        return 0.0070
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '08':
        return 0.0100
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '09':
        return 0.0100
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '10':
        return 0.0100
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '11':
        return 0.0100
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '12':
        return 0.0100
    elif df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 0 \
    and df_resultado['Tipo de Crédito 19/'] == '13':
        return 0.0070
    ## tasa de provisión específica
    elif df_resultado['Saldo de Garantías Autoliquidables 35/'] > 0:
        return 0.0100
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 1:
        return 0.0250  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 1:
        return 0.0500  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 2:
        return 0.1250  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 2:
        return 0.2500 
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 3:
        return 0.3000  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 3:
        return 0.6000 
    elif df_resultado['Saldos de Garantías Preferidas 34/'] > 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 4:
        return 0.6000  
    elif df_resultado['Saldos de Garantías Preferidas 34/'] == 0 \
    and df_resultado['Clasificación del Deudor con Alineamiento 15/'] == 4:
        return 1.0000
    else:
        return 'revisar caso'

df_resultado['Tasa de Provisión'] = df_resultado.apply(provision, axis=1)


#%%
'tasa de interés anual'
df_resultado['Tasa de Interés Anual 23/'].dtype

def int_diario(df_resultado):
    return (((1 + float(df_resultado['Tasa de Interés Anual 23/']))**(1/360))-1) *100

df_resultado['Tasa Diaria'] = df_resultado.apply(int_diario, axis=1)

#%%
#tal vez aquí debería ir 'Fecha Ultimo Pago'
#creo que no realmente
#%%
'garantías preferidas'
#para asignar las garantías preferidas, tenemos una lista de créditos con garantías preferidas,
#solo si estos créditos del anexo 06 están en esta lista se le va a asignar el saldo de crédito24

df_resultado['Monto de Garantías Preferidas'] = df_resultado['Saldos de Garantías Preferidas 34/']

def garant_pref(df_resultado):
    if df_resultado['''Nro Prestamo 
Fincore'''] in ['00025314'	,
'00021989'	,
'00024551'	,
'00023254'	,
'00025067'	,
'00024033'	,
'00025678'	,
'00023259'	,
'00022958'	,
'00024926'	,
'00023451'	,
'00023202'	,
'00023215'	,
'00024860'	,
'00025566'	,
'00021994'	
]:  
        return df_resultado['Saldo de colocaciones (créditos directos) 24/']
    else:
        return 0
    
    
df_resultado['Saldos de Garantías Preferidas 34/'] = df_resultado.apply(garant_pref, axis=1)   

#%%
'garantías autoliquidables'
#para las garantías autoliquidables 

df_resultado['Monto de Garantías Autoliquidables'] = df_resultado['Saldo de Garantías Autoliquidables 35/']

def garant_autoliqui(df_resultado):
    if df_resultado['Saldo de Garantías Autoliquidables 35/'] > 0:  
        return df_resultado['Saldo de colocaciones (créditos directos) 24/']
    else:
        return 0
    
df_resultado['Saldo de Garantías Autoliquidables 35/'] = df_resultado.apply(garant_autoliqui, axis=1)   

#%%
'cartera atrasada'

def cartera_atrasada(df_resultado):
    return df_resultado['Capital Vencido 29/'] + df_resultado['Capital en Cobranza Judicial 30/']

df_resultado['Cartera Atrasada'] = df_resultado.apply(cartera_atrasada, axis=1)   

#%%
'rango días mora'

def rango_dias_mora(df_resultado):
    if df_resultado['Dias de Mora 33/'] <= 8:
        return 'De 0 a 8'
    elif df_resultado['Dias de Mora 33/'] <= 30:
        return 'De 9 a 30'
    elif df_resultado['Dias de Mora 33/'] <= 60:
        return 'De 31 a 60'
    elif df_resultado['Dias de Mora 33/'] <= 90:
        return 'De 61 a 90'
    elif df_resultado['Dias de Mora 33/'] <= 120:
        return 'De 91 a 120'
    elif df_resultado['Dias de Mora 33/'] <= 180:
        return 'De 121 a 180'
    elif df_resultado['Dias de Mora 33/'] <= 365:
        return 'De 181 a 365'
    elif df_resultado['Dias de Mora 33/'] <= 730:
        return 'De 366 a 730'
    elif df_resultado['Dias de Mora 33/'] > 730:
        return 'De 731 a mas'
    else:
        return 'revisar caso'
    

df_resultado['Rango Días de Mora'] = df_resultado.apply(rango_dias_mora, axis=1) 

#%%
'columna auxiliar que indica si es vigente, refinanciado, vencido o judicial'
'servirá para asignar la cuenta contbale 25'

def situacion(df_resultado):
    if (df_resultado['Capital Vigente 26/'] > df_resultado['Capital Refinanciado 28/'] and
        df_resultado['Capital Vigente 26/'] > df_resultado['Capital Vencido 29/']  and
        df_resultado['Capital Vigente 26/'] > df_resultado['Capital en Cobranza Judicial 30/']):
       return 'VIGENTE'
    elif (df_resultado['Capital Refinanciado 28/'] > df_resultado['Capital Vigente 26/'] and
          df_resultado['Capital Refinanciado 28/'] > df_resultado['Capital Vencido 29/']  and
          df_resultado['Capital Refinanciado 28/'] > df_resultado['Capital en Cobranza Judicial 30/']):
       return 'REFINANCIADO'
    elif (df_resultado['Capital Vencido 29/'] > df_resultado['Capital Vigente 26/'] and
          df_resultado['Capital Vencido 29/'] > df_resultado['Capital Refinanciado 28/']  and
          df_resultado['Capital Vencido 29/'] > df_resultado['Capital en Cobranza Judicial 30/']):
       return 'VENCIDO'
    elif (df_resultado['Capital en Cobranza Judicial 30/'] > df_resultado['Capital Vigente 26/'] and
          df_resultado['Capital en Cobranza Judicial 30/'] > df_resultado['Capital Refinanciado 28/']  and
          df_resultado['Capital en Cobranza Judicial 30/'] > df_resultado['Capital Vencido 29/']):
       return 'JUDICIAL'
    else:
        return ' '
    
df_resultado['AUXILIAR_SITUACION'] = df_resultado.apply(situacion, axis=1) 

#%%
'CREACIÓN DE LAS TABLAS DE LAS CUENTAS CONTABLES'

cuentas_01 = pd.DataFrame({'TIPO CREDITO':['08','09','10','12','13'],
                           'VIGENTE':['1411120600','1411130600',
                                      '1411020600','1411030604',
                                      '1411040601'],
                           'REFINANCIADO':['1414120600','1414130600',
                                           '1414020600','1414030604',
                                           '1414040601'],
                           'VENCIDO':['1415120600','1415130600',
                                      '1415020600','1415030604',
                                      '1415040601'],
                           'JUDICIAL':['1416120600','1416130600',
                                       '1416020600','1416030604',
                                       '1416040601'],
                           ' ':['','',
                                       '','',
                                       '']})

cuentas_02 = pd.DataFrame({'TIPO CREDITO':['08','09','10','12','13'],
                           'VIGENTE':['1421120600','1421130600',
                                      '1421020600','1421030604',
                                      '1421040601'],
                           'REFINANCIADO':['1424120600','1424130600',
                                           '1424020600','1424030604',
                                           '1424040601'],
                           'VENCIDO':['1425120600','1425130600',
                                      '1425020600','1425030604',
                                      '1425040601'],
                           'JUDICIAL':['1426120600','1426130600',
                                       '1426020600','1426030604',
                                       '1426040601'],
                           ' ':['','',
                                       '','',
                                       '']})

#%%
'asignación de la cuenta contable 25'

def asignacion_25(df_resultado):
    
    valor1 = ''
    valor2 = ''
    
    tipo_credito = df_resultado['Tipo de Crédito 19/']
    situacion = df_resultado['AUXILIAR_SITUACION']
    
    if df_resultado['Moneda del crédito 17/'] == '01':
        if tipo_credito in cuentas_01['TIPO CREDITO'].values:
            valor1 = cuentas_01.loc[cuentas_01['TIPO CREDITO'] == tipo_credito, situacion].values[0]
        return valor1

    elif df_resultado['Moneda del crédito 17/'] == '02':
        if tipo_credito in cuentas_02['TIPO CREDITO'].values:
            valor2 = cuentas_02.loc[cuentas_01['TIPO CREDITO'] == tipo_credito, situacion].values[0]
        return valor2
    else:
        return ''
    

df_resultado['Cuenta Contable 25/'] = df_resultado.apply(asignacion_25, axis=1) 

# cuentas_02.loc[cuentas_02['TIPO CREDITO'] == '08', 'REFINANCIADO'].values[0]

#%%
'vamos a calcular el tipo de producto para mype'

#import pyodbc 


#conn = pyodbc.connect('DRIVER=SQL Server;SERVER=(local);UID=sa;Trusted_Connection=Yes;APP=Microsoft Office 2016;WSID=SM-DATOS')
#df_mype = pd.read_sql_query('''
#declare @fechacorte as datetime
#set @fechacorte = '20221231'
#
#select 
#
#FechaCorte1, ApellidosyNombresRazonSocial2,
#FechadeDesembolso21, MontodeDesembolso22, Saldodecolocacionescreditosdirectos24,
#NumerodeCredito18, Nro_Fincore, CodigoSocio7, TipodeProducto43
#
#from anexos_riesgos2..Anx06_preliminar as a
#
#where TipodeProducto43 in (15,16,17,18,19,
#						   21,22,23,24,25,29,
#						   95,96,97,98,99)
#
#and Nro_Fincore in (SELECT Nro_Fincore
#					FROM anexos_riesgos2..Anx06_preliminar
#					WHERE fechacorte1 = @fechacorte)
#
#order by FechaCorte1, FechadeDesembolso21''', conn)
#


'''
############################################################################################
#############    no olvidar que ya tenemos la fecha de corte del desembolso    #############
############################################################################################
'''

#%%
'con esta pivot mype vamos a asignar el tipo de producto43 en función de la sumatoria del saldo de cartera'

#pivot_mype = df_mype.pivot_table(columns='FechaCorte1',
#                                      values=['Saldodecolocacionescreditosdirectos24'], 
#                                      index=['CodigoSocio7'], 
#                                      
#                                      aggfunc='sum'
#                                      )

# Obtener el valor para un socio y fecha específicos
#pivot_mype.loc['00033668', ('Saldodecolocacionescreditosdirectos24', '2022-05-31')]

#'elimina el indice secundario'
#pivot_mype.columns = pivot_mype.columns.droplevel()
#pivot_mype = pivot_mype.reset_index()

'con esta función se puede acceder a una celda del dataframe'
#pivot_mype.loc[pivot_mype['CodigoSocio7'] == '00034420', '2022-07-31'].values[0]

'esto podría servir para crear un excel e importarlo si es que no se puede acceder bien al dataframe'
#'CREACIÓN DEL EXCEL AUXILIAR'
#nombre = "pivot.xlsx"
#try:
#    ruta = nombre
#    os.remove(ruta)
#except FileNotFoundError:
#    pass
#
#pivot_mype.to_excel(nombre,
#                      index=False)       


#%%
'por si acaso quitando espacios a la columna del código del socio'

df_resultado['Código Socio 7/'] = df_resultado['Código Socio 7/'].str.strip()

#%%
'creamos un diccionarios a partir del dataframe de pivot_mype'
#esto ya no hace falta pero lo dejo ahí porque no estorba
#dic_pivot_mype = pivot_mype.to_dict(orient='records')

#%%
#usamos la función melt para convertir pivot_mype en tabla larga
#df = pivot_mype.melt(id_vars='CodigoSocio7', var_name='fecha', value_name='monto')

#HACEMOS UN MERGE, FINALMENTE, ESTA SERÁ LA SOLUCIÓN
#df_resultado = df_resultado.merge(df[['CodigoSocio7', 'fecha', 'monto']], 
#                          how='left', 
#                          left_on=['Código Socio 7/', 'fecha corte del desembolso'], 
#                          right_on=['CodigoSocio7', 'fecha'])
#df_resultado['monto'] = df_resultado['monto'].fillna(0)

#%%
#bacán y todo eso pero según Enrique esta no es la solución, igual lo dejo porque estaba bueno el código

#%%
#eliminamos estas columnas de más
#df_resultado.drop(['fecha', 'CodigoSocio7', '''Nro Prestamo 
#Fincore2'''], axis=1, inplace=True)

    
#%%lo mismo pero en función del tipo de producto
#df_resultado['Tipo de Producto 43/'] = df_resultado['Tipo de Producto 43/'].astype(float)
#def asignacion_mype(df_resultado):
#    if df_resultado['Tipo de Producto 43/'] in [15,16,17,18,19,
#    						                            21,22,23,24,25,29, 
#    						                            95,96,97,98,99]:
#        if df_resultado['monto'] <= 20000:
#            return 20
#        elif df_resultado['monto'] <= 300000:
#            return 10
#        else:
#            return 90
#    else:
#        return df_resultado.loc['Tipo de Producto 43/']

#df_resultado['producto_mype'] = df_resultado.apply(asignacion_mype, axis=1)
#df_resultado['Tipo de Producto 43/'] = df_resultado['Tipo de Producto 43/'].astype(int)
#%%
#nos muestra si hay alguna diferencia en la parte de las decenas de la asignación del tipo de producto 43
#df_resultado['resta_decenas'] = ((df_resultado['producto_mype'] // 10) - (df_resultado['Tipo de Producto 43/'] // 10))
 
#%%

['15','16','17','18','19',
'21','22','23','24','25','29',
'95','96','97','98','99']

#%%
#vamos a volver a calcular el tipo de producto43

df_resultado['Tipo de Producto 43/ original'] = df_resultado['Tipo de Producto 43/']

df_corto = df_resultado[['Tipo de Producto 43/',
                         'Saldos de Créditos Castigados 38/',
                         'Saldo de colocaciones (créditos directos) 24/',
                         'Código Socio 7/']]

#sumamos saldo de cartera y saldo castigado
df_corto.loc[:, 'monto mype'] = df_corto['Saldos de Créditos Castigados 38/'] + df_corto['Saldo de colocaciones (créditos directos) 24/']

# convierte la columna 'Tipo de Producto 43/' al tipo de dato int
df_corto['Tipo de Producto 43/'] = df_corto['Tipo de Producto 43/'].astype(int)

#filtrado
corto_filtrado = df_corto.loc[df_corto['Tipo de Producto 43/'].isin([15,16,17,18,19,
						                                             21,22,23,24,25,29, 
                                                                     95,96,97,98,99])]
#tabla resumen de sumarización						                                          
tabla_resumen = corto_filtrado.groupby('Código Socio 7/')['monto mype'].sum()
tabla_resumen = tabla_resumen.reset_index()

#rename
tabla_resumen = tabla_resumen.rename(columns={"Código Socio 7/": "socio mype"})

#%%
#asignamos
df_resultado_2 = df_resultado.copy()

df_resultado_2 = df_resultado_2.merge(tabla_resumen[['socio mype','monto mype']], 
                                      how='left', 
                                      left_on=['Código Socio 7/'], 
                                      right_on=['socio mype'])

df_resultado_2['monto mype'] = df_resultado_2['monto mype'].fillna(0)

#%%
df_resultado_2['Tipo de Producto 43/'] = df_resultado_2['Tipo de Producto 43/'].astype(float)
def asignacion_mype(df_resultado_2):
    if df_resultado_2['Tipo de Producto 43/'] in [15,16,17,18,19,
        						                  21,22,23,24,25,29, 
   						                          95,96,97,98,99]:
        if df_resultado_2['monto mype'] <= 20200:
            return 20
        elif df_resultado_2['monto mype'] <= 300000:
            return 10
        else:
            return 90
    else:
        return df_resultado_2.loc['Tipo de Producto 43/']

df_resultado_2['producto_mype_2'] = df_resultado_2.apply(asignacion_mype, axis=1)
df_resultado_2['Tipo de Producto 43/'] = df_resultado_2['Tipo de Producto 43/'].truncate(0) #no está haciendo nada este código xd

#%%
#nos muestra si hay alguna diferencia en la parte de las decenas de la asignación del tipo de producto 43
df_resultado_2['resta_decenas'] = ((df_resultado_2['producto_mype_2'] // 10) - (df_resultado_2['Tipo de Producto 43/'] // 10))

#%%
'ahora que ya tenemos la diferencia del tipo de producto, asignamos el tipo de producto que deben de tener'
def asign_mype(df_resultado_2):
#    if (df_resultado_2['resta_decenas'] == 1):
#        if (df_resultado_2['Tipo de Producto 43/'] == 15):
#            return 22
#        elif (df_resultado_2['Tipo de Producto 43/'] == 16):
#            return 23
#        elif (df_resultado_2['Tipo de Producto 43/'] == 17):
#            return 24
#        elif (df_resultado_2['Tipo de Producto 43/'] == 18):
#            return 20 #no tiene equivalente
#        elif (df_resultado_2['Tipo de Producto 43/'] == 19):
#            return 29
    if (df_resultado_2['resta_decenas'] == -1):
        if (df_resultado_2['Tipo de Producto 43/'] == 21):
            return 16 #no tenía equivalente
        elif (df_resultado_2['Tipo de Producto 43/'] == 22):
            return 15
        elif (df_resultado_2['Tipo de Producto 43/'] == 23):
            return 16
        elif (df_resultado_2['Tipo de Producto 43/'] == 24):
            return 17
        elif (df_resultado_2['Tipo de Producto 43/'] == 25):
            return 10 #no hay equivalente
        elif (df_resultado_2['Tipo de Producto 43/'] == 29):
            return 19
    elif (df_resultado_2['resta_decenas'] == 8):
        if (df_resultado_2['Tipo de Producto 43/'] == 15):
            return 95 #no tiene equivalente
        elif (df_resultado_2['Tipo de Producto 43/'] == 16):
            return 96
        elif (df_resultado_2['Tipo de Producto 43/'] == 17):
            return 97
        elif (df_resultado_2['Tipo de Producto 43/'] == 18):
            return 98
        elif (df_resultado_2['Tipo de Producto 43/'] == 19):
            return 99
#    elif (df_resultado_2['resta_decenas'] == -8):
#        if (df_resultado_2['Tipo de Producto 43/'] == 95):
#            return 15 #no tiene equivalente
#        elif (df_resultado_2['Tipo de Producto 43/'] == 96):
#            return 16
#        elif (df_resultado_2['Tipo de Producto 43/'] == 97):
#            return 17
#        elif (df_resultado_2['Tipo de Producto 43/'] == 98):
#            return 18
#        elif (df_resultado_2['Tipo de Producto 43/'] == 99):
#            return 19
    else:
        return df_resultado_2.loc['Tipo de Producto 43/']

df_resultado_2['producto final'] = df_resultado_2.apply(asign_mype, axis=1)
df_resultado_2['Tipo de Producto 43/ corregido'] = df_resultado_2['producto final']

#esta columna tiene el tipo de producto43 ya corregido
#%%
#comprobación de las diferencias de tipo de producto
df_resultado_2['anterior'] = df_resultado_2['Tipo de Producto 43/']
df_resultado_2['producto final'] = pd.to_numeric(df_resultado_2['producto final'])
df_resultado_2['anterior'] = pd.to_numeric(df_resultado_2['anterior'])

def comprobac(df_resultado_2):
    if df_resultado_2['producto final'] - df_resultado_2['anterior'] != 0:
        return 'diferente'
    else:
        return '='
    
df_resultado_2['dif_prod'] = df_resultado_2.apply(comprobac, axis=1)

df_resultado_2['Tipo de Producto 43/'] = df_resultado_2['Tipo de Producto 43/ corregido']

   
#%%

df_resultado_2['Fecha Ultimo Pago'] = df_resultado_2['''Fecha Ultimo 
Pago TXT''']

#%%
#moviendo estas dos columnas al final

lista_columns = list(df_resultado_2.columns)
columna_a_mover = "periodo de gracia por Reprog inicio"
lista_columns.remove(columna_a_mover)
columna_a_mover = "periodo de gracia por Reprog Término"
lista_columns.remove(columna_a_mover)

# Agrega el nombre de la columna al final de la lista
columnas_nuevas = lista_columns + ["periodo de gracia por Reprog inicio"]
columnas_nuevas = columnas_nuevas + ["periodo de gracia por Reprog Término"]

# Reordena las columnas del DataFrame utilizando la nueva lista de nombres de columnas
df_resultado_2 = df_resultado_2.reindex(columns=columnas_nuevas)

#%%
#parseando datos

#aqui hay riesgo de perder fechas si es que están mal escritas
df_resultado_2["periodo de gracia por Reprog inicio"] = \
pd.to_datetime(df_resultado_2["periodo de gracia por Reprog inicio"], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df_resultado_2["periodo de gracia por Reprog inicio"] = df_resultado_2["periodo de gracia por Reprog inicio"].dt.date

df_resultado_2["periodo de gracia por Reprog Término"] = \
pd.to_datetime(df_resultado_2["periodo de gracia por Reprog Término"], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df_resultado_2["periodo de gracia por Reprog Término"] = df_resultado_2["periodo de gracia por Reprog Término"].dt.date

#%%
#fecha término de gracia por desembolso
def fechatermino(fecha, periodo_gracia):
    return fecha + pd.DateOffset(days=periodo_gracia)

df_resultado_2['fecha término de gracia por desembolso'] = df_resultado_2.apply(
    lambda x: fechatermino(x['Fecha de Desembolso 21/'], x['Periodo de Gracia 47/']), axis=1)

x = df_resultado_2[['fecha término de gracia por desembolso','Fecha de Desembolso 21/', 'Periodo de Gracia 47/']]


#%%
#DD vs DF
def DD_vs_DF(df_resultado_2):
    if pd.isna(df_resultado_2['fecha término de gracia por desembolso']):
        return df_resultado_2["periodo de gracia por Reprog Término"]
    elif pd.isna(df_resultado_2["periodo de gracia por Reprog Término"]):
        return df_resultado_2['fecha término de gracia por desembolso']
    else:
        return max(df_resultado_2['fecha término de gracia por desembolso'], df_resultado_2["periodo de gracia por Reprog Término"])

df_resultado_2['DD vs DF'] = df_resultado_2.apply(DD_vs_DF, axis=1)

#%%
#moviendo esa columna al final
df_resultado_2['''Fecha Venc de Ult Cuota Cancelada
Contabilidad''']= df_resultado_2['''Fecha Venc de Ult Cuota Cancelada
(NVO)''']

#%%
#cálculo de las columnas de fechas
df_resultado_2['Fecha Ultimo Pago'] = \
pd.to_datetime(df_resultado_2['Fecha Ultimo Pago'], 
               format='%Y-%m-%d %H:%M:%S', errors='coerce')
df_resultado_2['Fecha Ultimo Pago'] = df_resultado_2['Fecha Ultimo Pago'].dt.date

def DG_vs_BW(df_resultado_2):
    if pd.isna(df_resultado_2['DD vs DF']):
        return df_resultado_2['Fecha Ultimo Pago']
    elif pd.isna(df_resultado_2['Fecha Ultimo Pago']):
        return df_resultado_2['DD vs DF']
    else:
        return max(df_resultado_2['DD vs DF'], df_resultado_2['Fecha Ultimo Pago'])

df_resultado_2['DG vs BW'] = df_resultado_2.apply(DG_vs_BW, 
                                                  axis=1)

#%%
df_resultado_2['''Fecha Venc de Ult Cuota Cancelada
Contabilidad'''] = \
pd.to_datetime(df_resultado_2['''Fecha Venc de Ult Cuota Cancelada
Contabilidad'''], 
               format='%Y-%m-%d %H:%M:%S', errors='coerce')
df_resultado_2['''Fecha Venc de Ult Cuota Cancelada
Contabilidad'''] = df_resultado_2['''Fecha Venc de Ult Cuota Cancelada
Contabilidad'''].dt.date
#

df_resultado_2 = df_resultado_2.rename(columns={'''Fecha Venc de Ult Cuota Cancelada
Contabilidad''': '''Fecha Venc de Ult Cuota Cancelada Contabilidad'''})


#cálculo de DG vs BW con FVUCC
def con_fvucc(df_resultado_2):
    if pd.isna(df_resultado_2['Fecha Venc de Ult Cuota Cancelada Contabilidad']):
        return df_resultado_2['DG vs BW']
    else:
        return df_resultado_2['Fecha Venc de Ult Cuota Cancelada Contabilidad']

df_resultado_2['DG vs BW con FVUCC'] = df_resultado_2.apply(con_fvucc, 
                                                            axis=1)

#%%
#noup
fecha_fija = pd.to_datetime(fecha_corte)

# Definir función para aplicar a cada fila
def max_fecha(row):
    if pd.isna(row['DG vs BW con FVUCC']):
        return (fecha_fija - row['Fecha de Desembolso 21/']).days
    else:
        return max((fecha_fija - row['DG vs BW con FVUCC']).days, 0)
                   

# Aplicar la función a cada fila del DataFrame
df_resultado_2['DH vs CS'] = df_resultado_2.apply(max_fecha, axis=1)

#%%
#calculando 'DH vs CS'para los créditos que tienen días mora

def dh_vs_cs_morosos(row, dias_sumar):
    if row['Dias de Mora 33/'] > 0:
        return row['Dias de Mora 33/'] + dias_sumar
    else:
        return row['DH vs CS']

df_resultado_2['DH vs CS 2'] = df_resultado_2.apply(dh_vs_cs_morosos, 
                                                    axis=1,
                                                    args=(dias_corte,))


df_resultado_2['DH vs CS'] = df_resultado_2['DH vs CS 2']
df_resultado_2.drop(['DH vs CS 2'], axis=1, inplace=True)

#%%
#calculando DH vs CS para los que tienen capital vigente y vencido al mismo tiempo
def dh_vs_ambos(df_resultado_2, dias_sumar):
    if (df_resultado_2['Capital Vigente 26/'] > 0 and \
        df_resultado_2['Capital Vencido 29/'] > 0):
        return dias_sumar
    else:
        return df_resultado_2['DH vs CS']

df_resultado_2['DH vs CS 2'] = df_resultado_2.apply(dh_vs_ambos, 
                                                    axis=1,
                                                    args=(dias_corte,))

df_resultado_2['DH vs CS'] = df_resultado_2['DH vs CS 2']
df_resultado_2.drop(['DH vs CS 2'], axis=1, inplace=True)


#%%
'intereses devengados, calculados de manera genérica'
def devengados_genericos(df_resultado_2):
    if df_resultado_2['Número de Cuotas Programadas 44/'] != 1:
        return df_resultado_2['Capital Vigente 26/']* (\
       (((1+(df_resultado_2['Tasa Diaria']/100))**df_resultado_2['DH vs CS']))-1)
    elif df_resultado_2['Número de Cuotas Programadas 44/'] == 1:
        return df_resultado_2['Capital Vigente 26/']* (\
       (((1+(df_resultado_2['Tasa Diaria']/100))**float(max((fecha_fija - df_resultado_2['Fecha de Desembolso 21/']).days, 0))))-1)
    
            
df_resultado_2['rendimiento devengado'] = df_resultado_2.apply(devengados_genericos, axis=1)
df_resultado_2['rendimiento devengado'] = df_resultado_2['rendimiento devengado'].round(2)

df_resultado_2['''Rendimiento
Devengado 40/'''] = df_resultado_2['rendimiento devengado']



#%%
'intereses en suspenso, calculados de manera genérica'

fecha_fija = pd.to_datetime(fecha_corte)

import pandas as pd
from datetime import datetime

def dias_suspenso(row):
    # verificamos que las columnas 'Capital Vigente 26/' y 'Capital Vencido 29/' sean mayores que cero
    if (row['Capital Vigente 26/'] > 0) & (row['Capital Vencido 29/'] > 0):
        # si se cumple la condición, retornamos la columna 'Dias de Mora 33/'
        return row['Dias de Mora 33/']
    else:
        # si no se cumple la condición, calculamos la diferencia de días entre la fecha '28-03-2023' y la fecha en 'DG vs BW con FVUCC'
        fecha1 = datetime.strptime(fecha_corte, '%Y-%m-%d').date()
        fecha2 = row['DG vs BW con FVUCC'].strftime('%Y-%m-%d')
        fecha2 = datetime.strptime(fecha2, '%Y-%m-%d').date()
        dias_suspenso = (fecha1 - fecha2).days
        # retornamos el resultado
        return dias_suspenso

df_resultado_2['dias int suspenso'] = df_resultado_2.apply(dias_suspenso, axis=1)

#%% #reemplazando los negativos
def ceros(df_resultado_2):
    if df_resultado_2['dias int suspenso'] < 0:
        return 0
    else:
        return df_resultado_2['dias int suspenso']

df_resultado_2['dias int suspenso'] = df_resultado_2.apply(ceros, axis=1)

#%%
#última parte de los días en suspenso:
def ultima_dias_suspenso(df_resultado_2):
    fecha1 = datetime.strptime(fecha_corte, '%Y-%m-%d').date()
    fecha2 = df_resultado_2['DG vs BW con FVUCC'].strftime('%Y-%m-%d')
    fecha2 = datetime.strptime(fecha2, '%Y-%m-%d').date()

    if (fecha1 - fecha2).days < df_resultado_2['Dias de Mora 33/']:
        return df_resultado_2['Dias de Mora 33/'] + dias_corte
    else:
        return df_resultado_2['dias int suspenso']
    
df_resultado_2['dias int suspenso 2'] = df_resultado_2.apply(ultima_dias_suspenso, axis=1)

df_resultado_2['dias int suspenso'] = df_resultado_2['dias int suspenso 2']
df_resultado_2.drop(['dias int suspenso 2'], axis=1, inplace=True)

    
#%%
'intereses en suspenso'
def int_suspenso(df_resultado_2):
    return (df_resultado_2['Capital Vencido 29/'] + df_resultado_2['Capital en Cobranza Judicial 30/'])* (\
    (((1+(df_resultado_2['Tasa Diaria']/100))**df_resultado_2['dias int suspenso']))-1)

df_resultado_2['intereses en suspenso'] = df_resultado_2.apply(int_suspenso, axis=1)

df_resultado_2['''Intereses en Suspenso 41/'''] = df_resultado_2['intereses en suspenso']


#%%
'AHORA CALCULAR LOS INTERESES DIFERIDOS'
#necesario para poder calcular la cartera neta = 
#Saldo de colocaciones (créditos directos) 24/ - Ingresos Diferidos 42/
'algoritmo que nos tiene que explicar Jenny'

'de momento no se va a poder programar, no tenemos info, Jenny lo va a realizar, y tendremos que volver a procesar el archivo'
#%%
'AHORA QUE YA TENEMOS LOS INGRESOS DIFERIDOS'
#calculamos la cartera neta
def cartera_neta(df_resultado_2):
    return df_resultado_2['Saldo de colocaciones (créditos directos) 24/'] - \
        df_resultado_2['Ingresos Diferidos 42/']
        
df_resultado_2['Cartera Neta'] = df_resultado_2.apply(cartera_neta, axis=1)

#%%
#cálculo de provisiones requeridas 36 SA

df_resultado_2['Provisiones Requeridas 36/ SA'] = df_resultado_2['Cartera Neta'] * \
                                                  df_resultado_2['Tasa de Provisión SA']

#%%
#cálculo de las provisiones constituidas 37/
def prov_cons_37(df_resultado_2):
    if df_resultado_2['''Nro Prestamo 
Fincore'''] in ['00000681',
                '00025314',
                '00025678',
                '00001346',
                '00009592',
                '00050796',
                '00021245',
                '00014203',
                '00019911',
                '00052890',
                '00020153',
                '00000633',
                '00021016',
                '00000942',
                '00023215',
                '00020154',
                '00054955',
                '00016572',
                '00001147',
                '00001287',
                '00021994'
]:  
        return df_resultado_2['Provisiones Requeridas 36/ SA']
    else:
        return  df_resultado_2['Provisiones Requeridas 36/ SA'] * 0.60 # 0.50 es lo mínimo

df_resultado_2['Provisiones Constituidas 37/'] = df_resultado_2.apply(prov_cons_37, axis=1)

#%%


#%%
'VERIFICACIÓN'
#LAS PROVISIONES CONSTITUIDAS DEL MES, DEBEN SER (EN MONTO) MAYORES A LA DEL MES PASADO
#Y LAS PROVISIONES CONSTITUIDAS DIVIDIDAS ENTRE LAS PROVISIONES REQUERIDAS DEBE SER > 60%

suma_requeridas = df_resultado_2['Provisiones Requeridas 36/ SA'].sum()
suma_constituidas = df_resultado_2['Provisiones Constituidas 37/'].sum()

div = suma_constituidas/suma_requeridas
print('EL PORCENTAJE ES: ',"{:.2f}%".format(div*100))
print('constituidas mes pasado: 7881762.75')
print(suma_constituidas)


#%%
#añadiendo las columnas que Jenny necesita

df_resultado_2['FEC_REPROG'] = df_resultado_2['FEC_ULT_REPROG']

# reemplazar guiones con None
df_resultado_2['FEC_REPROG'] = df_resultado_2['FEC_REPROG'].replace('--', None)

# convertir a datetime
df_resultado_2['FEC_REPROG'] = pd.to_datetime(df_resultado_2['FEC_REPROG'], errors='coerce')

df_resultado_2['FEC_REPROG'] = df_resultado_2['FEC_REPROG'].fillna('--')

#%%
# añadiendo -- a algunas columnas de fechas, para que las fórmulas de excel funcionen bien

df_resultado_2['Fecha Ultimo Pago'] = df_resultado_2['Fecha Ultimo Pago'].fillna('--')

#%%
#redondeando columnas 
df_resultado_2['rendimiento devengado'] = df_resultado_2['rendimiento devengado'].round(2)
df_resultado_2['intereses en suspenso'] = df_resultado_2['intereses en suspenso'].round(2)

#%%
df_resultado_2['TEA TXT'] = df_resultado_2['Tasa de Interés Anual 23/'].round(4)

#%%
'''
x = df_resultado_2.columns
df_x = pd.DataFrame(x, columns=['columnas'])

# exportar el dataframe a un archivo de Excel
df_x.to_excel('columnas.xlsx', index=False)
'''

columnas_casi_final = ['''Socios al menos con un cred < 100 soles\namarillo = cred <100\nrosado = cred >= 100\n PROV.REQUERIDA A SER EVALUADA.''',
'''Registro 1/''',
'''Apellidos y Nombres / Razón Social 2/''',
'''Fecha de Nacimiento 3/''',
'''Género 4/''',
'''Estado Civil 5/''',
'''Sigla de la Empresa 6/''',
'''Código Socio 7/''',
'''Partida Registral 8/''',
'''Tipo de Documento 9/''',
'''Número de Documento 10/''',
'''Tipo de Persona 11/''',
'''Domicilio 12/''',
'''Relación Laboral con la Cooperativa 13/''',
'''Tasa de Provisión SA''',
'''Clasificación del Deudor 14/''',
'''Clasificación del Deudor con Alineamiento 15/ ORIGINAL''',
'''Clasificación del Deudor con Alineamiento 15/''',
'''Tasa de Provisión''',
'''Código de Agencia 16/''',
'''Moneda del crédito 17/''',
'''Numero de Crédito 18/''',
'''Tipo de Crédito 19/''',
'''Sub Tipo de Crédito 20/''',
'''Fecha de Desembolso 21/''',
'''Monto de Desembolso Origuinal TXT''',
'''Monto de Desembolso 22/''',
'''Tasa de Interés Anual 23/''',
'''Saldo de colocaciones (créditos directos) 24/''',
'''Cuenta Contable 25/''',
'''Capital Vigente 26/''',
'''Capital Reestrucutado 27/''',
'''Capital Refinanciado 28/''',
'''Capital Vencido 29/''',
'''Capital en Cobranza Judicial 30/''',
'''Cartera Atrasada''',
'''Capital Contingente 31/''',
'''Cuenta Contable Capital Contingente 32/''',
'''Dias de Mora 33/''',
'''Saldos de Garantías Preferidas 34/''',
'''Saldo de Garantías Autoliquidables 35/''',
'''Provisiones Requeridas 36/ SA''',
'''Provisiones Requeridas 36/''',
'''Provisiones Constituidas 37/''',
'''Saldos de Créditos Castigados 38/''',
'''Cuenta Contable Crédito Castigado 39/''',
'''Rendimiento
Devengado 40/''',
'''Intereses en Suspenso 41/''',
'''Ingresos Diferidos 42/''',
'''Tipo de Producto 43/ original''',
'''Tipo de Producto 43/''',
'''Número de Cuotas Programadas 44/''',
'''Número de Cuotas Pagadas 45/''',
'''Periodicidad de la cuota 46/''',
'''Periodo de Gracia 47/''',
'''Fecha de Vencimiento Origuinal del Credito 48/''',
'''Fecha de Vencimiento Actual del Crédito 49/''',
'''Saldo de Créditos con Sustitución de Contraparte Crediticia 50/''',
'''Saldo de Créditos que no cuentan con cobertura 51/''',
'''Saldo Capital de Créditos Reprogramados 52/''',
'''Saldo Capital en Cuenta de Orden por efecto del Covid 53/''',
'''Subcuenta de orden 
54/
''',
'''Rendimiento Devengado por efecto del COVID 19 55/''',
'''Saldo de Garantías con Sustitución de Contraparte 56/''',
'''Saldo Capital de Créditos Reprogramados por efecto del COVID 19 57/''',
'''FEC_ULT_REPROG''',
'''PLAZO_REPR''',
'''TIPO_REPRO''',
'''PLAZO REPRO ACUMULADO''',
'''NRO CUOTAS REPROG CANCELADAS''',
'''NRO REPROG''',
'''fecha desemb (v)''',
'''fecha término de gracia por desembolso ["v" + dias gracia (av)]''',
'''Fecha Venc de Ult Cuota Cancelada
(NVO)''',
'''Categoria TXT''',
'''Saldo Colocacion Con Capitalizacion de Intereses TXT''',
'''Fecha Castigo TXT''',
'''Dscto Enviado TXT''',
'''Desc Pagado TXT''',
'''Fecha Vencimiento 
Origuinal TXT''',
'''Fecha Vencimiento Actual TXT''',
'''Fecha Creacion Reprogramacion Nacimiento TXT''',
'''Fecha Creacion Reprogramacion Corte TXT''',
'''Nro Dias Gracia Corte RPG TXT''',
'''Nro Cuotas Canc Post Regro''',
'''Nro Prestamos X Deudor TXT''',
'''Fecha Ultimo 
Pago TXT''',
'''Nro Dias Gracia Acumulado RPG TXT''',
'''Tipo Reprogramacion TXT''',
'''Fecha Primer Cuota Gracia Nacimiento RPG TXT''',
'''Primer Fecha Cuota Gracia Corte RPG TXT''',
'''Nro Reprogramaciones TXT''',
'''Origen
 Prestamo''',
'''Nro Prestamo 
Fincore''',
'''Por Cobrar Mes Actual TXT''',
'''Reprogramado TXT''',
'''Funcionaria TXT''',
'''Nombre Empresa TXT''',
'''Nombre PlanillaTXT''',
'''Planilla Anterior TXT''',
'''Cod Usuario Pri Aprob''',
'''Cod Usuario Seg Aprob''',
'''Profesion''',
'''Ocupacion''',
'''Actividad Economica''',
'''Fecha Venc Ult Cuota Cancelada''',
'''Interes
Devengado Total''',
'''Interes 
Suspenso Total''',
'''Departamento''',
'''Provincia''',
'''Distrito''',
'''Tipo Credito TXT''',
'''TEA TXT''',
'''Refinanciado TXT''',
'''Situacion TXT''',
'''Fecha Situacion TXT''',
'''Abogado TXT''',
'''Fecha Asignacion Abogado TXT''',
'''Nro Expediente TXT''',
'''Fecha Expediente TXT''',
'''Tasa Clasificacion Deudor con Alineamiento TXT''',
'''Monto de Garantías Preferidas''',
'''Monto de Garantías Autoliquidables''',
'''Importe Vencido > 60d
(Solo DxP)''',
'''Dias vencido (Solo DxP)''',
'''Porción Vencido''',
'''Situación del Credito (Solo DxP)''',
'''Tasa Diaria''',
'''Fecha Ultimo Pago''',
'''periodo de gracia por Reprog inicio''',
'''periodo de gracia por Reprog Término''',
'''fecha término de gracia por desembolso''',
'''DD vs DF''',
'''Fecha Venc de Ult Cuota Cancelada Contabilidad''',
'''DG vs BW''',
'''DG vs BW con FVUCC''',
'''DH vs CS''',
'''rendimiento devengado''',
'dias int suspenso',
'''intereses en suspenso''',
'''Cartera Neta''',
'''FEC_REPROG''']
anexo06_casi = df_resultado_2[columnas_casi_final]

#%%
#agregando las 2 nuevas columnas establecidas por la sbs
#Saldo Capital en Cuenta de Orden Programa IMPULSO MYPERU 58/	Rendimiento Devengado por Programa IMPULSO MYPERU 59/

#al añadir estas columnas debemos modificar las formulas en excel
anexo06_casi['Saldo Capital en Cuenta de Orden Programa IMPULSO MYPERU 58/'] = '' 
anexo06_casi['Rendimiento Devengado por Programa IMPULSO MYPERU 59/'] = '' 

#%%

'CREACIÓN DEL EXCEL'
nombre = "ANX06 devengados" + fecha_corte + ".xlsx"
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

anexo06_casi.to_excel(nombre,
                      index=False)

#%%
# POR SI NO SABEMOS DÓNDE ESTÁN LOS ARCHIVOS
# Obtener la ubicación actual
ubicacion_actual = os.getcwd()

# Imprimir la ubicación actual
print("La ubicación actual es: " + ubicacion_actual)


#%%
#######################################################
#██████╗  █████╗ ██████╗ ████████╗███████╗    ██████╗ #
#██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝    ╚════██╗#
#██████╔╝███████║██████╔╝   ██║   █████╗       █████╔╝#
#██╔═══╝ ██╔══██║██╔══██╗   ██║   ██╔══╝      ██╔═══╝ #
#██║     ██║  ██║██║  ██║   ██║   ███████╗    ███████╗#
#╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝#
#######################################################                                                                                                                                                                                                 
'UNA VEZ QUE JENNY NOS DE EL ANEXO 06 CON LOS INTERESES DIFERIDOS:'

#%%
#leyendo el excel que nos envía CONTABILIDAD
os.chdir('C:\\Users\\sanmiguel38\\Desktop\\TRANSICION  ANEXO 6\\2023 marzo') #cambiar ubicación

df_diferidos = pd.read_excel('Rpt_DeudoresSBS_Marzo 2023 HT version 01 enviado por contabilidad.xlsx',
                 dtype={'Registro 1/': object, 
                        'Fecha de Nacimiento 3/': object,
                        'Código Socio 7/':object, 
                        'Número de Documento 10/': object,
                        'Relación Laboral con la Cooperativa 13/':object, 
                        'Código de Agencia 16/': object,
                        'Moneda del crédito 17/':object, 
                        'Numero de Crédito 18/': object,
                        'Tipo de Crédito 19/': object,
                        'Sub Tipo de Crédito 20/': object,
                        'Fecha de Desembolso 21/': object,
                        'Cuenta Contable 25/': object,
                        'Tipo de Producto 43/': object,
                        'Fecha de Vencimiento Origuinal del Credito 48/': object,
                        'Fecha de Vencimiento Actual del Crédito 49/': object,
                        '''Nro Prestamo 
Fincore''': object},
                     skiprows=1
                     )

df_diferidos.dropna(subset=['Apellidos y Nombres / Razón Social 2/', 
                   'Fecha de Nacimiento 3/',
                   'Número de Documento 10/',
                   'Domicilio 12/',
                   'Numero de Crédito 18/'], inplace=True, how= 'all') 

#%%
#chequear si es que los diferidos NO están en la columna 42/

df_diferidos['Ingresos Diferidos 42/'].sum()

df_diferidos['Ingresos Diferidos 42/'] = df_diferidos['Ingresos Diferidos 2']

df_diferidos['Ingresos Diferidos 42/'] = df_diferidos['Ingresos Diferidos 42/'].round(2)

#%%
'AHORA QUE YA TENEMOS LOS INGRESOS DIFERIDOS'
#calculamos la cartera neta
def cartera_neta(df_diferidos):
    return df_diferidos['Saldo de colocaciones (créditos directos) 24/'] - \
        df_diferidos['Ingresos Diferidos 42/']
        
df_diferidos['Cartera Neta'] = df_diferidos.apply(cartera_neta, axis=1)

df_diferidos['Cartera Neta'].sum()

#%%
#cálculo de provisiones requeridas 36

df_diferidos['Provisiones Requeridas 36/'] = df_diferidos['Cartera Neta'] * \
                                                  df_diferidos['Tasa de Provisión']

df_diferidos['Provisiones Requeridas 36/'].sum()
                                                
#%%
#cálculo de las provisiones constituidas 37/
def prov_cons_37(df_diferidos):
    if df_diferidos['''Nro Prestamo 
Fincore'''] in ['00000681',
                '00025314',
                '00025678',
                '00001346',
                '00009592',
                '00050796',
                '00021245',
                '00014203',
                '00019911',
                '00052890',
                '00020153',
                '00000633',
                '00021016',
                '00000942',
                '00023215',
                '00020154',
                '00054955',
                '00016572',
                '00001147',
                '00001287',
                '00021994'
]:  
        return df_diferidos['Provisiones Requeridas 36/']
    else:
        return  df_diferidos['Provisiones Requeridas 36/'] * 0.585 # 0.50 es lo mínimo

df_diferidos['Provisiones Constituidas 37/'] = df_diferidos.apply(prov_cons_37, axis=1)

df_diferidos['Provisiones Constituidas 37/'] = df_diferidos['Provisiones Constituidas 37/'].round(2)

#%%%%
#sin redondear marzo
#df_diferidos['Provisiones Requeridas 36/'].sum()     11919296.21076
#df_diferidos['Provisiones Constituidas 37/'].sum()    7891147.647244599
#df_diferidos['Provisiones Constituidas 37/'].sum()    7891142.25

#si primero redondeamos las provisiones requeridas
#df_diferidos['Provisiones Requeridas 36/'].sum()     11919296.38
#df_diferidos['Provisiones Constituidas 37/'].sum()    7891147.746249999
#df_diferidos['Provisiones Constituidas 37/'].sum()    7891142.67


#%%
'VERIFICACIÓN'
#LAS PROVISIONES CONSTITUIDAS DEL MES, DEBEN SER (EN MONTO) MAYORES A LA DEL MES PASADO
#Y LAS PROVISIONES CONSTITUIDAS DIVIDIDAS ENTRE LAS PROVISIONES REQUERIDAS DEBE SER > 60%

suma_requeridas = df_diferidos['Provisiones Requeridas 36/ SA'].sum()
suma_constituidas = df_diferidos['Provisiones Constituidas 37/'].sum()

div = suma_constituidas/suma_requeridas
print('EL PORCENTAJE ES: ',"{:.2f}%".format(div*100))

#%%
#comparando provisiones constituidas contra el del mes pasado
'AQUI HAY QUE CAMBIAR LA FECHA PARA QUE VAYA DEL MES PASADO al que estamos elaborando'

conn = pyodbc.connect('DRIVER=SQL Server;SERVER=(local);UID=sa;Trusted_Connection=Yes;APP=Microsoft Office 2016;WSID=SM-DATOS')
provisiones_mes_pasado = pd.read_sql_query('''
declare @fechacorte as datetime
set @fechacorte = '20230228'

select sum(ProvisionesConstituidas37) as 'ProvisionesConstituidas37' 
from anexos_riesgos2..Anx06_preliminar
where FechaCorte1 = @fechacorte''', conn)

mes_pasado = provisiones_mes_pasado.loc[0, 'ProvisionesConstituidas37']

#%%

if mes_pasado < suma_constituidas:
    print('todo bien')
    print('mes actual: ', int(suma_constituidas))
    print('mes pasado: ', int(mes_pasado))
else:
    print('todo mal')
    print('mes actual: ', int(suma_constituidas))
    print('mes pasado: ', int(mes_pasado))
    
print('diferencia:  '+ str(suma_constituidas - mes_pasado))

calculo_que_pidio_enrique = suma_constituidas / (df_diferidos['Capital Vencido 29/'].sum() + df_diferidos['Capital en Cobranza Judicial 30/'].sum())
print("{:.2f}%".format(calculo_que_pidio_enrique*100))


#%%

'CREACIÓN DEL EXCEL'
nombre = "ANX06 con instereses en suspenso " + fecha_corte + ".xlsx"
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

df_diferidos.to_excel(nombre,
                      index=False)

#%%
'hay que convertir a fechas:'

# D, Y, BD, BE, BN, BT, BU, BV, CB, CC, CD, CE, CL, CM, DB, DL, DN, DP
# DY, DZ, EA, EB, EC, ED, EE, EF, EL


#faltan agregar algunas columnas como el funcionario originador
#también el departamento, distrito y provincia del negocio



