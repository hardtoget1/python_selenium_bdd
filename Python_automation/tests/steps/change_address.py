import ConfigParser
import random
import requests
from requests.auth import HTTPBasicAuth

import time
from behave import then, when
from Python_automation.locators import REGISTRATION_PAGE_LOOKUP, DASHBOARD_LOOKUP
from Python_automation.page_objects import Register, Dashboard
CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')


@when(u'I change the value for Address to another value')
def step_impl(context):
    context.settings = Dashboard(browser=context.browser,
                                 lookup=DASHBOARD_LOOKUP)
    context.registration = Register(browser=context.browser,
                                    lookup=REGISTRATION_PAGE_LOOKUP)

    context.Address_line_1 = context.registration.random_word()
    context.Address_line_2 = context.registration.random_word()
    context.city = context.registration.random_word()
    context.postcode = "M"+str(random.randint(10, 99))+" "+str(random.randint(1, 9))+"AG"
    context.country = "United Kingdom"
    print("Expected Address_line_1 = "+context.Address_line_1)
    print("Expected Address_line_2 = "+context.Address_line_2)
    print("Expected city = "+context.city)
    print("Expected postcode = "+context.postcode)
    print("Expected country = "+context.country)

    context.address_object = {
        "Address line 1": context.Address_line_1,
        "Address line 2": context.Address_line_2,
        "City": context.city,
        "Postcode": context.postcode
    }
    context.settings.change_address(address_object=context.address_object)


@when(u'I change the address to another community which has associated causes')
def step_impl(context):
    context.settings = Dashboard(browser=context.browser,
                                 lookup=DASHBOARD_LOOKUP)
    context.registration = Register(browser=context.browser,
                                    lookup=REGISTRATION_PAGE_LOOKUP)

    auth_user = CONFIG.get("SIT AUTH", "user")
    auth_pass = CONFIG.get("SIT AUTH", "pass")
    url_first_part = CONFIG.get("GET_MEMBER_ADDRESS_LAT_LONG", "url")
    mdm_id = CONFIG.get("ALREADY_REGISTERED_MEMBER_WITH_CAUSE", "mdm")
    url = url_first_part.replace("@", mdm_id)
    print("DAPI endpoint for member address lat/long is * " + url)
    lat_long_r = requests.get(url=url,
                              auth=HTTPBasicAuth(auth_user, auth_pass))
    context.login.verify_end_point_response(lat_long_r, 200)
    actual_post_code = str(lat_long_r.json()["currentAddress"]['postCode'])
    print("ACTUAL Post code " + actual_post_code)

    if actual_post_code == 'KA27 8DL':
        context.postcode = 'CB6 2SX'
    else:
        context.postcode = 'KA27 8DL'

    context.Address_line_1 = context.registration.random_word()
    context.Address_line_2 = context.registration.random_word()
    context.city = context.registration.random_word()
    context.country = "United Kingdom"
    print("Expected Address_line_1 = "+context.Address_line_1)
    print("Expected Address_line_2 = "+context.Address_line_2)
    print("Expected city = "+context.city)
    print("Expected postcode = "+context.postcode)
    print("Expected country = "+context.country)

    context.address_object = {
        "Address line 1": context.Address_line_1,
        "Address line 2": context.Address_line_2,
        "City": context.city,
        "Postcode": context.postcode
    }
    context.settings.change_address(address_object=context.address_object)




@when(u'I click the Save button')
def step_impl(context):
    context.settings.click_save_button()


@then(u'I can see the updated Address on the \'Change your details\' page')
def step_impl(context):
    assert context.settings.check_update_success()
    time.sleep(3)
    current_address = str(context.settings.get_current_address())
    first_line_address = current_address.splitlines()[0]
    second_line_address = current_address.splitlines()[1]
    city_in_portal = current_address.splitlines()[2]
    postcode_in_portal = current_address.splitlines()[3]
    country_in_portal = current_address.splitlines()[4]

    assert context.Address_line_1 == first_line_address
    assert context.Address_line_2 == second_line_address
    assert context.city == city_in_portal
    assert context.postcode == postcode_in_portal
    assert context.country == country_in_portal


@then(u'I can see the updated Address in MDM')
def step_impl(context):
    time.sleep(3)
    auth_user = CONFIG.get("SIT AUTH", "user")
    auth_pass = CONFIG.get("SIT AUTH", "pass")
    url = CONFIG.get("GET_MEMBER_ADDRESS", "url")
    r = requests.get(url=url,
                     auth=HTTPBasicAuth(auth_user, auth_pass))
    context.login.verify_end_point_response(r, 200)
    assert context.Address_line_1 == str(r.json()["currentAddress"]['addressLine1'])
    assert context.Address_line_2 == str(r.json()["currentAddress"]['addressLine2'])
    assert context.city == str(r.json()["currentAddress"]['city'])
    assert context.postcode == str(r.json()["currentAddress"]['postCode'])
    assert context.country == str(r.json()["currentAddress"]['country'])

@then(u'I select the membership home page')
def step_impl(context):
    context.settings.click_home_page()
