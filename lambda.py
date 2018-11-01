import json
import requests
from elasticsearch import Elasticsearch

def lambda_handler(event, context):
    params = event.get("queryStringParameters", {'name': 'hot sauce'})
    es = Elasticsearch([{'host': 'vpc-sali-gtqooycfzlb4e5nnexd3hgubcm.us-east-1.es.amazonaws.com', 'scheme': 'https', 'port': 443 }])
    if es.ping():
        results = []
        res = es.search(index="food", body={"query": {"match_phrase_prefix": {"name": params['name']}}})
        for doc in res['hits']['hits'][:5]:
            results.append({'score': doc['_score'], 'name': doc['_source']['name'], 'rating': doc['_source']['rating']})
        return {
            "statusCode": 200,
            "body": json.dumps(results)
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps('Could not connect to ElasticSearch')
        }