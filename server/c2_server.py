from flask import Flask, request
from .helpers import parse_hex_for_signal

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_beacon():
    if request.method == 'POST':
        hex_data = request.data.hex()

        print(hex_data)

        if parse_hex_for_signal(hex_data, 'aa', 8, 10):
            print("byte found")
        
        else: print("byte not found")
        return "test"