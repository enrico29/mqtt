from json import *
from datetime import *
from random import *
from time import *
 
def dati():
    n=0
    dati=[]
    while(n<4):
        #file = open('dati.json', 'w')
        n = n+1
        
        time_stamp = datetime.now()
        stanza = n
        temp = randrange(0,40)

        dato = {
            "timeStamp": str(time_stamp),
            "stanza": stanza,
            "temp": temp
        }

        dati.append(dato)

        
        #file.write(dumps(dati , indent=2))
    
    return dati