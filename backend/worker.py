from os import getenv
from  redis import from_url
from rq import Worker, Queue, Connection

listen = ['default']
redis_url = getenv('redis_url')
conn = from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()