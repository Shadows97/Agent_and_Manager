from configparser import ConfigParser

import psycopg2


class ConfigDb ():

    connect=None
    @classmethod
    def config(cls,filename='dbConfig.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db
    @classmethod
    def connection(cls,filename,section):
        try:
            params = cls.config(filename,section)

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            cls.connect = psycopg2.connect(**params)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return cls.connect
    @classmethod
    def disconnect(cls,conn):
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    @classmethod
    def check_hote(cls,data):
        params = cls.config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("", data)
        response = cur.fetchone()
        cur.close()
        return response

