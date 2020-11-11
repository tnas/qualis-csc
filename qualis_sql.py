AWS_RDS_MYSQL_DBNAME = 'qualis'
USE_DATABASE = f'USE {AWS_RDS_MYSQL_DBNAME}'
CREATE_DATABASE = f'CREATE DATABASE {AWS_RDS_MYSQL_DBNAME}'
CREATE_TABLE = 'CREATE TABLE qualis_cs_conference(year SMALLINT NOT NULL, acronym VARCHAR(20) NOT NULL,' \
               'standard_name VARCHAR(300) NOT NULL, h5 SMALLINT, schollar SMALLINT, previous_year SMALLINT NOT NULL,' \
               'previous_qualis VARCHAR(5), no_induction_qualis VARCHAR(5), qualis_sbc VARCHAR(5), ' \
               'ce_indication TINYINT, final_qualis VARCHAR(5) NOT NULL, google_scholar VARCHAR(1000),' \
               'comments VARCHAR(1000), PRIMARY KEY(year, acronym))'