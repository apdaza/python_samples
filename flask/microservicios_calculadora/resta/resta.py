from flask import Flask
app = Flask(__name__)


@app.route('/')
def saludar():
   return "resta"
   
@app.route('/<val1>/<val2>')
def operar(val1, val2):
   return str(int(val1) -  int(val2))

if __name__ == '__main__':
   app.run(host='0.0.0.0',port='4040')
