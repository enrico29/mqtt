# IoT
# MQTT e PYTHON
# SUBSCRIBER
# DATI FORMATO JSON
# Simulazione
# Misura temperatura in una serra
# Topic: serre/serra1/sensori/temperatura
# Ricezione dati IoT dal broker


import os
from flask import Flask, render_template
from datetime import timedelta, datetime
from time import time
from flask_mqtt import Mqtt

app = Flask(__name__)


  


# Configurazione MQQT Server (Broker)
app.config['MQTT_BROKER_URL'] = "192.168.5.37"

#"80.210.122.173"
#192.168.5.37

app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 60
#
mqtt = Mqtt(app)
# Parametri
refresh = 5		# Tempo in secondi per il refresh della dashboard
topic = "serre/serra1/sensori/temperatura"
#	
# Route
#	

temperatura=2

@app.route('/') # root route (default page)
def index():
    Dati_per_template = {'TEMP': temperatura,'UMID': 85,'REFRESH': refresh}
    print(temperatura)  # Debug
    return render_template("home.html",**Dati_per_template)
    #eturn render_template("home.html")
    
#
# MQTT client subscriber
#

#if __name__ == "__main__":
#    app.run(debug=True)  


@mqtt.on_connect()
def gestione_connect(client, userdata, flags, rc):
    print("Connect-Client:", client) # Debug
    mqtt.subscribe(topic)
@mqtt.on_subscribe()
def gestione_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe-Client:", client)  # Debug
@mqtt.on_message()
def gestione_message(client, userdata, message):
    global temperatura    # FONDAMENTALE
    topic = message.topic
    temperatura = message.payload.decode()
    print ("topic: ",topic," - temperatura: ",temperatura)
    return temperatura
@mqtt.on_disconnect()
def gestione_disconnect(client, userdata, rc):
    print("Disconnect-Client:", client)  # Debug
@mqtt.on_log()
def gestione_logging(client, userdata, level, buf):
    print(level, buf)   # Debug

#

#
# Nicola Ceccon - laboratorio LTR
# Aprile 2021
#
app.run(port=5001)