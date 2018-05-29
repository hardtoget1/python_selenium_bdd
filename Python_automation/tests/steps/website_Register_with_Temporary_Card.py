import ConfigParser

from behave import *

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')


@when(u'I click on the \'Register a temporary card\' link')
def step_impl(context):
    context.registration.select_yes_key_fob()


@when(u'I enter my unique card number')
def step_impl(context):
    context.registration.enter_membership_card_number(context.registration.get_a_temp_card())


@when(u'I enter all mandatory details')
def step_impl(context):
    context.surname = context.registration.random_word()

    context.reg_object = {
        "title": "MR",
        "first": "TempCardUser",
        "last": context.surname,
        "employee": None,
        "dd": "01",
        "mm": "01",
        "yyyy": "1971",
        "postcode": "M60 0AG",
        "email": "testingcycle04+{}@gmail.com".format(context.surname),
        "password": "Team1234"
    }

    context.registration.register_member(reg_object=context.reg_object)


@then(u'I should see a success message')
def step_impl(context):
    assert context.settings.check_register_success_message()


@then(u'I should not see a success message')
def step_impl(context):
    success_message_present = context.settings.check_register_success_message()
    assert success_message_present == False
