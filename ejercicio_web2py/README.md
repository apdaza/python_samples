# Ejercicio con web2py

- en db.py
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


- en default.py para crear los formularios dinámicos
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

- para crear las vistas se crean en views los archivos:
  - form_registration.html

    {{extend 'layout.html'}}
    <h5> User Registration Form </h5>
    <br  />
    {{=form}}
    <br  />

  - form_personal.html

    {{extend 'layout.html'}}
    <h5> User Registration Form </h5>
    <br  />
    {{=form}}
    <br  />


- en default.py para crear las grid respectivas

    @auth.requires_login()
    def records_registration():
       records = SQLFORM.grid(db.registration, user_signature=True)
       return locals()

    @auth.requires_login()
    def records_personal():
       records = SQLFORM.grid(db.personal, user_signature=True)
       return locals()
