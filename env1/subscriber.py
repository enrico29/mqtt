from textwrap import indent
import paho.mqtt.client as mqtt
from paho import mqtt as mqtt2

def on_message(client,userdata,msg):
    
    TEMPERATURA = msg.payload.decode('utf8')
    print(TEMPERATURA)
    print('---------------------------')

#BROKER_HOST='80.210.122.173'
#BROKER_HOST='192.168.5.37'
BROKER_HOST='9fe9cc9c581f455dbb228c6a907ae1e3.s1.eu.hivemq.cloud'
TOPIC = 'stanza/{}/temperatura'
indice=0 
#PORTA_BROKER=1883
PORTA_BROKER=8883
QOS=0
KEEPALIVE=60

while(indice==0):
    indice = input('inserisci numero di stanza (1-4):')
    if(indice=='1' or indice=='2' or indice=='3' or indice=='4'):
        break
    indice=0

print(TOPIC.format(indice))

client = mqtt.Client()


client.on_message = on_message  

client.tls_set(tls_version=mqtt2.client.ssl.PROTOCOL_TLS)
client.username_pw_set("trive2004", "beppe100204")
client.connect(BROKER_HOST,PORTA_BROKER,KEEPALIVE)
client.subscribe(TOPIC.format(indice))


try:
    client.loop_forever()
except KeyboardInterrupt:
    print('Stop subscriber')