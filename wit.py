#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import codecs
import sys
import requests
import json
import pyaudio
import wave
reload(sys)
sys.setdefaultencoding('utf8')

def read_audio(WAVE_FILENAME):
	# lectura de wav
    with open(WAVE_FILENAME, 'rb') as f:
        audio = f.read()
    return audio

# Wit.ai "endpoint"
API_ENDPOINT = 'https://api.wit.ai/speech'
 
# Wit.ai "token de acceso"
wit_access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
 
def ReconocimientoVoz(AUDIO_FILENAME):

    audio = read_audio(AUDIO_FILENAME)
 
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
 
	# Llamada a API
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
 
    data = json.loads(resp.content)
 
    text = data['_text']
 
    return text
 
if __name__ == "__main__":
    text =  ReconocimientoVoz('voz.wav')
    print("{}".format(text))
