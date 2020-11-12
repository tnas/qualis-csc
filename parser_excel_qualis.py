import pandas as pd
import pymysql
import os
import sys
import qualis_sql

RDS_CREDENTIALS_FILE = 's3://data-qualis/rds-credentials.json'
EXCEL_SHEET_NAME = 'Qualis'
LIMIT_COMMIT = 100
sheet_columns = ['SIGLA', 'Nome Padrão', 'h5', 'Uso do Scholar', 'Qualis 2016',
                 'Qualis sem indução', 'Ajuste ou evento SBC', 'CE Indicou', 'Qualis Final',
                 'Link para o Google Metrics ou Google Scholar', 'Comentário']
index_int_columns = [4, 5, 9]


def get_db_connection():
    rds_credentials = pd.read_json(RDS_CREDENTIALS_FILE)
    rds_host = rds_credentials['host'][0]
    rds_user = rds_credentials['user'][0]
    rds_pass = rds_credentials['pass'][0]

    try:
        conn = pymysql.connect(rds_host, user=rds_user, passwd=rds_pass)
        print("SUCCESS: Connection to RDS MySQL instance succeeded")
        return conn

    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()


def prepare_database(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(qualis_sql.USE_DATABASE)
        print('Database has been selected.')
        conn.commit()
    except pymysql.MySQLError as e:
        print(f'Database {qualis_sql.AWS_RDS_MYSQL_DBNAME} not found.')
        print('Creating database...')
        cursor.execute(qualis_sql.CREATE_DATABASE)
        cursor.execute(qualis_sql.USE_DATABASE)
        cursor.execute(qualis_sql.CREATE_TABLE)
        conn.commit()


def load_database(conn, excel, year, previous_year):
    cursor = conn.cursor()
    count = 0
    for row in excel.index:

        row_values = list([year, previous_year])

        for col in range(len(sheet_columns)):
            cell = excel[sheet_columns[col]][row] if str(excel[sheet_columns[col]][row]) != 'nan' else None
            row_values.append(cell)

        for int_col in index_int_columns:
            if row_values[int_col] is not None:
                row_values[int_col] = int(row_values[int_col])

        cursor.execute(qualis_sql.INSERT_TABLE, row_values)
        count += 1
        if count % LIMIT_COMMIT == 0:
            print(f"Commiting the insertion of {count} rows")
            conn.commit()
            count = 0

    print(f"Commiting the insertion of {count} rows")
    conn.commit()


def parser(event, context):
    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    file_name = record['s3']['object']['key']
    path_file_name = os.path.join(bucket_name, file_name)

    info_file = file_name.split('_')
    year = info_file[1]
    previous_year = info_file[2].split('.')[0]
    excel = pd.read_excel(f's3://{path_file_name}', sheet_name=EXCEL_SHEET_NAME)

    connect = get_db_connection()
    prepare_database(connect)
    load_database(connect, excel, year, previous_year)
    connect.close()