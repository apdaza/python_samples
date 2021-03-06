from behave import *
from calculadora import Calculadora

@given('a {values} to sum')
def step_imp(context, values):
    context.calculadora = Calculadora()
    context.values = values.split(',')

@when('the calc sum the values')
def step_imp(context):
    context.total = context.calculadora.sumar(int(context.values[0]),int(context.values[1]))

@then('the {total:d} is ok')
def step_imp(context, total):
    assert(total == context.total)

@given('a {values} to times')
def step_imp(context, values):
    context.calculadora = Calculadora()
    context.values = values.split(',')

@when('the calc time the values')
def step_imp(context):
    context.total = context.calculadora.multiplicar(int(context.values[0]),int(context.values[1]))

@then('the {product:d} is ok')
def step_imp(context, total):
    assert(total == context.total)