class Constant():
    SQL = """INSERT INTO "Dashboard_equipement" (adresse_ip) VALUES (%s);"""
    query_insert_hote = """INSERT INTO "Dashboard_equipement" (nom,adresse_ip,adresse_mac,etat) VALUES (%s,%s,%s,%s);"""
    query_check_hote = """SELECT * FROM "Dashboard_equipement" WHERE adresse_mac =%s;"""
    query_insert_cpuInfo = """INSERT INTO "Dashboard_cpu_info" (cpu_number,cpu_current_freq,cpu_min_freq,cpu_max_freq,equipement_id) VALUES (%s, %s,%s, %s,%s);"""
    query_insert_ramInfo = """INSERT INTO "Dashboard_ram_info" (ram_total,ram_available,ram_percent,ram_free,ram_used,equipement_id) VALUES (%s,%s,%s,%s,%s,%s);"""
    query_insert_diskInfo = """INSERT INTO "Dashboard_disk_info" (total_size,size_used,size_free,equipement_id) VALUES (%s,%s,%s,%s);"""
    query_insert_debitInfo = """INSERT INTO "Dashboard_interface_data_info" (byte_send,byte_recv,equipement_id) VALUES (%s,%s,%s);"""
    query_count_cpuInfo = """ SELECT * FROM "Dashboard_cpu_info" WHERE equipement_id = %s;"""
    query_count_ramInfo = """ SELECT * FROM "Dashboard_ram_info" WHERE equipement_id = %s;"""
    query_count_diskInfo = """ SELECT * FROM "Dashboard_disk_info" WHERE equipement_id = %s;"""
    query_count_debitInfo = """ SELECT * FROM "Dashboard_interface_data_info" WHERE equipement_id = %s;"""
    query_delete_ramInfo = """ DELETE FROM "Dashboard_ram_info" WHERE equipement_id = %s;"""
    query_delete_cpuInfo = """ DELETE FROM "Dashboard_cpu_info" WHERE equipement_id = %s;"""
    query_delete_diskInfo = """ DELETE FROM "Dashboard_disk_info" WHERE equipement_id = %s;"""
    query_delete_debitInfo = """ DELETE FROM "Dashboard_interface_data_info" WHERE equipement_id = %s;"""
    query_update_ip = """ UPDATE "Dashboard_equipement" SET adresse_ip = %s WHERE adresse_mac = %s;  """

    INSERT_ALERT_QUERY =  """INSERT INTO "Dashboard_alert" (titre, message,status, equipement_id) VALUES (%s,%s,%s,%s);"""
    CHECK_ALERT_QUERY = """SELECT * FROM "Dashboard_alert" WHERE message = %s AND status = %s;"""
    CHECK_ALL_ALERT_QUERY = """SELECT * FROM "Dashboard_alert" WHERE message = %s ;"""