# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:30:56 2023

@author: sanmiguel38
"""

#!pip install pyautogui

import time
import pyautogui
from datetime import datetime, timedelta
import os
import sys
import pandas as pd

import win32clipboard

#si por A o B no funciona el copiado y pegado, es porque hay que reiniciar el portapapeles,
# abrir el cmd y escribir 'echo off | clip'

#%%

import tkinter as tk
from tkinter import messagebox

#%%

'CON ESTE CÓDIGO PODEMOS PROGRAMAR EL REPORTE A UNA HORA EN ESPECÍFICO'
#pyautogui.sleep(150) #número de segundos de espera

#%%
'ESTE LADO DEL CÓDIGO SIRVE PARA ESCRIBIR MANUALMENTE LA FECHA'
#fecha_siguiente_manual = '24/04/2023' #aquí va la fecha de cálculo
#fecha_final_manual = '29/04/2023'     #aquí va la fecha de vigencia

#PARA QUE FUNCIONE QUITAR EL # y poner las fechas deseadas

#%%

# Obtenemos las dimensiones de la pantalla
screenWidth, screenHeight = pyautogui.size()
print('el ancho es: ' + str(screenWidth)) #ancho
print('la altura es: ' + str(screenHeight)) #altura

#%%
#abrimos la página web del Kasnet
pyautogui.moveTo(220, 1065, 0.3, pyautogui.easeInBack)
pyautogui.rightClick()
pyautogui.sleep(0.5)
pyautogui.moveTo(220, 950, 0.3, pyautogui.easeInBack)
pyautogui.click()
pyautogui.sleep(1)
pyautogui.hotkey('alt', 'space', 'x')

pyautogui.moveTo(300, 50, 0.3, pyautogui.easeInBack) #click a la pestaña del kasnet
pyautogui.click()
pyautogui.sleep(0.1)
pyautogui.write('https://stkprod.globokas.com/appgknweb/Login')
pyautogui.hotkey('enter')

pyautogui.sleep(5)

pyautogui.moveTo(250, 570, 0.3, pyautogui.easeInBack)
###########################################################################
pyautogui.click() #quitar este comentado cuando realmente se vaya a trabajar
###########################################################################

#%%
#vamos a leer el archivo donde están las credenciales del fincore
ruta_txt = 'C:\\Users\\sanmiguel38\\Desktop\\fincore joseph.txt'
df = pd.read_csv(ruta_txt, sep='\t', header=None, names=['Col1'])
user = str(df.iloc[0,0])
clave = str(df.iloc[1,0])
del(df)
#%%
# abrimos el ícono del fincore
pyautogui.moveTo(310, 1065, 0.4, pyautogui.easeInBack)
#click para abrir la ventana
pyautogui.click() #pyautogui.doubleClick()

#procedemos a poner las credenciales
pyautogui.sleep(1)
pyautogui.moveTo(900, 470, 0.4, pyautogui.easeInBack)

pyautogui.click()
pyautogui.write(user)
del(user)
#hasta aquí pusimos el nombre de usuario
#%%
#ponemos la clave
pyautogui.moveTo(950, 514, 0.4, pyautogui.easeInBack)
pyautogui.click()
pyautogui.write(clave)
del(clave)

#enter
pyautogui.moveTo(950, 610, 0.4, pyautogui.easeInBack)
pyautogui.click()

pyautogui.sleep(3)

#reporte
pyautogui.moveTo(510, 35, 0.4, pyautogui.easeInBack)
pyautogui.click()
pyautogui.moveTo(510, 85, 0.4, pyautogui.easeInBack)
pyautogui.click()
pyautogui.moveTo(700, 85, 0.4, pyautogui.easeInCubic)
pyautogui.moveTo(700, 470, 0.4)
pyautogui.click()
pyautogui.sleep(2)

#%%
#cambiamos la fecha
pyautogui.moveTo(200, 149, 0.4, pyautogui.easeInCubic)
pyautogui.doubleClick()
# Presionar las teclas de copiar
pyautogui.hotkey('ctrl', 'c')

# Obtener el texto del portapapeles y asignarlo a una variable
win32clipboard.OpenClipboard()
texto_seleccionado = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
pyautogui.sleep(0.5)
#%%
#procesamiento de la primera fecha
def fecha_siguiente(fecha):
    fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
    fecha_siguiente_obj = fecha_obj + timedelta(days=1)
    return fecha_siguiente_obj.strftime('%d/%m/%Y')

fecha_calculo = fecha_siguiente(texto_seleccionado)

x = dir()
def existencia():
    if 'fecha_siguiente_manual' not in x:
        return fecha_calculo
    else:
        return fecha_siguiente_manual
    
pyautogui.write(existencia())
# Pegar el valor en la ubicación actual del cursor
pyautogui.hotkey('ctrl', 'v')

#%%
#procesamiento de la segunda fecha
pyautogui.moveTo(450, 149, 0.4, pyautogui.easeInCubic)
pyautogui.doubleClick()
# Presionar las teclas de copiar
pyautogui.hotkey('ctrl', 'c')

# Obtener el texto del portapapeles y asignarlo a una variable
win32clipboard.OpenClipboard()
texto_seleccionado2 = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
pyautogui.sleep(0.5)

from datetime import datetime, timedelta

def ultimo_dia_mes(fecha):
    fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
    ultimo_dia_mes_obj = fecha_obj.replace(day=28) + timedelta(days=4)
    ultimo_dia_mes_obj = ultimo_dia_mes_obj.replace(day=1) - timedelta(days=1)
    return ultimo_dia_mes_obj.strftime('%d/%m/%Y')

fecha_vigencia = ultimo_dia_mes(texto_seleccionado2)

x = dir()
def existencia2():
    if 'fecha_final_manual' not in x:
        return fecha_vigencia
    else:
        return fecha_final_manual


pyautogui.write(existencia2())

# Pegar el valor en la ubicación actual del cursor
pyautogui.hotkey('ctrl', 'v')

#%%
#cambiando el monto

pyautogui.moveTo(200, 280, 0.4, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.typewrite("3000")

#%%
#antes de procesar, eliminamos el archivo si es que ya existe
def fecha_a_string(fecha):
    fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
    return fecha_obj.strftime('%m%d')

string_nombre  = fecha_a_string(texto_seleccionado)
string_nombre = str(string_nombre)

ruta_archivo = "D:\SCBCM" + string_nombre+".txt"

#aqui estamos eliminando el archivo si es que previamente ya existe
try:
    os.remove(ruta_archivo)
except FileNotFoundError:
    pass

#%%

#procesando
pyautogui.moveTo(200, 320, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(4)
pyautogui.click()
pyautogui.sleep(100)

#aceptando el mensaje
pyautogui.moveTo(950, 550, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.5)

#exportamos
pyautogui.moveTo(320, 320, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.5)

#aceptamos nuevamente
pyautogui.moveTo(900, 550, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.moveTo(980, 550, 0.2, pyautogui.easeInCubic)
pyautogui.click()


#%%
#nos vamos al disco D

if os.path.isfile(ruta_archivo):
    # Abrir el archivo
    os.startfile(ruta_archivo)
else:
    # Crear una ventana con el mensaje "No se ha encontrado el archivo"
    ventana = tk.Tk()
    ventana.title("Error")
    etiqueta = tk.Label(ventana, text="No se ha encontrado el archivo, se ha pausado la ejecución")
    etiqueta.pack(padx=20, pady=20)
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=ventana.destroy)
    boton_aceptar.pack(padx=10, pady=10)
    ventana.mainloop()
    # Salir del programa completo
    sys.exit()

pyautogui.sleep(1)
#%%
#seleccionamos
pyautogui.moveTo(320, 98, 0.3, pyautogui.easeInCubic)
pyautogui.doubleClick()
pyautogui.hotkey('ctrl', 'c')

#%%abrimos el excel que vamos a modificar:

ruta_excel = 'C:\\Users\\sanmiguel38\\Desktop\\BATCH KASNET\\abril 2023\\BATCH Kasnet - Archivo Entrada - 05-04-23  7_00pm con cuotas hasta 30-04-23.xlsx'
os.startfile(ruta_excel)
pyautogui.sleep(3)
#maximizamos
pyautogui.hotkey('alt', 'space', 'x')

pyautogui.moveTo(1365, 270, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.9)
pyautogui.click()

pyautogui.hotkey('ctrl', 'left')
pyautogui.hotkey('ctrl', 'left')
pyautogui.sleep(0.4)

pyautogui.moveTo(200, 240, 0.2, pyautogui.easeInCubic)
pyautogui.doubleClick()
pyautogui.keyDown('del')
#%%
#pegamos el título
pyautogui.moveTo(200, 287, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')

#vamos al resto del texto
pyautogui.moveTo(360, 1050, 0.2, pyautogui.easeInCubic)
pyautogui.click()

pyautogui.moveTo(320, 98, 0.3, pyautogui.easeInCubic)
pyautogui.doubleClick()
pyautogui.sleep(0.2)
pyautogui.hotkey('ctrl', 'e')
pyautogui.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
#vamos al excel
pyautogui.moveTo(180, 1060, 0.3, pyautogui.easeInCubic)
pyautogui.click()

pyautogui.moveTo(180, 350, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.moveTo(180, 350, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.keyDown('del')

#%% vamos por el siguiente:
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('down')

#eliminamos toda la columna
pyautogui.moveTo(1800, 240, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.1)
pyautogui.keyDown('del') #ELIMINAMOS TODA LA COLUMNA

pyautogui.moveTo(1700, 350, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.1)
pyautogui.hotkey('ctrl', 'c') #COPIAMOS LA LETRA R DEL COSTADO
pyautogui.moveTo(1800, 350, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.1)
pyautogui.hotkey('ctrl', 'v') #PEGAMOS LA LETRA R A SU COSTADO

pyautogui.moveTo(1740, 380, 0.1, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.write('=SI.ERROR(K5*0.01;"")')
pyautogui.hotkey('enter')

pyautogui.moveTo(1740, 370, 0.1, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.moveTo(1842, 384, 0.2, pyautogui.easeInCubic)
pyautogui.doubleClick()

#%%

pyautogui.hotkey('up')
pyautogui.hotkey('up')
pyautogui.hotkey('up')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('right')
pyautogui.hotkey('ctrl', 'c')

#%% vamos a verificar que salga verdadero
pyautogui.moveTo(1600, 290, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
pyautogui.moveTo(1600, 270, 0.3, pyautogui.easeInCubic)

pyautogui.rightClick()
pyautogui.moveTo(1670,400, 0.3, pyautogui.easeInCubic)
pyautogui.click()

pyautogui.moveTo(1600, 270, 0.3, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.sleep(0.2)
pyautogui.click()
pyautogui.sleep(0.2)
pyautogui.click()
pyautogui.click()
pyautogui.hotkey('ctrl', 'c')
pyautogui.sleep(0.2)
pyautogui.hotkey('del')
pyautogui.moveTo(1300, 270, 0.2, pyautogui.easeInCubic)
pyautogui.click()
# Obtener el texto del portapapeles y asignarlo a una variable
win32clipboard.OpenClipboard()
verificacion = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
pyautogui.sleep(0.5)

#

if verificacion == 'VERDADERO':
    print('continua')
else:
    # Crear una ventana con el mensaje "No se ha encontrado el archivo"
    ventana = tk.Tk()
    ventana.title("Error")
    etiqueta = tk.Label(ventana, text="Error en la verificación")
    etiqueta.pack(padx=20, pady=20)
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=ventana.destroy)
    boton_aceptar.pack(padx=10, pady=10)
    ventana.mainloop()
    # Salir del programa completo
    sys.exit()

pyautogui.sleep(1)

#%%

pyautogui.moveTo(50,50, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.moveTo(50,320, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.moveTo(250,360, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.hotkey('del')

#%%
#creamos el nombre del archivo
from datetime import datetime
#procesamiento de la primera fecha
def fecha_formato(fecha):
    fecha_obj = datetime.strptime(fecha, '%d/%m/%Y')
    return str(fecha_obj.strftime('%d-%m-%Y'))

fecha_txt = fecha_formato(texto_seleccionado)
fecha_vigencia_txt = fecha_formato(fecha_vigencia)

nombre_archivo = 'BATCH Kasnet - Archivo Entrada - ' + fecha_txt + ' 7_00pm con cuotas hasta ' + fecha_vigencia_txt + '.xlsx'

#%%
#nos movemos
pyautogui.write(nombre_archivo)

#%%
#cambiamos la dirección de los archivos también:
import datetime

MESES_ESPANOL = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

def fecha_a_mes_y_anio(fecha_str):
    fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%Y')
    mes_num = fecha.month
    nombre_mes = MESES_ESPANOL[mes_num]
    anio = fecha.year
    return f"{nombre_mes} {anio}"


#%%
#ahora sí el nombre del directorio
directorio = r"C:\Users\sanmiguel38\Desktop\BATCH KASNET" + "\\" + str(fecha_a_mes_y_anio(texto_seleccionado))

#%% clicando para guardar el archivo
 
pyautogui.moveTo(600,50, 0.2, pyautogui.easeInCubic)
pyautogui.click()
pyautogui.write(directorio)
pyautogui.hotkey('enter')
pyautogui.sleep(0.4)

pyautogui.moveTo(750,1010, 0.2, pyautogui.easeInCubic)
pyautogui.click() #hasta aquí ya hemos guardado el archivo
