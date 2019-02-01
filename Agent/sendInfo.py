import socket
import time
import json
from Agent.info import Info

class SendInfo():



    @classmethod
    def sendInfo(cls):
        hote = "localhost"
        port = 9094

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion.connect((hote, port))
        print("Connexion établie avec le serveur sur le port: {}".format(port))

        info = Info()
        sendInfo = info.getInfo()
        print(info.getInfo())
        msg = json.dumps(sendInfo).encode()
        connexion.send(msg)

        connexion.close()










