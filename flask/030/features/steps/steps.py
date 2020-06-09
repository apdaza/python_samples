from behave import *
import requests


@given('a {name} to greet')
def step_impl(context, name):
    context.api_url = 'http://localhost:5000/user/' + name
    print('url :'+context.api_url)

@when('the greeter greets the names')
def step_impl(context):
    response = requests.get(url=context.api_url, headers="")
    print(response.text)
    context.saludo = response.text

@then('the {greet} of name is correct')
def step_impl(context, greet):
    assert (context.saludo == greet)
