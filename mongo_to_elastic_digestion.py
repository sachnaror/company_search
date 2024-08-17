import json

from bson import ObjectId
from elasticsearch import Elasticsearch, helpers
from pymongo import MongoClient

# Initialize Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
mongo_db = client['companyDB']
mongo_collection = mongo_db['companies']

def doc_generator():
    for doc in mongo_collection.find():
        # Remove the MongoDB _id field before indexing
        if '_id' in doc:
            del doc['_id']
        # Convert ObjectId to string if necessary (for other fields)
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
        yield {
            "_index": "company_index",
            "_source": doc
        }

try:
    # Perform the bulk indexing
    success_count = 0
    failure_count = 0
    for success, info in helpers.streaming_bulk(es, doc_generator()):
        if not success:
            print(f"Failed to index document: {info}")
            failure_count += 1
        else:
            success_count += 1

    print(f"Successfully indexed {success_count} documents.")
    print(f"Failed to index {failure_count} documents.")
except Exception as e:
    print(f"An error occurred: {e}")
