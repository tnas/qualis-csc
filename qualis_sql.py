AWS_RDS_MYSQL_DBNAME = 'qualis'
USE_DATABASE = f'USE {AWS_RDS_MYSQL_DBNAME}'
CREATE_DATABASE = f'CREATE DATABASE {AWS_RDS_MYSQL_DBNAME}'
CREATE_TABLE = 'CREATE TABLE qualis_cs_conference(conf_id INT NOT NULL AUTO_INCREMENT, year SMALLINT NOT NULL, ' \
               'previous_year SMALLINT NOT NULL, acronym VARCHAR(20) NOT NULL, standard_name VARCHAR(300) NOT NULL, ' \
               'h5 SMALLINT, scholar SMALLINT, previous_qualis VARCHAR(5), no_induction_qualis VARCHAR(5), ' \
               'qualis_sbc VARCHAR(5), ce_indication TINYINT, final_qualis VARCHAR(5) NOT NULL, ' \
               'google_scholar VARCHAR(1000), comments VARCHAR(1000), PRIMARY KEY(conf_id))'
INSERT_TABLE = 'INSERT INTO qualis_cs_conference (year, previous_year, acronym, standard_name, h5, scholar, ' \
               'previous_qualis, no_induction_qualis, qualis_sbc, ce_indication, final_qualis, google_scholar, comments) ' \
               'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'