import os
import redis
import yaml
from rq import Queue, Worker

# Get current working dir
current_dir = os.getcwd()
config_path = os.path.join(current_dir, 'config.yaml')

with open(config_path, 'r') as stream:
    settings = yaml.safe_load(stream)

redis_host = settings['REDIS']['HOST']
redis_port = settings['REDIS']['PORT']

redis_conn = redis.Redis(host=redis_host, port=redis_port)

# Create a Redis Queue
rq = Queue(connection=redis_conn)

# Create and run worker to process jobs from queue
worker = Worker([rq], connection=redis_conn)
worker.work()
