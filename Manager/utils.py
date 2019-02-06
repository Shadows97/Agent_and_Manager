from db_config.sql_constant import Constant


class Utils ():


    @classmethod
    def managerUpdate(cls,cur,conn,data,id_hote):
        cur.execute(Constant.query_update_ip, (data[1], data[2]))
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

        cur.execute(Constant.query_insert_ramInfo,
                    (data[7], data[8], data[9], data[10], data[11], id_hote,))
        conn.commit()

        cur.execute(Constant.query_insert_debitInfo, (data[12], data[13], id_hote))
        conn.commit()

        cur.execute(Constant.query_insert_diskInfo, (data[14], data[15], data[16], id_hote))
        conn.commit()


    @classmethod
    def managerInsertion(cls,cur,conn,data):
        cur.execute(Constant.query_insert_hote, (data[0], data[1], data[2], True, data[17]))
        conn.commit()
        cur.execute(Constant.query_check_hote, (data[2],))
        id_hote = cur.fetchone()[0]
        cur.execute(Constant.query_insert_cpuInfo, (data[3], data[4], data[5], data[6], id_hote,))
        conn.commit()
        cur.execute(Constant.query_insert_ramInfo,
                    (data[7], data[8], data[9], data[10], data[11], id_hote,))
        conn.commit()
        cur.execute(Constant.query_insert_debitInfo, (data[12], data[13], id_hote,))
        conn.commit()
        cur.execute(Constant.query_insert_diskInfo, (data[14], data[15], data[16], id_hote,))
        conn.commit()