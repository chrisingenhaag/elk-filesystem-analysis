import requests
import os
import sys
import datetime
import json

from datetime import datetime

walkdir = sys.argv[1]
elasticurl = "http://localhost:9200"

for root, directories, filenames in os.walk(walkdir):
    for filename in filenames:
        stat = os.stat(os.path.join(root, filename))
        fileinfo = {
            'name': filename,
            'fullpath': os.path.join(root, filename),
            'filesize': stat.st_size,
            'suffix': os.path.splitext(filename)[1],
            'ctime': datetime.utcfromtimestamp(stat.st_ctime).isoformat()
        }
        #print(json.dumps(fileinfo))
        r = requests.post(elasticurl + '/fsanalyze/file?pretty',
            data=json.dumps(fileinfo),
            auth=('elastic', 'changeme'),
            headers={'content-type': 'application/json'})
        #print(r)
