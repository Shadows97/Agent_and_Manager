import socket
import time
import json
from Agent.sendInfo import SendInfo
from Agent.sendAlert import SendAlert


class Agent ():

    @classmethod
    def run (cls):

       while True:
           SendAlert.sendAlert()
           time.sleep(2)
           SendInfo.sendInfo()
           time.sleep(5)

if __name__ == '__main__':
    Agent.run()









