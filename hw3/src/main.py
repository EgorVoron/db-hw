import redis
import pickle
import time

r = redis.Redis(host='localhost', port=5000, decode_responses=True)

N = 1000
t = time.time()
for _ in range(N):
    r.lindex('events_idx', 0)
print((time.time() - t)/N)

t = time.time()
for i in range(N):
    idx = r.lindex('events_ids', i)
    type = r.hget(f'event:{idx}', 'type')
print((time.time() - t)/N)


t = time.time()
for i in range(N):
    idx = r.lindex('events_ids', i)
    r.hset(f'event:{idx}', 'type', 'testType')
print((time.time() - t)/N)

