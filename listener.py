from sseclient import SSEClient
from flask import Flask, url_for, request, jsonify
import json, requests, atexit

app = Flask(__name__)

with open('config.json') as data_file:
  config = json.load(data_file)

@app.route('/')
def multiply(a, b):
  return a*b

messages = SSEClient('{0}/notifyr?access_token={1}'
                        .format(config["particle-url"],config["token"]))

for msg in messages:
  event = str(msg.event).encode('ascii', 'ignore').decode('ascii')
  data = str(msg.data).encode('ascii', 'ignore').decode('ascii')
  print event
  print data
#  dataJson = json.loads(data)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
