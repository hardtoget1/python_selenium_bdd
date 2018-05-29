import time

from Python_automation.page_objects.base import BasePageObject
import random, string


class Register(BasePageObject):

    def register_member(self, reg_object):

        def set_field(selector, keys):
            self._wait_until_visible(
                self.lookup[selector].locator,
                self.lookup[selector].locator_type
            ).send_keys(keys)



        # Set title
        self._select_option_by_value(
            self.lookup['member_title'].locator,
            value=reg_object['title']
        )

        # Set first name
        set_field("first_name", reg_object['first'])

        # Set last name
        set_field("last_name", reg_object['last'])

        if reg_object['employee']:
            set_field("employee_id", reg_object['employee'])

        # Set day
        set_field("day", reg_object['dd'])

        # Set month
        set_field("month", reg_object['mm'])

        # Set year
        set_field("year", reg_object['yyyy'])

        if 'address line 1' in str(reg_object):
            self._wait_until_visible(
                self.lookup['enter_address_manually'].locator,
                self.lookup['enter_address_manually'].locator_type
            ).click()
            set_field("address_line_1", reg_object['address line 1'])
            set_field("address_line_2", reg_object['address line 2'])
            set_field("city", reg_object['city'])
            set_field("post_code", reg_object['postcode'])
        else:
            # Set postcode
                 set_field("postcode", reg_object['postcode'])

                # Address search
                 self._wait_until_visible(
                 self.lookup['postcode_button'].locator,
                 self.lookup['postcode_button'].locator_type
                ).click()

                #temp fix while I find a better solution
                 self._wait_for_ajax()
                 time.sleep(3)
                # Select Address

                 self._wait_until_visible(
                 self.lookup['first_address_result'].locator,
                 self.lookup['first_address_result'].locator_type
                ).click()

                #temp fix while I find a better solution
                 self._wait_for_ajax()
                 time.sleep(3)

        # Set Email
        set_field("email", reg_object["email"])
        print("!!!!!!!!!!!!!!!!!!!!!  created email is  "+reg_object["email"])
        
        # Set Confirm Email
        set_field("confirm_email", reg_object["email"])

        # Set Password
        set_field("password", reg_object["password"])

        # Set confirm password
        set_field("confirm_password", reg_object["password"])

    def register_employee_no_address(self, reg_object):

        def set_field(selector, keys):
            self._wait_until_visible(
                self.lookup[selector].locator,
                self.lookup[selector].locator_type
            ).send_keys(keys)

        # Set title
        self._select_option_by_value(
            self.lookup['member_title'].locator,
            value=reg_object['title']
        )

        # Set first name
        set_field("first_name", reg_object['first'])

        # Set last name
        set_field("last_name", reg_object['last'])

        # Set employee
        set_field("employee_id", reg_object['employee'])

        # Set day
        set_field("day", reg_object['dd'])

        # Set month
        set_field("month", reg_object['mm'])

        # Set year
        set_field("year", reg_object['yyyy'])

        self._wait_for_ajax()
        time.sleep(3)

        # Set Email
        set_field("email", reg_object["email"])

        # Set Confirm Email
        set_field("confirm_email", reg_object["email"])

        # Set Password
        set_field("password", reg_object["password"])

        # Set confirm_Password
        set_field("confirm_password", reg_object["password"])

    def create_account(self):

        self._wait_until_visible(
            self.lookup['create_account'].locator,
            self.lookup['create_account'].locator_type
        ).click()

    def prove_identity(self, day, month, year):
        def set_field(selector, keys):
            self._wait_until_visible(
                self.lookup[selector].locator,
                self.lookup[selector].locator_type
            ).send_keys(keys)
        # Set day
        set_field("day", [day])

        # Set month
        set_field("month", [month])

        # Set year
        set_field("year", [year])
        self._wait_until_visible(
            self.lookup['continue_button'].locator,
            self.lookup['continue_button'].locator_type
        ).click()


    def enter_payment_details(self, card_number, mm, yy, cvv ):

        def set_card_no(value):

            # select_by_Card = self._wait_until_visible(
            #     self.lookup['card_option'].locator,
            #     self.lookup['card_option'].locator_type,
            #     wait_time=10
            #
            # )

            # Added to wait for page to settle down after display - can click select "by card" too soon
            time.sleep(2)
            # select_by_Card.click()

            time.sleep(3)
            card_frame = self._wait_until_visible(
                self.lookup['card_number_iframe'].locator,
                self.lookup['card_number_iframe'].locator_type
            )

            self._driver.switch_to.frame(card_frame)
            time.sleep(3)
            self._wait_until_visible(
                self.lookup['card_number'].locator,
                self.lookup['card_number'].locator_type
            ).send_keys(value)

        def set_field(selector, value):
            self._driver.switch_to.default_content()
            time.sleep(2)
            element = self._wait_until_visible(
                self.lookup[selector].locator,
                self.lookup[selector].locator_type
            )


            element.send_keys(value)

        def set_cvv(value):
            cvv_frame = self._wait_until_visible(
                self.lookup['cvv_frame'].locator,
                self.lookup['cvv_frame'].locator_type
            )

            self._driver.switch_to.frame(cvv_frame)

            self._wait_until_visible(
                self.lookup['card_number'].locator,
                self.lookup['card_number'].locator_type
            ).send_keys(value)

        # Set Card Number
        set_card_no(card_number)
        # Set expiry MM
        set_field("card_month", mm)
        # Set Expiry YY
        set_field("card_year", yy)
        # Set CVV
        set_cvv(cvv)

        self._driver.switch_to.default_content()
        time.sleep(3)
        self._wait_until_visible(
            self.lookup['submit_payment'].locator,
            self.lookup['submit_payment'].locator_type
        ).click()

    def get_success_message(self):
        return self._wait_until_visible(
            self.lookup['success_message'].locator,
            self.lookup['success_message'].locator_type
        ).text

    def get_membership_card_number(self):
        return self._wait_until_visible(
            self.lookup['membership_card_number'].locator,
            self.lookup['membership_card_number'].locator_type
        ).text

    def check_reg_error_message(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['reg_error_message'].locator,
                self.lookup['reg_error_message'].locator_type
            )
            return True
        except:
            return False

    def error_at_failed_identity(self):

        try:
            self._wait_until_visible(
                self.lookup['error_at_failed_identity'].locator,
                self.lookup['error_at_failed_identity'].locator_type
            )
            return True
        except:
            return False

    def fill_link_account_fields(self, card_no, firstname, lastname, dd, mm, yyyy):

        def fill_field(lookup, text):
            self._wait_until_visible(
                self.lookup[lookup].locator,
                self.lookup[lookup].locator_type
            ).send_keys(text)

        fill_field("link_first_name_field", firstname)
        fill_field("link_last_name_field", lastname)
        fill_field("link_dd_field", dd)
        fill_field("link_mm_field", mm)
        fill_field("link_yyyy_field", yyyy)

    def click_link_account(self):

        self._wait_until_visible(
            self.lookup["link_account_button"].locator,
            self.lookup["link_account_button"].locator_type
        ).click()

    def add_linked_username_and_pass(self, email, password):

        def fill_field(lookup, text):
            self._wait_until_visible(
                self.lookup[lookup].locator,
                self.lookup[lookup].locator_type
            ).send_keys(text)

        link_account_email = self._wait_until_visible(
            self.lookup['link_account_email'].locator,
            self.lookup['link_account_email'].locator_type
        )

        link_account_email.clear()

        fill_field("link_account_email", email)
        fill_field("confirm_account_email", email)
        fill_field("link_account_password", password)
        fill_field("link_account_confirm_password", password)

        self._wait_until_visible(
            self.lookup['link_account_submit_credentials'].locator,
            self.lookup['link_account_submit_credentials'].locator_type
        ).click()

    def check_underage_message(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['age_error'].locator,
                self.lookup['age_error'].locator_type
            )
            return True
        except:
            return False

    def check_for_address_errors(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['address_1_error'].locator,
                self.lookup['address_1_error'].locator_type
            )
            return True
        except:
            return False


    def check_year_error(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['year_error'].locator,
                self.lookup['year_error'].locator_type
            )
            return True
        except:
            return False

    def select_no_key_fob(self):
        no_fob=self._wait_until_visible(
            self.lookup['no_key_fob'].locator,
            self.lookup['no_key_fob'].locator_type
        )
        no_fob.click()
        next_button=self._wait_until_visible(
            self.lookup['verify_card_button'].locator,
            self.lookup['verify_card_button'].locator_type
        )
        next_button.click()

    def select_yes_key_fob(self):
        yes_fob = self._wait_until_visible(
            self.lookup['yes_key_fob'].locator,
            self.lookup['yes_key_fob'].locator_type
        )
        yes_fob.click()

    def enter_membership_card_number(self, temp_card):
        card_number_field = self._wait_until_visible(
            self.lookup['card_number_field'].locator,
            self.lookup['card_number_field'].locator_type
        )
        card_number_field.send_keys(temp_card)


    def check_email_error(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
                self.lookup['email_error'].locator,
                self.lookup['email_error'].locator_type
            )
            return True
        except:
            return False

    def log_out(self):

        self._wait_for_ajax()
        self._wait_until_visible(
            self.lookup['log_out'].locator,
            self.lookup['log_out'].locator_type
        ).click()
        time.sleep(15)

    def goto_linked_account_page(self):
        self._wait_until_visible(
            self.lookup['yes_button_at_linked_account'].locator,
            self.lookup['yes_button_at_linked_account'].locator_type
        ).click()


    def fill_email(self, email):

        self._wait_until_visible(
            self.lookup['username_field'].locator,
            self.lookup['username_field'].locator_type
        ).send_keys(email)

        self._wait_until_clickable(
            self.lookup['verify_email_button'].locator,
            self.lookup['verify_email_button'].locator_type
        ).click()

        self._wait_for_ajax()

    def fill_card_no(self, card_no):

        self._wait_until_visible(
            self.lookup['initial_card_number'].locator,
            self.lookup['initial_card_number'].locator_type
        ).send_keys(card_no)

        self._wait_until_clickable(
            self.lookup['verify_card_button'].locator,
            self.lookup['verify_card_button'].locator_type
        ).click()

    def random_word(self):
       return ''.join(random.choice(string.lowercase) for i in range(11))