import os
import redis
import yaml
import django_rq

# Get current working dir
current_dir = os.getcwd()
config_path = os.path.join(current_dir, 'config.yaml')

with open(config_path, 'r') as stream:
    settings = yaml.safe_load(stream)

redis_host = settings['REDIS']['HOST']
redis_port = settings['REDIS']['PORT']

# redis_conn = redis.Redis(host=redis_host, port=redis_port)

# Create a Redis Queue

# Create and run worker to process jobs from queue
worker = django_rq.get_worker()
worker.work()
