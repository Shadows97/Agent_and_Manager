class Constant():
    SQL = """INSERT INTO equipement (adresse_ip) VALUES (%s);"""
    query_insert_hote = """INSERT INTO equipement (nom,adresse_ip,adresse_mac) VALUES (%s,%s,%s);"""
    query_check_hote = """SELECT * FROM equipement WHERE adresse_mac =%s;"""
    query_insert_cpuInfo = """INSERT INTO cpu (cpunumber,cpufreqcurrent,cpufreqmin,cpufreqmax,equipement) VALUES (%s, %s,%s, %s,%s);"""
    query_insert_ramInfo = """INSERT INTO ram (ramtotal,ramavailable,rampercent,ramfree,ramused,equipement) VALUES (%s,%s,%s,%s,%s,%s);"""
    query_insert_diskInfo = """INSERT INTO disk (total_size,size_used,size_free,equipement) VALUES (%s,%s,%s,%s);"""
    query_insert_debitInfo = """INSERT INTO interface_data (byte_send,byte_recv,equipement) VALUES (%s,%s,%s);"""
    query_count_cpuInfo = """ SELECT * FROM cpu WHERE equipement = %s;"""
    query_count_ramInfo = """ SELECT * FROM ram WHERE equipement = %s;"""
    query_count_diskInfo = """ SELECT * FROM disk WHERE equipement = %s;"""
    query_count_debitInfo = """ SELECT * FROM interface_data WHERE equipement = %s;"""
    query_delete_ramInfo = """ DELETE FROM ram WHERE equipement = %s;"""
    query_delete_cpuInfo = """ DELETE FROM cpu WHERE equipement = %s;"""
    query_delete_diskInfo = """ DELETE FROM disk WHERE equipement = %s;"""
    query_delete_debitInfo = """ DELETE FROM interface_data WHERE equipement = %s;"""
    query_update_ip = """ UPDATE equipement SET adresse_ip = %s WHERE adresse_mac = %s;  """