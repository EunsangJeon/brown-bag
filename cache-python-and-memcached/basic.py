from pymemcache.client import base
from pymongo import MongoClient

def findJohn():
  mongoClient = MongoClient()
  collection = mongoClient.cache_python_memcached.test
  # print(collection.find_one({'name': 'John'}))
  return collection.find_one({'name': 'John'}) 

memClient = base.Client(('localhost', 11211))
result = memClient.get('John')

if result is None:
  result = findJohn()
  memClient.set('John', result)

print(result)
