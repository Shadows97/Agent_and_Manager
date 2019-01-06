import socket
import select
import json


import psycopg2 as psycopg2
from db_config.sql_constant import Constant
from db_config.config import ConfigDb


hote ='192.168.43.55'
port = 6061
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.bind((hote,port))
connection.listen(5)

print("Le serveur ecoute à présent sur le port: {}".format(port))

server_start = True
donnees = {}

clients_connectes =[]
client_info =[]
while server_start:
    connexion_demandees, wlist, xlist = select.select([connection],[],[],0.05)

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
            msg = client.recv(5000)
            msg = msg.decode()
            #msg1 = json.dumps(msg)
            donnees = json.loads(msg)
            print("data ==>"+str(donnees))
            data =()
            for donne in donnees:
              print(donne)
              data +=(donnees[donne],)
            print("data == "+ str(data))
            conn =None
            filename ="/home/shadows/PycharmProjects/Agent_and_Manager/db_config/dbConfig.ini"
            conn = ConfigDb().connection(filename,"postgresql")
            # create a cursor
            cur = conn.cursor()
            cur.execute(Constant.query_check_hote, (data[2],))
            response = cur.fetchone()
            if response:
                print("check true")
                id_hote = response[0]
                print("id === "+str(id_hote))
                cur.execute(Constant.query_update_ip,(data[1],data[2]))
                conn.commit()
                cur.execute(Constant.query_count_cpuInfo, (id_hote,))
                print(cur.rowcount)
                if cur.rowcount == 10:
                    cur.execute(Constant.query_delete_cpuInfo, (id_hote,))
                    conn.commit()
                cur.execute(Constant.query_count_ramInfo, (id_hote,))
                print(cur.rowcount)
                if cur.rowcount == 10:
                    cur.execute(Constant.query_delete_ramInfo, (id_hote,))
                    conn.commit()
                cur.execute(Constant.query_count_debitInfo, (id_hote,))
                if cur.rowcount == 10:
                    cur.execute(Constant.query_delete_debitInfo, (id_hote,))
                    conn.commit()
                cur.execute(Constant.query_count_diskInfo, (id_hote,))
                if cur.rowcount == 10:
                    cur.execute(Constant.query_delete_diskInfo, (id_hote,))
                    conn.commit()
                cur.execute(Constant.query_insert_cpuInfo, (data[3], data[4], data[5], data[6], id_hote,))
                conn.commit()

                cur.execute(Constant.query_insert_ramInfo, (data[7], data[8], data[9], data[10], data[11], id_hote,))
                conn.commit()

                cur.execute(Constant.query_insert_debitInfo, (data[12], data[13], id_hote))
                conn.commit()

                cur.execute(Constant.query_insert_diskInfo, (data[14], data[15], data[16], id_hote))
                conn.commit()



            else:
                print("check false")
                cur.execute(Constant.query_insert_hote, (data[0], data[1], data[2],True))
                conn.commit()
                cur.execute(Constant.query_check_hote, (data[2],))
                id_hote = cur.fetchone()[0]
                cur.execute(Constant.query_insert_cpuInfo, (data[3], data[4], data[5], data[6], id_hote,))
                conn.commit()
                cur.execute(Constant.query_insert_ramInfo, (data[7], data[8], data[9], data[10], data[11], id_hote,))
                conn.commit()
                cur.execute(Constant.query_insert_debitInfo, (data[12], data[13], id_hote,))
                conn.commit()
                cur.execute(Constant.query_insert_diskInfo, (data[14], data[15], data[16], id_hote,))
                conn.commit()

            cur.close()

            ConfigDb().disconnect(conn)



