from db_query import get_last_results
import uuid
from elasticsearch import Elasticsearch
import json
client = Elasticsearch(
  "https://aa9600fc481c48df997e3d93bb0ccca7.europe-west9.gcp.elastic-cloud.com:443",
  api_key="Umo3QnRKSUJ4U1JKa2s5Nkx0bVk6Qno5c3FGN3BRSG04blpZVFBxUU9RUQ=="
)
results = get_last_results()
document = [ {"index": {"_index": "soda", "_id": str(uuid.uuid1())}}, results ]

print(json.dumps(results))
client.bulk(operations=document, pipeline="ent-search-generic-ingestion")