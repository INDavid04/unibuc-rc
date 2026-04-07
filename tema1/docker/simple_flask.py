# Socket pentru exercitiul 3
import socket

from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

# Ex. 1
@app.route('/')
def hello():
    return "Irimia David 271/2024"

# Ex. 2
@app.route('/items/<item_id>')
def itemId(item_id):
    return jsonify({"item_id": item_id})

# Ex. 3
@app.route('/ip')
def containerIp():
    return jsonify({"ip": socket.gethostbyname(socket.gethostname())})

'''
This method expects a json content.
Use header: 'Content-Type: application/json'
'''
@app.route('/post', methods=['POST'])
def post_method():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    return jsonify({'got_it': 'yes'})


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
