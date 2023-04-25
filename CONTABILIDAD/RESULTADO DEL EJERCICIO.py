# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:16:46 2023

@author: sanmiguel38
"""

"""ESTADO DE RESULTADOS"""


import pandas as pd
pd.options.display.float_format = '{:.2f}'.format
import os


#%%


'anotar esta vaina de acá porque está buena para solucionar el problema de los números decimales'
def convert_number(n):
    return "{:.2f}".format(n)

df = pd.read_excel('C:\\Users\\sanmiguel38\\Desktop\\contabilidad automatizando para jenny\\resultado del ejercicio\\EEFF - San Miguel Noviembre2022 - ADM.xlsx', 
                   sheet_name='BALCOMP',
                   skiprows=4,
                   engine='openpyxl',  #esta vaina es importante para que no pase por la notación científica
                   converters={'Saldo Actual': convert_number,
                               'Saldo Anterior': convert_number,
                               'Débito': convert_number,
                               'Crédito': convert_number},
                   dtype={'Nro Cuenta': str}
                   )
'código para eliminar las filas que no quiero'
#for i in range (543,552):
#    df = df.drop(i)
#del i

'para eliminar la columna que no sirve de nada'
df = df.drop('Unnamed: 0', axis=1)

#%%

#OBTENIENDO LOS VALORES ABSOLUTOS
df['Saldo Actual'] = pd.to_numeric(df['Saldo Actual'], errors='coerce')
df_abs = df.copy()
df_abs = df_abs.drop(columns=['Saldo Actual'])
df_saldo = df['Saldo Actual'].copy()
df_saldo = pd.DataFrame(df_saldo)
df_saldo = df_saldo['Saldo Actual'].abs()
df_saldo = pd.DataFrame(df_saldo)
df_abs['Saldo Actual'] = df_saldo['Saldo Actual']

#%%
#AQUI LOS CÁLCULOS

#100
'AQUÍ AÚN NO HAY NADA'

#200
df200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5111')]
eeff200_1 = float(df200_1['Saldo Actual'].sum())

df200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5121')]
eeff200_2 = float(df200_2['Saldo Actual'].sum())

tota200_ = eeff200_1 + eeff200_2

#300
df300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5112')]
eeff300_1 = float(df300_1['Saldo Actual'].sum())

df300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5122')]
eeff300_2 = float(df300_2['Saldo Actual'].sum())

tota300_ = eeff300_1 + eeff300_2

#400
df400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511302')]
eeff400_1 = float(df400_1['Saldo Actual'].sum())

df400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512302')]
eeff400_2 = float(df400_2['Saldo Actual'].sum())

tota400_ = eeff400_1 + eeff400_2

#500
df500_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511304')]
eeff500_1 = float(df500_1['Saldo Actual'].sum())

df500_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512304')]
eeff500_2 = float(df500_2['Saldo Actual'].sum())

tota500_ = eeff500_1 + eeff500_2

#600
df600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511305')]
eeff600_1 = float(df600_1['Saldo Actual'].sum())

df600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512305')]
eeff600_2 = float(df600_2['Saldo Actual'].sum())

tota600_ = eeff600_1 + eeff600_2

#700
df700_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5114') |
                     (df_abs['Nro Cuenta'] == '5117')]
eeff700_1 = float(df700_1['Saldo Actual'].sum())

df700_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5124') |
                     (df_abs['Nro Cuenta'] == '5127')]
eeff700_2 = float(df700_2['Saldo Actual'].sum())

tota700_ = eeff700_1 + eeff700_2

#800
dfsuma800_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5119170102') |
                         (df_abs['Nro Cuenta'] == '5119170202') |
                         (df_abs['Nro Cuenta'] == '5119240101')]
suma800_1 = float(dfsuma800_1['Saldo Actual'].sum())
dfrest800_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4119170102') |
                         (df_abs['Nro Cuenta'] == '4119170202') |
                         (df_abs['Nro Cuenta'] == '4119240101')]
rest800_1 = float(dfrest800_1['Saldo Actual'].sum())
eeff800_1 = suma800_1 - rest800_1

dfsuma800_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5129170102') |
                         (df_abs['Nro Cuenta'] == '5129170202') |
                         (df_abs['Nro Cuenta'] == '5129240101')]
suma800_2 = float(dfsuma800_2['Saldo Actual'].sum())
dfrest800_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4129170102') |
                         (df_abs['Nro Cuenta'] == '4129170202') |
                         (df_abs['Nro Cuenta'] == '4129240101')]
rest800_2 = float(dfrest800_2['Saldo Actual'].sum())
eeff800_2 = suma800_2 - rest800_2

tota800_ = eeff800_1 + eeff800_2

#900
df900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511504') |
                     (df_abs['Nro Cuenta'] == '511505') |
                     (df_abs['Nro Cuenta'] == '511506')]
eeff900_1 = float(df900_1['Saldo Actual'].sum())

df900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512504') |
                     (df_abs['Nro Cuenta'] == '512505') |
                     (df_abs['Nro Cuenta'] == '512506')]
eeff900_2 = float(df900_2['Saldo Actual'].sum())

tota900_ = eeff900_1 + eeff900_2

#1000
dfsuma1000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511901') |
                          (df_abs['Nro Cuenta'] == '511919') |
                          (df_abs['Nro Cuenta'] == '511999') |
                          (df_abs['Nro Cuenta'] == '511925')]
suma1000_1 = float(dfsuma1000_1['Saldo Actual'].sum())
dfrest1000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411925')]
rest1000_1 = float(dfrest1000_1['Saldo Actual'].sum())
eeff1000_1 = suma1000_1 - rest1000_1

dfsuma1000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '511901') |
                          (df_abs['Nro Cuenta'] == '511919') |
                          (df_abs['Nro Cuenta'] == '511999') |
                          (df_abs['Nro Cuenta'] == '511925')]
suma1000_2 = float(dfsuma1000_2['Saldo Actual'].sum())
dfrest1000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '411925')]
rest1000_2 = float(dfrest1000_2['Saldo Actual'].sum())
eeff1000_2 = suma1000_2 - rest1000_2

tota1000_ = eeff1000_1 + eeff1000_2

#regresando al 100

eeff100_1 = eeff200_1 + eeff300_1 + eeff400_1 + eeff500_1 + eeff600_1 \
            + eeff700_1 + eeff800_1+ eeff900_1 + eeff1000_1

eeff100_2 = eeff200_2 + eeff300_2 + eeff400_2 + eeff500_2 + eeff600_2 \
            + eeff700_2 + eeff800_2+ eeff900_2 + eeff1000_2

tota100_ = eeff100_1 + eeff100_2

#%%
#AQUÍ LA INCERTACIÓN DE LOS DATOS
'crear dataframe'
a_eeff = pd.DataFrame(columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])


nueva_fila = pd.DataFrame([['100', 'INGRESOS POR INTERESES', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['200', 'Disponible', 
                            '{:.2f}'.format(abs(float(eeff200_1))), 
                            '{:.2f}'.format(abs(float(eeff200_2))), 
                            '{:.2f}'.format(abs(float(tota200_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['300', 'Fondos Intercooperativos', 
                            '{:.2f}'.format(abs(float(eeff300_1))), 
                            '{:.2f}'.format(abs(float(eeff300_2))), 
                            '{:.2f}'.format(abs(float(tota300_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['400', 'Inversiones a Valor Razonable con Cambios en Resultados', 
                            '{:.2f}'.format(abs(float(eeff400_1))), 
                            '{:.2f}'.format(abs(float(eeff400_2))), 
                            '{:.2f}'.format(abs(float(tota400_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['500', 'Inversiones Disponibles para la venta', 
                            '{:.2f}'.format(abs(float(eeff500_1))), 
                            '{:.2f}'.format(abs(float(eeff500_2))), 
                            '{:.2f}'.format(abs(float(tota500_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['600', 'Inversiones a Vencimiento', 
                            '{:.2f}'.format(abs(float(eeff600_1))), 
                            '{:.2f}'.format(abs(float(eeff600_2))), 
                            '{:.2f}'.format(abs(float(tota600_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['700', 'Cartera de Créditos Directos', 
                            '{:.2f}'.format(abs(float(eeff700_1))), 
                            '{:.2f}'.format(abs(float(eeff700_2))), 
                            '{:.2f}'.format(abs(float(tota700_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['800', 'Resultado por Operaciones de Cobertura (1)', 
                            '{:.2f}'.format(abs(float(eeff800_1))), 
                            '{:.2f}'.format(abs(float(eeff800_2))), 
                            '{:.2f}'.format(abs(float(tota800_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['900', 'Cuentas por Cobrar', 
                            '{:.2f}'.format(abs(float(eeff900_1))), 
                            '{:.2f}'.format(abs(float(eeff900_2))), 
                            '{:.2f}'.format(abs(float(tota900_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1000', 'Otros Ingresos Financieros', 
                            '{:.2f}'.format(abs(float(eeff1000_1))), 
                            '{:.2f}'.format(abs(float(eeff1000_2))), 
                            '{:.2f}'.format(abs(float(tota1000_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

a_eeff.iloc[0,2] = '{:.2f}'.format(eeff100_1)
a_eeff.iloc[0,3] = '{:.2f}'.format(eeff100_2)
a_eeff.iloc[0,4] = '{:.2f}'.format(tota100_)

#%%

#1100
'AQUÍ AÚN NO HAY NADA'

#1200
df1200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4111')]
eeff1200_1 = float(df1200_1['Saldo Actual'].sum())

df1200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4121')]
eeff1200_2 = float(df1200_2['Saldo Actual'].sum())

tota1200_ = eeff1200_1 + eeff1200_2

#1300
df1300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4112')]
eeff1300_1 = float(df1300_1['Saldo Actual'].sum())

df1300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4122')]
eeff1300_2 = float(df1300_2['Saldo Actual'].sum())

tota1300_ = eeff1300_1 + eeff1300_2

#1400
df1400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4113')]
eeff1400_1 = float(df1400_1['Saldo Actual'].sum())

df1400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4123')]
eeff1400_2 = float(df1400_2['Saldo Actual'].sum())

tota1400_ = eeff1400_1 + eeff1400_2

#1500
'tendremos que regresar aquí luego'

#1600
df1600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411402') |
                      (df_abs['Nro Cuenta'] == '411403')]
eeff1600_1 = float(df1600_1['Saldo Actual'].sum())

df1600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412402') |
                      (df_abs['Nro Cuenta'] == '412403')]
eeff1600_2 = float(df1600_2['Saldo Actual'].sum())

tota1600_ = eeff1600_1 + eeff1600_2

#1700
df1700_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411404') |
                      (df_abs['Nro Cuenta'] == '411405')]
eeff1700_1 = float(df1700_1['Saldo Actual'].sum())

df1700_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412404') |
                      (df_abs['Nro Cuenta'] == '412405')]
eeff1700_2 = float(df1700_2['Saldo Actual'].sum())

tota1700_ = eeff1700_1 + eeff1700_2

#1800
df1800_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411406') |
                      (df_abs['Nro Cuenta'] == '411407')]
eeff1800_1 = float(df1800_1['Saldo Actual'].sum())

df1800_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412406') |
                      (df_abs['Nro Cuenta'] == '412407')]
eeff1800_2 = float(df1800_2['Saldo Actual'].sum())

tota1800_ = eeff1800_1 + eeff1800_2

#1900
df1900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4117')]
eeff1900_1 = float(df1900_1['Saldo Actual'].sum())

df1900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4127')]
eeff1900_2 = float(df1900_2['Saldo Actual'].sum())

tota1900_ = eeff1900_1 + eeff1900_2

#2000
df2000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4116')]
eeff2000_1 = float(df2000_1['Saldo Actual'].sum())

df2000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4126')]
eeff2000_2 = float(df2000_2['Saldo Actual'].sum())

tota2000_ = eeff2000_1 + eeff2000_2

#2100
'volver luego'

#2200
df2200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4115')]
eeff2200_1 = float(df2200_1['Saldo Actual'].sum())

df2200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4125')]
eeff2200_2 = float(df2200_2['Saldo Actual'].sum())

tota2200_ = eeff2200_1 + eeff2200_2

#2300
dfsuma2300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5119170102') |
                          (df_abs['Nro Cuenta'] == '5119170202') |
                          (df_abs['Nro Cuenta'] == '5119240101')]
suma2300_1 = float(dfsuma2300_1['Saldo Actual'].sum())
dfrest2300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4119170102') |
                          (df_abs['Nro Cuenta'] == '4119170202') |
                          (df_abs['Nro Cuenta'] == '4119240101')]
rest2300_1 = float(dfrest2300_1['Saldo Actual'].sum())
eeff2300_1 = suma2300_1 - rest2300_1

dfsuma2300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5129170102') |
                          (df_abs['Nro Cuenta'] == '5129170202') |
                          (df_abs['Nro Cuenta'] == '5129240101')]
suma2300_2 = float(dfsuma2300_2['Saldo Actual'].sum())
dfrest2300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4129170102') |
                          (df_abs['Nro Cuenta'] == '4129170202') |
                          (df_abs['Nro Cuenta'] == '4129240101')]
rest2300_2 = float(dfrest2300_2['Saldo Actual'].sum())
eeff2300_2 = suma2300_2 - rest2300_2

tota2300_ = eeff2300_1 + eeff2300_2

#2400
dfsuma2400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411901') |
                          (df_abs['Nro Cuenta'] == '411908') |
                          (df_abs['Nro Cuenta'] == '411909') |
                          (df_abs['Nro Cuenta'] == '411922') |
                          (df_abs['Nro Cuenta'] == '411923') |
                          (df_abs['Nro Cuenta'] == '511925')]
suma2400_1 = float(dfsuma2400_1['Saldo Actual'].sum())
dfrest2400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411925')]
rest2400_1 = float(dfrest2400_1['Saldo Actual'].sum())
eeff2400_1 = suma2400_1 - rest2400_1

dfsuma2400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412901') |
                          (df_abs['Nro Cuenta'] == '412908') |
                          (df_abs['Nro Cuenta'] == '412909') |
                          (df_abs['Nro Cuenta'] == '412922') |
                          (df_abs['Nro Cuenta'] == '412923') |
                          (df_abs['Nro Cuenta'] == '512925')]
suma2400_2 = float(dfsuma2400_2['Saldo Actual'].sum())
dfrest2400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412925')]
rest2400_2 = float(dfrest2400_2['Saldo Actual'].sum())
eeff2400_2 = suma2400_2 - rest2400_2

tota2400_ = eeff2400_1 + eeff2400_2

#%% 

#volviendo al 1500
eeff1500_1 = eeff1600_1 + eeff1700_1 + eeff1800_1 + eeff1900_1 + eeff2000_1
eeff1500_2 = eeff1600_2 + eeff1700_2 + eeff1800_2 + eeff1900_2 + eeff2000_2
tota1500_  = eeff1500_1 + eeff1500_2


#volviendo al 1100
eeff2100_1 = eeff2200_1
eeff2100_2 = eeff2200_2
tota2100_  = tota2200_



eeff1100_1 = eeff1200_1 + eeff1300_1 + eeff1400_1 + eeff1500_1 + eeff2100_1 \
            + eeff2300_1 + eeff2400_1

eeff1100_2 = eeff1200_2 + eeff1300_2 + eeff1400_2 + eeff1500_2 + eeff2100_2 \
            + eeff2300_2 + eeff2400_2

tota1100_ = eeff1100_1 + eeff1100_2

#%%
#2500
eeff2500_1 = eeff100_1 - eeff1100_1
eeff2500_2 = eeff100_2 - eeff1100_2
tota2500_ = eeff2500_1 + eeff2500_2


#%%

nueva_fila = pd.DataFrame([['1100', 'GASTOS POR INTERESES ', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1200', 'Obligaciones con el Público', 
                            '{:.2f}'.format(abs(float(eeff1200_1))), 
                            '{:.2f}'.format(abs(float(eeff1200_2))), 
                            '{:.2f}'.format(abs(float(tota1200_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1300', 'Fondos Intercooperativos', 
                            '{:.2f}'.format(abs(float(eeff1300_1))), 
                            '{:.2f}'.format(abs(float(eeff1300_2))), 
                            '{:.2f}'.format(abs(float(tota1300_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1400', 'Obligaciones por depósitos de las COOPAC', 
                            '{:.2f}'.format(abs(float(eeff1400_1))), 
                            '{:.2f}'.format(abs(float(eeff1400_2))), 
                            '{:.2f}'.format(abs(float(tota1400_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1500', 'Adeudos y Obligaciones Financieras', 
                            '{:.2f}'.format(abs(float(0))), #aqui van ceros de momento
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1600', 'Adeudos y Obligaciones  con COOPAC y Empresas del Sistema Financiero del País', 
                            '{:.2f}'.format(abs(float(eeff1600_1))), 
                            '{:.2f}'.format(abs(float(eeff1600_2))), 
                            '{:.2f}'.format(abs(float(tota1600_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1700', 'Adeudos y Obligaciones con Instituciones Financieras del Exter. y Organ. Financ. Internac.', 
                            '{:.2f}'.format(abs(float(eeff1700_1))), 
                            '{:.2f}'.format(abs(float(eeff1700_2))), 
                            '{:.2f}'.format(abs(float(tota1700_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1800', 'Otros Adeudos y Obligaciones del  País y del Exterior', 
                            '{:.2f}'.format(abs(float(eeff1800_1))), 
                            '{:.2f}'.format(abs(float(eeff1800_2))), 
                            '{:.2f}'.format(abs(float(tota1800_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1900', 'Comisiones y otros cargos por adeudos y obligaciones financieras', 
                            '{:.2f}'.format(abs(float(eeff1900_1))), 
                            '{:.2f}'.format(abs(float(eeff1900_2))), 
                            '{:.2f}'.format(abs(float(tota1900_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2000', 'Valores, Títulos y Obligaciones en Circulación', 
                            '{:.2f}'.format(abs(float(eeff2000_1))), 
                            '{:.2f}'.format(abs(float(eeff2000_2))), 
                            '{:.2f}'.format(abs(float(tota2000_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)


nueva_fila = pd.DataFrame([['2100', 'Cuentas por pagar', 
                            '{:.2f}'.format(abs(float(eeff2100_1))), 
                            '{:.2f}'.format(abs(float(eeff2100_2))), 
                            '{:.2f}'.format(abs(float(tota2100_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2200', 'Intereses de Cuentas por Pagar', 
                            '{:.2f}'.format(abs(float(eeff2200_1))), 
                            '{:.2f}'.format(abs(float(eeff2200_2))), 
                            '{:.2f}'.format(abs(float(tota2200_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2300', 'Resultado por Operaciones de Cobertura (1)', 
                            '{:.2f}'.format(abs(float(eeff2300_1))), 
                            '{:.2f}'.format(abs(float(eeff2300_2))), 
                            '{:.2f}'.format(abs(float(tota2300_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2400', 'Otros Gastos Financieros', 
                            '{:.2f}'.format(abs(float(eeff2400_1))), 
                            '{:.2f}'.format(abs(float(eeff2400_2))), 
                            '{:.2f}'.format(abs(float(tota2400_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

a_eeff.iloc[10,2] = '{:.2f}'.format(eeff1100_1)
a_eeff.iloc[10,3] = '{:.2f}'.format(eeff1100_2)
a_eeff.iloc[10,4] = '{:.2f}'.format(tota1100_)

a_eeff.iloc[14,2] = '{:.2f}'.format(eeff1500_1)
a_eeff.iloc[14,3] = '{:.2f}'.format(eeff1500_2)
a_eeff.iloc[14,4] = '{:.2f}'.format(tota1500_)

nueva_fila = pd.DataFrame([['2500', 'MARGEN FINANCIERO BRUTO', 
                            '{:.2f}'.format(abs(float(eeff2500_1))), 
                            '{:.2f}'.format(abs(float(eeff2500_2))), 
                            '{:.2f}'.format(abs(float(tota2500_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

#%%
#2600
dfsuma2600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4312')]
suma2600_1 = float(dfsuma2600_1['Saldo Actual'].sum())
dfrest2600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511927') |
                          (df_abs['Nro Cuenta'] == '541401')]
rest2600_1 = float(dfrest2600_1['Saldo Actual'].sum())
eeff2600_1 = suma2600_1 - rest2600_1

dfsuma2600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4322')]
suma2600_2 = float(dfsuma2600_2['Saldo Actual'].sum())
dfrest2600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512927') |
                          (df_abs['Nro Cuenta'] == '542401')]
rest2600_2 = float(dfrest2600_2['Saldo Actual'].sum())
eeff2600_2 = suma2600_2 - rest2600_2

tota2600_ = eeff2600_1 + eeff2600_2

#2700
eeff2700_1 = eeff2500_1 - eeff2600_1
eeff2700_2 = eeff2500_2 - eeff2600_2
tota2700_  = eeff2700_1 + eeff2700_2

#2800
'volveremos luego'

#2900
df2900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5211')]
eeff2900_1 = float(df2900_1['Saldo Actual'].sum())

df2900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5221')]
eeff2900_2 = float(df2900_2['Saldo Actual'].sum())

tota2900_ = eeff2900_1 + eeff2900_2

#3000
df3000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '521204')]
eeff3000_1 = float(df3000_1['Saldo Actual'].sum())

df3000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '522204')]
eeff3000_2 = float(df3000_2['Saldo Actual'].sum())

tota3000_ = eeff3000_1 + eeff3000_2

#3100
dfsuma3100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5212')]
suma3100_1 = float(dfsuma3100_1['Saldo Actual'].sum())
dfrest3100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '521204')]
rest3100_1 = float(dfrest3100_1['Saldo Actual'].sum())
eeff3100_1 = suma3100_1 - rest3100_1

dfsuma3100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5222')]
suma3100_2 = float(dfsuma3100_2['Saldo Actual'].sum())
dfrest3100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '522204') ]
rest3100_2 = float(dfrest3100_2['Saldo Actual'].sum())
eeff3100_2 = suma3100_2 - rest3100_2

tota3100_ = eeff3100_1 + eeff3100_2

#retornando al 2800

eeff2800_1 = eeff2900_1 + eeff3000_1 + eeff3100_1
eeff2800_2 = eeff2900_2 + eeff3000_2 + eeff3100_2
tota2800_  = eeff2800_1 + eeff2800_2


#%%
nueva_fila = pd.DataFrame([['2600', 'Provisiones para Créditos Directos', 
                            '{:.2f}'.format(abs(float(eeff2600_1))), 
                            '{:.2f}'.format(abs(float(eeff2600_2))), 
                            '{:.2f}'.format(abs(float(tota2600_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2700', 'MARGEN FINANCIERO NETO', 
                            '{:.2f}'.format(abs(float(eeff2700_1))), 
                            '{:.2f}'.format(abs(float(eeff2700_2))), 
                            '{:.2f}'.format(abs(float(tota2700_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2800', 'INGRESOS POR SERVICIOS FINANCIEROS', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2900', 'Ingresos por Créditos Indirectos', 
                            '{:.2f}'.format(abs(float(eeff2900_1))), 
                            '{:.2f}'.format(abs(float(eeff2900_2))), 
                            '{:.2f}'.format(abs(float(tota2900_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3000', 'Ingresos por Fideicomisos', 
                            '{:.2f}'.format(abs(float(eeff3000_1))), 
                            '{:.2f}'.format(abs(float(eeff3000_2))), 
                            '{:.2f}'.format(abs(float(tota3000_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3100', 'Ingresos Diversos ', 
                            '{:.2f}'.format(abs(float(eeff3100_1))), 
                            '{:.2f}'.format(abs(float(eeff3100_2))), 
                            '{:.2f}'.format(abs(float(tota3100_)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)


a_eeff.iloc[27,2] = '{:.2f}'.format(eeff2800_1)
a_eeff.iloc[27,3] = '{:.2f}'.format(eeff2800_2)
a_eeff.iloc[27,4] = '{:.2f}'.format(tota2800_)

#%%
#3200 
'volveremos'

#3300
df3300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4211') |
                      (df_abs['Nro Cuenta'] == '411907')]
eeff3300_1 = float(df3300_1['Saldo Actual'].sum())

df3300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4221') |
                      (df_abs['Nro Cuenta'] == '412907')]
eeff3300_2 = float(df3300_2['Saldo Actual'].sum())

tota3300_ = eeff3300_1 + eeff3300_2

#3400
df3400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '421204')]
eeff3400_1 = float(df3400_1['Saldo Actual'].sum())

df3400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '422204')]
eeff3400_2 = float(df3400_2['Saldo Actual'].sum())

tota3400_ = eeff3400_1 + eeff3400_2

#3500
df3500_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411905')]
eeff3500_1 = float(df3500_1['Saldo Actual'].sum())

df3500_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412905')]
eeff3500_2 = float(df3500_2['Saldo Actual'].sum())

tota3500_ = eeff3500_1 + eeff3500_2

#3600
dfsuma3600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4212')]
suma3600_1 = float(dfsuma3600_1['Saldo Actual'].sum())
dfrest3600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '421204')]
rest3600_1 = float(dfrest3600_1['Saldo Actual'].sum())
eeff3600_1 = suma3600_1 - rest3600_1

dfsuma3600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4222')]
suma3600_2 = float(dfsuma3600_2['Saldo Actual'].sum())
dfrest3600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '422204') ]
rest3600_2 = float(dfrest3600_2['Saldo Actual'].sum())
eeff3600_2 = suma3600_2 - rest3600_2

tota3600_ = eeff3600_1 + eeff3600_2

#retornando al 3200
eeff3200_1 = eeff3300_1 + eeff3400_1 + eeff3500_1 + eeff3600_1
eeff3200_2 = eeff3300_2 + eeff3400_2 + eeff3500_2 + eeff3600_2
tota3200_  = eeff3200_1  + eeff3200_2 

#3700
'ya volveremos algún día'

#3800
'ya volveremos algún día'

#3900
'ya volveremos algún día'


#4000
dfsuma4000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511301') |
                          (df_abs['Nro Cuenta'] == '511911') |
                          (df_abs['Nro Cuenta'] == '511912') ]
suma4000_1 = float(dfsuma4000_1['Saldo Actual'].sum())
dfrest4000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411911') |
                          (df_abs['Nro Cuenta'] == '411912')]
rest4000_1 = float(dfrest4000_1['Saldo Actual'].sum())
eeff4000_1 = suma4000_1 - rest4000_1

dfsuma4000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512301') |
                          (df_abs['Nro Cuenta'] == '512911') |
                          (df_abs['Nro Cuenta'] == '512912')]
suma4000_2 = float(dfsuma4000_2['Saldo Actual'].sum())
dfrest4000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412911') |
                          (df_abs['Nro Cuenta'] == '412912') ]
rest4000_2 = float(dfrest4000_2['Saldo Actual'].sum())
eeff4000_2 = suma4000_2 - rest4000_2

tota4000_ = eeff4000_1 + eeff4000_2

#4100
dfsuma4100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511306') |
                          (df_abs['Nro Cuenta'] == '511915') ]
suma4100_1 = float(dfsuma4100_1['Saldo Actual'].sum())
dfrest4100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411915')]
rest4100_1 = float(dfrest4100_1['Saldo Actual'].sum())
eeff4100_1 = suma4100_1 - rest4100_1

dfsuma4100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512306') |
                          (df_abs['Nro Cuenta'] == '512915')]
suma4100_2 = float(dfsuma4100_2['Saldo Actual'].sum())
dfrest4100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412915')]
rest4100_2 = float(dfrest4100_2['Saldo Actual'].sum())
eeff4100_2 = suma4100_2 - rest4100_2

tota4100_ = eeff4100_1 + eeff4100_2

#4200
dfsuma4200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511303') |
                          (df_abs['Nro Cuenta'] == '511913') |
                          (df_abs['Nro Cuenta'] == '511912')]
suma4200_1 = float(dfsuma4200_1['Saldo Actual'].sum())
dfrest4200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411913') |
                          (df_abs['Nro Cuenta'] == '411914')]
rest4200_1 = float(dfrest4200_1['Saldo Actual'].sum())
eeff4200_1 = suma4200_1 - rest4200_1

dfsuma4200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512303') |
                          (df_abs['Nro Cuenta'] == '512913') |
                          (df_abs['Nro Cuenta'] == '512912')]
suma4200_2 = float(dfsuma4200_2['Saldo Actual'].sum())
dfrest4200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412913') |
                          (df_abs['Nro Cuenta'] == '412914')]
rest4200_2 = float(dfrest4200_2['Saldo Actual'].sum())
eeff4200_2 = suma4200_2 - rest4200_2

tota4200_ = eeff4200_1 + eeff4200_2

#4300
dfsuma4300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511916')]
suma4300_1 = float(dfsuma4300_1['Saldo Actual'].sum())
dfrest4300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411916')]
rest4300_1 = float(dfrest4300_1['Saldo Actual'].sum())
eeff4300_1 = suma4300_1 - rest4300_1

dfsuma4300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512916')]
suma4300_2 = float(dfsuma4300_2['Saldo Actual'].sum())
dfrest4300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412919')]
rest4300_2 = float(dfrest4300_2['Saldo Actual'].sum())
eeff4300_2 = suma4300_2 - rest4300_2

tota4300_ = eeff4300_1 + eeff4300_2

#4400
dfsuma4400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511917') |
                          (df_abs['Nro Cuenta'] == '5119240102') |
                          (df_abs['Nro Cuenta'] == '4119170102') |
                          (df_abs['Nro Cuenta'] == '4119140202')]
suma4400_1 = float(dfsuma4400_1['Saldo Actual'].sum())
dfrest4400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5119170102') |
                          (df_abs['Nro Cuenta'] == '5119170202') |
                          (df_abs['Nro Cuenta'] == '411917') |
                          (df_abs['Nro Cuenta'] == '4119240102')]
rest4400_1 = float(dfrest4400_1['Saldo Actual'].sum())
eeff4400_1 = suma4400_1 - rest4400_1

dfsuma4400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512917') |
                          (df_abs['Nro Cuenta'] == '5129240102') |
                          (df_abs['Nro Cuenta'] == '4129170102') |
                          (df_abs['Nro Cuenta'] == '4129140202')]
suma4400_2 = float(dfsuma4400_2['Saldo Actual'].sum())
dfrest4400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5129170102') |
                          (df_abs['Nro Cuenta'] == '5129170202') |
                          (df_abs['Nro Cuenta'] == '412917') |
                          (df_abs['Nro Cuenta'] == '4129240102')]
rest4400_2 = float(dfrest4400_2['Saldo Actual'].sum())
eeff4400_2 = suma4400_2 - rest4400_2

tota4400_ = eeff4400_1 + eeff4400_2

#4500
dfsuma4500_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511904')]
suma4500_1 = float(dfsuma4500_1['Saldo Actual'].sum())
dfrest4500_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411904')]
rest4500_1 = float(dfrest4500_1['Saldo Actual'].sum())
eeff4500_1 = suma4500_1 - rest4500_1

dfsuma4500_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512904')]
suma4500_2 = float(dfsuma4500_2['Saldo Actual'].sum())
dfrest4500_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412904')]
rest4500_2 = float(dfrest4500_2['Saldo Actual'].sum())
eeff4500_2 = suma4500_2 - rest4500_2

tota4500_ = eeff4500_1 + eeff4500_2

#4600
dfsuma4600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5118')]
suma4600_1 = float(dfsuma4600_1['Saldo Actual'].sum())
dfrest4600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4118')]
rest4600_1 = float(dfrest4600_1['Saldo Actual'].sum())
eeff4600_1 = suma4600_1 - rest4600_1

dfsuma4600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5128')]
suma4600_2 = float(dfsuma4600_2['Saldo Actual'].sum())
dfrest4600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4128')]
rest4600_2 = float(dfrest4600_2['Saldo Actual'].sum())
eeff4600_2 = suma4600_2 - rest4600_2

tota4600_ = eeff4600_1 + eeff4600_2

#4700
dfsuma4700_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '511918') |
                          (df_abs['Nro Cuenta'] == '511926') |
                          (df_abs['Nro Cuenta'] == '511903') |
                          (df_abs['Nro Cuenta'] == '511928')]
suma4700_1 = float(dfsuma4700_1['Saldo Actual'].sum())
dfrest4700_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '411918') |
                          (df_abs['Nro Cuenta'] == '411920') |
                          (df_abs['Nro Cuenta'] == '411926') |
                          (df_abs['Nro Cuenta'] == '411903') ]
rest4700_1 = float(dfrest4700_1['Saldo Actual'].sum())
eeff4700_1 = suma4700_1 - rest4700_1

dfsuma4700_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '512918') |
                          (df_abs['Nro Cuenta'] == '512926') |
                          (df_abs['Nro Cuenta'] == '512903') |
                          (df_abs['Nro Cuenta'] == '512928')]
suma4700_2 = float(dfsuma4700_2['Saldo Actual'].sum())
dfrest4700_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '412918') |
                          (df_abs['Nro Cuenta'] == '412920') |
                          (df_abs['Nro Cuenta'] == '412926') |
                          (df_abs['Nro Cuenta'] == '412903')]
rest4700_2 = float(dfrest4700_2['Saldo Actual'].sum())
eeff4700_2 = suma4700_2 - rest4700_2

tota4700_ = eeff4700_1 + eeff4700_2

#retornando al 3700
eeff3700_1 = eeff2700_1 + eeff2800_1 - eeff3200_1
eeff3700_2 = eeff2700_2 + eeff2800_2 - eeff3200_2
tota3700_  = eeff3700_1 + eeff3700_2

#retornando al 3900
eeff3900_1 = eeff4000_1 + eeff4100_1
eeff3900_2 = eeff4000_2 + eeff4100_2
tota3900_  = eeff3900_1 + eeff3900_2


#retornando al 3800
eeff3800_1 = eeff3900_1 + eeff4200_1 + eeff4300_1 + eeff4400_1 + eeff4500_1 \
                 + eeff4600_1  + eeff4700_1
eeff3800_2 = eeff3900_2 + eeff4200_2 + eeff4300_2 + eeff4400_2 + eeff4500_2 \
                 + eeff4600_2  + eeff4700_2
tota3800_  = eeff3800_1 + eeff3800_2

#%%
nueva_fila = pd.DataFrame([['3200', 'GASTOS POR SERVICIOS FINANCIEROS', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3300', 
                            'Gastos por Créditos indirectos', 
                            '{:.2f}'.format(abs(float(eeff3300_1))), 
                            '{:.2f}'.format(abs(float(eeff3300_2))), 
                            '{:.2f}'.format(abs(float(tota3300_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3400', 
                            'Gastos por Fideicomisos', 
                            '{:.2f}'.format(abs(float(eeff3400_1))), 
                            '{:.2f}'.format(abs(float(eeff3400_2))), 
                            '{:.2f}'.format(abs(float(tota3400_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

a_eeff.iloc[31,2] = '{:.2f}'.format(eeff3200_1)
a_eeff.iloc[31,3] = '{:.2f}'.format(eeff3200_2)
a_eeff.iloc[31,4] = '{:.2f}'.format(tota3200_)

nueva_fila = pd.DataFrame([['3500', 
                            'Primas al Fondo Seguro de Depósito', 
                            '{:.2f}'.format(abs(float(eeff3500_1))), 
                            '{:.2f}'.format(abs(float(eeff3500_2))), 
                            '{:.2f}'.format(abs(float(tota3500_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3600', 
                            'Gastos Diversos', 
                            '{:.2f}'.format(abs(float(eeff3600_1))), 
                            '{:.2f}'.format(abs(float(eeff3600_2))), 
                            '{:.2f}'.format(abs(float(tota3600_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3700', 
                            'MARGEN FINANCIERO NETO DE INGRESOS Y GASTOS POR SERVICIOS FINANCIEROS', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3800', 
                            'RESULTADOS POR OPERACIONES FINANCIERAS (ROF)', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3900', 
                            'Inversiones a Valor Razonable con Cambios en Resultados', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4000', 
                            'Inversiones a Valor Razonable con Cambios en Resultados', 
                            '{:.2f}'.format(abs(float(eeff4000_1))), 
                            '{:.2f}'.format(abs(float(eeff4000_2))), 
                            '{:.2f}'.format(abs(float(tota4000_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4100', 
                            'Inversiones en Commodities', 
                            '{:.2f}'.format(abs(float(eeff4100_1))), 
                            '{:.2f}'.format(abs(float(eeff4100_2))), 
                            '{:.2f}'.format(abs(float(tota4100_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4200', 
                            'Inversiones Disponibles para la Venta', 
                            '{:.2f}'.format(abs(float(eeff4200_1))), 
                            '{:.2f}'.format(abs(float(eeff4200_2))), 
                            '{:.2f}'.format(abs(float(tota4200_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4300', 
                            'Derivados de Negociación', 
                            '{:.2f}'.format(abs(float(eeff4300_1))), 
                            '{:.2f}'.format(abs(float(eeff4300_2))), 
                            '{:.2f}'.format(abs(float(tota4300_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4400', 
                            'Resultado por Operaciones de Cobertura', 
                            '{:.2f}'.format(abs(float(eeff4400_1))), 
                            '{:.2f}'.format(abs(float(eeff4400_2))), 
                            '{:.2f}'.format(abs(float(tota4400_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4500', 
                            'Ganancias (Pérdida) en Participaciones', 
                            '{:.2f}'.format(abs(float(eeff4500_1))), 
                            '{:.2f}'.format(abs(float(eeff4500_2))), 
                            '{:.2f}'.format(abs(float(tota4500_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4600', 
                            'Utilidad-Pérdida en Diferencia de Cambio', 
                            '{:.2f}'.format(abs(float(eeff4600_1))), 
                            '{:.2f}'.format(abs(float(eeff4600_2))), 
                            '{:.2f}'.format(abs(float(tota4600_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4700', 
                            'Otros', 
                            '{:.2f}'.format(abs(float(eeff4700_1))), 
                            '{:.2f}'.format(abs(float(eeff4700_2))), 
                            '{:.2f}'.format(abs(float(tota4700_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

a_eeff.iloc[36,2] = '{:.2f}'.format(eeff3700_1)
a_eeff.iloc[36,3] = '{:.2f}'.format(eeff3700_2)
a_eeff.iloc[36,4] = '{:.2f}'.format(tota3700_)

a_eeff.iloc[38,2] = '{:.2f}'.format(eeff3900_1)
a_eeff.iloc[38,3] = '{:.2f}'.format(eeff3900_2)
a_eeff.iloc[38,4] = '{:.2f}'.format(tota3900_)

a_eeff.iloc[37,2] = '{:.2f}'.format(eeff3800_1)
a_eeff.iloc[37,3] = '{:.2f}'.format(eeff3800_2)
a_eeff.iloc[37,4] = '{:.2f}'.format(tota3800_)

#%%
#4800
eeff4800_1 = eeff3700_1 + eeff3800_1 
eeff4800_2 = eeff3700_2 + eeff3800_2 
tota4800_  = eeff4800_1 + eeff4800_1

#4900
dfsuma4900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4511') |
                          (df_abs['Nro Cuenta'] == '4512') |
                          (df_abs['Nro Cuenta'] == '4513') |
                          (df_abs['Nro Cuenta'] == '4514')]
suma4900_1 = float(dfsuma4900_1['Saldo Actual'].sum())
dfrest4900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay') ]
rest4900_1 = float(dfrest4900_1['Saldo Actual'].sum())
eeff4900_1 = suma4900_1 - rest4900_1

dfsuma4900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4521') |
                          (df_abs['Nro Cuenta'] == '4522') |
                          (df_abs['Nro Cuenta'] == '4523') |
                          (df_abs['Nro Cuenta'] == '4524')]
suma4900_2 = float(dfsuma4900_2['Saldo Actual'].sum())
dfrest4900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest4900_2 = float(dfrest4900_2['Saldo Actual'].sum())
eeff4900_2 = suma4900_2 - rest4900_2

tota4900_ = eeff4900_1 + eeff4900_2

#5000
dfsuma5000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4511') |
                          (df_abs['Nro Cuenta'] == '4512')]
suma5000_1 = float(dfsuma5000_1['Saldo Actual'].sum())
dfrest5000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay') ]
rest5000_1 = float(dfrest5000_1['Saldo Actual'].sum())
eeff5000_1 = suma5000_1 - rest5000_1

dfsuma5000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4521') |
                          (df_abs['Nro Cuenta'] == '4522')]
suma5000_2 = float(dfsuma5000_2['Saldo Actual'].sum())
dfrest5000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest5000_2 = float(dfrest5000_2['Saldo Actual'].sum())
eeff5000_2 = suma5000_2 - rest5000_2

tota5000_ = eeff5000_1 + eeff5000_2

#5100
dfsuma5100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4513')]
suma5100_1 = float(dfsuma5100_1['Saldo Actual'].sum())
dfrest5100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay') ]
rest5100_1 = float(dfrest5100_1['Saldo Actual'].sum())
eeff5100_1 = suma5100_1 - rest5100_1

dfsuma5100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4523')]
suma5100_2 = float(dfsuma5100_2['Saldo Actual'].sum())
dfrest5100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest5100_2 = float(dfrest5100_2['Saldo Actual'].sum())
eeff5100_2 = suma5100_2 - rest5100_2

tota5100_ = eeff5100_1 + eeff5100_2

#5200
dfsuma5200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4514')]
suma5200_1 = float(dfsuma5200_1['Saldo Actual'].sum())
dfrest5200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay') ]
rest5200_1 = float(dfrest5200_1['Saldo Actual'].sum())
eeff5200_1 = suma5200_1 - rest5200_1

dfsuma5200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4524')]
suma5200_2 = float(dfsuma5200_2['Saldo Actual'].sum())
dfrest5200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest5200_2 = float(dfrest5200_2['Saldo Actual'].sum())
eeff5200_2 = suma5200_2 - rest5200_2

tota5200_ = eeff5200_1 + eeff5200_2

#5300
dfsuma5300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4411') |
                          (df_abs['Nro Cuenta'] == '4413')]
suma5300_1 = float(dfsuma5300_1['Saldo Actual'].sum())
dfrest5300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay') ]
rest5300_1 = float(dfrest5300_1['Saldo Actual'].sum())
eeff5300_1 = suma5300_1 - rest5300_1

dfsuma5300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4421') |
                          (df_abs['Nro Cuenta'] == '4423')]
suma5300_2 = float(dfsuma5300_2['Saldo Actual'].sum())
dfrest5300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest5300_2 = float(dfrest5300_2['Saldo Actual'].sum())
eeff5300_2 = suma5300_2 - rest5300_2

tota5300_ = eeff5300_1 + eeff5300_2

#5400

eeff5400_1 = eeff4800_1 - eeff4900_1 - eeff5300_1
eeff5400_2 = eeff4800_2 - eeff4900_2 - eeff5300_2

tota5400_ = eeff5400_1 + eeff5400_2

#5500
'volveremos pronto'

#5600
dfsuma5600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '431501') |
                          (df_abs['Nro Cuenta'] == '431502')]
suma5600_1 = float(dfsuma5600_1['Saldo Actual'].sum())
dfrest5600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '541402') ]
rest5600_1 = float(dfrest5600_1['Saldo Actual'].sum())
eeff5600_1 = suma5600_1 - rest5600_1

dfsuma5600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '432501') |
                          (df_abs['Nro Cuenta'] == '432502')]
suma5600_2 = float(dfsuma5600_2['Saldo Actual'].sum())
dfrest5600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '542402')]
rest5600_2 = float(dfrest5600_2['Saldo Actual'].sum())
eeff5600_2 = suma5600_2 - rest5600_2

tota5600_ = eeff5600_1 + eeff5600_2

#5700
dfsuma5700_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4313')]
suma5700_1 = float(dfsuma5700_1['Saldo Actual'].sum())
dfrest5700_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5415') ]
rest5700_1 = float(dfrest5700_1['Saldo Actual'].sum())
eeff5700_1 = suma5700_1 - rest5700_1

dfsuma5700_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4323')]
suma5700_2 = float(dfsuma5700_2['Saldo Actual'].sum())
dfrest5700_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5425')]
rest5700_2 = float(dfrest5700_2['Saldo Actual'].sum())
eeff5700_2 = suma5700_2 - rest5700_2

tota5700_ = eeff5700_1 + eeff5700_2

#5800
dfsuma5800_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '431401') |
                          (df_abs['Nro Cuenta'] == '431402')]
suma5800_1 = float(dfsuma5800_1['Saldo Actual'].sum())
dfrest5800_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5416') ]
rest5800_1 = float(dfrest5800_1['Saldo Actual'].sum())
eeff5800_1 = suma5800_1 - rest5800_1

dfsuma5800_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '432401') |
                          (df_abs['Nro Cuenta'] == '432402')]
suma5800_2 = float(dfsuma5800_2['Saldo Actual'].sum())
dfrest5800_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5426')]
rest5800_2 = float(dfrest5800_2['Saldo Actual'].sum())
eeff5800_2 = suma5800_2 - rest5800_2

tota5800_ = eeff5800_1 + eeff5800_2

#5900
dfsuma5900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '431403')]
suma5900_1 = float(dfsuma5900_1['Saldo Actual'].sum())
dfrest5900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'nein') ]
rest5900_1 = float(dfrest5900_1['Saldo Actual'].sum())
eeff5900_1 = suma5900_1 - rest5900_1

dfsuma5900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '432403')]
suma5900_2 = float(dfsuma5900_2['Saldo Actual'].sum())
dfrest5900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'nein')]
rest5900_2 = float(dfrest5900_2['Saldo Actual'].sum())
eeff5900_2 = suma5900_2 - rest5900_2

tota5900_ = eeff5900_1 + eeff5900_2

#6000
dfsuma6000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4311')]
suma6000_1 = float(dfsuma6000_1['Saldo Actual'].sum())
dfrest6000_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5311') ]
rest6000_1 = float(dfrest6000_1['Saldo Actual'].sum())
eeff6000_1 = suma6000_1 - rest6000_1

dfsuma6000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4321')]
suma6000_2 = float(dfsuma6000_2['Saldo Actual'].sum())
dfrest6000_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5321')]
rest6000_2 = float(dfrest6000_2['Saldo Actual'].sum())
eeff6000_2 = suma6000_2 - rest6000_2

tota6000_ = eeff6000_1 + eeff6000_2

#6100
dfsuma6100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4414')]
suma6100_1 = float(dfsuma6100_1['Saldo Actual'].sum())
dfrest6100_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5312') ]
rest6100_1 = float(dfrest6100_1['Saldo Actual'].sum())
eeff6100_1 = suma6100_1 - rest6100_1

dfsuma6100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4424')]
suma6100_2 = float(dfsuma6100_2['Saldo Actual'].sum())
dfrest6100_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5322')]
rest6100_2 = float(dfrest6100_2['Saldo Actual'].sum())
eeff6100_2 = suma6100_2 - rest6100_2

tota6100_ = eeff6100_1 + eeff6100_2

#6200
dfsuma6200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '4415')]
suma6200_1 = float(dfsuma6200_1['Saldo Actual'].sum())
dfrest6200_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '5313') ]
rest6200_1 = float(dfrest6200_1['Saldo Actual'].sum())
eeff6200_1 = suma6200_1 - rest6200_1

dfsuma6200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '4425')]
suma6200_2 = float(dfsuma6200_2['Saldo Actual'].sum())
dfrest6200_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '5323')]
rest6200_2 = float(dfrest6200_2['Saldo Actual'].sum())
eeff6200_2 = suma6200_2 - rest6200_2

tota6200_ = eeff6200_1 + eeff6200_2

#6300
dfsuma6300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '431503')]
suma6300_1 = float(dfsuma6300_1['Saldo Actual'].sum())
dfrest6300_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay no busques')]
rest6300_1 = float(dfrest6300_1['Saldo Actual'].sum())
eeff6300_1 = suma6300_1 - rest6300_1

dfsuma6300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '432503')]
suma6300_2 = float(dfsuma6300_2['Saldo Actual'].sum())
dfrest6300_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'entiende, no hay')]
rest6300_2 = float(dfrest6300_2['Saldo Actual'].sum())
eeff6300_2 = suma6300_2 - rest6300_2

tota6300_ = eeff6300_1 + eeff6300_2

#6400
dfsuma6400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '431504')]
suma6400_1 = float(dfsuma6400_1['Saldo Actual'].sum())
dfrest6400_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '431509') ]
rest6400_1 = float(dfrest6400_1['Saldo Actual'].sum())
eeff6400_1 = suma6400_1 - rest6400_1

dfsuma6400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '432504')]
suma6400_2 = float(dfsuma6400_2['Saldo Actual'].sum())
dfrest6400_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '432509')]
rest6400_2 = float(dfrest6400_2['Saldo Actual'].sum())
eeff6400_2 = suma6400_2 - rest6400_2

tota6400_ = eeff6400_1 + eeff6400_2

#volviendo al 5500
eeff5500_1 = eeff5600_1 + eeff5700_1 + eeff5800_1 + eeff5900_1 + \
             eeff6000_1 + eeff6100_1 + eeff6200_1 + eeff6300_1 \
             + eeff6400_1
print(eeff5500_1)
eeff5500_2 = eeff5600_2 + eeff5700_2 + eeff5800_2 + eeff5900_2 + \
             eeff6000_2 + eeff6100_2 + eeff6200_2 + eeff6300_2 \
             + eeff6400_2             

tota5500_ = eeff5500_1 + eeff5500_2

#6500
eeff6500_1 = eeff5400_1 - eeff5500_1
eeff6500_2 = eeff5400_2 - eeff5500_2
tota6500_  = eeff6500_1 + eeff6500_2



#%%

nueva_fila = pd.DataFrame([['4800', 
                            'MARGEN OPERACIONAL', 
                            '{:.2f}'.format(abs(float(eeff4800_1))), 
                            '{:.2f}'.format(abs(float(eeff4800_2))), 
                            '{:.2f}'.format(abs(float(tota4800_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4900', 
                            'GASTOS DE ADMINISTRACIÓN', 
                            '{:.2f}'.format(abs(float(eeff4900_1))), 
                            '{:.2f}'.format(abs(float(eeff4900_2))), 
                            '{:.2f}'.format(abs(float(tota4900_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)


nueva_fila = pd.DataFrame([['5000', 
                            'Gastos de Personal y Directivos', 
                            '{:.2f}'.format(abs(float(eeff5000_1))), 
                            '{:.2f}'.format(abs(float(eeff5000_2))), 
                            '{:.2f}'.format(abs(float(tota5000_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5100', 
                            'Gastos por Servicios Recibidos de Terceros', 
                            '{:.2f}'.format(abs(float(eeff5100_1))), 
                            '{:.2f}'.format(abs(float(eeff5100_2))), 
                            '{:.2f}'.format(abs(float(tota5100_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5200', 
                            'Impuestos y Contribuciones', 
                            '{:.2f}'.format(abs(float(eeff5200_1))), 
                            '{:.2f}'.format(abs(float(eeff5200_2))), 
                            '{:.2f}'.format(abs(float(tota5200_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5300', 
                            'DEPRECIACIONES Y AMORTIZACIONES', 
                            '{:.2f}'.format(abs(float(eeff5300_1))), 
                            '{:.2f}'.format(abs(float(eeff5300_2))), 
                            '{:.2f}'.format(abs(float(tota5300_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5400', 
                            'MARGEN OPERACIONAL NETO', 
                            '{:.2f}'.format(abs(float(eeff5400_1))), 
                            '{:.2f}'.format(abs(float(eeff5400_2))), 
                            '{:.2f}'.format(abs(float(tota5400_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5500', 
                            'VALUACIÓN DE ACTIVOS Y PROVISIONES', 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0))), 
                            '{:.2f}'.format(abs(float(0)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5600', 
                            'Provisiones para Créditos Indirectos', 
                            '{:.2f}'.format(abs(float(eeff5600_1))), 
                            '{:.2f}'.format(abs(float(eeff5600_2))), 
                            '{:.2f}'.format(abs(float(tota5600_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5700', 
                            'Provisiones para Incobrabilidad de Cuentas por Cobrar', 
                            '{:.2f}'.format(abs(float(eeff5700_1))), 
                            '{:.2f}'.format(abs(float(eeff5700_2))), 
                            '{:.2f}'.format(abs(float(tota5700_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5800', 
                            'Provisiones para Bienes Realizables, Recibidos en Pago, Recuperados y Adjudicados y Otros ', 
                            '{:.2f}'.format(abs(float(eeff5800_1))), 
                            '{:.2f}'.format(abs(float(eeff5800_2))), 
                            '{:.2f}'.format(abs(float(tota5800_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

a_eeff.iloc[54,2] = '{:.2f}'.format(eeff5500_1)
a_eeff.iloc[54,3] = '{:.2f}'.format(eeff5500_2)
a_eeff.iloc[54,4] = '{:.2f}'.format(tota5500_)

nueva_fila = pd.DataFrame([['5900', 
                            'Provisiones para Activos No Corrientes Mantenidos para la Venta', 
                            '{:.2f}'.format(abs(float(eeff5900_1))), 
                            '{:.2f}'.format(abs(float(eeff5900_2))), 
                            '{:.2f}'.format(abs(float(tota5900_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6000', 
                            'Deterioro de Inversiones', 
                            '{:.2f}'.format(abs(float(eeff6000_1))), 
                            '{:.2f}'.format(abs(float(eeff6000_2))), 
                            '{:.2f}'.format(abs(float(tota6000_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6100', 
                            'Deterioro de Activo Fijo', 
                            '{:.2f}'.format(abs(float(eeff6100_1))), 
                            '{:.2f}'.format(abs(float(eeff6100_2))), 
                            '{:.2f}'.format(abs(float(tota6100_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6200', 
                            'Deterioro de Activos Intangibles', 
                            '{:.2f}'.format(abs(float(eeff6200_1))), 
                            '{:.2f}'.format(abs(float(eeff6200_2))), 
                            '{:.2f}'.format(abs(float(tota6200_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6300', 
                            'Provisiones por Litigios y Demandas', 
                            '{:.2f}'.format(abs(float(eeff6300_1))), 
                            '{:.2f}'.format(abs(float(eeff6300_2))), 
                            '{:.2f}'.format(abs(float(tota6300_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6400', 
                            'Otras Provisiones', 
                            '{:.2f}'.format(abs(float(eeff6400_1))), 
                            '{:.2f}'.format(abs(float(eeff6400_2))), 
                            '{:.2f}'.format(abs(float(tota6400_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6500', 
                            'RESULTADO DE OPERACIÓN', 
                            '{:.2f}'.format(abs(float(eeff6500_1))), 
                            '{:.2f}'.format(abs(float(eeff6500_2))), 
                            '{:.2f}'.format(abs(float(tota6500_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

#%%
#6600
dfsuma6600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '56') |
                          (df_abs['Nro Cuenta'] == '57') |
                          (df_abs['Nro Cuenta'] == '511507') |
                          (df_abs['Nro Cuenta'] == '511910') |
                          (df_abs['Nro Cuenta'] == '5213') |
                          (df_abs['Nro Cuenta'] == '511519')]
suma6600_1 = float(dfsuma6600_1['Saldo Actual'].sum())
dfrest6600_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '46') |
                          (df_abs['Nro Cuenta'] == '49') |
                          (df_abs['Nro Cuenta'] == '411910') |
                          (df_abs['Nro Cuenta'] == '4515')]
rest6600_1 = float(dfrest6600_1['Saldo Actual'].sum())
eeff6600_1 = suma6600_1 - rest6600_1

dfsuma6600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
suma6600_2 = float(dfsuma6600_2['Saldo Actual'].sum())
dfrest6600_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest6600_2 = float(dfrest6600_2['Saldo Actual'].sum())
eeff6600_2 = suma6600_2 - rest6600_2

tota6600_ = eeff6600_1 + eeff6600_2

#6700
eeff6700_1 = eeff6600_1
eeff6700_2 = eeff6600_2
tota6700_  = eeff6700_1 + eeff6700_2

#6800
eeff6800_1 = eeff6500_1 + eeff6600_1
eeff6800_2 = eeff6500_2 + eeff6600_2 #tiene que ir suma porque en ingresos o gastos

tota6800_ = eeff6800_1 + eeff6800_2

#6900
dfsuma6900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '68')]
suma6900_1 = float(dfsuma6900_1['Saldo Actual'].sum())
dfrest6900_1 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest6900_1 = float(dfrest6900_1['Saldo Actual'].sum())
eeff6900_1 = suma6900_1 - rest6900_1

dfsuma6900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
suma6900_2 = float(dfsuma6900_2['Saldo Actual'].sum())
dfrest6900_2 = df_abs.loc[(df_abs['Nro Cuenta'] == 'no hay')]
rest6900_2 = float(dfrest6900_2['Saldo Actual'].sum())
eeff6900_2 = suma6900_2 - rest6900_2

tota6900_ = eeff6900_1 + eeff6900_2

#7000
eeff7000_1 = eeff6800_1 - eeff6900_1
eeff7000_2 = eeff6800_2 - eeff6900_2


tota7000_ = eeff7000_1 + eeff7000_2


#%%
nueva_fila = pd.DataFrame([['6600', 
                            'OTROS INGRESOS Y GASTOS ', 
                            '{:.2f}'.format(abs(float(eeff6600_1))), 
                            '{:.2f}'.format(abs(float(eeff6600_2))), 
                            '{:.2f}'.format(abs(float(tota6600_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6700', 
                            'Otros Ingresos y Gastos', 
                            '{:.2f}'.format(abs(float(eeff6700_1))), 
                            '{:.2f}'.format(abs(float(eeff6700_2))), 
                            '{:.2f}'.format(abs(float(tota6700_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6800', 
                            'RESULTADOS DEL EJERCICIO ANTES DE  IMPUESTO A LA RENTA (2)', 
                            '{:.2f}'.format(abs(float(eeff6800_1))), 
                            '{:.2f}'.format(abs(float(eeff6800_2))), 
                            '{:.2f}'.format(abs(float(tota6800_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6900', 
                            'IMPUESTO A LA RENTA', 
                            '{:.2f}'.format(abs(float(eeff6900_1))), 
                            '{:.2f}'.format(abs(float(eeff6900_2))), 
                            '{:.2f}'.format(abs(float(tota6900_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7000', 
                            'RESULTADO NETO DEL EJERCICIO (3)', 
                            '{:.2f}'.format(abs(float(eeff7000_1))), 
                            '{:.2f}'.format(abs(float(eeff7000_2))), 
                            '{:.2f}'.format(abs(float(tota7000_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
a_eeff = pd.concat([a_eeff,nueva_fila], ignore_index=True)



nombre = "RESULTADO_EJERCICIO.xlsx"
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

a_eeff.to_excel(nombre, index=False)



