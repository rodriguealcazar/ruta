#!/bin/bash

set -e

EXPORT_CONFIG=$1
INPUT_FILE=$2
OUTPUT_FILE=$3

# Export slim dump into a compressed TSV file
osmium export \
  --config=${EXPORT_CONFIG} \
  --index-type=flex_mem \
  --output-format=pg \
  --overwrite \
  --verbose \
  ${INPUT_FILE} > ${OUTPUT_FILE}

if [ ${4:+x} ]; then
  echo "Zipping"
  gzip -f ${OUTPUT_FILE}
  OUTPUT_FILE=${OUTPUT_FILE}.gz
fi

echo "Exported and compressed ${INPUT_FILE} to ${OUTPUT_FILE} ($(stat --printf="%s" ${OUTPUT_FILE} | numfmt --to=iec))"
