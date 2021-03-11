import pandas as pd
import xlrd
import psycopg2
from psycopg2 import sql
import csv

from postgresql.service.GldService import GldService
from postgresql.service.LldService import LldService
# from postgresql.service.LogService import LogService


gldService = GldService()
lldService = LldService()
# logService = LogService()


if __name__ == "__main__":

    # postgresql_gld = gldService.get_gld_values_from_xlsx_file()
    # gldService.safe_gld_values_into_db(postgresql_gld)
    # lldService.create_table_for_lld()
    # logService.read_log_file()


    # gld = gldService.get_gld_values_from_db()
    # with open("C:/Program Files/PostgreSQL/12/data/log/postgresql.csv") as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     # Loop until we have parsed all the lines.
    #     for line in csv_reader:
    #         if "statement:" in line[13]:  # column - message
    #             lldService.create_lld_and_safe_into_db(line[13][10:], gld)  # [10:] - substring


    matrix = lldService.get_matrix()
