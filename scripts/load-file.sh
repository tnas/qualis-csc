#!/bin/sh
aws s3 rm s3://data-qualis/qualis_2019_2016.xlsx
aws s3 cp ../data/qualis_2019_2016.xlsx s3://data-qualis
