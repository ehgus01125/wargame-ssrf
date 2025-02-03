from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def route():
    return "99% complete"

@app.route('/flag')
def flag():
    return "GH{SSRF_L0c4l_Tr4v3l3r}"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
