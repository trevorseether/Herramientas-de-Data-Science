# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:56:31 2023

@author: sanmiguel38
"""

import pandas as pd
import os
from datetime import datetime
import numpy as np

'AQUÍ SE PONE EL DIRECTORIO DE LOS ARCHIVOS CON LOS QUE VAMOS A TRABAJAR'
DIRECTORIO = "C:\\Users\sanmiguel38\Desktop\BAJAS KONECTA\CRUCE 11 04 2023"
os.chdir(DIRECTORIO)

'AQUI SE PONE LA FECHA QUE UNO QUIERE QUE APAREZCA EN EL NOMBRE DEL ARCHIVO'
FECHATXT = '11-04-2023'
#%%

'función poderosa para convertir texto de fechas a fechas datetime'
def parse_date(date_str):
    try:
        # Intentar parsear como fecha con formato DD/MM/YYYY HH:MM:SS
        return datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    except ValueError:
        try:
            # Si falla, intentar parsear como fecha con formato DD/MM/YYYY
            return datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            try:
                # Si falla, intentar parsear como fecha con formato DD-MM-YYYY HH:MM:SS
                return datetime.strptime(date_str, '%d-%m-%Y %H:%M:%S')
            except ValueError:
                try:
                    # Si falla, intentar parsear como fecha con formato DD-MM-YYYY HH:MM:SS
                    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    return date_str
                

#%%    
'importación de los excels'

columna_de_dni = 'Documento' #por si cambian el nombre donde está el dni
#esto se hace al reporte que mandan de cobranzas
'''al momento de importar el archivo de bajas, debemos crear una columna auxiliar con la fórmula
=texto(documento;"00000000000000"), que complete con ceros para tener 14 dígitos,
a este ponle el nombre de Documento, y la antigua el nombre Documentoque no funciona'''

bajas = pd.read_excel("Informe de bajas II - Abril.xlsx"
                      , #aqui cambiar el nombre y/o ubicación del archivo
                      dtype={columna_de_dni: object})  


bajas[columna_de_dni] = bajas[columna_de_dni].str.strip()


vigentes = pd.read_excel("creditos vigentes SM al 11-04-23 - para bajas Konecta - Borja corte 10_00pm.xlsx", #aqui cambiar el nombre y/o ubicación del archivo
                      dtype={'Doc_Identidad': object,
                             'codigosocio': object,
                             'pagare_fincore': object
                             },
                      parse_dates=['fechadesembolso']
                                   ,
                         date_parser=parse_date)


#La función "str.strip()" se utiliza para quitar los espacios en blanco en el principio y al final de cada valor en la columna "Doc_Identidad"
vigentes["Doc_Identidad"] = vigentes["Doc_Identidad"].str.strip()

#%%
'por si acaso, nos quedamos solo con los que tienen estado = pendiente'

vigentes["Estado"] = vigentes["Estado"].str.strip()

vigentes2 = vigentes.copy() #este es un checkpoint del dataframe, por si acaso, se malogra algo, para no empezar desde el principio
vigentes = vigentes[vigentes["Estado"] == 'PENDIENTE']

#%%
'nos quedamos solo con las columnas necesarias'

vigentes2 = vigentes[["Doc_Identidad", "Socio", "fechadesembolso", "pagare_fincore", "CuotaFija", "Planilla"]]
vigentes2 = vigentes2.rename(columns={"Doc_Identidad": "DOC_IDENTIDAD",
                                      "Socio": "SOCIO",
                                      "fechadesembolso": "FECHA_DESEMBOLSO",
                                      "pagare_fincore": "PAGARE_FINCORE",
                                      "CuotaFija": "CUOTA MENSUAL",
                                      "Planilla": "EMPRESA/PLANILLA"})

bajas2 = bajas[[columna_de_dni, 'Documentoque no funciona']] #hay que revisar este dataframe a ver si están todos los dnis
#%%

'agregamos 14 ceros para un mejor match'

vigentes2["DOC_IDENTIDAD"] = vigentes2["DOC_IDENTIDAD"].astype(str)
vigentes2["DOC_IDENTIDAD_ceros"] = vigentes2["DOC_IDENTIDAD"].str.zfill(14)


#%%

'inner join usando '
df_resultado = vigentes2.merge(bajas2, 
                         left_on=["DOC_IDENTIDAD_ceros"], 
                         right_on=[columna_de_dni]
                         ,how='inner')

#%%
'''creamos el archivo final'''

df_resultado['SALDO A DESCONTAR'] = np.nan
df_resultado['# CUOTAS'] = np.nan

final = df_resultado[['DOC_IDENTIDAD','SOCIO', 'FECHA_DESEMBOLSO', 'SALDO A DESCONTAR', '# CUOTAS',"CUOTA MENSUAL", 'PAGARE_FINCORE', "EMPRESA/PLANILLA"]]

#%%

NOMBRE = 'BAJAS '+ FECHATXT +'.xlsx'
try:

    os.remove(DIRECTORIO + '\\'+NOMBRE)
except FileNotFoundError:
    pass

final.to_excel(NOMBRE, index=False,
               sheet_name=FECHATXT)














