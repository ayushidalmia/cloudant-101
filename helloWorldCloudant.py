"""
Does basic operations like creating a database, adding documents, 
retrieving documents from the database using primary index and delete the 
database.
"""

__author__      = "Ayushi Dalmia"
__email__ = "ayushidalmia2604@gmail.com"

from cloudant import cloudant
import json
import time
from cloudant.result import Result,ResultByKey

with open('credentials.json') as f:
	cred  = json.load(f)

with cloudant(str(cred['credentials']['username']),str(cred['credentials']['password']),url=str(cred['credentials']['url'])) as client:

	#To print databases
	print 'Databases: {0}'.format(client.all_dbs())

	try:
		client.delete_database('test')
	except:
		pass
	#To create a database
	my_database = client.create_database('test')
	

	#To open a database
	my_database = client['test']

	
	#To insert in a database from a file:
	filename = "dummyDatabase.json" #Sample line in xyz.txt: { 'name': 'Julia','age': 30,'pets': ['cat', 'dog', 'frog']}
	f=open(filename,"r")
	for line in f:
		my_database.create_document(eval(line.strip()))
	f.close()

	'''
    #To retrieve from a database
	result = my_database.custom_result(include_docs=True) #Insert keys to retrieve using parameter keys=[] as a list
	with result as r:
		print r[:] 
	'''

	#To retrieve from a database
	result = my_database.custom_result(include_docs=True,keys=['1','2','3','11']) #Insert keys to retrieve using parameter keys=[] as a list
	with result as r:
		print r[:] 
	


