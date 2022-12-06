import paho.mqtt.client as mqtt
from paho import mqtt as mqtt2
import json

def on_message(client,userdata,msg):

    f = open('db.json', 'r') 
    data = json.loads(f.read())
    print()
    


    for i in f:
        n=n+1

        if(n == (int())):
            break

        x = str(i)
        
        
    print(x)   
    x = x.split(' - ') 


    print('Topic:',msg.topic)
    print('QoS:',msg.qos)
    TEMPERATURA = msg.payload.decode('utf8')
    print('Temperatura:',TEMPERATURA)
    print('---------------------------')


BROKER_HOST='9fe9cc9c581f455dbb228c6a907ae1e3.s1.eu.hivemq.cloud'
#TOPIC = 'stanza/1/temperatura'
TOPIC='home/stanza1/temperatura'
PORTA_BROKER=8883
QOS=0 
KEEPALIVE=60

client = mqtt.Client()


client.on_message = on_message

client.tls_set(tls_version=mqtt2.client.ssl.PROTOCOL_TLS)
client.username_pw_set("trive2004", "beppe100204")
client.connect(BROKER_HOST,PORTA_BROKER,KEEPALIVE)
client.subscribe(TOPIC)

 
try:
    client.loop_forever()
except KeyboardInterrupt:
    print('Stop subscriber')