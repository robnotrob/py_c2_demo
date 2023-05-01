from flask import Flask, request, send_file
from .helpers import parse_hex_for_signal

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_beacon():
    if request.method == 'POST':
        hex_data = request.data.hex()

        if parse_hex_for_signal(hex_data, 'aa', 8, 10):
            print("sending injection...")
            return send_file("injections/ls_injection.json")
        
        return "test"