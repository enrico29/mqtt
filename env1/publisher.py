from textwrap import indent
import paho.mqtt.client as mqtt
from paho import mqtt as mqtt2
from json import *
import time
import code


#PORTA_BROKER=1883
PORTA_BROKER= 8883
QOS=0
KEEPALIVE= 60
INTERVALLO= 5
#BROKER_HOST='80.210.122.173'
BROKER_HOST='9fe9cc9c581f455dbb228c6a907ae1e3.s1.eu.hivemq.cloud'
TOPIC = 'stanza/{}/temperatura'

client = mqtt.Client()
client.tls_set(tls_version= mqtt2.client.ssl.PROTOCOL_TLS)
client.username_pw_set("trive2004", "beppe100204") #accesso al broker cloud hivemq
client.connect(BROKER_HOST,PORTA_BROKER,KEEPALIVE)
client.loop_start()  #il client rimane in ascolto

try:
    while True:
        
        x = code.dati()
        print('---------------------------------------------')
        
        i2=0
        for i in x:
            i2=i2+1
            print(dumps(i,indent=4))
            print()
            client.publish(TOPIC.format(i2),dumps(i),QOS) 

        time.sleep(INTERVALLO)

except KeyboardInterrupt:
    print('Stop publisher')

client.loop_stop()
client.disconnect()