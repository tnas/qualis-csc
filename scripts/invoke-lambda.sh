#!/bin/sh
aws lambda invoke --function-name etl-qualis ../data/qualis_2019_2016.xlsx 
