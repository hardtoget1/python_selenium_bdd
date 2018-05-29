"""
Provides shared Page Objects functionality.

All the Page Object related shared functionality lives here.
No helper or utils files are necessary.
"""
import ConfigParser
import json
import requests
from requests.auth import HTTPBasicAuth

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    presence_of_element_located,
    visibility_of_element_located
)
from selenium.webdriver.support.ui import WebDriverWait

from .exceptions import NoURLException

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')


class ElementMethods(object):  # pylint: disable=R0903
    """
    Defines waiting methods.

    """


    def _wait_until_condition(self, condition, wait_time=50):
        """
        Helper to wait for a condition to be fulfilled.

        :param condition: condition to be fulfilled
        :param wait_time: timeout in seconds

        :type condition: selenium.webdriver.support.expected_conditions
        :type wait_time: int

        :returns: instance of WebElement
        :rtype: selenium.webdriver.remote.webelement.WebElement
        """

        if not wait_time:
            wait_time = 15

        wait = WebDriverWait(self._driver, wait_time)
        return wait.until(condition)

    def _wait_until_condition_locator(self, locator, condition_class,
                                      wait_time=None):
        """Helper to wait for DOM to be ready."""
        return self._wait_until_condition(
            condition_class(locator),
            wait_time=wait_time,
        )

    def _wait_until_condition_by_css_selector(self, css_selector,
                                              condition_class, wait_time=None):
        """Helper to wait for DOM to be ready using a css selector."""

        return self._wait_until_condition_locator(
            (By.CSS_SELECTOR, css_selector),
            condition_class,
            wait_time=wait_time,
        )

    def _wait_until_condition_by_xpath(self, xpath, condition_class,
                                       wait_time=None):
        """Helper to wait for DOM to be ready using xpath."""

        return self._wait_until_condition_locator(
            (By.XPATH, xpath),
            condition_class,
            wait_time=wait_time,
        )

    def _wait_until_clickable(self, selector, selector_type, wait_time=None):
        """
        Wait until a DOM element is clickable.


        """

        return self._wait_until_condition_locator(
            locator=(selector_type, selector),
            condition_class=element_to_be_clickable,
            wait_time=wait_time,
        )



    def _wait_until_present(self, selector, selector_type, wait_time=None):
        """
        Wait until a DOM element is present.


        """

        return self._wait_until_condition_locator(
            locator=(selector_type, selector),
            condition_class=presence_of_element_located,
            wait_time=wait_time,
        )



    def _wait_until_visible(self, selector, selector_type,
                            wait_time=None):
        """
        Wait until a DOM element is visible.

        Element is not only displayed but also has a height and width
        that is greater than 0.

        :param selector: selector for the web element we are looking for
        :param selector_type: type of the selector
        :param wait_time: max time to wait for the web element expressed
            in seconds

        :type selector: string
        :type selector_type: selenium.webdriver.common.by.By
        :type wait_time: int

        :returns: instance of WebElement
        :rtype: selenium.webdriver.remote.webelement.WebElement
        """

        return self._wait_until_condition_locator(
            locator=(selector_type, selector),
            condition_class=visibility_of_element_located,
            wait_time=wait_time,
        )

    def _wait_for_ajax(self):


        wait = WebDriverWait(self._driver, 25)
        wait.until(lambda s: s.execute_script("return jQuery.active == 0"))






class BasePageObject(ElementMethods):
    """
    Base class for Page Objects.

    Provides shared functionality for the Page Objects.

    Please note that this is not to be understood as a whole page. This
    is a page object understood as an area of the web application
    representing a set of controls allowing to execute cohesive
    functionality.

    :param browser: a webdriver pointer
    :param lookup: dictionary of Locator tuples describing web elements
        that we will be interacting with
    :param url: http path to the page where the page object is
        expected to exist

    :type browser: webdriver instance
    :type lookup: dict of locators.base.Locator instances
    :type url: string

    .. note:: The class defines self.container as the starting point for
        any DOM discovery. This ensures that the driver's scope is
        limited to what is defined with the page objects's `selector`
        parameter. The container is realized with the `contain`
        decorator present in this module

    .. note:: Read more at: http://martinfowler.com/bliki/PageObject.html
    """
    _DEFAULT_WAIT_TIME = 25  # increased wait time for slow environments

    def __init__(self, browser, lookup, url=None):
        super(BasePageObject, self).__init__()
        self.browser = browser
        self.lookup = lookup
        self.container = None
        self._url = url

    def navigate(self):
        """
        Navigation to url stored in self._url.

        """
        if not self._url:
            raise NoURLException("You must provide the url to the class!")
        if self.browser.current_url != self._url:
            self.browser.get(self._url)

    @property
    def _driver(self):
        """Returns the preferable driver if present.

        """
        return self.container or self.browser

    def _select_option_by_value(self, select_box_css_selector, value):
        """Select an option from a select box."""
        self._driver.find_element_by_css_selector(
            "{select} > option[value='{value}']".format(
                select=select_box_css_selector,
                value=value,
            )
        ).click()

    def _set_text(self, lookup_name, value):
        field = self._wait_until_clickable(
            self.lookup[lookup_name].locator,
            self.lookup[lookup_name].locator_type,
        )
        field.send_keys(value)

    @staticmethod
    def add_employee_to_db(surname):

        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        url = CONFIG.get("CREATE_EMP_URL", "url")

        headers = {'content-type': 'application/json'}

        payload = {"batchNumber": 0, "employeeUpdateRequestRecords": [{
            "transaction": "NEW",
            "staffNumber": "1234567",
            "surname": "{}".format(surname),
            "dateOfBirth": "1971-01-01",
            "employmentStartDate": "2016-05-31T13:42:20.254Z"}]}

        r = requests.post(url=url,
                          data=json.dumps(payload),
                          headers=headers,
                          auth=HTTPBasicAuth(auth_user, auth_pass))

        actual_status_code = r.status_code

        print("Actual status code for add_employee_to_db is  " + str(actual_status_code))


        assert actual_status_code == 200

    @staticmethod
    def register_call_centre_no_email(surname):

        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        url = CONFIG.get("REG_CC_URL", "url")

        headers = {'content-type': 'application/json'}

        payload = {"member": {
                        "birthDate": "1971-01-01",
                        "title": "Mr",
                        "firstName": "Jon",
                        "lastName": "{}".format(surname),
                        "vipType": "VIP Member",
                        "shareAccountStatus": "Active",
                        "shareAccountNumber": "12323",
                        "sunlightId": "123456",
                        "informationFormat": "Large Print"
                      },
                      "address": {
                        "addressLine1": "Floor 13",
                        "addressLine2": "1 Angel Square",
                        "city": "Manchester",
                        "country": "United Kingdom",
                        "postCode": "M60 0AG",
                        "usage": "PRIMARY",
                        "startDate": "2016-02-17",
                        "foreignIndicator": True,
                        "overridden": True,
                        "latitude": 0,
                        "longitude": 0
                      },
                   "employeeNumber": "1234567",
                   "sourceIdentifier": "DBS"}

        r = requests.post(url=url,
                          data=json.dumps(payload),
                          headers=headers,
                          auth=HTTPBasicAuth(auth_user, auth_pass))


        actual_status_code = r.status_code

        print("Actual status code for register_call_centre_no_email is  " + str(actual_status_code))

        assert r.status_code == 200

        return r.json()["card"]["cardNumber"]

    @staticmethod
    def evict_wallet_cache(mem_no):

        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        url = "{0}:9502/{1}/cache-evict".format(CONFIG.get('SIT', 'api url'), mem_no)


        r = requests.post(url=url,
                          auth = HTTPBasicAuth(auth_user, auth_pass)
                          )

        assert r.status_code == 200

    @staticmethod
    def get_a_temp_card():
        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        url = CONFIG.get("GET_TEMP_CARD", "url")

        headers = {'content-type': 'application/json'}
        payload = {
                 "cardTypeName": "member",
                 "customerTypeName": "Co-operative Food",
                 "cardStatusName": "Sent for fulfilment",
                 "numberOfCards": 1
            }
        r = requests.post(url=url,
                          data=json.dumps(payload),
                          headers=headers,
                          auth=HTTPBasicAuth(auth_user, auth_pass))
        print(" actual status code for GET_TEMP_CARD "+str(r.status_code))

        assert r.status_code == 200
        temp_card_number = r.json()["cardNumbers"][0]
        print(" temp_card_number ***" + temp_card_number)

        return temp_card_number