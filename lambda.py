import json
import requests
from elasticsearch import Elasticsearch

def lambda_handler(event, context):
    params = event["queryStringParameters"]
    # search_string = event["queryStringParameters"].get('search_string')
    # print("Search string is:")
    # print(search_string)
    es = Elasticsearch([{'host': 'vpc-sali-gtqooycfzlb4e5nnexd3hgubcm.us-east-1.es.amazonaws.com', 'scheme': 'https', 'port': 443 }])
    # print('Doing a GET on  HTTPS......')
    # r=requests.get("https://vpc-sali-gtqooycfzlb4e5nnexd3hgubcm.us-east-1.es.amazonaws.com")
    # print(r)
    print('Pinging es...')
    if es.ping():
        response_str = ''
        res = es.search(index="customer", body={"query": {"match": {"name": params.get('search_string', 'Joe')}}})
        for doc in res['hits']['hits']:
            response_str = response_str + '\n' + str(doc['_score']) + doc['_source']['name']
        return {
            "statusCode": 200,
            "body": json.dumps(str(params) + 'Hello from Sali! Connected to ES.' + response_str)
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps('Could not connect to ES')
        }