import redis
import json
import pickle
import time

r = redis.Redis(host='localhost', port=5000, decode_responses=True)

with open('../large-file.json', 'rb') as json_file:
    data = json.load(json_file)

for event in data:
    r.hset(f"event:{event['id']}", mapping={
        "type": event["type"],
        "actor": pickle.dumps(event.get("actor")),
        "repo": pickle.dumps(event.get("repo")),
        "payload": pickle.dumps(event.get("payload")),
        "commits": pickle.dumps(event.get("commits")),
        "created_at": event.get("created_at")
    })
    r.lpush("events_ids", event['id'])

