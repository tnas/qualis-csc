#!/bin/sh
rm -f etl-qualis.zip
cd .. && zip scripts/etl-qualis.zip parser_excel_qualis.py qualis_sql.py && cd scripts
aws lambda update-function-code --function-name etl-qualis --zip-file fileb://etl-qualis.zip
rm -f etl-qualis.zip
