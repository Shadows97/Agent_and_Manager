import socket
import time
import json
from Agent.info import Info


hote = "localhost"
port = 7000

connexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion.connect((hote,port))

print("Connexion établie avec le serveur sur le port: {}".format(port))

c = 30
while c > 10:

    sendInfo =Info()
    sendInfo = sendInfo.getInfo()
    print(sendInfo)
    msg = json.dumps(sendInfo).encode()
    connexion.send(msg)
    time.sleep(60)



connexion.close()







