#!/bin/bash

SCRIPT_DIR=$(cd $(dirname ${0});pwd)
REPOSITORY_DIR=${SCRIPT_DIR}/opt/local/pyspark-pytest
REPOSITORY_DIRNAME=$(basename $REPOSITORY_DIR)

docker run -it \
  --volume $REPOSITORY_DIR:/opt/local/pyspark-pytest \
  --workdir /opt/local/pyspark-pytest \
  i05nagai/pyspark-pytest pytest --cov=. --pep8
