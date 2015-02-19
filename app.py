from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host=os.environ['APP_DB_HOST'], port=os.environ['APP_DB_PORT'])

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
