import socket
import time
import json
from Agent.info import Info

class Alert():



    @classmethod
    def sendAlert (cls):
        hote = "localhost"
        port = 9094

        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion.connect((hote, port))

        print("Connexion établie avec le serveur sur le port: {}".format(port))

        info = Info()
        sendAlert = info.getAlert()
        print(info.getAlert())
        if sendAlert is not None:
            msg = json.dumps(sendAlert).encode()
            connexion.send(msg)



        connexion.close()


if __name__ == '__main__':
    Alert().sendAlert()








