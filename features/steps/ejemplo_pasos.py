# Archivo:features/steps/ejemplo_pasos.py
# https://glud.udistrital.edu.co/feature-testing-layout-with-behave/

from behave import given, when, then

@given('Nosotros corremos nuestro primer programa con behave')
def step_impl(context):
    pass

@when('Nosotros implementamos el primer caso')
def step_impl(context):
    assert True is not False

@then('Behave probara nuestro caso, !por nosotros!')
def step_impl(context):
    assert context.failed is False
