from elasticsearch import Elasticsearch
#create elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#input search text
searchText = input("Input text to search?\n")

#send query to elasticsearch service
#find the record which column "PdfText" contains searchText
res = es.search(index="gba", body={"query": {"match": {"PdfText": searchText}}})
print("Got %d Hits:" %res['hits']['total']['value'])
print("Max_Score: %lf" %res['hits']['max_score'])
#output first record
print(res['hits']['hits'][0])