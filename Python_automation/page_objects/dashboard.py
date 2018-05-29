import re
import time
import ConfigParser
import json
import requests
from requests.auth import HTTPBasicAuth

from Python_automation.page_objects.base import BasePageObject

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')

class Dashboard(BasePageObject):

    member_card_number = None

    def go_to_account_settings(self):

        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['account_settings'].locator,
            self.lookup['account_settings'].locator_type
        )

        self._wait_until_clickable(
            self.lookup['account_settings'].locator,
            self.lookup['account_settings'].locator_type
        ).click()

    def edit_password(self, old_pass, new_pass):

        self._wait_until_clickable(
            self.lookup['edit_password'].locator,
            self.lookup['edit_password'].locator_type
        ).click()
        time.sleep(2)

        old_pass_field = self._wait_until_visible(
            self.lookup['old_pass_field'].locator,
            self.lookup['old_pass_field'].locator_type
        )

        old_pass_field.clear()
        old_pass_field.send_keys(old_pass)

        self._wait_until_visible(
            self.lookup['new_pass_field'].locator,
            self.lookup['new_pass_field'].locator_type
        ).send_keys(new_pass)

        self._wait_until_visible(
            self.lookup['confirm_pass_field'].locator,
            self.lookup['confirm_pass_field'].locator_type
        ).send_keys(new_pass)
        time.sleep(2)

        self._wait_until_visible(
            self.lookup['submit_new_password'].locator,
            self.lookup['submit_new_password'].locator_type
        ).click()
        time.sleep(2)

    def change_name(self, first_name, last_name):

        first_name_field = self._wait_until_visible(
            self.lookup['member_firstname'].locator,
            self.lookup['member_firstname'].locator_type
        )

        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self._wait_until_visible(
            self.lookup['member_lastname'].locator,
            self.lookup['member_lastname'].locator_type
        )

        last_name_field.clear()
        last_name_field.send_keys(last_name)

        self._wait_until_visible(
            self.lookup['submit_new_details'].locator,
            self.lookup['submit_new_details'].locator_type
        ).click()

    def get_card_number(self):
        self._wait_for_ajax()
        card_number=self._wait_until_visible(
                self.lookup['card_number'].locator,
                self.lookup['card_number'].locator_type
            ).text
        return card_number

    def check_update_success(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
            self.lookup['update_success'].locator,
            self.lookup['update_success'].locator_type
            )
            return True
        except:
            return False

    def check_register_success_message(self):

        self._wait_for_ajax()

        try:
            self._wait_until_visible(
            self.lookup['register_success_message'].locator,
            self.lookup['register_success_message'].locator_type
            )
            return True
        except:
            return False

    def change_dob(self, day, month, year):


        day_field = self._wait_until_clickable(
            self.lookup['day_field'].locator,
            self.lookup['day_field'].locator_type,
        )

        day_field.clear()
        day_field.send_keys(day)

        month_field = self._wait_until_clickable(
            self.lookup['month_field'].locator,
            self.lookup['month_field'].locator_type,
        )

        month_field.clear()
        month_field.send_keys(month)

        year_field = self._wait_until_clickable(
            self.lookup['year_field'].locator,
            self.lookup['year_field'].locator_type,
        )

        year_field.clear()
        year_field.send_keys(year)

        self._wait_until_visible(
            self.lookup['submit_new_details'].locator,
            self.lookup['submit_new_details'].locator_type
        ).click()

    def edit_email(self, email):

        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['edit_email_link'].locator,
            self.lookup['edit_email_link'].locator_type
        ).click()

        self._wait_for_ajax()

        email_field = self._wait_until_visible(
            self.lookup['email_field'].locator,
            self.lookup['email_field'].locator_type
        )

        email_confirm_field = self._wait_until_visible(
            self.lookup['email_confirm'].locator,
            self.lookup['email_confirm'].locator_type
        )

        self._wait_for_ajax()

        email_field.clear()
        email_field.send_keys(email)
        email_confirm_field.clear()
        email_confirm_field.send_keys(email)

        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['save_email_button'].locator,
            self.lookup['save_email_button'].locator_type
        ).click()

    def get_first_surname(self):
        return self._wait_until_visible(
            self.lookup['first_last_name'].locator,
            self.lookup['first_last_name'].locator_type
        ).text

    def click_marketing_prefs(self, yes=False):
        element_now = self._driver.find_element_by_id("edit-marketing-preferences-link")
        self._driver.execute_script("arguments[0].click();", element_now)
        print("****************************************************************************")

        # self._wait_until_visible(
        #     self.lookup['edit_preferences_link'].locator,
        #     self.lookup['edit_preferences_link'].locator_type
        # ).click()
        # element_now = self._driver.find_element_by_id("edit-marketing-preferences-link")
        # self._driver.execute_script("arguments[0].click();", element_now)

        element_now = self._driver.find_element_by_id("marketing-opt-in-post-label")
        self._driver.execute_script("arguments[0].click();", element_now)


        # self._wait_until_visible(
        #     self.lookup['opt_in_post_button'].locator,
        #     self.lookup['opt_in_post_button'].locator_type
        # ).click()
        element_now = self._driver.find_element_by_id("marketing-opt-in-email-label")
        self._driver.execute_script("arguments[0].click();", element_now)
        #
        # self._wait_until_visible(
        #     self.lookup['opt_in_email_button'].locator,
        #     self.lookup['opt_in_email_button'].locator_type
        # ).click()



       ## if yes:
       ##     self._wait_until_visible(
       ##         self.lookup['yes_pref_but'].locator,
       ##         self.lookup['yes_pref_but'].locator_type
       ##     ).click()

       ## else:
       ##     self._wait_until_visible(
       ##         self.lookup['no_pref_but'].locator,
       ##         self.lookup['no_pref_but'].locator_type
       ##     ).click()

        element_now = self._driver.find_element_by_id("save-marketing-preferences")
        self._driver.execute_script("arguments[0].click();", element_now)




        #
        # self._wait_until_visible(
        #     self.lookup['save_marketing_preferences'].locator,
        #     self.lookup['save_marketing_preferences'].locator_type
        # ).click()



    def click_report_lost_stolen(self):

        self._wait_until_clickable(
            self.lookup['report_lost_stolen'].locator,
            self.lookup['report_lost_stolen'].locator_type
        ).click()

    def click_next_at_order_new_card(self):

        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['next_button_at_order_new_card'].locator,
            self.lookup['next_button_at_order_new_card'].locator_type
        ).click()

    def verify_edit_name_and_Change_address_links(self):
        self._wait_for_ajax()
        self._wait_until_visible(
            self.lookup['edit_your_name_link'].locator,
            self.lookup['edit_your_name_link'].locator_type
        ).is_displayed()

        self._wait_until_visible(
            self.lookup['change_your_address_link'].locator,
            self.lookup['change_your_address_link'].locator_type
        ).is_displayed()


    def click_order_card_button(self):
        self._wait_for_ajax()
        self._wait_until_visible(
            self.lookup['order_card_button'].locator,
            self.lookup['order_card_button'].locator_type
        ).click()
        self._wait_for_ajax()

        return self._wait_until_visible(
            self.lookup['card_message'].locator,
            self.lookup['card_message'].locator_type
        ).text

    def get_replacement_card_number(self):

        self._wait_for_ajax()

        card_text = self._wait_until_visible(
            self.lookup['new_card_message'].locator,
            self.lookup['new_card_message'].locator_type
        ).text

        number = re.search(': (.*)', card_text)


        if number:
            return number.group(1)
        else:
            return False

    def sign_out(self):

        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['logout'].locator,
            self.lookup['logout'].locator_type
        ).click()

    def click_receipt_claim(self):

        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['claim_receipt_link'].locator,
            self.lookup['claim_receipt_link'].locator_type
        ).click()

        self._wait_for_ajax()

    def fill_claim_fields(self, claim_object):

        def fill_field(lookup, text):
            self._wait_until_visible(
                self.lookup[lookup].locator,
                self.lookup[lookup].locator_type
            ).send_keys(text)

            self._wait_for_ajax()

        fill_field("till_no_field", claim_object['till_no'])
        fill_field("store_no_field", claim_object['store_no'])
        fill_field("dd_receipt_field", claim_object['dd'])
        fill_field("mm_receipt_field", claim_object['mm'])
        fill_field("yyyy_receipt_field", claim_object['yyyy'])
        fill_field("txn_receipt_field", claim_object['txn'])

    def retrieve_salesforce_receipt(self):

        username = CONFIG.get("SALESFORCE_WORKBENCH_LOGIN", "user")
        password = CONFIG.get("SALESFORCE_WORKBENCH_LOGIN", "pass")

        def click_element(self, element):
            self._wait_until_visible(
                self.lookup[element].locator,
                self.lookup[element].locator_type
            ).click()

        def send_keys(self, element, keys):
            self._wait_until_visible(
                self.lookup[element].locator,
                self.lookup[element].locator_type
            ).send_keys(keys)

        self.browser.get("https://workbench.developerforce.com/login.php")
        self._select_option_by_value(
            self.lookup['salesforce_env_drop'].locator,
            "test.salesforce.com"
        )


        click_element(self, "salesforce_accept")
        click_element(self, "login_with_salesforce")
        time.sleep(5)
        send_keys(self, "salesforce_user", username)
        send_keys(self, "salesforce_pass", password)
        click_element(self, "salesforce_login_button")
        time.sleep(5)
        self.browser.get("https://workbench.developerforce.com/query.php")
        send_keys(self, "salesforce_query", "SELECT MM_Branch_ID__c, MM_Terminal_ID__c, MM_Transaction_Date__c, MM_Transaction_Number__c FROM MM_99_Transaction__c WHERE MM_Claimed__c = false AND MM_Transaction_Date__c = LAST_N_DAYS:13 AND MM_Branch_ID__c=8215.0")
        click_element(self, "query_submit")
        time.sleep(1)


        def get_table_value(self, index):
            return self._wait_until_visible(
                self.lookup['first_query_row'].locator.format(index),
                self.lookup['first_query_row'].locator_type
            )


        branch_id = get_table_value(self, 2).text[0:4]
        terminal_id = get_table_value(self, 3).text[-1:]
        transact_date = get_table_value(self, 4).text
        transact_no = get_table_value(self, 5).text[11:15]

        dd = transact_date[8:10]
        mm = transact_date[5:7]
        yyyy = transact_date[0:4]

        receipt_object = {
            "store_no": branch_id,
            "till_no": terminal_id,
            "dd": dd,
            "mm": mm,
            "yyyy": yyyy,
            "txn":transact_no
        }

        return receipt_object



    def register_txn(self):

        self._wait_for_ajax()
        self._wait_until_visible(
            self.lookup['submit_txn'].locator,
            self.lookup['submit_txn'].locator_type
        ).click()
        self._wait_for_ajax()

    def get_x_balance(self):

        self._wait_for_ajax()
        return self._wait_until_visible(
            self.lookup['x_balance'].locator,
            self.lookup['x_balance'].locator_type
        ).text

    def check_invalid_date_receipt_message(self):

        self._wait_for_ajax()
        try:
            self._wait_until_visible(
                self.lookup['invalid_date_receipt'].locator,
                self.lookup['invalid_date_receipt'].locator_type
            )
            return True
        except:
            return False

    def get_error_message_befor_15days(self):

        self._wait_for_ajax()
        self._wait_until_visible(
            self.lookup['invalid_date_receipt'].locator,
            self.lookup['invalid_date_receipt'].locator_type
        ).click()
        return self._wait_until_visible(
            self.lookup['invalid_date_receipt'].locator,
            self.lookup['invalid_date_receipt'].locator_type
        ).text

    def is_signout_button_visible(self):

        self._wait_for_ajax()
        try:
            self._wait_until_visible(
                self.lookup['logout'].locator,
                self.lookup['logout'].locator_type
            )
            return True
        except:
            return False

    def is_x_balance_visible(self):

        self._wait_for_ajax()
        try:
            self._wait_until_visible(
                self.lookup['x_balance'].locator,
                self.lookup['x_balance'].locator_type
            )
            return True
        except:
            return False

    def is_y_balance_visible(self):

        self._wait_for_ajax()
        try:
            self._wait_until_visible(
                self.lookup['y_balance'].locator,
                self.lookup['y_balance'].locator_type
            )
            return True
        except:
            return False

    def click_on_change_name_at_update_details(self):

        change_name_field = self._wait_until_visible(
            self.lookup['edit_name_at_update_details'].locator,
            self.lookup['edit_name_at_update_details'].locator_type
        ).click()

    def get_normal_member_card_number(self, context):
        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        card_url = CONFIG.get("GET_NORMAL_MEMBER_CARD", "url")

        card_r = requests.get(url=card_url,
                              auth=HTTPBasicAuth(auth_user, auth_pass))
        context.card_no = str(card_r.json()["membershipCards"][0]['cardNumber'])

    def get_updated_email(self):
        return self._wait_until_visible(
            self.lookup['updated_email'].locator,
            self.lookup['updated_email'].locator_type
        ).text

    def change_address(self, address_object):
        self._wait_until_visible(
            self.lookup['change_your_address_link'].locator,
            self.lookup['change_your_address_link'].locator_type
        ).click()
        self._wait_until_visible(
            self.lookup['enter-address-manually'].locator,
            self.lookup['enter-address-manually'].locator_type
        ).click()

        def set_field(selector, keys):
            self._wait_until_visible(
                self.lookup[selector].locator,
                self.lookup[selector].locator_type
            ).send_keys(keys)

        # Set address first line
        set_field("address_line1", address_object['Address line 1'])
        # Set address second line
        set_field("address_line2", address_object['Address line 2'])
        # Set address city
        set_field("address_city", address_object['City'])
        # Set address postcode
        set_field("address_postcode", address_object['Postcode'])

    def click_save_button(self):

        element_now = self._driver.find_element_by_css_selector("#submit-button")
        self._driver.execute_script("arguments[0].click();", element_now)


    def get_current_address(self):
        return self._wait_until_visible(
            self.lookup['address_text'].locator,
            self.lookup['address_text'].locator_type
        ).text


    def get_member_current_x_balance(self, card_number):
        wallet_balance = CONFIG.get("wallet_balance", "url")+card_number
        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        request = requests.get(url=wallet_balance,
                              auth=HTTPBasicAuth(auth_user, auth_pass))
        print("** Actual status code for wallet_balance =" + str(request.status_code))
        assert request.status_code == 200
        return int(request.json()["card"]['SaveItSpendIt'])


    def adjust_x_balance(self,card_number):
        auth_user = CONFIG.get("SIT AUTH", "user")
        auth_pass = CONFIG.get("SIT AUTH", "pass")
        url = CONFIG.get("adjust_balance", "url").format(card_number)
        adjust_balance = 1
        headers = {'content-type': 'application/json'}
        payload = {
            "AdjustCardBalanceRequest": {
                "MerchantCode": "1234",
                "CardNum": card_number,
                "Pot": [
                    {"Debit": adjust_balance,
                     "IsRefund": True,
                     "CardAcceptorId": "string",
                     "PotName": "SaveItSpendIt"
                     }
                    ]
                }
            }
        r = requests.post(url=url,
                          data=json.dumps(payload),
                          headers=headers,
                          auth=HTTPBasicAuth(auth_user, auth_pass))
        print("** actual status code for adjust_x_balance is "+str(r.status_code))
        assert r.status_code == 200
        return int(adjust_balance)

    def display_causes(self):
        self._wait_until_visible(
            self.lookup['causes_link'].locator,
            self.lookup['causes_link'].locator_type
        ).click()

        self._wait_until_visible(
            self.lookup['local_causes'].locator,
            self.lookup['local_causes'].locator_type
        )

    def view_cause(self):
        self._wait_until_visible(
            self.lookup['current_cause'].locator,
            self.lookup['current_cause'].locator_type
        ).click()


    def select_cause(self):
        self._wait_until_visible(
            self.lookup['change_cause'].locator,
            self.lookup['change_cause'].locator_type,
            ).click()




    def select_new_cause(self):
        self._wait_until_visible(
            self.lookup['select_new_cause'].locator,
            self.lookup['select_new_cause'].locator_type,
            ).click()


    def display_community_causes(self):
        self._wait_until_visible(
            self.lookup['community_causes'].locator,
            self.lookup['community_causes'].locator_type,
            ).click()

    def view_historical_causes(self):
        self._wait_until_visible(
            self.lookup['historical_causes'].locator,
            self.lookup['historical_causes'].locator_type
            ).click()

    def click_home_page(self):
        self._wait_until_visible(
            self.lookup['home_page'].locator,
            self.lookup['home_page'].locator_type,
            ).click()

    def view_historical_contributions(self):
        self._wait_until_visible(
            self.lookup['historical_causes_data'].locator,
            self.lookup['historical_causes_data'].locator_type)

    def view_historical_cause_details(self):
        self._wait_until_visible(
            self.lookup['historical_cause_details'].locator,
            self.lookup['historical_cause_details'].locator_type
        ).click()