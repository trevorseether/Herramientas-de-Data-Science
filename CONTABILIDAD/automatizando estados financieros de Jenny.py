# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 16:02:59 2023

@author: sanmiguel38
"""

import pandas as pd
pd.options.display.float_format = '{:.2f}'.format
import os

#%%
'anotar esta vaina de acá porque está buena para solucionar el problema de los números decimales'
def convert_number(n):
    return "{:.2f}".format(n)

df = pd.read_excel('C:\\Users\\sanmiguel38\\Desktop\\contabilidad Jenny\\EEFF - Nivel 2 - Formato.xlsx', 
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
for i in range (543,552):
    df = df.drop(i)
del i

'para eliminar la columna que no sirve de nada'
df = df.drop('Unnamed: 0', axis=1)


#df['Saldo Actual'] = pd.to_numeric(df['Saldo Actual'], downcast='float')
#%%

df['Saldo Actual'] = pd.to_numeric(df['Saldo Actual'], errors='coerce')
df_abs = df.copy()
df_abs = df_abs.drop(columns=['Saldo Actual'])
df_saldo = df['Saldo Actual'].copy()
df_saldo = pd.DataFrame(df_saldo)
df_saldo = df_saldo['Saldo Actual'].abs()
df_saldo = pd.DataFrame(df_saldo)
df_abs['Saldo Actual'] = df_saldo['Saldo Actual']


#%%
'aqui aprendí que si escribes la variable en mayúscula, no aparece en el explorador de variables'
#2
disponible = df.loc[(df['Nro Cuenta'] == '11')]
eeff1_0 = disponible['Saldo Actual'].sum()
del(disponible)

#3
caja300_1 = df.loc[(df['Nro Cuenta'] == '1111')]
eeff3_1 = caja300_1['Saldo Actual'].sum()
del(caja300_1)
caja300_2 = df.loc[(df['Nro Cuenta'] == '1121')]
eeff3_2 = caja300_2['Saldo Actual'].sum()
del(caja300_2)
tot1101 = float(eeff3_1) + float(eeff3_2)

#4
ban_f_ext = df.loc[(df['Nro Cuenta'] == '1113') | #este palito sirve de 'or' 
                   (df['Nro Cuenta'] == '111803')]
eeff4_1 = ban_f_ext['Saldo Actual'].sum()
del(ban_f_ext)
ban_f_ext_me = df.loc[(df['Nro Cuenta'] == '1123') | #este palito sirve de 'or' 
                   (df['Nro Cuenta'] == '112803')]
eeff4_2 = ban_f_ext_me['Saldo Actual'].sum()
del(ban_f_ext_me)
tot400 = float(eeff4_1) + float(eeff4_2)
#5
df5_1 = df.loc[(df['Nro Cuenta'] == '1114') | #este palito sirve de 'or' 
                   (df['Nro Cuenta'] == '111804')]
eeff5_1 = df5_1['Saldo Actual'].sum()
del(df5_1)
df5_2 = df.loc[(df['Nro Cuenta'] == '1124') | #este palito sirve de 'or' 
                   (df['Nro Cuenta'] == '112804')]
eeff5_2 = df5_2['Saldo Actual'].sum()
del(df5_2)
tot500 = eeff5_1 + eeff5_2

#6
df6_1 = df.loc[(df['Nro Cuenta'] == '1116') | 
               (df['Nro Cuenta'] == '1117') | 
               (df['Nro Cuenta'] == '111807')]
eeff6_1 = df6_1['Saldo Actual'].sum()
del(df6_1)
df6_2 = df.loc[(df['Nro Cuenta'] == '1126') | 
               (df['Nro Cuenta'] == '1127') | 
               (df['Nro Cuenta'] == '112807')]
eeff6_2 = df6_2['Saldo Actual'].sum()
del(df6_2)
tot600 = float(eeff6_1) + float(eeff6_2)

#7
df7_1 = df.loc[(df['Nro Cuenta'] == '12')]
eeff7_1 = df7_1['Saldo Actual'].sum()
del(df7_1)
df7_2 = df.loc[(df['Nro Cuenta'] == 'no hay en dólares')]
eeff7_2 = df7_2['Saldo Actual'].sum()
del(df7_2)
tota7_ = float(eeff7_1) + float(eeff7_2)
#8
df8_1 = df.loc[(df['Nro Cuenta'] == '1311') |
               (df['Nro Cuenta'] == '1312') |
               (df['Nro Cuenta'] == '1316') |
               (df['Nro Cuenta'] == '131801')]
eeff8_1 = df8_1['Saldo Actual'].sum()
del df8_1
df8_2 = df.loc[(df["Nro Cuenta"] == '1321') |
               (df["Nro Cuenta"] == '1322') |
               (df["Nro Cuenta"] == '1326') |
               (df["Nro Cuenta"] == '132801')]
eeff8_2 = df8_2['Saldo Actual'].sum()
del df8_2
tot800 = float(eeff8_1) + float(eeff8_2)

#9
df9_1 = df.loc[(df['Nro Cuenta'] == '1311') |              
               (df['Nro Cuenta'] == '131801')]
eeff9_1 = df9_1['Saldo Actual'].sum()
del df9_1
df9_2 = df.loc[(df["Nro Cuenta"] == '1321') |               
               (df["Nro Cuenta"] == '132801')]
eeff9_2 = df9_2['Saldo Actual'].sum()
del df9_2
tot900 = float(eeff9_1) + float(eeff9_2)

#10
df10_1 = df.loc[(df['Nro Cuenta'] == '1312')]
eeff10_1 = df10_1['Saldo Actual'].sum()
del df10_1
df10_2 = df.loc[(df['Nro Cuenta'] == '1322')]
eeff10_2 = df10_2['Saldo Actual'].sum()
del df10_2
tot10 = float(eeff10_1) + float(eeff10_2)

#11
df11_1 = df.loc[(df['Nro Cuenta'] == '1316')]
eeff11_1 = df11_1['Saldo Actual'].sum()
del df11_1
df11_2 = df.loc[(df['Nro Cuenta'] == '1326')]
eeff11_2 = df11_2['Saldo Actual'].sum()
del df11_2
tot11 = float(eeff11_1) + float(eeff11_2)

#12
df12_1 = df.loc[(df['Nro Cuenta'] == '1313') |
                (df['Nro Cuenta'] == '1314') |
                (df['Nro Cuenta'] == '131803') |
                (df['Nro Cuenta'] == '131903') |
                (df['Nro Cuenta'] == '131904')]
eeff12_1 = df12_1['Saldo Actual'].sum()
del df12_1
df12_2 = df.loc[(df['Nro Cuenta'] == '1323') |
                (df['Nro Cuenta'] == '1324') |
                (df['Nro Cuenta'] == '132803') |
                (df['Nro Cuenta'] == '132903') |
                (df['Nro Cuenta'] == '132904')]
eeff12_2 = df12_2['Saldo Actual'].sum()
del df12_2
tot12 = float(eeff12_1) + float(eeff12_2)

#13
df13_1 = df.loc[(df['Nro Cuenta'] == '1313') |
                (df['Nro Cuenta'] == '131803') |
                (df['Nro Cuenta'] == '131903')]
eeff13_1 = df13_1['Saldo Actual'].sum()
del df13_1
df13_2 = df.loc[(df['Nro Cuenta'] == '1323') |
                (df['Nro Cuenta'] == '132803') |
                (df['Nro Cuenta'] == '132903')]
eeff13_2 = df13_2['Saldo Actual'].sum()
del df13_2
tot13_ = float(eeff13_1) + float(eeff13_2)

#14
df14_1 = df.loc[(df['Nro Cuenta'] == '1314') |
                (df['Nro Cuenta'] == '131904')]
eeff14_1 = df14_1['Saldo Actual'].sum()
del df14_1
df14_2 = df.loc[(df['Nro Cuenta'] == '1324') |
                (df['Nro Cuenta'] == '132904')]
eeff14_2 = df14_2['Saldo Actual'].sum()
del df14_2
tot14_ = float(eeff14_1) + float(eeff14_2)

#15
df15_1 = df.loc[(df['Nro Cuenta'] == '1315') |
                (df['Nro Cuenta'] == '131905')]
eeff15_1 = df15_1['Saldo Actual'].sum()
del df15_1
df15_2 = df.loc[(df['Nro Cuenta'] == '1325') |
                (df['Nro Cuenta'] == '132905')]
eeff15_2 = df15_2['Saldo Actual'].sum()
del df15_2
tot15_ = float(eeff15_1) + float(eeff15_2)

#16
'este será la suma de 17 + 18 +19 + 20 + 21 + 22'

#17
df17_1 = df.loc[(df['Nro Cuenta'] == '1411') |
                (df['Nro Cuenta'] == '1418') |
                (df['Nro Cuenta'] == '29110101') |
                (df['Nro Cuenta'] == '29110201') |
                (df['Nro Cuenta'] == '2911070201') |
                (df['Nro Cuenta'] == '2911080101')]
eeff17_1 = df17_1['Saldo Actual'].sum()
del df17_1
df17_2 = df.loc[(df['Nro Cuenta'] == '1421') |
                (df['Nro Cuenta'] == '1428') |
                (df['Nro Cuenta'] == '29210101') |
                (df['Nro Cuenta'] == '29210201') |
                (df['Nro Cuenta'] == '2921070201') |
                (df['Nro Cuenta'] == '2921080101')]
eeff17_2 = df17_2['Saldo Actual'].sum()
del df17_2
tot17_ = float(eeff17_1) + float(eeff17_2)

#18
df18_1 = df.loc[(df['Nro Cuenta'] == '1413') |
                (df['Nro Cuenta'] == '29110103') |
                (df['Nro Cuenta'] == '2911070203') |
                (df['Nro Cuenta'] == '2911080103')]
eeff18_1 = df18_1['Saldo Actual'].sum()
del df18_1
df18_2 = df.loc[(df['Nro Cuenta'] == '1423') |
                (df['Nro Cuenta'] == '29210103') |
                (df['Nro Cuenta'] == '2921070203') |
                (df['Nro Cuenta'] == '2921080103')]
eeff18_2 = df18_2['Saldo Actual'].sum()
del df18_2
tot18_ = float(eeff18_1) + float(eeff18_2)

#19
df19_1 = df.loc[(df['Nro Cuenta'] == '1414') |
                (df['Nro Cuenta'] == '29110104') |
                (df['Nro Cuenta'] == '2911070204') |
                (df['Nro Cuenta'] == '2911080104')]
eeff19_1 = df19_1['Saldo Actual'].sum()
del df19_1
df19_2 = df.loc[(df['Nro Cuenta'] == '1424') |
                (df['Nro Cuenta'] == '29210104') |
                (df['Nro Cuenta'] == '2921070204') |
                (df['Nro Cuenta'] == '2921080104')]
eeff19_2 = df19_2['Saldo Actual'].sum()
del df19_2
tot19_ = float(eeff19_1) + float(eeff19_2)

#20
df20_1 = df.loc[(df['Nro Cuenta'] == '1415') |
                (df['Nro Cuenta'] == '29110105') |
                (df['Nro Cuenta'] == '29110205') |
                (df['Nro Cuenta'] == '2911070205') |
                (df['Nro Cuenta'] == '2911080105')]
eeff20_1 = df20_1['Saldo Actual'].sum()
del df20_1
df20_2 = df.loc[(df['Nro Cuenta'] == '1425') |
                (df['Nro Cuenta'] == '29210105') |
                (df['Nro Cuenta'] == '29210205') |
                (df['Nro Cuenta'] == '2921070205') |
                (df['Nro Cuenta'] == '2921080105')]
eeff20_2 = df20_2['Saldo Actual'].sum()
del df20_2
tot20_ = float(eeff20_1) + float(eeff20_2)

#21
df21_1 = df.loc[(df['Nro Cuenta'] == '1416') |
                (df['Nro Cuenta'] == '29110106') |
                (df['Nro Cuenta'] == '29110206') |
                (df['Nro Cuenta'] == '2911070206') |
                (df['Nro Cuenta'] == '2911080106')]
eeff21_1 = df21_1['Saldo Actual'].sum()
del df21_1
df21_2 = df.loc[(df['Nro Cuenta'] == '1426') |
                (df['Nro Cuenta'] == '29210106') |
                (df['Nro Cuenta'] == '29210206') |
                (df['Nro Cuenta'] == '2921070206') |
                (df['Nro Cuenta'] == '2921080106')]
eeff21_2 = df21_2['Saldo Actual'].sum()
del df21_2
tot21_ = float(eeff21_1) + float(eeff21_2)

#22_
df22_1 = df.loc[(df['Nro Cuenta'] == '1419')]
eeff22_1 = df22_1['Saldo Actual'].sum()
del df22_1
df22_2 = df.loc[(df['Nro Cuenta'] == '1429')]
eeff22_2 = df22_2['Saldo Actual'].sum()
del df22_2
tot22_ = float(eeff22_1) + float(eeff22_2)

#16 regresando a este
eeff16_1 = float(eeff17_1) + float(eeff18_1) + float(eeff19_1) + float(eeff20_1) + float(eeff21_1) + float(eeff22_1)
eeff16_2 = float(eeff17_2) + float(eeff18_2) + float(eeff19_2) + float(eeff20_2) + float(eeff21_2) + float(eeff22_2)
tota16_ = eeff16_1 + eeff16_2


#23_
df23_1 = df.loc[(df['Nro Cuenta'] == '1512')]
eeff23_1 = df23_1['Saldo Actual'].sum()
del df23_1
df23_2 = df.loc[(df['Nro Cuenta'] == '1522')]
eeff23_2 = df23_2['Saldo Actual'].sum()
del df23_2
tot23_ = float(eeff23_1) + float(eeff23_2)

#24_
df24_1 = df.loc[(df['Nro Cuenta'] == '1513')]
eeff24_1 = df24_1['Saldo Actual'].sum()
del df24_1
df24_2 = df.loc[(df['Nro Cuenta'] == '1523')]
eeff24_2 = df24_2['Saldo Actual'].sum()
del df24_2
tot24_ = float(eeff24_1) + float(eeff24_2)

#25_
df25_1 = df.loc[(df['Nro Cuenta'] == '1514') |
                (df['Nro Cuenta'] == '1515') |
                (df['Nro Cuenta'] == '1516') |
                (df['Nro Cuenta'] == '1517') |
                (df['Nro Cuenta'] == '1518') |
                (df['Nro Cuenta'] == '1519')]
eeff25_1 = df25_1['Saldo Actual'].sum()
del df25_1
df25_2 = df.loc[(df['Nro Cuenta'] == '1524') |
                (df['Nro Cuenta'] == '1525') |
                (df['Nro Cuenta'] == '1526') |
                (df['Nro Cuenta'] == '1527') |
                (df['Nro Cuenta'] == '1528') |
                (df['Nro Cuenta'] == '1529')]
eeff25_2 = df25_2['Saldo Actual'].sum()
del df25_2
tot25_ = float(eeff25_1) + float(eeff25_2)

#26_
df26_1 = df.loc[(df['Nro Cuenta'] == '1514') |
                (df['Nro Cuenta'] == '151804') |
                (df['Nro Cuenta'] == '151904')]
eeff26_1 = df26_1['Saldo Actual'].sum()
del df26_1
df26_2 = df.loc[(df['Nro Cuenta'] == '1524') |
                (df['Nro Cuenta'] == '152804') |
                (df['Nro Cuenta'] == '152904')]
eeff26_2 = df26_2['Saldo Actual'].sum()
del df26_2
tot26_ = float(eeff26_1) + float(eeff26_2)

#27_
df27_1 = df.loc[(df['Nro Cuenta'] == '1515') |
                (df['Nro Cuenta'] == '1516') |
                (df['Nro Cuenta'] == '1517') |
                (df['Nro Cuenta'] == '151805') |
                (df['Nro Cuenta'] == '151807') |
                (df['Nro Cuenta'] == '1519') |
                (df['Nro Cuenta'] == '151904')]
eeff27_1 = df27_1['Saldo Actual'].sum()
del df27_1
df27_2 = df.loc[(df['Nro Cuenta'] == '1525') |
                (df['Nro Cuenta'] == '1526') |
                (df['Nro Cuenta'] == '1527') |
                (df['Nro Cuenta'] == '152805') |
                (df['Nro Cuenta'] == '152807') |
                (df['Nro Cuenta'] == '1529') |
                (df['Nro Cuenta'] == '152904')]
eeff27_2 = df27_2['Saldo Actual'].sum()
del df27_2
tot27_ = float(eeff27_1) + float(eeff27_2)

#28_
df28_1 = df.loc[(df['Nro Cuenta'] == '1611') |
                (df['Nro Cuenta'] == '1612') |
                (df['Nro Cuenta'] == '161901') |
                (df['Nro Cuenta'] == '161902')]
eeff28_1 = df28_1['Saldo Actual'].sum()
del df28_1
df28_2 = df.loc[(df['Nro Cuenta'] == '1621') |
                (df['Nro Cuenta'] == '1622') |
                (df['Nro Cuenta'] == '162901') |
                (df['Nro Cuenta'] == '162902')]
eeff28_2 = df28_2['Saldo Actual'].sum()
del df28_2
tot28_ = float(eeff28_1) + float(eeff28_2)

#29_
df29_1 = df.loc[(df['Nro Cuenta'] == '1611') |
                (df['Nro Cuenta'] == '161901')]
eeff29_1 = df29_1['Saldo Actual'].sum()
del df29_1
df29_2 = df.loc[(df['Nro Cuenta'] == '1621') |
                (df['Nro Cuenta'] == '162901')]
eeff29_2 = df29_2['Saldo Actual'].sum()
del df29_2
tot29_ = float(eeff29_1) + float(eeff29_2)

#30_
df30_1 = df.loc[(df['Nro Cuenta'] == '1612') |
                (df['Nro Cuenta'] == '161902')]
eeff30_1 = df30_1['Saldo Actual'].sum()
del df30_1
df30_2 = df.loc[(df['Nro Cuenta'] == '1622') |
                (df['Nro Cuenta'] == '162902')]
eeff30_2 = df30_2['Saldo Actual'].sum()
del df30_2
tot30_ = float(eeff30_1) + float(eeff30_2)

#31_
'es la suma de 32 + 33'

#32_
df32_1 = df.loc[(df['Nro Cuenta'] == '171101') |
                (df['Nro Cuenta'] == '171201')]
eeff32_1 = df32_1['Saldo Actual'].sum()
del df32_1
df32_2 = df.loc[(df['Nro Cuenta'] == '172101') |
                (df['Nro Cuenta'] == '172201')]
eeff32_2 = df32_2['Saldo Actual'].sum()
del df32_2
tot32_ = float(eeff32_1) + float(eeff32_2)

#33_
df33_1 = df.loc[(df['Nro Cuenta'] == '171102') |
                (df['Nro Cuenta'] == '171202')]
eeff33_1 = df33_1['Saldo Actual'].sum()
del df33_1
df33_2 = df.loc[(df['Nro Cuenta'] == '172102') |
                (df['Nro Cuenta'] == '172202')]
eeff33_2 = df33_2['Saldo Actual'].sum()
del df33_2
tot33_ = float(eeff33_1) + float(eeff33_2)

#34_
df34_1 = df.loc[(df['Nro Cuenta'] == '18')]
eeff34_1 = df34_1['Saldo Actual'].sum()
del df34_1

#35_
df35_1 = df.loc[(df['Nro Cuenta'] == '1914')]
eeff35_1 = df35_1['Saldo Actual'].sum()
del df35_1
df35_2 = df.loc[(df['Nro Cuenta'] == '1924')]
eeff35_2 = df35_2['Saldo Actual'].sum()
del df35_2
tot35_ = float(eeff35_1) + float(eeff35_2)

#36_
df36_1 = df.loc[(df['Nro Cuenta'] == '191407') |
                (df['Nro Cuenta'] == '19140907')]
eeff36_1 = df36_1['Saldo Actual'].sum()
del df36_1
df36_2 = df.loc[(df['Nro Cuenta'] == '192407') |
                (df['Nro Cuenta'] == '19240907')]
eeff36_2 = df36_2['Saldo Actual'].sum()
del df36_2
tot36_ = float(eeff36_1) + float(eeff36_2)

#37_
df37_1 = df.loc[(df['Nro Cuenta'] == '1914') |
                (df['Nro Cuenta'] == '191407') |
                (df['Nro Cuenta'] == '19140907')]
eeff37_1 = df37_1['Saldo Actual'].sum()
del df37_1
df37_2 = df.loc[(df['Nro Cuenta'] == '1924') |
                (df['Nro Cuenta'] == '192407') |
                (df['Nro Cuenta'] == '19240907')]
eeff37_2 = df37_2['Saldo Actual'].sum()
del df37_2
tot37_ = float(eeff37_1) + float(eeff37_2)

#38_
df38_1 = df.loc[(df['Nro Cuenta'] == '191601') |
                (df['Nro Cuenta'] == '191602') |
                (df['Nro Cuenta'] == '25170301') |
                (df['Nro Cuenta'] == '25170302') ]
eeff38_1 = df38_1['Saldo Actual'].sum()
del df38_1
df38_2 = df.loc[(df['Nro Cuenta'] == '192601') |
                (df['Nro Cuenta'] == '192602') |
                (df['Nro Cuenta'] == '25270301') |
                (df['Nro Cuenta'] == '25270302')]
eeff38_2 = df38_2['Saldo Actual'].sum()
del df38_2
tot38_ = float(eeff38_1) + float(eeff38_2)

#39_
df39_1 = df.loc[(df['Nro Cuenta'] == '1913')]
eeff39_1 = df39_1['Saldo Actual'].sum()
del df39_1
df39_2 = df.loc[(df['Nro Cuenta'] == '1923')]
eeff39_2 = df39_2['Saldo Actual'].sum()
del df39_2
tot39_ = float(eeff39_1) + float(eeff39_2)

#40_
df40_1 = df.loc[(df['Nro Cuenta'] == '1613') |
                (df['Nro Cuenta'] == '161903')]
eeff40_1 = df40_1['Saldo Actual'].sum()
del df40_1
df40_2 = df.loc[(df['Nro Cuenta'] == '1623') |
                (df['Nro Cuenta'] == '162903')]
eeff40_2 = df40_2['Saldo Actual'].sum()
del df40_2
tot40_ = float(eeff40_1) + float(eeff40_2)

#41_
df41_1 = df.loc[(df['Nro Cuenta'] == '1911') |
                (df['Nro Cuenta'] == '191609') |
                (df['Nro Cuenta'] == '1917') |
                (df['Nro Cuenta'] == '1918') |
                (df['Nro Cuenta'] == '1919')]
eeff41_1 = df41_1['Saldo Actual'].sum()
del df41_1
df41_2 = df.loc[(df['Nro Cuenta'] == '1921') |
                (df['Nro Cuenta'] == '192609') |
                (df['Nro Cuenta'] == '1927') |
                (df['Nro Cuenta'] == '1928') |
                (df['Nro Cuenta'] == '1929')]
eeff41_2 = df41_2['Saldo Actual'].sum()
del df41_2
tot41_ = float(eeff41_1) + float(eeff41_2)


#%%
'crear dataframe'
eeff = pd.DataFrame(columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])

nueva_fila = pd.DataFrame([['100', 'ACTIVO', '', '', '']], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['200', 'DISPONIBLE', '', '', 
                            '{:.2f}'.format(float(eeff1_0))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['300', 'Caja', 
                            '{:.2f}'.format(float(eeff3_1)), 
                            '{:.2f}'.format(float(eeff3_2)), 
                            '{:.2f}'.format(float(tot1101))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['400', 'Bancos, otras Empresas del Sistema Financiero del País y COOPAC',
                            '{:.2f}'.format(float(eeff4_1)), 
                            '{:.2f}'.format(float(eeff4_2)), 
                            '{:.2f}'.format(tot400)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['500', 'Bancos y otras Instituciones Financieras del Exterior',
                            '{:.2f}'.format(float(eeff5_1)), 
                            '{:.2f}'.format(float(eeff5_2)), 
                            '{:.2f}'.format(tot500)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['600', 'Otras Disponibilidades',
                            '{:.2f}'.format(float(eeff6_1)), 
                            '{:.2f}'.format(float(eeff6_2)), 
                            '{:.2f}'.format(tot600)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['700', 'FONDOS INTERCOOPERATIVOS',
                            '{:.2f}'.format(float(eeff7_1)),
                            '{:.2f}'.format(float(eeff7_2)), 
                            '{:.2f}'.format(float(tota7_))]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)
'añadiendo la suma de los demás'
dis1 = float(eeff3_1) + float(eeff4_1) + float(eeff5_1) + float(eeff6_1)
eeff.iloc[1,2] = '{:.2f}'.format(dis1)

dis2 = float(eeff3_2) + float(eeff4_2) + float(eeff5_2) + float(eeff6_2)
eeff.iloc[1,3] = '{:.2f}'.format(dis2)


#%%
nueva_fila = pd.DataFrame([['800', 'INVERSIONES A VALOR RAZONABLE CON CAMBIOS EN RESULTADOS',
                            '{:.2f}'.format(float(eeff8_1)), 
                            '{:.2f}'.format(float(eeff8_2)), 
                            '{:.2f}'.format(tot800)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['900', 'Instrumentos de capital',
                            '{:.2f}'.format(float(eeff9_1)), 
                            '{:.2f}'.format(float(eeff9_2)), 
                            '{:.2f}'.format(tot900)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1000', 'Instrumentos de deuda',
                            '{:.2f}'.format(float(eeff10_1)), 
                            '{:.2f}'.format(float(eeff10_2)), 
                            '{:.2f}'.format(tot10)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1100', 'Inversiones en Commodities',
                            '{:.2f}'.format(float(eeff11_1)), 
                            '{:.2f}'.format(float(eeff11_2)), 
                            '{:.2f}'.format(tot11)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1200', 'Inversiones en Commodities',
                            '{:.2f}'.format(float(eeff12_1)), 
                            '{:.2f}'.format(float(eeff12_2)), 
                            '{:.2f}'.format(tot12)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)


nueva_fila = pd.DataFrame([['1300', 'Instrumentos Representativos de Capital',
                            '{:.2f}'.format(float(eeff13_1)), 
                            '{:.2f}'.format(float(eeff13_2)), 
                            '{:.2f}'.format(tot13_)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1400', 'Instrumentos Representativos de Deuda',
                            '{:.2f}'.format(float(eeff14_1)), 
                            '{:.2f}'.format(float(eeff14_2)), 
                            '{:.2f}'.format(tot14_)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1500', 'INVERSIONES A VENCIMIENTO',
                            '{:.2f}'.format(float(eeff15_1)), 
                            '{:.2f}'.format(float(eeff15_2)), 
                            '{:.2f}'.format(tot15_)]], columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

#%%

nueva_fila = pd.DataFrame([['1600', 'CARTERA DE CREDITOS',
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1700', 'Cartera de Créditos Vigentes',
                            '{:.2f}'.format(float(eeff17_1)), 
                            '{:.2f}'.format(float(eeff17_2)), 
                            '{:.2f}'.format(float(tot17_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1800', 'Cartera de Créditos Reestructurados',
                            '{:.2f}'.format(float(eeff18_1)), 
                            '{:.2f}'.format(float(eeff18_2)), 
                            '{:.2f}'.format(float(tot18_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['1900', 'Cartera de Créditos Refinanciados',
                            '{:.2f}'.format(float(eeff19_1)), 
                            '{:.2f}'.format(float(eeff19_2)), 
                            '{:.2f}'.format(float(tot19_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2000', 'Cartera de Créditos Vencidos',
                            '{:.2f}'.format(float(eeff20_1)), 
                            '{:.2f}'.format(float(eeff20_2)), 
                            '{:.2f}'.format(float(tot20_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2100', 'Cartera de Créditos en Cobranza Judicial',
                            '{:.2f}'.format(float(eeff21_1)), 
                            '{:.2f}'.format(float(eeff21_2)), 
                            '{:.2f}'.format(float(tot21_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2200', '- Provisiones para Créditos ...........',
                            '{:.2f}'.format(float(eeff22_1)), 
                            '{:.2f}'.format(float(eeff22_2)), 
                            '{:.2f}'.format(float(tot22_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)


eeff.iloc[15,2] = '{:.2f}'.format(eeff16_1)
eeff.iloc[15,3] = '{:.2f}'.format(eeff16_2)
eeff.iloc[15,4] = '{:.2f}'.format(tota16_)

#%%
nueva_fila = pd.DataFrame([['2300', 'DERIVADOS PARA NEGOCIACION',
                            '{:.2f}'.format(float(eeff23_1)), 
                            '{:.2f}'.format(float(eeff23_2)), 
                            '{:.2f}'.format(float(tot23_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2400', 'DERIVADOS DE COBERTURA',
                            '{:.2f}'.format(float(eeff24_1)), 
                            '{:.2f}'.format(float(eeff24_2)), 
                            '{:.2f}'.format(float(tot24_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2500', 'CUENTAS POR COBRAR',
                            '{:.2f}'.format(float(eeff25_1)), 
                            '{:.2f}'.format(float(eeff25_2)), 
                            '{:.2f}'.format(float(tot25_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2600', 'Cuentas por Cobrar por Venta de Bienes y Servicios y Fideicomiso',
                            '{:.2f}'.format(float(eeff26_1)), 
                            '{:.2f}'.format(float(eeff26_2)), 
                            '{:.2f}'.format(float(tot26_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2700', 'Otras Cuentas por Cobrar',
                            '{:.2f}'.format(float(eeff27_1)), 
                            '{:.2f}'.format(float(eeff27_2)), 
                            '{:.2f}'.format(float(tot27_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2800', 'BIENES REALIZABLES, RECIBIDOS EN PAGO Y ADJUDICADOS',
                            '{:.2f}'.format(float(eeff28_1)), 
                            '{:.2f}'.format(float(eeff28_2)), 
                            '{:.2f}'.format(float(tot28_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['2900', 'Bienes Realizables',
                            '{:.2f}'.format(float(eeff29_1)), 
                            '{:.2f}'.format(float(eeff29_2)), 
                            '{:.2f}'.format(float(tot29_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3000', 'Bienes  Recibidos en Pago y Adjudicados',
                            '{:.2f}'.format(float(eeff30_1)), 
                            '{:.2f}'.format(float(eeff30_2)), 
                            '{:.2f}'.format(float(tot30_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)




#%%
x31_1 = float(eeff32_1) + float(eeff33_1) 
x31_2 = float(eeff32_2) + float(eeff33_2) 
tot31 = x31_1 + x31_2

nueva_fila = pd.DataFrame([['3100', 'PARTICIPACIONES',
                            '{:.2f}'.format(float(x31_1)), 
                            '{:.2f}'.format(float(x31_2)), 
                            '{:.2f}'.format(float(tot31))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3200', 'Subsidiarias',
                            '{:.2f}'.format(float(eeff32_1)), 
                            '{:.2f}'.format(float(eeff32_2)), 
                            '{:.2f}'.format(float(tot32_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3300', 'Asociadas',
                            '{:.2f}'.format(float(eeff33_1)), 
                            '{:.2f}'.format(float(eeff33_2)), 
                            '{:.2f}'.format(float(tot33_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3400', 'INMUEBLES, MOBILIARIO Y EQUIPO',
                            '{:.2f}'.format(float(eeff34_1)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(eeff34_1))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3500', 'ACTIVO INTANGIBLE',
                            '{:.2f}'.format(float(eeff35_1)), 
                            '{:.2f}'.format(float(eeff35_2)), 
                            '{:.2f}'.format(float(tot35_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3600', 'Plusvalía',
                            '{:.2f}'.format(float(eeff36_1)), 
                            '{:.2f}'.format(float(eeff36_2)), 
                            '{:.2f}'.format(float(tot36_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3700', 'Otros activos intangibles',
                            '{:.2f}'.format(float(eeff35_1)), 
                            '{:.2f}'.format(float(eeff35_2)), 
                            '{:.2f}'.format(float(tot35_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3800', 'IMPUESTOS CORRIENTES',
                            '{:.2f}'.format(float(eeff38_1)), 
                            '{:.2f}'.format(float(eeff38_2)), 
                            '{:.2f}'.format(float(tot38_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['3900', 'IMPUESTO DIFERIDO',
                            '{:.2f}'.format(float(eeff39_1)), 
                            '{:.2f}'.format(float(eeff39_2)), 
                            '{:.2f}'.format(float(tot39_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4000', 'ACTIVOS NO CORRIENTES MANTENIDOS PARA LA VENTA',
                            '{:.2f}'.format(float(eeff40_1)), 
                            '{:.2f}'.format(float(eeff40_2)), 
                            '{:.2f}'.format(float(tot40_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4100', 'OTROS ACTIVOS ',
                            '{:.2f}'.format(float(eeff41_1)), 
                            '{:.2f}'.format(float(eeff41_2)), 
                            '{:.2f}'.format(float(tot41_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

eeff42_1 = float(dis1) + float(eeff7_1) + float(eeff8_1) \
            + float(eeff12_1) + float(eeff15_1) + float(eeff16_1) \
            + float(eeff23_1)+ float(eeff24_1)+ float(eeff25_1)+ \
            float(eeff28_1)+ float(x31_1)+ float(eeff34_1)+ \
            float(eeff35_1)+ float(eeff38_1)+ float(eeff39_1)+ \
            float(eeff40_1)+ float(eeff41_1)
eeff42_2 = float(dis2) + float(eeff7_2) + float(eeff8_2) + float(eeff12_2)\
            + float(eeff15_2) + float(eeff16_2) + float(eeff23_2)+ float(eeff24_2)+\
                float(eeff25_2)+ float(eeff28_2)+ float(x31_2)+     float(0)   \
                    + float(eeff35_2)+ float(eeff38_2)+ float(eeff39_2)+ float(eeff40_2)+ float(eeff41_2)
tota42_ = float(eeff42_1) + float(eeff42_2)

nueva_fila = pd.DataFrame([['4200', 'TOTAL DEL ACTIVO ',
                            '{:.2f}'.format(float(eeff42_1)), 
                            '{:.2f}'.format(float(eeff42_2)), 
                            '{:.2f}'.format(float(tota42_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)



#%%
'43 es solo texto'
'44 es una suma que se hará posteriormente'
#45_
df45_1 = df.loc[(df['Nro Cuenta'] == '2111') |
                (df['Nro Cuenta'] == '211801')]
eeff45_1 = df45_1['Saldo Actual'].sum()
del df45_1
df45_2 = df.loc[(df['Nro Cuenta'] == '2121') |
                (df['Nro Cuenta'] == '212801')]
eeff45_2 = df45_2['Saldo Actual'].sum()
del df45_2
tota45_ = float(eeff45_1) + float(eeff45_2)

#46_
df46_1 = df.loc[(df['Nro Cuenta'] == '2112') |
                (df['Nro Cuenta'] == '211802')]
eeff46_1 = df46_1['Saldo Actual'].sum()
del df46_1
df46_2 = df.loc[(df['Nro Cuenta'] == '2122') |
                (df['Nro Cuenta'] == '212802')]
eeff46_2 = df46_2['Saldo Actual'].sum()
del df46_2
tota46_ = float(eeff46_1) + float(eeff46_2)

#47_
df47_1 = df.loc[(df['Nro Cuenta'] == '2113') |
                (df['Nro Cuenta'] == '211803')]
eeff47_1 = df47_1['Saldo Actual'].sum()
del df47_1
df47_2 = df.loc[(df['Nro Cuenta'] == '2123') |
                (df['Nro Cuenta'] == '212803')]
eeff47_2 = df47_2['Saldo Actual'].sum()
del df47_2
tota47_ = float(eeff47_1) + float(eeff47_2)

#48_
df48_1 = df.loc[(df['Nro Cuenta'] == '2117') |
                (df['Nro Cuenta'] == '211807')]
eeff48_1 = df48_1['Saldo Actual'].sum()
del df48_1
df48_2 = df.loc[(df['Nro Cuenta'] == '2127') |
                (df['Nro Cuenta'] == '212807')]
eeff48_2 = df48_2['Saldo Actual'].sum()
del df48_2
tota48_ = float(eeff48_1) + float(eeff48_2)


#%%
nueva_fila = pd.DataFrame([['4300', 'PASIVO',
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4400', 'OBLIGACIONES CON LOS SOCIOS',
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4500', 'Obligaciones a la Vista',
                            '{:.2f}'.format(abs(float(eeff45_1))), 
                            '{:.2f}'.format(abs(float(eeff45_2))), 
                            '{:.2f}'.format(abs(float(tota45_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4600', 'Obligaciones por Cuentas de Ahorro',
                            '{:.2f}'.format(abs(float(eeff46_1))), 
                            '{:.2f}'.format(abs(float(eeff46_2))), 
                            '{:.2f}'.format(abs(float(tota46_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4700', 'Obligaciones por Cuentas a Plazo',
                            '{:.2f}'.format(abs(float(eeff47_1))), 
                            '{:.2f}'.format(abs(float(eeff47_2))), 
                            '{:.2f}'.format(abs(float(tota47_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['4800', 'Obligaciones por Cuentas a Plazo',
                            '{:.2f}'.format(abs(float(eeff48_1))), 
                            '{:.2f}'.format(abs(float(eeff48_2))), 
                            '{:.2f}'.format(abs(float(tota48_)))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

eeff44_1 = abs(float(eeff45_1)) + abs(float(eeff46_1)) + \
    abs(float(eeff47_1)) + abs(float(eeff48_1))    
eeff44_2 = abs(float(eeff45_2)) + abs(float(eeff46_2)) + \
    abs(float(eeff47_2)) + abs(float(eeff48_2))
tota44_ = eeff44_1 +eeff44_2
eeff.iloc[43,2] = '{:.2f}'.format(eeff44_1)
eeff.iloc[43,3] = '{:.2f}'.format(eeff44_2)
eeff.iloc[43,4] = '{:.2f}'.format(tota44_)


#%%
#49_
df49_1 = df.loc[(df['Nro Cuenta'] == '22')]
eeff49_1 = df49_1['Saldo Actual'].sum()
del df49_1
eeff49_2 = 0
tota49_ = float(eeff49_1) + float(eeff49_2)

#50_
df50_1 = df.loc[(df['Nro Cuenta'] == '23')]
eeff50_1 = df50_1['Saldo Actual'].sum()
del df50_1
eeff50_2 = 0
tota50_ = float(eeff50_1) + float(eeff50_2)

#51_
df51_1 = df.loc[(df['Nro Cuenta'] == '2117') |
                (df['Nro Cuenta'] == '211807')]
eeff51_1 = df51_1['Saldo Actual'].sum()
del df51_1
df51_2 = df.loc[(df['Nro Cuenta'] == '2127') |
                (df['Nro Cuenta'] == '212807')]
eeff51_2 = df51_2['Saldo Actual'].sum()
del df51_2
tota51_ = float(eeff51_1) + float(eeff51_2)

#52_
df52_1 = df.loc[(df['Nro Cuenta'] == '2312') |
                (df['Nro Cuenta'] == '231802')]
eeff52_1 = df52_1['Saldo Actual'].sum()
del df52_1
df52_2 = df.loc[(df['Nro Cuenta'] == '2322') |
                (df['Nro Cuenta'] == '232802')]
eeff52_2 = df52_2['Saldo Actual'].sum()
del df52_2
tota52_ = float(eeff52_1) + float(eeff52_2)

#53_
df53_1 = df.loc[(df['Nro Cuenta'] == '2313') |
                (df['Nro Cuenta'] == '231803')]
eeff53_1 = df53_1['Saldo Actual'].sum()
del df53_1
df53_2 = df.loc[(df['Nro Cuenta'] == '2323') |
                (df['Nro Cuenta'] == '232803')]
eeff53_2 = df53_2['Saldo Actual'].sum()
del df53_2
tota53_ = float(eeff53_1) + float(eeff53_2)

#54_ 
'54 será la suma de los valores que tiene abajo'
#eeeff54_1 = float(eeff55_1)+ float(eeff56_1) + float(eeff57_1)+ float(eeff58_1)
#eeeff54_2 = float(eeff55_2)+ float(eeff56_2) + float(eeff57_2)+ float(0)
#tota54 = eeeff54_1 + eeeff54_2


#55_
df55_1 = df.loc[(df['Nro Cuenta'] == '2412') |
                (df['Nro Cuenta'] == '2413') |
                (df['Nro Cuenta'] == '2612') |
                (df['Nro Cuenta'] == '2613') |
                (df['Nro Cuenta'] == '241802') |
                (df['Nro Cuenta'] == '241803') |
                (df['Nro Cuenta'] == '261802') |
                (df['Nro Cuenta'] == '261803') |
                (df['Nro Cuenta'] == '191202') |
                (df['Nro Cuenta'] == '191203')]
eeff55_1 = df55_1['Saldo Actual'].sum()
del df55_1
df55_2 = df.loc[(df['Nro Cuenta'] == '2422') |
                (df['Nro Cuenta'] == '2423') |
                (df['Nro Cuenta'] == '2622') |
                (df['Nro Cuenta'] == '2623') |
                (df['Nro Cuenta'] == '242802') |
                (df['Nro Cuenta'] == '242803') |
                (df['Nro Cuenta'] == '262802') |
                (df['Nro Cuenta'] == '262803') |
                (df['Nro Cuenta'] == '192202') |
                (df['Nro Cuenta'] == '192203')]
eeff55_2 = df55_2['Saldo Actual'].sum()
del df55_2
tota55_ = float(eeff55_1) + float(eeff55_2)

#56_
df56_1 = df.loc[(df['Nro Cuenta'] == '2414') |
                 (df['Nro Cuenta'] == '2415') |
                 (df['Nro Cuenta'] == '2614') |
                 (df['Nro Cuenta'] == '2615') |
                 (df['Nro Cuenta'] == '241804') |
                 (df['Nro Cuenta'] == '241805') |
                 (df['Nro Cuenta'] == '261804') |
                 (df['Nro Cuenta'] == '261805') |
                 (df['Nro Cuenta'] == '191204') |
                 (df['Nro Cuenta'] == '191205')]
eeff56_1 = df56_1['Saldo Actual'].sum()
del df56_1
df56_2 = df.loc[(df['Nro Cuenta'] == '2424') |
                 (df['Nro Cuenta'] == '2425') |
                 (df['Nro Cuenta'] == '2624') |
                 (df['Nro Cuenta'] == '2625') |
                 (df['Nro Cuenta'] == '242804') |
                 (df['Nro Cuenta'] == '242805') |
                 (df['Nro Cuenta'] == '262804') |
                 (df['Nro Cuenta'] == '262805') |
                 (df['Nro Cuenta'] == '192204') |
                 (df['Nro Cuenta'] == '192205')]
eeff56_2 = df56_2['Saldo Actual'].sum()
del df56_2
tota56_ = float(eeff56_1) + float(eeff56_2)

#57_
df57_1 = df.loc[(df['Nro Cuenta'] == '2416') |
                 (df['Nro Cuenta'] == '2417') |
                 (df['Nro Cuenta'] == '2616') |
                 (df['Nro Cuenta'] == '2617') |
                 (df['Nro Cuenta'] == '241806') |
                 (df['Nro Cuenta'] == '241807') |
                 (df['Nro Cuenta'] == '261806') |
                 (df['Nro Cuenta'] == '261807') |
                 (df['Nro Cuenta'] == '191206') |
                 (df['Nro Cuenta'] == '191207')]
eeff57_1 = df57_1['Saldo Actual'].sum()
del df57_1
df57_2 = df.loc[(df['Nro Cuenta'] == '2426') |
                 (df['Nro Cuenta'] == '2427') |
                 (df['Nro Cuenta'] == '2626') |
                 (df['Nro Cuenta'] == '2627') |
                 (df['Nro Cuenta'] == '242806') |
                 (df['Nro Cuenta'] == '242807') |
                 (df['Nro Cuenta'] == '262806') |
                 (df['Nro Cuenta'] == '262807') |
                 (df['Nro Cuenta'] == '192206') |
                 (df['Nro Cuenta'] == '192207')]
eeff57_2 = df57_2['Saldo Actual'].sum()
del df57_2
tota57_ = float(eeff57_1) + float(eeff57_2)

#58_
df58_1 = df.loc[(df['Nro Cuenta'] == '28')]
eeff58_1 = df58_1['Saldo Actual'].sum()
del df58_1

eeff54_1 = float(eeff55_1)+ float(eeff56_1) + float(eeff57_1)+ float(eeff58_1)
eeff54_2 = float(eeff55_2)+ float(eeff56_2) + float(eeff57_2)+ float(0)
tota54 = eeff54_1 + eeff54_2


#59_
df59_1 = df.loc[(df['Nro Cuenta'] == '2512')]
eeff59_1 = df59_1['Saldo Actual'].sum()
del df59_1
df59_2 = df.loc[(df['Nro Cuenta'] == '2522')]
eeff59_2 = df59_2['Saldo Actual'].sum()
del df59_2
tota59_ = float(eeff59_1) + float(eeff59_2)

#60_
df60_1 = df.loc[(df['Nro Cuenta'] == '2513')]
eeff60_1 = df60_1['Saldo Actual'].sum()
del df60_1
df60_2 = df.loc[(df['Nro Cuenta'] == '2523')]
eeff60_2 = df60_2['Saldo Actual'].sum()
del df60_2
tota60_ = float(eeff60_1) + float(eeff60_2)

#61_
df61_suma1 = df_abs.loc[(df_abs['Nro Cuenta'] == '2514') |
                    (df_abs['Nro Cuenta'] == '2515') |
                    (df_abs['Nro Cuenta'] == '2516') |
                    (df_abs['Nro Cuenta'] == '2517') |
                    (df_abs['Nro Cuenta'] == '2518') ]
                
df61_resta1 = df_abs.loc[(df['Nro Cuenta'] == '25170301') |
                    (df['Nro Cuenta'] == '25170302') ]
eeff61_sumado_1 = df61_suma1['Saldo Actual'].sum()                
eeff61_resta_1 = df61_resta1['Saldo Actual'].sum() 
eeff61_1 = float(eeff61_sumado_1) - float(eeff61_resta_1)
del df61_suma1
del df61_resta1
df61_suma2 = df_abs.loc[(df_abs['Nro Cuenta'] == '2524') |
                    (df_abs['Nro Cuenta'] == '2525') |
                    (df_abs['Nro Cuenta'] == '2526') |
                    (df_abs['Nro Cuenta'] == '2527') |
                    (df_abs['Nro Cuenta'] == '2528') ]
                
df61_resta2 = df_abs.loc[(df_abs['Nro Cuenta'] == '25270301') |
                     (df_abs['Nro Cuenta'] == '25270302') ]
eeff61_sumado_2 = df61_suma2['Saldo Actual'].sum()                
eeff61_resta_2 = df61_resta2['Saldo Actual'].sum() 
eeff61_2 = float(eeff61_sumado_2) - float(eeff61_resta_2)
del df61_suma2
del df61_resta2
tota61_ = float(eeff61_1) + float(eeff61_2)

#62_
df62_1 = df.loc[(df['Nro Cuenta'] == '27')
                ]
eeff62_1 = abs(df62_1['Saldo Actual'].sum())
del df62_1

eeff62_2 = 0
tota62_ = float(eeff62_1) + float(eeff62_2)


#63_
df63_1 = df.loc[(df['Nro Cuenta'] == '271101') |
                (df['Nro Cuenta'] == '271102')
                ]
eeff63_1 = df63_1['Saldo Actual'].sum()
del df63_1
df63_2 = df.loc[(df['Nro Cuenta'] == '272101') |
                (df['Nro Cuenta'] == '272102')]
eeff63_2 = df63_2['Saldo Actual'].sum()
del df63_2
tota63_ = float(eeff63_1) + float(eeff63_2)

#64_
df64_1 = df.loc[(df['Nro Cuenta'] == '271202')
                ]
eeff64_1 = df64_1['Saldo Actual'].sum()
del df64_1
df64_2 = df.loc[(df['Nro Cuenta'] == '272202')]
eeff64_2 = df64_2['Saldo Actual'].sum()
del df64_2
tota64_ = float(eeff64_1) + float(eeff64_2)

#65_
dfsuma65_1 = df_abs.loc[(df['Nro Cuenta'] == '27')]
suma65 = dfsuma65_1['Saldo Actual'].sum()
dfresta65_1 =   df_abs.loc[(df['Nro Cuenta'] == '271101') |
                           (df['Nro Cuenta'] == '271102') |
                           (df['Nro Cuenta'] == '271202')]                
resta65 = dfresta65_1['Saldo Actual'].sum()
eeff65_1 = abs(float(suma65) - float(resta65))
del dfsuma65_1
del dfresta65_1
df65_2 = df.loc[(df['Nro Cuenta'] == 'no hay en dolares')]
eeff65_2 = df65_2['Saldo Actual'].sum()
del df65_2
tota65_ = float(eeff65_1) + float(eeff65_2)

#66_
dfsuma66_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '191601')]
suma66_1 = dfsuma66_1['Saldo Actual'].sum()
dfresta66_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '191602') |
                     (df_abs['Nro Cuenta'] == '25170301') |
                     (df_abs['Nro Cuenta'] == '25170302')]                
resta66_1 = dfresta66_1['Saldo Actual'].sum()
eeff66_1 = abs(float(suma66_1)) - abs(float(resta66_1))
del dfsuma66_1
del dfresta66_1

dfsuma66_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '192601')]
suma66_2 = dfsuma66_2['Saldo Actual'].sum()
dfresta66_2 = df_abs.loc[(df_abs['Nro Cuenta'] == '192602') |
                     (df_abs['Nro Cuenta'] == '25270301') |
                     (df_abs['Nro Cuenta'] == '25270302')]                
resta66_2 = dfresta66_2['Saldo Actual'].sum()
eeff66_2 = abs(float(suma66_2)) - abs(float(resta66_2))
del dfsuma66_2
del dfresta66_2

tota66_ = float(eeff66_1) + float(eeff66_2)

#67_
df67_1 = df.loc[(df['Nro Cuenta'] == '2913')]                
eeff67_1 = df67_1['Saldo Actual'].sum()
del df67_1
df67_2 = df.loc[(df['Nro Cuenta'] == '2923')]
eeff67_2 = df67_2['Saldo Actual'].sum()
del df67_2
tota67_ = float(eeff67_1) + float(eeff67_2)

#68_ 'hay que revisar esto'
dfsuma68_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '29') |
                (df_abs['Nro Cuenta'] == '29110207')]
suma68_1 = dfsuma68_1['Saldo Actual'].sum()
print(suma68_1)

dfresta68_1 = df_abs.loc[(df_abs['Nro Cuenta'] == '291101') |
                         (df_abs['Nro Cuenta'] == '291102') |
                         (df_abs['Nro Cuenta'] == '29110702') |
                         (df_abs['Nro Cuenta'] == '29110801') |
                         (df_abs['Nro Cuenta'] == '2913')]                
resta68_1 = abs(float(dfresta68_1['Saldo Actual'].sum()))
print(resta68_1)
eeff68_1 = suma68_1 - resta68_1

df68_2 = df.loc[(df['Nro Cuenta'] == 'no hay en dólares')]
eeff68_2 = df68_2['Saldo Actual'].sum()

tota68_ = float(eeff68_1) + float(eeff68_2)

#69_
               
eeff69_1 = float(eeff44_1) + float(eeff49_1)+ float(eeff50_1) + float(eeff54_1) + float(eeff59_1) + float(eeff60_1) + float(eeff61_1) + float(eeff62_1) + float(eeff66_1) + float(eeff67_1) + float(eeff68_1)
eeff69_2 = float(eeff44_2) + float(eeff49_2)+ float(eeff50_2) + float(eeff54_2) + float(eeff59_2) + float(eeff60_2) + float(eeff61_2) + float(eeff62_2) + float(eeff66_2) + float(eeff67_2) + float(eeff68_2)
tota69_  = eeff69_1 + eeff69_2

#%%
print(float(eeff49_1))
print(float(eeff50_1))
print(float(eeff54_1)) 
print(float(eeff59_1)) 
print(float(eeff60_1))
print(float(eeff61_1)) 
print(float(eeff62_1)) 
print(float(eeff66_1)) 
print(float(eeff67_1)) 
print(float(eeff68_1))




#%%
nueva_fila = pd.DataFrame([['4900', 'FONDOS INTERCOOPERATIVOS',
                            '{:.2f}'.format(float(eeff49_1)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(eeff49_1))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5000', 'DEPÓSITOS DE COOPAC',
                            '{:.2f}'.format(float(eeff50_1)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(eeff50_2))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5100', 'Depósitos a la Vista',
                            '{:.2f}'.format(float(eeff51_1)), 
                            '{:.2f}'.format(float(eeff51_2)), 
                            '{:.2f}'.format(float(tota51_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5200', 'Depósitos de Ahorro',
                            '{:.2f}'.format(float(eeff52_1)), 
                            '{:.2f}'.format(float(eeff52_2)), 
                            '{:.2f}'.format(float(tota52_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5300', 'Depósitos a Plazo',
                            '{:.2f}'.format(float(eeff53_1)), 
                            '{:.2f}'.format(float(eeff53_2)), 
                            '{:.2f}'.format(float(tota53_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)



nueva_fila = pd.DataFrame([['5400', 'ADEUDOS Y OBLIGACIONES FINANCIERAS',
                            '{:.2f}'.format(float(eeff54_1)), 
                            '{:.2f}'.format(float(eeff54_2)), 
                            '{:.2f}'.format(float(tota54))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5500', 'Adeudos y Obligaciones con COOPAC y Empresas e Instituciones financieras del  País',
                            '{:.2f}'.format(float(eeff55_1)), 
                            '{:.2f}'.format(float(eeff55_2)), 
                            '{:.2f}'.format(float(tota55_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5600', 'Adeudos y Obligaciones con Empresas del Exterior y Organismos Financieros Internacionales',
                            '{:.2f}'.format(float(eeff56_1)), 
                            '{:.2f}'.format(float(eeff56_2)), 
                            '{:.2f}'.format(float(tota56_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5700', 'Otros Adeudos  y  Obligaciones del país  y del  exterior',
                            '{:.2f}'.format(float(eeff57_1)), 
                            '{:.2f}'.format(float(eeff57_2)), 
                            '{:.2f}'.format(float(tota57_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5800', 'Valores y Títulos',
                            '{:.2f}'.format(float(eeff58_1)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(eeff58_1))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['5900', 'DERIVADOS PARA NEGOCIACIÓN',
                            '{:.2f}'.format(float(eeff59_1)), 
                            '{:.2f}'.format(float(eeff59_2)), 
                            '{:.2f}'.format(float(tota59_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6000', 'DERIVADOS DE COBERTURA',
                            '{:.2f}'.format(float(eeff60_1)), 
                            '{:.2f}'.format(float(eeff60_2)), 
                            '{:.2f}'.format(float(tota60_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6100', 'CUENTAS POR PAGAR',
                            '{:.2f}'.format(float(eeff61_1)), 
                            '{:.2f}'.format(float(eeff61_2)), 
                            '{:.2f}'.format(float(tota61_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6200', 'PROVISIONES',
                            '{:.2f}'.format(float(eeff62_1)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(eeff62_1))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6300', 'Provisión para créditos contingentes',
                            '{:.2f}'.format(float(eeff63_1)), 
                            '{:.2f}'.format(float(eeff63_2)), 
                            '{:.2f}'.format(float(tota63_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6400', 'Provisión para litigios y demandas',
                            '{:.2f}'.format(float(eeff64_1)), 
                            '{:.2f}'.format(float(eeff64_2)), 
                            '{:.2f}'.format(float(tota64_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6500', 'Otros',
                            '{:.2f}'.format(float(eeff65_1)), 
                            '{:.2f}'.format(float(eeff65_2)), 
                            '{:.2f}'.format(float(tota65_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6600', 'IMPUESTOS CORRIENTES',
                            '{:.2f}'.format(float(eeff66_1)), 
                            '{:.2f}'.format(float(eeff66_2)), 
                            '{:.2f}'.format(float(tota66_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6700', 'IMPUESTO DIFERIDO',
                            '{:.2f}'.format(float(eeff67_1)), 
                            '{:.2f}'.format(float(eeff67_2)), 
                            '{:.2f}'.format(float(tota67_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6800', 'OTROS PASIVOS',
                            '{:.2f}'.format(float(eeff68_1)), 
                            '{:.2f}'.format(float(eeff68_2)), 
                            '{:.2f}'.format(float(tota68_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['6900', 'TOTAL  DEL  PASIVO',
                            '{:.2f}'.format(float(eeff69_1)), 
                            '{:.2f}'.format(float(eeff69_2)), 
                            '{:.2f}'.format(float(tota69_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

'falta arreglar el 6800' # linea 1322

#%%
#70_ este es patrimonio

#71_
df71_1 = df.loc[(df['Nro Cuenta'] == '3111') |
                (df['Nro Cuenta'] == '3112') |
                (df['Nro Cuenta'] == '3113')]                
eeff71_1 = df71_1['Saldo Actual'].sum()
eeff71_1 = abs(float(eeff71_1))
del df71_1
df71_2 = df.loc[(df['Nro Cuenta'] == '3121') |
                (df['Nro Cuenta'] == '3122') |
                (df['Nro Cuenta'] == '3123')]
eeff71_2 = df71_2['Saldo Actual'].sum()
eeff71_2 = abs(float(eeff71_2))
del df71_2
tota71_ = float(eeff71_1) + float(eeff71_2)

#72_
df72_1 = df.loc[(df['Nro Cuenta'] == '3211')]                
eeff72_1 = df72_1['Saldo Actual'].sum()
eeff72_1 = abs(float(eeff72_1))
del df72_1
df72_2 = df.loc[(df['Nro Cuenta'] == '3221')]
eeff72_2 = df72_2['Saldo Actual'].sum()
eeff72_2 = abs(float(eeff72_2))

del df72_2
tota72_ = float(eeff72_1) + float(eeff72_2)

#73_
df73_1 = df.loc[(df['Nro Cuenta'] == '3311') |
                (df['Nro Cuenta'] == '3313')]                
eeff73_1 = df73_1['Saldo Actual'].sum()
eeff73_1 = abs(float(eeff73_1))
del df73_1
df73_2 = df.loc[(df['Nro Cuenta'] == '3321') |
                (df['Nro Cuenta'] == '3323')]
eeff73_2 = df73_2['Saldo Actual'].sum()
eeff73_2 = abs(float(eeff73_2))
del df73_2
tota73_ = float(eeff73_1) + float(eeff73_2)

#74_
dfsuma74_1 = df.loc[(df['Nro Cuenta'] == '38') |
                    (df['Nro Cuenta'] == '36')]
positivos74_1 = dfsuma74_1['Saldo Actual'].sum()
eeff74_1 = abs(float(positivos74_1))
dfresta74_1 = df.loc[(df['Nro Cuenta'] == '381101') |
                    (df['Nro Cuenta'] == '381102') |
                    (df['Nro Cuenta'] == '381201')]                
resta74_1 = dfresta74_1['Saldo Actual'].sum()
eeff74_1 = abs(float(resta74_1))
del dfsuma74_1
del dfresta74_1
df74_2 = df.loc[(df['Nro Cuenta'] == 'no hay en dólares')]
eeff74_2 = df74_2['Saldo Actual'].sum()
del df74_2
tota74_ = float(eeff74_1) + float(eeff74_2)

#75_ 
df75_1 = df.loc[(df['Nro Cuenta'] == '381101') |
                (df['Nro Cuenta'] == '381102') |
                (df['Nro Cuenta'] == '381201')]                
eeff75_1 = df75_1['Saldo Actual'].sum()
eeff75_1 = abs(float(eeff75_1))
del df75_1
df75_2 = df.loc[(df['Nro Cuenta'] == '382101') |
                (df['Nro Cuenta'] == '382102') |
                (df['Nro Cuenta'] == '382201')]
eeff75_2 = df75_2['Saldo Actual'].sum()
eeff75_2 = abs(float(eeff75_2))

del df75_2
tota75_ = float(eeff75_1) + float(eeff75_2)

#76_
df76_1 = df.loc[(df['Nro Cuenta'] == '3911') |
                (df['Nro Cuenta'] == '3912') ]                
eeff76_1 = df76_1['Saldo Actual'].sum()
eeff76_1 = abs(float(eeff76_1))
del df76_1
df76_2 = df.loc[(df['Nro Cuenta'] == '3921') |
                (df['Nro Cuenta'] == '3922') ]
eeff76_2 = df76_2['Saldo Actual'].sum()
eeff76_2 = abs(float(eeff76_2))
del df76_2
tota76_ = float(eeff76_1) + float(eeff76_2)

#77_ 
df77_1 = df.loc[(df['Nro Cuenta'] == '31') |
                (df['Nro Cuenta'] == '32') |
                (df['Nro Cuenta'] == '33') |
                (df['Nro Cuenta'] == '36') |
                (df['Nro Cuenta'] == '38') |
                (df['Nro Cuenta'] == '39')]                
eeff77_1 = df77_1['Saldo Actual'].sum()
eeff77_1 = abs(float(eeff77_1))
del df77_1
df77_2 = df.loc[(df['Nro Cuenta'] == 'no hay en dólares') ]
eeff77_2 = df77_2['Saldo Actual'].sum()
del df77_2
tota77_ = float(eeff77_1) + float(eeff77_2)

#78
eeff78_1 = eeff69_1 + eeff77_1
eeff78_2 = eeff69_2 + eeff77_2
tota78_  = eeff78_1 + eeff78_2

#%%
nueva_fila = pd.DataFrame([['7000', 'PATRIMONIO',
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0)), 
                            '{:.2f}'.format(float(0))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7100', 'Capital Social',
                            '{:.2f}'.format(float(eeff71_1)), 
                            '{:.2f}'.format(float(eeff71_2)), 
                            '{:.2f}'.format(float(tota71_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7200', 'Capital Adicional',
                            '{:.2f}'.format(float(eeff72_1)), 
                            '{:.2f}'.format(float(eeff72_2)), 
                            '{:.2f}'.format(float(tota72_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7300', 'Reservas',
                            '{:.2f}'.format(float(eeff73_1)), 
                            '{:.2f}'.format(float(eeff73_2)), 
                            '{:.2f}'.format(float(tota73_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7400', 'Ajustes al Patrimonio',
                            '{:.2f}'.format(float(eeff74_1)), 
                            '{:.2f}'.format(float(eeff74_2)), 
                            '{:.2f}'.format(float(tota74_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7500', 'Resultados Acumulados',
                            '{:.2f}'.format(float(eeff75_1)), 
                            '{:.2f}'.format(float(eeff75_2)), 
                            '{:.2f}'.format(float(tota75_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7600', 'Resultado Neto del Ejercicio',
                            '{:.2f}'.format(float(eeff76_1)), 
                            '{:.2f}'.format(float(eeff76_2)), 
                            '{:.2f}'.format(float(tota76_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7700', 'TOTAL DEL PATRIMONIO',
                            '{:.2f}'.format(float(eeff77_1)), 
                            '{:.2f}'.format(float(eeff77_2)), 
                            '{:.2f}'.format(float(tota77_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

nueva_fila = pd.DataFrame([['7800', 'TOTAL DEL  PASIVO Y PATRIMONIO',
                            '{:.2f}'.format(float(eeff78_1)), 
                            '{:.2f}'.format(float(eeff78_2)), 
                            '{:.2f}'.format(float(tota78_))]], 
                          columns=["Fila", "Detalle", "M.N.", "Equiv. a M.E.", "TOTAL"])
eeff = pd.concat([eeff,nueva_fila], ignore_index=True)

#%%

ajuste_patrimonio = df.loc[(df['Nro Cuenta'] == '38') |
                (df['Nro Cuenta'] == '36')]                
a_p = ajuste_patrimonio['Saldo Actual'].sum()

ajuste_patrimonio2 = df.loc[(df['Nro Cuenta'] == '381101') |
                           (df['Nro Cuenta'] == '381102') |
                           (df['Nro Cuenta'] == '381201')]                
a_p2 = ajuste_patrimonio2['Saldo Actual'].sum()

#%%
#este código es solo para crear un excel y revisarlo

nombre = "SITUACION_FINANCIERA.xlsx"
try:
    ruta = nombre
    os.remove(ruta)
except FileNotFoundError:
    pass

eeff.to_excel(nombre, index=False)