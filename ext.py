from flask import Flask, request
import requests

app = Flask(__name__)
app.jinja_env.autoescape = False

def filter_url(a):
   black = ['127.0.0.1', 'localhost']
   for keyword in black:
       if keyword in a.lower():
           return False
   return True

@app.route('/')
def index():
   return '<p style="margin: 0">hello<a href="/submit">Click to go to /submit</a></p>'

def submit():
   a = request.args.get('a')
   if not a:
       return 'Use the "a" parameter to access internal network'
   if not filter_url(a):
       return "filtering", 404
   try:
       response = requests.get(a)
       return response.text
   except Exception:
       return "404 Not Found", 404

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
