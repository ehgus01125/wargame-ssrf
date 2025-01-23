from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def route():
    return "99% complete"

@app.route('/flag')
def flag():
    return "GH{fake_flag}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
