import os

from pymongo import MongoClient
# username = os.environ['MONGO_INITDB_ROOT_USERNAME']
# password = os.environ['MONGO_INITDB_ROOT_PASSWORD']

client = MongoClient('mongodb://%s:%s@db:27017/stcDb' % ('root', 'example'))

database = client.stcDb
