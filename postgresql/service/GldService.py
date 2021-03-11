import xlrd
import psycopg2

class GldService:

    def get_gld_values_from_xlsx_file(self):
        # пока читаю все значения из столбца, затем исправить согласно условию зарезервированный/незарезервированный
        postgresql_file = xlrd.open_workbook("C:/D/Diplom/other/GLD_PostgreSQL.xlsx")
        sheets = postgresql_file.sheet_names()
        required_data = []
        for sheet_name in sheets:
            sh = postgresql_file.sheet_by_name(sheet_name)
            for rownum in range(1, sh.nrows):  # с 1, т.к. 0=заголовок
                row_valaues = sh.row_values(rownum)
                required_data.append((row_valaues[0]))
        # проверим на уникальность и удалим повторы
        res = []
        [res.append(x) for x in required_data if x not in res]
        print(res)
        return res

    def safe_gld_values_into_db(self, postgresql_gld):
        conn = psycopg2.connect(dbname='diplom', user='postgres', password='1234', host='localhost', port='5432')
        cursor = conn.cursor()
        conn.autocommit = True
        for x in postgresql_gld:
            cursor.execute("INSERT INTO postgresql_gld (key_word) VALUES (%s)", (x,))  # Для привязки позиционных переменных
            # второй аргумент всегда должен быть последовательностью , даже если он содержит одну переменную (помните, что
            # Python требует запятую для создания одноэлементного кортежа)
        conn.commit()
        cursor.close()
        conn.close()

    def get_gld_values_from_db(self):
        conn = psycopg2.connect(dbname='diplom', user='postgres', password='1234', host='localhost', port='5432')
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute("SELECT DISTINCT key_word FROM postgresql_gld")
        tuples_list = cursor.fetchall()
        # tuples_list = [('ABORT',), ('ABS',), ('ABSENT',), ('ABSOLUTE',), ... ]
        rows = [x[0] for x in tuples_list] # https://coderoad.ru/14861162/cursor-fetchall-%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B0%D0%B5%D1%82-%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8F-MySQldb-%D0%B8-python
        cursor.close()
        conn.close()
        return rows