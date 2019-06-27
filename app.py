import os

from flask import Flask
from redis import Redis


app = Flask(__name__)

redis = Redis.from_url(os.environ.get('REDIS_URL', 'redis://localhost:6379/0'))


@app.route('/')
def hello_world():
    counter = redis.incr('counter')
    return 'Counter: %d' % counter
