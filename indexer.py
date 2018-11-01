import csv
import requests
from elasticsearch import Elasticsearch
from time import sleep

es = Elasticsearch([{'host': 'localhost', 'scheme': 'https', 'verify_certs': False, 'port': 9200 }])

if not es.ping():
    print('Could not connect to ElasticSearch')
else:
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        id = 0
        for row in csv_reader:
            doc = {
                'name': row[0].strip(),
                'rating': int(row[1]),
            }
            res = es.index(index="food", doc_type='text', id=id, body=doc)
            print(res['result'])
            sleep(0.1)
            id += 1

