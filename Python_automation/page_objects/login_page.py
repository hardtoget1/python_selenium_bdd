from Python_automation.page_objects.base import BasePageObject
import time
import ConfigParser
import requests
from requests.auth import HTTPBasicAuth

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')
class LoginPage(BasePageObject):
    normal_member_card_number = None
    normal_member_mdm_id = None



    def log_in(self, username, password):
        time.sleep(2)
        name_field = self._wait_until_visible(
            self.lookup['email'].locator,
            self.lookup['email'].locator_type
        )

        name_field.send_keys(username)

        pass_field = self._wait_until_visible(
            self.lookup['password'].locator,
            self.lookup['password'].locator_type
        )

        pass_field.send_keys(password)


        self._wait_until_clickable(
            self.lookup['sign_in_button'].locator,
            self.lookup['sign_in_button'].locator_type
        ).click()


        self._wait_for_ajax()

    def enter_email_and_click(self, username):

        name_field = self._wait_until_visible(
            self.lookup['username_field'].locator,
            self.lookup['username_field'].locator_type
        )
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"+username)
        name_field.send_keys(username)

        self._wait_until_clickable(
            self.lookup['verify_email_button'].locator,
            self.lookup['verify_email_button'].locator_type
        ).click()


    def click_forgotten_password(self):

        self._wait_for_ajax()

        self._wait_until_clickable(
            self.lookup['forgotten_password'].locator,
            self.lookup['forgotten_password'].locator_type
        ).click()


        self._wait_for_ajax()

    def enter_email_for_password_reset(self, email):

        self._wait_for_ajax()

        self._wait_until_clickable(
            self.lookup['forgotten_password_email'].locator,
            self.lookup['forgotten_password_email'].locator_type
        ).send_keys(email)

        self._wait_for_ajax()

    def submit_forgotten_password(self):

        self._wait_for_ajax()

        self._wait_until_clickable(
            self.lookup['forgotten_password_submit'].locator,
            self.lookup['forgotten_password_submit'].locator_type
        ).click()

        self._wait_for_ajax()

    def get_success_message(self):

        self._wait_for_ajax()

        text = self._wait_until_visible(
            self.lookup['reset_success_message'].locator,
            self.lookup['reset_success_message'].locator_type
        ).text

        self._wait_for_ajax()

        return text

    def get_error_message(self):

        self._wait_for_ajax()

        text = self._wait_until_visible(
            self.lookup['reset_error_message'].locator,
            self.lookup['reset_error_message'].locator_type
        ).text

        self._wait_for_ajax()

        return text

    def check_for_login_page(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['forgotten_password'].locator,
                self.lookup['forgotten_password'].locator_type
            )
            return True
        except:
            return False

    def check_for_login_failure(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['invalid_credentials'].locator,
                self.lookup['invalid_credentials'].locator_type
            )
            return True
        except:
            return False

    def check_logged_in(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['member_greeting'].locator,
                self.lookup['member_greeting'].locator_type
            )
            return True
        except:
            return False

    def check_for_login_failure_message(self):

        self._wait_for_ajax()

        return self._wait_until_visible(
            self.lookup['invalid_credentials'].locator,
            self.lookup['invalid_credentials'].locator_type
        ).text

    def verify_end_point_response(self, response, expected_response_code):

        if response.status_code != expected_response_code:
            print("Expected status code is   " + str(expected_response_code) + " but actual status code is  " + str(response.status_code))
        assert response.status_code == expected_response_code

    def get_normal_member_card_number(self):
        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        card_url = CONFIG.get("GET_NORMAL_MEMBER_CARD", "url")

        card_r = requests.get(url=card_url,
                              auth=HTTPBasicAuth(auth_user, auth_pass))
        return str(card_r.json()["membershipCards"][0]['cardNumber'])


    def reset_password(self, new_pass, confirm_pass):
        time.sleep(2)
        new_password_field = self._wait_until_visible(
            self.lookup['new_password'].locator,
            self.lookup['new_password'].locator_type
        )

        new_password_field.send_keys(new_pass)

        confirm_password_field = self._wait_until_visible(
            self.lookup['confirm_password'].locator,
            self.lookup['confirm_password'].locator_type
        )

        confirm_password_field.send_keys(confirm_pass)


        self._wait_until_clickable(
            self.lookup['save_password'].locator,
            self.lookup['save_password'].locator_type
        ).click()