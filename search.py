"""
Allows to create search index on the database and query it in lucene style
"""

__author__      = "Ayushi Dalmia"
__email__ = "ayushidalmia2604@gmail.com"


from cloudant import cloudant
import json
from cloudant.result import Result,ResultByKey
import random
from cloudant.design_document import DesignDocument
from cloudant.query import Query

with open('credentials.json') as f:
	cred  = json.load(f)

with cloudant(str(cred['credentials']['username']),str(cred['credentials']['password']),url=str(cred['credentials']['url'])) as client:
	
	my_database = client['test']


	index = my_database.create_query_index(fields=[{'name': 'description','type':'string'}],index_type='text')
	selector = {'$text': "happiest	"}
	docs = my_database.get_query_result(selector,use_index = index.name)
	for d in docs:
		print d
	


	'''
	#create design doc
	ddoc = DesignDocument(my_database,document_id="_design/description")

	
	search_index = "function(doc){index(\"default\", doc._id);if (doc.description){index(\"filename\", doc.description, {\"store\": true});}}"
	ddoc.add_search_index("freesearch", search_index,analyzer="english")

	ddoc.save()

	
	#save to remote db
	try:
		ddoc.save()
	except:
		pass
	

	index = my_database.create_query_index(design_document_id="_design/description",fields=[{'name': 'description','type':'string'}],index_type='text')
	selector = {'$text': "happiest	"}
	docs = my_database.get_query_result(selector,use_index = index.name)
	for d in docs:
		print d

	'''
