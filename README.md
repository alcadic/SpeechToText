#SpeechToText

Para las transcripciones se hace el uso de la API de WIT (wit.ai) para el reconocimiento de voz. Hay que registrarse y obtener un token de acceso a su API, el cual se utilizará en el código.

Instalaciones
Windows

Hay que instalar PyAudio con el siguiente comando: pip install pyaudio

Linux

Primero hay que instalar las librerias de desarrollo con el siguiente comando:
sudo apt-get install portaudio19-dev

Posteriormente, hay que instalar el módulo PyAudio utilizando PIP:
pip install pyaudio

Uso
Clonar este repositorio.
Ejecutar el siguiente comando en el terminal:
python voz.py
