import psycopg2
import numpy as np
from postgresql.service.GldService import GldService

gldService = GldService()

class LldService:

    def create_table_for_lld(self):
        # Establishing the connection
        conn = psycopg2.connect(dbname='diplom', user='postgres', password='1234', host='localhost', port='5432')
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        conn.autocommit = True
        # Droping LLD table if already exists.
        cursor.execute("DROP TABLE IF EXISTS LLD")

        gld = gldService.get_gld_values_from_db()

        # Creating table as per requirement
        sql = '''CREATE TABLE LLD(id serial PRIMARY KEY, '''
        for i in gld:
            # if "-" in str(i):
            #     str(i).replace("-", "_")
            sql += '''_''' + i.replace("-", "_") + ''' float, '''
        sql = sql[:-2] + ''')'''
        print(sql)
        cursor.execute(sql)
        cursor.close()
        conn.close()


    def create_lld_and_safe_into_db(self, message, gld):
        lld = []
        for i in message.split():
            if (i in gld):
                lld.append(i)
        # print(lld): ['SELECT', 'DISTINCT', 'FROM']
        size = len(lld)
        dict = {i:lld.count(i) for i in lld}
        # print(dict): {'SELECT': 1, 'DISTINCT': 1, 'FROM': 1}
        for key, value in dict.items():
             dict[key] = value/size
        # print(dict): {'SELECT': 0.3333333333333333, 'DISTINCT': 0.3333333333333333, 'FROM': 0.3333333333333333}
        self.safe_into_lld_table(dict)
        return lld


    def safe_into_lld_table(self, dict):
        conn = psycopg2.connect(dbname='diplom', user='postgres', password='1234', host='localhost', port='5432')
        cursor = conn.cursor()
        conn.autocommit = True
        sql = '''INSERT INTO lld('''
        for key, value in dict.items():
            sql += '''_''' + key + ''', '''
        sql = sql[:-2] + ''') VALUES ('''
        for key, value in dict.items():
            sql += str(value) + ''', '''
        sql = sql[:-2] + ''')'''
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def get_lld_values_from_db(self):
        conn = psycopg2.connect(dbname='diplom', user='postgres', password='1234', host='localhost', port='5432')
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute('''SELECT * FROM lld''')
        tuples_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return tuples_list

    def get_matrix(self):
        values = self.get_lld_values_from_db()
        # [(4678, None, None, ...), ()...]
        matrix = np.array(values)
        # print(matrix)
        # [[1 None None ... None None None] [] ]
        return matrix