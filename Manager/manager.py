import os
import socket
import select
import json


import psycopg2 as psycopg2
from db_config.sql_constant import Constant
from db_config.config import ConfigDb
from Manager.utils import Utils
from Constant.AlertConstant import AlertConstant


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def create_socket(TCP_PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', TCP_PORT))
    server_socket.listen(5)

    return server_socket

read_list = []
hote =''
port = [9094,9096]
for TCP_PORT in port:
        read_list.append(create_socket(TCP_PORT))

print("Le serveur ecoute à présent sur le port: {}".format(port))

server_start = True
donnees = {}

clients_connectes =[]
client_info =[]
while server_start:
    connexion_demandees, wlist, xlist = select.select(read_list,[],[],0.05)

    for conected in connexion_demandees:
        connection_client, infos = conected.accept()

        clients_connectes.append(connection_client)

    client_a_lire = []


    try:
        client_a_lire, wlist,xlist = select.select(clients_connectes,[],[],0.05)

    except select.error:
        pass
    else:
        for client in client_a_lire:
            conn = None
            # filename = "/home/charbel/PycharmProjects/agent_and_manager/db_config/dbConfig.ini"
            filename = os.path.join(BASE_DIR, 'db_config/dbConfig.ini')
            conn = ConfigDb().connection(filename, "postgresql")
            # create a cursor
            cur = conn.cursor()
            msg = client.recv(5000)
            if msg != b'' :
                print(msg)
                msg = msg.decode()

                donnees = json.loads(msg)
                print("data ==>" + str(donnees))
                keys = ()
                data = ()
                for donne in donnees:
                    print(donne)
                    keys += (donne,)
                    data += (donnees[donne],)
                print("data == " + str(data))
                if keys.__contains__(AlertConstant.RAM_TITRE) or keys.__contains__(AlertConstant.DISK_TITRE) or keys.__contains__(AlertConstant.CPU_TITRE):
                    print("true")
                    for key in keys:
                        print("Titre {}".format(key))
                        print("Message {}".format(donnees[key]))
                        cur.execute(Constant.query_check_hote, (donnees[AlertConstant.EQUIPEMENT_MAC],))
                        response = cur.fetchone()
                        if response :
                            id_hote = response[0]
                            if key != AlertConstant.EQUIPEMENT_MAC:
                                cur.execute(Constant.CHECK_ALL_ALERT_QUERY, ())

                                if cur.rowcount == 0:
                                    cur.execute(Constant.INSERT_ALERT_QUERY, (key, donnees[key], False, id_hote))
                                    conn.commit()
                                else:
                                    cur.execute(Constant.CHECK_ALERT_QUERY, (donnees[key], True))
                                    response = cur.fetchone()
                                    if response:
                                        cur.execute(Constant.INSERT_ALERT_QUERY, (key, donnees[key], False, id_hote))
                                        conn.commit()


                else:
                    cur.execute(Constant.query_check_hote, (data[2],))
                    response = cur.fetchone()
                    if response:
                        print("check true")
                        id_hote = response[0]
                        print("id === " + str(id_hote))
                        Utils.managerUpdate(cur, conn, data, id_hote)
                    else:
                        print("check false")
                        Utils.managerInsertion(cur, conn, data)
                    cur.close()

                    ConfigDb().disconnect(conn)




