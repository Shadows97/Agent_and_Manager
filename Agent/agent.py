import socket
import time
import json
from Agent.info import Info
from Agent.alert import Alert


hote = "localhost"
port = 9094

connexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion.connect((hote,port))

print("Connexion établie avec le serveur sur le port: {}".format(port))

c = 30
while c > 10:


    info =Info()
    sendInfo = info.getInfo()
    print(info.getInfo())
    msg = json.dumps(sendInfo).encode()
    connexion.send(msg)
    Alert.sendAlert()
    time.sleep(1)



connexion.close()







