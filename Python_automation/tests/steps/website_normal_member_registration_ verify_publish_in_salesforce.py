
from behave import then

from Python_automation.locators.salesforce_dash import SALESFORCE_DASH_LOOKUP
from Python_automation.page_objects import SalesforceDash
from Python_automation.page_objects import Dashboard






@then(u'I log in to Salesforce')
def step_impl(context):
    context.salesforce = SalesforceDash(
        browser=context.browser,
        lookup=SALESFORCE_DASH_LOOKUP,
    )
    context.salesforce.salesforce_login()

@then(u'verify that the Member can be found')
def step_impl(context):
    print(" Card number at verify that the Member can be found"+Dashboard.member_card_number)
    context.salesforce.salesforce_search_by_card_no(Dashboard.member_card_number)

    context.salesforce.select_member()



