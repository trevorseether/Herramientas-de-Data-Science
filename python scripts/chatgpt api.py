# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:10:30 2023

@author: sanmiguel38
"""

!pip install openai

import openai

openai.api_key = 'insertar api key'
descripcion = '''eres un niño llamado josé juan, te mucho la tecnología y 
            sueñas con crear una empresa de tecnología cuando seas grande'''

situacion = '''estás caminando y ves otro niño, ¿quieres acercarte
            a hablarle sobre tecnología?'''

respuesta = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'system', 'content':descripcion},
        {'role': 'user', 'content':situacion}
        ]
    )

resultado = ''
for opcion in respuesta.choices:
    resultado += opcion.message.content
    
print(resultado)

