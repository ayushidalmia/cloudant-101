"""
Allows to generate various views to generate secondary index using design 
documents
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

	index = my_database.create_query_index(fields=['description'])
	selector = {'description': {'$eq': 'I love quora'}}
	docs = my_database.get_query_result(selector,use_index = index.name)
	for d in docs:
		print d

	print "\n\n"

	
	index = my_database.create_query_index(fields=['age'])
	selector = {'age': {'$lt': 30}}
	docs = my_database.get_query_result(selector,use_index = index.name,sort=[{'age': 'desc'}])
	for d in docs:
		print d

	print "\n\n"
	
	
	index = my_database.create_query_index(fields=['color','description'])
	selector = {'description': {'$eq': 'I have a huge beard'},'color': {'$eq': 'black'}}
	docs = my_database.get_query_result(selector,use_index = index.name)
	for d in docs:
		print d


	'''
	#Doing things such that the views are in the same design document

	#create design doc
	ddoc = DesignDocument(database=my_database,document_id= '_design/DDOC/_view/description')

	ddoc.save()

	
	#create index, selector and run
	index = my_database.create_query_index(design_document_id ="_design/DDOC/_view/description", fields=['description'])
	selector = {'description': {'$eq': 'I love quora'}}
	docs = my_database.get_query_result(selector,use_index = index.name)
	for d in docs:
		print d

	print "\n\n"
	
	'''


	'''
	#Doing things from scratch

	#create design doc
	ddoc = DesignDocument(database=my_database,document_id= '_design/DDOC/_view/description')

	#add view
	ddoc.add_view("description_view","function(doc) {if(doc.description) {emit(doc._id, doc.description);}}")
	ddoc.add_view("color_view","function(doc) {if(doc.color) {emit(doc._id, doc.color);}}")
	ddoc.add_view("age_view","function(doc) {if(doc.age) {emit(doc._id, doc.age);}}")

	#save to remote db

	try:
		ddoc.save()
	except:
		pass

	
	#create index, selector and run
	#some gap in function here
	index = my_database.create_query_index(design_document_id ="_design/DDOC/_view/description", fields=['description'])
	selector = {'description': {'$eq': 'I love quora'}}
	docs = my_database.get_query_result(selector,use_index = index.name)
	for d in docs:
		print d

	print "\n\n"
	
	'''