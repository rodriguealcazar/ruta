#!/bin/bash

set -e

TAG_FILTERS=$1
INPUT_FILE=$2
OUTPUT_FILE=$3

# Remove all unnecessary OSM entities and tags from pbf file to keep it slim
osmium tags-filter \
  ${INPUT_FILE} \
  --output=${OUTPUT_FILE} \
  --expressions=${TAG_FILTERS} \
  --remove-tags \
  --overwrite \
  --verbose

echo "Filtered ${INPUT_FILE} to ${OUTPUT_FILE} ($(stat --printf="%s" ${OUTPUT_FILE} | numfmt --to=iec))"
