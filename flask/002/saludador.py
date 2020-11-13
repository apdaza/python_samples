from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/hello')
def hello():
   return "No name "

if __name__ == '__main__':
   app.run(debug = True)
