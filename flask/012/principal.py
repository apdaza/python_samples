from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      lista = [x.split(',') for x in open(f.filename).readlines()]
      resultados = []
      for x in lista:
          x[2] = x[2][:-1]
          if x[2]=='+':
              print "suma"
              r = int(x[0]) + int(x[1])
          elif x[2]=='-':
              r = int(x[0]) - int(x[1])
          elif x[2]=='*':
              r = int(x[0]) * int(x[1])
          elif x[2]=='/':
              r = int(x[0]) / int(x[1])
          else:
              r = 0
          resultados.append(x + [r])

      print len(lista)
      return render_template('showall.html', msg = "file loaded successfully", rows = resultados)

if __name__ == '__main__':
   app.run(debug = True)
