#!/bin/sh

LAYER_INSTALL_DIR='python-dependencies/python/lib/python3.8/site-packages'
LAYER_FILE_NAME='python-dependencies'
LAMBDA_FUNCTION='etl-qualis'

#rm -f ${LAYER_FILE_NAME}.zip
#mkdir -p ${LAYER_FILE_NAME}
#pip3 install pandas -t ${LAYER_INSTALL_DIR}
#pip3 install xlrd -t ${LAYER_INSTALL_DIR}
#pip3 install fsspec -t $LAYER_INSTALL_DIR}
#pip3 install s3fs -t ${LAYER_INSTALL_DIR}
#pip3 install pymysql -t ${LAYER_INSTALL_DIR}
cd ${LAYER_FILE_NAME} && zip -r ../${LAYER_FILE_NAME}.zip * && cd .. 
aws lambda publish-layer-version --layer-name ${LAYER_FILE_NAME} --description "Python dependencies for etl-qualis" --license-info "MIT" --zip-file fileb://${LAYER_FILE_NAME}.zip 
rm -f ${LAYER_FILE_NAME}.zip
ARN=$(aws lambda list-layers --query "Layers[?LayerName=='${LAYER_FILE_NAME}'].LatestMatchingVersion.LayerVersionArn" --output text)
aws lambda update-function-configuration --function-name ${LAMBDA_FUNCTION} --layers ${ARN}
