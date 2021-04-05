from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hojas.sqlite3'
app.config['SECRET_KEY'] = "secret_key"

db = SQLAlchemy(app)

class basicos (db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   nombres = db.Column(db.String(100))
   apellidos = db.Column(db.String(100))
   fecha_nacimiento = db.Column(db.Date)
   direccion = db.Column(db.String(100))
   correo = db.Column(db.String(100))
   telefono = db.Column(db.String(20))
   
   def __init__(self, name, city, addr,pin):
       self.name = name
       self.city = city
       self.addr = addr
       self.pin = pin

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],request.form['addr'], request.form['pin'])

         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    name = request.form.get("oldname")
    student = students.query.filter_by(name=name).first()
    return render_template('update.html', result = student, oldname = name)

@app.route("/update_record", methods=["POST"])
def update_record():
    name = request.form.get("oldname")
    student = students.query.filter_by(name=name).first()
    student.name = request.form['name']
    student.city = request.form['city']
    student.addr = request.form['addr']
    student.pin = request.form['pin']
    db.session.commit()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("oldname")
    student = students.query.filter_by(name=name).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
