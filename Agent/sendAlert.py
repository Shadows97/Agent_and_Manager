import socket
import time
import json
from Agent.info import Info

class SendAlert():



    @classmethod
    def sendAlert (cls):
        hote = "192.168.150.95"
        port = 9094

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion.connect((hote, port))
        print("Connexion établie avec le serveur sur le port: {}".format(port))

        info = Info()
        sendAlert = info.getAlert()
        print(info.getAlert())
        msg = json.dumps(sendAlert).encode()
        connexion.send(msg)

        connexion.close()










