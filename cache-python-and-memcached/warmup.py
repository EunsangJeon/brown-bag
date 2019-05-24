from pymemcache.client import base
from pymongo import MongoClient
from pymemcache import fallback

def findJohn():
  mongoClient = MongoClient()
  collection = mongoClient.cache_python_memcached.test
  # print(collection.find_one({'name': 'John'}))
  return collection.find_one({'name': 'John'}) 

# Set `ignore_exc=True` so it is possible to shut down
old_cache = base.Client(('localhost', 11211), ignore_exc=True)
new_cache = base.Client(('localhost', 11212))
memClient = fallback.FallbackClient((new_cache, old_cache))
result = memClient.get('John')

if result is None:
  result = findJohn()
  memClient.set('John', result)

print(result)
