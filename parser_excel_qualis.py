import pandas as pd
import pymysql
import os
import logging
import sys
import qualis_sql

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_db_connection():
    rds_host = os.environ['AWS_RDS_MYSQL_HOST']
    rds_user = os.environ['AWS_RDS_MYSQL_USER']
    rds_pass = os.environ['AWS_RDS_MYSQL_PASS']

    try:
        conn = pymysql.connect(rds_host, user=rds_user, passwd=rds_pass)
        logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
        return conn

    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        sys.exit()


def prepare_database(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(qualis_sql.USE_DATABASE)
        conn.commit()
    except pymysql.MySQLError as e:
        logger.error(f'Database {qualis_sql.AWS_RDS_MYSQL_DBNAME} not found.')
        logger.info('Creating database...')
        cursor.execute(qualis_sql.CREATE_DATABASE)
        cursor.execute(qualis_sql.USE_DATABASE)
        cursor.execute(qualis_sql.CREATE_TABLE)
        conn.commit()


def parser(event, context):

    # record = event['Records'][0]
    # bucket_name = record['s3']['bucket']['name']
    # file_name = record['s3']['object']['key']
    # path_file_name = os.path.join(bucket_name, file_name)

    path_file_name = 'data-qualis/qualis_2019_2016.xlsx'
    file_name = 'qualis_2019_2016.xlsx'
    info_file = file_name.split('_')
    year = info_file[1]
    previous_year = info_file[2].split('.')[0]

    excel_qualis = pd.read_excel(f's3://{path_file_name}', sheet_name='Qualis')
    for row in excel_qualis.index:
        print(excel_qualis['SIGLA'][row])

    # connect = get_db_connection()
    # prepare_database(connect)
    # connect.close()

parser(None, None)

