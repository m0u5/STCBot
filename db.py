import os
from pymongo import MongoClient


client = MongoClient('mongodb://db_user:db_password@mongodb:27017/stcDb')
database = client.stcDb
