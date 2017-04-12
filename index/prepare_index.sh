#!/bin/bash
echo "delete index"
curl -u elastic:changeme -XDELETE 'localhost:9200/fsanalyze?pretty'

echo "prepare elasticsearch index"
curl -u elastic:changeme -XPUT 'localhost:9200/fsanalyze?pretty' --data-binary "@index_settings.json" -H 'Content-Type: application/json'
