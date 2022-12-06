import time 
import paho.mqtt.client as mqtt 
import random
from paho import mqtt as mqtt2


def on_temp(): #funzione temperature
    TEMP = random.randint(10,20)  
    return TEMP

BROKER_HOST='9fe9cc9c581f455dbb228c6a907ae1e3.s1.eu.hivemq.cloud' 
#TOPIC = 'stanza/1/temperatura'
TOPIC='home/stanza1/temperatura' 
password = 'beppe10024'



PORTA_BROKER= 8883
QOS=0
KEEPALIVE= 60
INTERVALLO= 5

client = mqtt.Client()
client.tls_set(tls_version= mqtt2.client.ssl.PROTOCOL_TLS)
client.username_pw_set("trive2004", password)
client.connect(BROKER_HOST,PORTA_BROKER,KEEPALIVE)
client.loop_start()

try:       
    while True:
        TEMPERATURA = on_temp()
        print('------------')
        print(TEMPERATURA)
        client.publish(TOPIC,TEMPERATURA,QOS)
        time.sleep(INTERVALLO)

except KeyboardInterrupt:
    print('Stop publisher')

client.loop_stop()
client.disconnect()
