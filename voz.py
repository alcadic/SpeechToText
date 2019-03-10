#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess, string, time, configparser
import os
import io

def escuchar():
    #Grabar audio del microfono en wav
    #y enviarlo a Google quien devolvera el texto en una variable
    envio = subprocess.Popen(["./grabar.sh"], shell=True, universal_newlines=True, stdout=subprocess.PIPE)
    texto = envio.communicate()[0]
    texto = texto.strip('\n')
    return texto

while True:
    clave = escuchar()
    print("Escuche:" + clave)
    
    if clave == 'encender luz' or clave == 'enciende la luz' :
        print("encender luz")

    if clave == 'apagar luz' or clave == 'apaga la luz' :
        print("apagar luz")