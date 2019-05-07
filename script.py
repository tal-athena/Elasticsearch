#import requests
#res = requests.get('http://localhost:9200')
#print(res.content)

from elasticsearch import Elasticsearch
# create Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


import sqlite3

conn = sqlite3.connect('gba.db')
print ("Opened database successfully")

#Read all records from gba.db
cursor = conn.execute("SELECT Id, PdfLink, PdfText, DocumentUrl from Records")
#for each row
for row in cursor:
	# insert data to elasticsearch
	# if index 'gba' and doc_type 'abschluse' don't exist, it create automatically
	# set the id same as gba.db id, so elasticsearch db will be same as gba.db
	# if the id is already exist, it update with new record
	es.index(index='gba', doc_type='abschluse', id=row[0], body={'PdfLink':row[1], 'PdfText':row[2], 'DocumentUrl': row[3]})
	print (row[0])
print ("Operation done successfully")
conn.close()

