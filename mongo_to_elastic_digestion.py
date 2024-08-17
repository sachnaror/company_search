from elasticsearch import Elasticsearch, helpers
from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['companyDB']  # Replace with your database name
collection = db['companies']  # Replace with your collection name

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Index MongoDB data into Elasticsearch
def index_data():
    actions = []
    for document in collection.find():
        # Prepare the data for Elasticsearch
        action = {
            "_index": "company_index",  # Replace with your index name
            "_id": str(document['_id']),
            "_source": document
        }
        actions.append(action)

    # Bulk index the data
    helpers.bulk(es, actions)
    print("Data indexed successfully.")

if __name__ == "__main__":
    index_data()
