from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   dict = {'python':50,'java':10,'php':25}
   return render_template('hello_render.html', name = user, dict = dict)

if __name__ == '__main__':
   app.run(debug = True)
