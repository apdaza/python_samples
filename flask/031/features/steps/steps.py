from behave import *
import requests

@given('a {entity} to show fields')
def step_impl(context, entity):
    context.api_url = 'http://localhost:5000/list/' + entity

@when('the entity was selected')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="")
    context.texto = response.text

@then('the {fields} are listed')
def step_impl(context, fields):
    assert (fields in context.texto)

@given('a data base of banco de preguntas')
def step_impl(context):
    context.api_url = 'http://localhost:5000/'

@when('the db was connected')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="")
    context.texto = response.text

@then('the {entity} was listed')
def step_impl(context, entity):
    assert(entity in context.texto)
