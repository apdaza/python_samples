# Ejercicio con web2py

- en db.py
<pre>
    db = DAL('sqlite://storage.sqlite')
    db.define_table('registration',
        Field('firstname', requires=IS_NOT_EMPTY()),
        Field('lastname', requires=IS_NOT_EMPTY()),
        Field('gender', requires=IS_IN_SET(['Male', 'Female'])),
        Field('username', requires=IS_NOT_EMPTY()),
        Field('password', 'password'),
        Field('about_you', 'text'),
        Field('image', 'upload'))

    db.define_table('personal',
        Field('nick_name', requires=IS_NOT_EMPTY()),
        Field('address', requires=IS_NOT_EMPTY()),
        Field('married', 'boolean'),
        Field('zip_code', requires=IS_NOT_EMPTY()))
</pre>

- en default.py para crear los formularios dinámicos

<pre>
    def form_registration():
        form = SQLFORM(db.registration, request.args(0), deletable=True, upload=URL(r=request, f='download'))
        if form.accepts(request.vars, session):
           if not form.record:
               response.flash = 'Your input data has been submitted.'
           else:
               if form.vars.delete_this_record:
                   session.flash = 'User record successfully deleted.'
               else:
                   session.flash = 'User record successfully updated.'
               redirect(URL(r=request, f='form_a'))
        records = db().select(db.registration.ALL)
        return dict(form=form, records=records)

    def form_personal():
        form = SQLFORM(db.personal, request.args(0), deletable=True, upload=URL(r=request, f='download'))
        if form.accepts(request.vars, session):
           if not form.record:
               response.flash = 'Your input data has been submitted.'
           else:
               if form.vars.delete_this_record:
                   session.flash = 'User record successfully deleted.'
               else:
                   session.flash = 'User record successfully updated.'
               redirect(URL(r=request, f='form_a'))
        records = db().select(db.registration.ALL)
        return dict(form=form, records=records)
</pre>

- para crear las vistas se crean en views los archivos:
  - form_registration.html

<pre>
    {{extend 'layout.html'}}
    <h5> User Registration Form </h5>
    <br  />
    {{=form}}
    <br  />
</pre>

  - form_personal.html

<pre>
    {{extend 'layout.html'}}
    <h5> User Registration Form </h5>
    <br  />
    {{=form}}
    <br  />
</pre>

- en default.py para crear las grid respectivas

<pre>
    @auth.requires_login()
    def records_registration():
       records = SQLFORM.grid(db.registration, user_signature=True)
       return locals()

    @auth.requires_login()
    def records_personal():
       records = SQLFORM.grid(db.personal, user_signature=True)
       return locals()
</pre>


- en default.py modificamos la función index()

<pre>
    def index():
        response.flash = T("Hola mundo en web2py")
        rawrows = db.executesql("select * from registration")
        return dict(message=T('Ejemplo básico'), regs=rawrows)
</pre>


- y en la vista index.html

<pre>
    {{extend 'layout.html'}}

    {{block header}}
    <div class="jumbotron jumbotron-fluid background" style="background-color: #333; color:white; padding:30px;word-wrap:break-word;">
      <div class="container center">
        <h1 class="display-5">/{{=request.application}}/{{=request.controller}}/{{=request.function}}</h1>
      </div>
    </div>
    {{end}}

    <div class="row">
      <div class="col-md-12">
        {{if 'message' in globals():}}
        <h2>{{=message}}</h2>
        aqui lo que queremos que se vea de texto plano
          <table class="propios">
              {{for i in regs:}}
              <tr>
                  <td class="propios">{{=i[0]}}</td>
                  <td class="propios">{{=i[1]}}</td>
                  <td class="propios">{{=i[2]}}</td>
              </tr>
              {{pass}}
          </table>

        <div class="jumbotron jumbotron-fluid" style="padding:30px;word-wrap:break-word;">
          <div class="container center">
            Un ejemplo de web2py
          </div>
        </div>
        {{elif 'content' in globals():}}
        {{=content}}
        {{else:}}
        {{=BEAUTIFY(response._vars)}}
        {{pass}}
      </div>
    </div>
</pre>
