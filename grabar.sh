#!/bin/bash
arecord -D plughw:1,0 -q -f cd -t wav -d 4 -r 16000 voz.wav -c 1

#Llamamos al script y pasamos todo a minusculas para no tener problemas
python wit.py | tr 'A-Z' 'a-z' > voz.txt;

value=`cat voz.txt`
echo "$value"
