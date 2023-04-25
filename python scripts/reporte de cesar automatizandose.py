# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

#%%

#IMPORTANDO LOS DATOS DE EXCEL

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

#    '%Y-%m-%d %H:%M:%S.%f'
    
# 1 el primero es la base de datos aún por procesar
df1=pd.read_excel("C:\\Users\\sanmiguel38\\Desktop\\reporte automatizado diciembre\\Saldo Gral SM-202212 - Insumo.xlsx",
                 dtype={'CodigoSocio': object, 'NroDocIdentidad': object,
                       'NumeroPrestamo':object, 'NroPrestamoFC': object,
                       'TlfSocio':object, 'CelularSocio': object,
                       'TipoCredito':object, 'SubTipoCredito': object}

                ,parse_dates=['FechaDesembolsoTXT'  #AQUI SI SE HA PROCESADO
                              # ,'FechaAsignacionAbogadoTXT'  #no procesado
                              # ,'FechaExpedienteTXT'         #no procesado
                              # ,'FechaAsignacion'            #no procesado
                              # ,'JFechaCastigo'              #no procesado
                              # ,'JFechaVentaCartera'         #no procesado
                              # ,'FechaProcesoSistemaTXT'     #no procesado
                             ],
                   date_parser=parse_date)
#df1 = df1.drop(9123) #esta partque habría que eliminar para el próximo mes

# 2 aqui va el reporte del mes pasado
df2=pd.read_excel("C:\\Users\\sanmiguel38\\Desktop\\reporte automatizado diciembre\\anteriores\\SALDO_COOPACSANMIGUEL - NOVIEMBRE-22_INC_CVV_DETALLADO Final (2).xlsx",
                  skiprows=1, #aqui podrían haber cambios dependiendo de dónde están las columnas con los nombres
                  dtype={'NroDocIdentidad': object,
                         'NumeroPrestamo':object,
                         'NroPrestamoFC': object})

for i in range (21073,21093):
    df2 = df2.drop(i)


#del i
#df2 = df2.drop(9123) #esta parte habría que eliminar para el próximo mes
#df2 = df2.drop(9124) #esto también hay que eliminar


# 3 ESTE TERCER ARCHIVO ES LA COBRANZA DEL MES
df3_cobranza = pd.read_excel("C:\\Users\\sanmiguel38\\Desktop\\archivos cesar\\noviembre\\Cobranza nov22 - para joseph.xlsx",
                 dtype={'codigosocio': object, 'doc_ident': object,
                       'PagareFincore':object} )


# 4 el reporte 'Utilidad año castigo 2018 2019 2020 y 2021 - JGM para añadir a Saldos e Ingresos'

df4_JGM_año_castigo = pd.read_excel("C:\\Users\\sanmiguel38\\Desktop\\archivos cesar\\noviembre\\Utilidad año castigo 2018 2019 2020 y 2021 - JGM para añadir a Saldos e Ingresos.xlsx",
                 dtype={'Numero Prestamo (Fox/Pond)': object, 'Nro Prestamo Fincore': object})

JGM_año_castigo =  df4_JGM_año_castigo[['Nro Prestamo Fincore', 'año castigo utilidad JGM']] #esta es la versión para hacer el merge

                        
#%%

dff1 = df1.copy() #dff1 será la copa de seguridad para no estar repitiendo
dff2 = df2.copy() #para no estar repitiendo el insertado de datos
dff3 = df3_cobranza.copy() #copia de seguridad

#df1 = dff1.copy()
#df2 = dff2.copy()
#df3_cobranza = dff3.copy()

#%%

#df1 = df1.drop(columns=['CodPrestamoTXT'])
df1 = df1.rename(columns={"Finalidad": "Finalidad TXT"})
df2["CodFinalidad"] = df2["CodFinalidad"].astype(str)
df2_finalidad = df2[["NroPrestamoFC", "CodFinalidad"]] #aquí revisar si tiene el nombre 'CodFinalidad' o 'Finalidad' a secas


df_resultado = df1.merge(df2_finalidad, 
                         left_on=["NroPrestamoFC"], 
                         right_on=["NroPrestamoFC"]
                         ,how='left')
############################
'aqui se duplicó un crédito'
############################

#%%
'''
#codigo que primero me funcionó pero ya no
def finalidad_producto(df_resultado):
    if pd.isnull(df_resultado['Finalidad']):
        if df_resultado['Finalidad TXT'].str.contains('LIBRE DISPONIBILIDAD').any() and df_resultado['TipoCreditoTXT'].str.contains('CONSUMO NO REVOLVENTE').any():
            return '30'
        elif df_resultado['Finalidad TXT'].str.contains('INDEPENDIENTES - OTROS').any() and df_resultado['TipoCreditoTXT'].str.contains('CONSUMO NO REVOLVENTE').any():
            return '30'
        elif df_resultado['Finalidad TXT'].str.contains('COMPRA DE PRODUCTO-BAZAR').any() and df_resultado['TipoCreditoTXT'].str.contains('CONSUMO NO REVOLVENTE').any():
            return '36'    
        elif df_resultado['Finalidad TXT'].str.contains('GARANTIA HIPOTECARIA').any():
            return '41'
        elif df_resultado['Finalidad TXT'].str.contains('ACTIVO FIJO').any() and df_resultado['TipoCreditoTXT'].str.contains('PEQUEÑA EMPRESAS').any():
            return '15'
        elif df_resultado['Finalidad TXT'].str.contains('CONSUMO ORDINARIO').any() and df_resultado['TipoCreditoTXT'].str.contains('MEDIANAS EMPRESAS').any():
            return '19'
        elif df_resultado['Finalidad TXT'].str.contains('CAPITAL DE TRABAJO').any() and df_resultado['TipoCreditoTXT'].str.contains('MEDIANAS EMPRESAS').any():
            return '19'    
        elif df_resultado['Finalidad TXT'].str.contains('ACTIVO FIJO').any() and df_resultado['TipoCreditoTXT'].str.contains('MEDIANAS EMPRESAS').any():
            return '16'
        #no olvidar que aquí hay 2 negaciones
        elif ~df_resultado['Finalidad TXT'].str.contains('GARANTIA HIPOTECARIA').any() and df_resultado['TipoCreditoTXT'].str.contains('MICROEMPRESAS').any():
            return '25'    
        elif ~(df_resultado['Finalidad TXT'].str.contains('LIBRE DISPONIBILIDAD').any() and df_resultado['Finalidad TXT'].str.contains('INDEPENDIENTES - OTROS').any()) and df_resultado['TipoCreditoTXT'].str.contains('CONSUMO NO REVOLVENTE').any():
            return '34'
        elif (df_resultado['Finalidad TXT'].str.contains('COMPRA DE SERVICIOS / OTROS').any() or df_resultado['Finalidad TXT'].str.contains('COMPRA DE PRODUCTO-BAZAR').any()) and df_resultado['TipoCreditoTXT'].str.contains('CONSUMO NO REVOLVENTE').any():
            return '39'
        elif df_resultado['Finalidad TXT'].str.contains('COMPRA DE PRODUCTO-BAZAR').any() and df_resultado['TipoCreditoTXT'].str.contains('CONSUMO NO REVOLVENTE').any():
            return '45'    

    else:
        return df_resultado['Finalidad']
    '''

#aqui hay que quitar comentario
'''
#5
def finalidad_producto(df_resultado):
    if pd.isnull(df_resultado['CodFinalidad']):
        if 'LIBRE DISPONIBILIDAD' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '30'
        elif 'INDEPENDIENTES - OTROS' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '30'
        elif 'COMPRA DE PRODUCTO-BAZAR' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '36'    
        elif 'GARANTIA HIPOTECARIA' in df_resultado['Finalidad TXT']:
            return '41'
        elif 'ACTIVO FIJO' in df_resultado['Finalidad TXT'] and 'PEQUEÑA EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '15'
        elif 'CONSUMO ORDINARIO' in df_resultado['Finalidad TXT'] and 'MEDIANAS EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '19'
        elif 'CAPITAL DE TRABAJO' in df_resultado['Finalidad TXT'] and 'MEDIANAS EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '19'    
        elif 'ACTIVO FIJO' in df_resultado['Finalidad TXT'] and 'MEDIANAS EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '16'
        #no olvidar que aquí hay negaciones
        elif ('GARANTIA HIPOTECARIA' not in df_resultado['Finalidad TXT']) and 'MICROEMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '25'
        elif ~('LIBRE DISPONIBILIDAD' in df_resultado['Finalidad TXT'] and 'INDEPENDIENTES - OTROS' in df_resultado['Finalidad TXT']) and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '34'
        elif ('COMPRA DE SERVICIOS / OTROS' in df_resultado['Finalidad TXT'] or 'COMPRA DE PRODUCTO-BAZAR' in df_resultado['Finalidad TXT']) and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '39'
        elif 'COMPRA DE PRODUCTO-BAZAR' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '45'
        elif 'PEQUEÑA EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '15'
        else:
            return 'investigar'
    else:
        return df_resultado['CodFinalidad']
    


df_resultado['CodFinalidad'] = df_resultado.apply(finalidad_producto, axis=1)
"hasta aquí está asignado el tipo de producto de la columna 'Finalidad'"
'''
#%%

df_resultado['CodFinalidad']= np.nan

def finalidad_producto(df_resultado):
    if pd.isnull(df_resultado['CodFinalidad']):
        if 'LIBRE DISPONIBILIDAD' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '30'
        elif 'INDEPENDIENTES - OTROS' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '30'
        elif 'COMPRA DE PRODUCTO-BAZAR' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '36'    
        elif 'GARANTIA HIPOTECARIA' in df_resultado['Finalidad TXT']:
            return '41'
        elif 'ACTIVO FIJO' in df_resultado['Finalidad TXT'] and 'PEQUEÑA EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '15'
        elif 'CONSUMO ORDINARIO' in df_resultado['Finalidad TXT'] and 'MEDIANAS EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '19'
        elif 'CAPITAL DE TRABAJO' in df_resultado['Finalidad TXT'] and 'MEDIANAS EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '19'    
        elif 'ACTIVO FIJO' in df_resultado['Finalidad TXT'] and 'MEDIANAS EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '16'
        #no olvidar que aquí hay negaciones
        elif ('GARANTIA HIPOTECARIA' not in df_resultado['Finalidad TXT']) and 'MICROEMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '25'
        elif ~('LIBRE DISPONIBILIDAD' in df_resultado['Finalidad TXT'] and 'INDEPENDIENTES - OTROS' in df_resultado['Finalidad TXT']) and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '34'
        elif ('COMPRA DE SERVICIOS / OTROS' in df_resultado['Finalidad TXT'] or 'COMPRA DE PRODUCTO-BAZAR' in df_resultado['Finalidad TXT']) and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '39'
        elif 'COMPRA DE PRODUCTO-BAZAR' in df_resultado['Finalidad TXT'] and 'CONSUMO NO REVOLVENTE' in df_resultado['TipoCreditoTXT']:
            return '45'
        elif 'PEQUEÑA EMPRESAS' in df_resultado['TipoCreditoTXT']:
            return '15'
        else:
            return 'investigar'
    else:
        return df_resultado['CodFinalidad']
    
df_resultado['CodFinalidad'] = df_resultado.apply(finalidad_producto, axis=1)


#%%

df_resultado2 = df_resultado.copy()

# Crear máscara booleana que indica cuáles filas cumplen la condición
mask = df_resultado2['MonedaTXT'].eq('US$')

# Seleccionar solo las filas que cumplen la condición y asignarles el resultado de la división
df_resultado2.loc[mask, 'SoloCapitalAmortizado']         = df_resultado2.loc[mask, 'SoloCapitalAmortizado']           / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'SaldoCapital']                  = df_resultado2.loc[mask, 'SaldoCapital']                    / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'InteresVencidoPactado']         = df_resultado2.loc[mask, 'InteresVencidoPactado']           / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'InteresPactadoPagado']          = df_resultado2.loc[mask, 'InteresPactadoPagado']            / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'SoloSaldoInteresVencido']       = df_resultado2.loc[mask, 'SoloSaldoInteresVencido']         / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'Saldo Deudor (Sobre la Cuota)'] = df_resultado2.loc[mask, 'Saldo Deudor (Sobre la Cuota)']   / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'InteresCompensatorioDeuda']     = df_resultado2.loc[mask, 'InteresCompensatorioDeuda']       / df_resultado2.loc[mask, 'TipoCambioTXT']
df_resultado2.loc[mask, 'InteresMoratorioDeuda']         = df_resultado2.loc[mask, 'InteresMoratorioDeuda']           / df_resultado2.loc[mask, 'TipoCambioTXT']

#con esto ya están divididas esas columnas entre el tipo de cambio si es que están en dólares
#%%
df_resultado3 = df_resultado2.copy()

def capitalizado(df_resultado3):
    if round(df_resultado3['MontoSolicitadoTXT'] - df_resultado3['SoloCapitalAmortizado'],2) < round(df_resultado3['SaldoCapital'],2):
        return 'CAPITALIZADO'
    elif round(df_resultado3['MontoSolicitadoTXT'] - df_resultado3['SoloCapitalAmortizado'],2) > round(df_resultado3['SaldoCapital'],2):
        return 'revisar'

    else:
        return ''

df_resultado4 = df_resultado3.copy()
df_resultado4['CRED CON CAPITALIZ'] = df_resultado3.apply(capitalizado, axis=1)
    
df4 = df_resultado4.copy()
mask2 = df4['CRED CON CAPITALIZ'].eq('revisar')


df4['MontoSolicitadoTXT'] = round(df4['MontoSolicitadoTXT'],2)
df4['SoloCapitalAmortizado'] = round(df4['SoloCapitalAmortizado'],2)
df4['SaldoCapital'] = round(df4['SaldoCapital'],2)


df4.loc[mask2, 'SaldoCapital'] = round(df4.loc[mask2, 'MontoSolicitadoTXT'] - df4.loc[mask2, 'SoloCapitalAmortizado'],2)

df4['CRED CON CAPITALIZ'] = df4['CRED CON CAPITALIZ'].replace('revisar', '')


df4['Nuevo Saldo'] = df4['Saldo Deudor (Sobre la Cuota)']+df4['InteresCompensatorioDeuda']+df4['InteresMoratorioDeuda']
#%%
'siguiente fase'

#suma group by de la tabla donde está la cobranza del mes actual
df_sum_capital = df3_cobranza.groupby('PagareFincore')['Capital'].sum().reset_index()
df_sum_INT_OTROS = df3_cobranza.groupby('PagareFincore')['Int y Otros'].sum().reset_index()
df_sum_INT_OTROS = df_sum_INT_OTROS.rename({'Int y Otros': 'Int y Otros mes actual'}, axis=1)

#esto es del mes pasado
#separo las columnas de nro de 'fincore' y 'IMPTE CASTIGADO (Asignado x PGB)' del mes pasado, para hacer un merge
df_cosas_mes_pasado = df2[["NroPrestamoFC", 'IMPTE CASTIGADO (Asignado x PGB)', 'FECHA DE CASTIGO', 
                           'Capital Amortizado', 'Int y Otros']]

#este codigo es para comprobar que sí está bien el resultado
#df_sum.where(df_sum['PagareFincore'] == '00083701').dropna(how='all')

"Merge de la tabla en bruto con la de cosas del reporte del mes pasado"
df5 = df4.merge(df_cosas_mes_pasado, 
                         left_on=["NroPrestamoFC"], 
                         right_on=["NroPrestamoFC"]
                         ,how='left')

"Merge de la tabla en bruto con el capital de la cobranza del mes actual"
df5 = df5.merge(df_sum_capital, 
                         left_on=["NroPrestamoFC"], 
                         right_on=["PagareFincore"]
                         ,how='left')

"Merge de la tabla en bruto con el int de la cobranza del mes actual"
df5 = df5.merge(df_sum_INT_OTROS, 
                         left_on=["NroPrestamoFC"], 
                         right_on=["PagareFincore"]
                         ,how='left')

'eliminando los NaN'
df5['Capital'].fillna(0, inplace=True)
df5['Int y Otros'].fillna(0, inplace=True)
df5['IMPTE CASTIGADO (Asignado x PGB)'].fillna(0, inplace=True)
df5['FECHA DE CASTIGO'].fillna(0, inplace=True)
df5['Capital Amortizado'].fillna(0, inplace=True)
df5['Int y Otros mes actual'].fillna(0, inplace=True)

df6 = df5.copy()


mascara = df5['IMPTE CASTIGADO (Asignado x PGB)'] != 0

df6.loc[mascara, 'Capital Amortizado'] = df6.loc[mascara, 'Capital Amortizado']+df6.loc[mascara, 'Capital']
df6.loc[mascara, 'Int y Otros'] = df6.loc[mascara, 'Int y Otros']+df6.loc[mascara, 'Int y Otros mes actual']
#hasta aqui ya está sumado el capital amortizado y el 'interés' de este mes con el mes pasado
#, y filtrado según saldo castigado

############################
'aqui se duplicaron dos créditos (ya van 4)'
############################

#%%
#sumar y restar
df6['Total Amortizado'] = df6['Capital Amortizado']+ df6['Int y Otros']
df6['SALDO CASTIGADO'] = df6['IMPTE CASTIGADO (Asignado x PGB)'] - df6['Total Amortizado']
df6.loc[mascara, 'SALDO DEUDOR REALISTA (SOLO PARA PGB)'] = df6.loc[mascara, 'Capital Amortizado']+df6.loc[mascara, 'Capital']

#df6.loc[mascara, 'columna'] = df6['columna5'].where(mascara, df6['columna6'])                  
df6['booleando'] = mascara


def asignar_saldo_deudor(df6):
  if df6['IMPTE CASTIGADO (Asignado x PGB)']:
    return df6['SALDO CASTIGADO']
  else:
    return df6['Nuevo Saldo']

df6['SALDO DEUDOR REALISTA (SOLO PARA PGB)'] = df6.apply(asignar_saldo_deudor, axis=1)

#ya está llenado hasta esta columna SALDO DEUDOR REALISTA (SOLO PARA PGB)


#%%
df2_observ_v_garantia = df2[['NroPrestamoFC','OBSERVACION','VALOR GARANTIA']].copy()
df2_observ_v_garantia['OBSERVACION'].fillna('--', inplace=True) #REEMPLAZANDO LOS NaN por --
df2_observ_v_garantia['VALOR GARANTIA'].fillna(0, inplace=True) #reemp



df6 = df6.rename(columns={'VALOR GARANTIA': 'VALOR GARANTIA ANTIGUA'})
df6 = df6.rename(columns={'OBSERVACION': 'OBSERVACION ANTIGUA'})

df6 = df6.merge(df2_observ_v_garantia, 
                         left_on=["NroPrestamoFC"], 
                         right_on=["NroPrestamoFC"]
                         ,how='left')

############################
'aqui se duplicó un crédito'
############################



#df6[['VALOR GARANTIA','OBSERVACION']]

# hasta aquí ya está el valor garantía
#%%
dff6 = df6.copy()
def saldo_real_vs_deudor(dff6):
    if dff6['VALOR GARANTIA'] > 0:
        if dff6['VALOR GARANTIA'] < dff6['Nuevo Saldo']:
            return dff6['VALOR GARANTIA']
        else:
            return dff6['Nuevo Saldo']
    else:
        return dff6['Nuevo Saldo']
    
dff6['SALDO REAL (S.DEUDOR Vs. GARANTIA)'] = dff6.apply(asignar_saldo_deudor, axis=1)

#solo para chequear
#%%

df7 = dff6.copy()
def alerta(df7):
    if df7['SALDO REAL (S.DEUDOR Vs. GARANTIA)'] > df7['Nuevo Saldo']:
        return "DEUDA SOBREPASA GARANTIA"
    else:
        return '--'
    
df7['ALERTA (Si Deuda sobrepasa V.Garantia)'] = df7.apply(alerta, axis=1)


#%%
df_final = df7.merge(JGM_año_castigo, 
                         left_on=["NroPrestamoFC"], 
                         right_on=["Nro Prestamo Fincore"]
                         ,how='left')

COLUMNAS = ['Socio',
'CodigoSocio',
'TipoDocumentoTXT',
'NroDocIdentidad',
'CodFinalidad',
'TipoCreditoTXT',
'NumeroPrestamo',
'NroPrestamoFC',
'FechaDesembolsoTXT',
'MonedaTXT',
'MontoSolicitadoTXT',
'SoloCapitalAmortizado',
'SaldoCapital',
'CRED CON CAPITALIZ',
'InteresVencidoPactado',
'InteresPactadoPagado',
'SoloSaldoInteresVencido',
'Saldo Deudor (Sobre la Cuota)',
'InteresCompensatorioDeuda',
'InteresMoratorioDeuda',
'Nuevo Saldo',
'IMPTE CASTIGADO (Asignado x PGB)',
'FECHA DE CASTIGO',
'Capital Amortizado',
'Int y Otros',
'Total Amortizado',
'SALDO CASTIGADO',
'SALDO DEUDOR REALISTA (SOLO PARA PGB)',
'OBSERVACION',
'VALOR GARANTIA',
'SALDO REAL (S.DEUDOR Vs. GARANTIA)',
'ALERTA (Si Deuda sobrepasa V.Garantia)',
'año castigo utilidad JGM',
'FechaUltimoPagoCBTXT',
'ImporteVencido',
'NroCuotasVencidas',
'NombrePlanilla',
'Domicilio',
'DistritoSocio',
'TlfSocio',
'CelularSocio',
'EmailSocio',
'OrigenTXT',
'DiasVencimientoSBS',
'Funcionaria',
'SituacionTXT',
'AbogadoTXT',
'FechaAsignacionAbogadoTXT',
'NroExpedienteTXT',
'FechaExpedienteTXT',
'Juzgado',
'FechaAsignacion',
'Etapa',
'ObservacionAbogado',
'JFechaCastigo',
'JFechaVentaCartera',
'UltObservacionSocio',
'TipoCredito',
'TipoCreditoTXT',
'Finalidad TXT',
'TipoCambioTXT',
'FechaProcesoSistemaTXT',
'FlagGarantiaPref',
'OrigenPrestamo'
]

RESULTADO_FINAL = df_final[COLUMNAS]
df_finalizado = RESULTADO_FINAL.copy()

indice = ['InteresMoratorioDeuda','InteresCompensatorioDeuda', 'Saldo Deudor (Sobre la Cuota)', 'SoloSaldoInteresVencido',
          'InteresPactadoPagado', 'InteresVencidoPactado', 'SaldoCapital', 'SoloCapitalAmortizado']
for col in indice:
    df_finalizado.loc[:, col] = df_finalizado[col].round(2) #redondeando las columnas

#df_finalizado
#%%
# creando las columnas auxiliares para los reportes 
#df_finalizado['Finalidad']

df_finalizado['CodFinalidad'] = pd.to_numeric(df_finalizado['CodFinalidad'], errors='coerce') #para convertir los tipos de datos a numérico
df_finalizado['CodFinalidad'].fillna(0, inplace=True) #para reemplazar los NaN por ceros

#df_finalizado.dropna(subset=['Finalidad'], inplace=True)  #####este código es peligroso porque elimina filas que tengan NaN, ni sé porqué lo puse

df_finalizado['CodFinalidad'] = df_finalizado['CodFinalidad'].astype(str)


#df_finalizado['CodFinalidad'] = df_finalizado['CodFinalidad'].str.replace('.0', '')
def asignacion_auxiliar(df_finalizado):
    if df_finalizado['CodFinalidad'] in ['15']:
        return 'PEQUEÑA EMPRESA'
    elif df_finalizado['CodFinalidad'] in ['16', '17', '18', '19']:
        return 'MEDIANA EMPRESA'   
    elif df_finalizado['CodFinalidad'] in ['30', '31', '32', '33']:
        return 'LIBRE DISPONIBILIDAD.'    
    elif df_finalizado['CodFinalidad'] in ['34', '35', '36', '37', '38', '39']:
        return 'CONSUMO ORD.'
    elif df_finalizado['CodFinalidad'] in ['41', '45']:
        return 'GARANTIA HIPOT (INCL HIPOCONSTR)'
    elif df_finalizado['CodFinalidad'] in ['20','21', '22', '23', '24', '25', '26', '27', '28', '29']:
        return 'MICRO COMERCIO'
    else:
        return 'investigar caso'

df_finalizado['auxiliar1'] = df_finalizado.apply(asignacion_auxiliar, axis=1)


#%%

#este código es solo para crear un excel y revisarlo

nombre = "df5.xlsx"
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

df_finalizado.to_excel(nombre, index=False)
            
   # impte castigado no varía, eso solo se jala del mes anterior
    
    
    
    
    
    
    
    
    
    
    
    
    
    



