import time

from selenium.common.exceptions import TimeoutException

from Python_automation.page_objects.base import BasePageObject

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import ConfigParser

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')


class SalesforceDash(BasePageObject):

    def salesforce_login(self):
        self.browser.get(CONFIG.get("SALESFORCE_URL", "url"))


        user = CONFIG.get("SALESFORCE_LOGIN", "user")
        password = CONFIG.get("SALESFORCE_LOGIN", "pass")


        self._wait_until_visible(
            self.lookup['salesforce_username'].locator,
            self.lookup['salesforce_username'].locator_type
        ).send_keys(user)

        self._wait_until_visible(
            self.lookup['salesforce_password'].locator,
            self.lookup['salesforce_password'].locator_type
        ).send_keys(password)

        self._wait_until_clickable(
            self.lookup['salesforce_login'].locator,
            self.lookup['salesforce_login'].locator_type
        ).click()

        self._wait_until_clickable(
            self.lookup['tab_menu'].locator,
            self.lookup['tab_menu'].locator_type,
            wait_time=60
        ).click()

        try:
            self._wait_until_clickable(
                self.lookup['close_primary_tabs'].locator,
                self.lookup['close_primary_tabs'].locator_type
            ).click()
        except TimeoutException:
            pass



    def salesforce_search_by_card_no(self, card_no):

        self._wait_until_visible(
            self.lookup['search_button'].locator,
            self.lookup['search_button'].locator_type
        ).click()

        self._driver.switch_to.frame("ext-comp-1005")

        print(self.lookup['salesforce_input_contains'].locator.format("cardNumber"))

        self._wait_until_visible(
            self.lookup['salesforce_input_contains'].locator.format("cardNumber"),
            self.lookup['salesforce_input_contains'].locator_type
        ).send_keys(card_no)

        self._wait_until_visible(
            self.lookup['salesforce_submit_search'].locator,
            self.lookup['salesforce_submit_search'].locator_type
        ).click()


    def click_edit_button_in_update(self):
        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])

            try:

                first_field = self._wait_until_clickable(
                    self.lookup['edit_button_in_change_contact'].locator,
                    self.lookup['edit_button_in_change_contact'].locator_type,
                    wait_time=2
                ).click()

                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue

    def select_member(self):

        self._wait_until_visible(
            self.lookup['search_result_radio'].locator,
            self.lookup['search_result_radio'].locator_type
        ).click()

        self._wait_until_visible(
            self.lookup['go_to_member'].locator,
            self.lookup['go_to_member'].locator_type
        ).click()

        # self._wait_for_ajax()


    def click_action_button_by_value(self, action):

        self._wait_for_ajax()
        time.sleep(10)

        self._driver.switch_to.default_content()

        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            try:
                self._driver.switch_to.frame(iframes[i])

                buttons = self._driver.find_elements_by_css_selector(".btn")

                values = [j.get_attribute('value') for j in buttons]

                if action in values:

                    self._wait_until_visible(
                        self.lookup['action_button'].locator.format(action),
                        self.lookup['action_button'].locator_type
                    ).click()
                    self._driver.switch_to.default_content()
                else:
                    self._driver.switch_to.default_content()
                    continue

                time.sleep(10)


                break
            except TimeoutException as e:
                print(str(e))
                self._driver.switch_to.default_content()
                continue

    def edit_contact_type_by_value(self, value, new_value):

        self._driver.switch_to.default_content()

        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):

            self._driver.switch_to.frame(iframes[i])

            inputs = self._driver.find_elements_by_css_selector("input")

            values = [j.get_attribute('value') for j in inputs]

            if "Edit" in values:

                try:
                    self._wait_until_visible(
                        self.lookup['edit_contact_button'].locator.format(value),
                        self.lookup['edit_contact_button'].locator_type
                    ).click()

                    break
                except TimeoutException as e:
                    print(str(e))
                    self._driver.switch_to.default_content()
                    continue

            else:

                self._driver.switch_to.default_content()
                continue

        field = self._wait_until_clickable(
            self.lookup['contact_value'].locator,
            self.lookup['contact_value'].locator_type
        )

        field.clear()
        field.send_keys(new_value)

    def click_update_contact(self):

        self._wait_until_clickable(
            self.lookup['update_contact'].locator,
            self.lookup['update_contact'].locator_type
        ).click()

    def click_confirm_contact(self):
        time.sleep(5)
        self._wait_until_clickable(
            self.lookup['confirm_contact_update'].locator,
            self.lookup['confirm_contact_update'].locator_type
        ).click()

    # print("UNder development")

    def click_update_button_for_cause(self):
        self._wait_until_clickable(
           self.lookup['update_cause_contribution_button'].locator,
           self.lookup['update_cause_contribution_button'].locator_type
          ).click()

    def click_radio_button(self):
        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])

            try:

                self._wait_until_clickable(
                    self.lookup['radio_button_at_update_cause_contribution'].locator,
                    self.lookup['radio_button_at_update_cause_contribution'].locator_type
                ).click()

                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue


    def complete_contact_case(self, case_reason, gen_reason):

        self._select_option_by_value(
            self.lookup['case_reason'].locator,
            case_reason
        )

        self._select_option_by_value(
            self.lookup['what_gen'].locator,
            gen_reason
        )

        self._wait_until_clickable(
            self.lookup['save_case'].locator,
            self.lookup['save_case'].locator_type
        ).click()


    def check_home_tel_no(self):

        # self._driver.switch_to.default_content()

        # self._wait_until_clickable(
        #     self.lookup['detail_tab'].locator,
        #     self.lookup['detail_tab'].locator_type
        # ).click()

        self._driver.refresh()
        self._driver.switch_to.default_content()


        iframes = self._driver.find_elements_by_xpath("//iframe")

        self._driver.switch_to.frame("ext-comp-1015")

        return self._wait_until_visible(
            self.lookup['tel_no_details'].locator,
            self.lookup['tel_no_details'].locator_type,
        ).text

    def enter_dob(self, dob):


        iframes = self._driver.find_elements_by_xpath("//iframe")
        print (iframes)

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])

            inputs = self._driver.find_elements_by_css_selector("input")

            values = [j.get_attribute('class') for j in inputs]
            print(values)

            if "datepicker hasDatepicker" in values:
                date_field = self._wait_until_visible(
                    self.lookup['edit_dob_field'].locator,
                    self.lookup['edit_dob_field'].locator_type
                )
                date_field.clear()
                date_field.send_keys(dob)
                break
            else:
                self._driver.switch_to.default_content()
                continue

    def close_tab(self):
        self._driver.switch_to.default_content()

        self._driver.switch_to.default_content()
        ActionChains(self._driver).move_to_element(
            self._driver.find_element_by_id("ext-gen23").find_element_by_class_name("x-tab-strip-active")).perform()
        self._driver.find_element_by_id("ext-gen23").find_element_by_css_selector("li.x-tab-strip-active a").click()



    def complete_dob_case(self, gen_reason):

        self._select_option_by_value(
            self.lookup['what_gen'].locator,
            gen_reason
        )

        self._wait_until_clickable(
            self.lookup['save_case'].locator,
            self.lookup['save_case'].locator_type
        ).click()

    def check_dob(self):
        self._driver.switch_to.default_content()

        self._wait_until_clickable(
            self.lookup['detail_tab'].locator,
            self.lookup['detail_tab'].locator_type
        ).click()

        self._driver.refresh()

        iframes = self._driver.find_elements_by_xpath("//iframe")

        print([i.get_attribute('id') for i in iframes])



        self._driver.switch_to.frame("ext-comp-1015")

        return self._wait_until_visible(
            self.lookup['dob_details'].locator,
            self.lookup['dob_details'].locator_type,
        ).text

    def update_name(self, first, last):

        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])


            try:

                first_field = self._wait_until_clickable(
                    self.lookup['first_name'].locator,
                    self.lookup['first_name'].locator_type,
                    wait_time=2
                )

                first_field.clear()
                first_field.send_keys(first)

                last_field = self._wait_until_clickable(
                    self.lookup['last_name'].locator,
                    self.lookup['last_name'].locator_type,
                    wait_time=2
                )

                last_field.clear()
                last_field.send_keys(last)

                self._wait_until_clickable(
                    self.lookup['confirm_contact_update'].locator,
                    self.lookup['confirm_contact_update'].locator_type
                ).click()

                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue


    def check_name(self):
        # self._driver.switch_to.default_content()

        # self._wait_until_clickable(
        #     self.lookup['detail_tab'].locator,
        #     self.lookup['detail_tab'].locator_type
        # ).click()

        self._driver.refresh()

        self._driver.switch_to.default_content()

        iframes = self._driver.find_elements_by_xpath("//iframe")


        self._driver.switch_to.frame("ext-comp-1015")

        return self._wait_until_visible(
            self.lookup['name_details'].locator,
            self.lookup['name_details'].locator_type,
        ).text

    def enter_employee_number(self):
        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])

            try:

                first_field = self._wait_until_clickable(
                    self.lookup['employee_number'].locator,
                    self.lookup['employee_number'].locator_type,
                    wait_time=2
                ).send_keys("12345")

                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue

    def enter_email_into_field(self,email_value):

        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])

            try:

                first_field = self._wait_until_clickable(
                    self.lookup['change_email_Value'].locator,
                    self.lookup['change_email_Value'].locator_type,
                    wait_time=2
                )
                first_field.clear()
                first_field.send_keys(email_value)
                time.sleep(2)
                first_fieldx = self._wait_until_clickable(
                    self.lookup['update_email_button'].locator,
                    self.lookup['update_email_button'].locator_type,
                    wait_time=2
                ).click()
                time.sleep(2)
                first_fieldy = self._wait_until_clickable(
                    self.lookup['confirm_contact_update'].locator,
                    self.lookup['confirm_contact_update'].locator_type,
                    wait_time=2
                ).click()
                time.sleep(3)
                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue

    def fill_the_case_form(self,fill_form):
        self._driver.switch_to.default_content()
        iframes = self._driver.find_elements_by_xpath("//iframe")
        time.sleep(10)
        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])
            try:
                # raga=self._driver.find_element_by_xpath(".//label[contains(.,'*Reason')]/following::div[1]")
                # raga.click()
                Select(self._driver.find_element_by_xpath(".//*[@tabindex='1']")).select_by_visible_text("Changed Email")
                def set_field(selector, keys):
                    self._wait_until_visible(
                        self.lookup[selector].locator,
                        self.lookup[selector].locator_type
                    ).send_keys(keys)

                # Set Reason
                self._select_option_by_value(
                    self.lookup['reason_drop_down'].locator,
                    value=fill_form['reason']
                )
                #
                # # Set Status
                # set_field("status_drop_down", fill_form['status'])
                #
                # # Set What Generated the Call
                # set_field("what_generated", fill_form['what_generated_the_call'])
                #
                # # Click Save Address
                #
                # self._wait_until_visible(
                #     self.lookup['save_button'].locator,
                #     self.lookup['save_button'].locator_type
                # ).click()

                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue

    def enter_email_value(self):
        time.sleep(1)
        self._driver.switch_to.default_content()
        iframes = self._driver.find_elements_by_xpath("//iframe")

        for i, val in enumerate(iframes):
            self._driver.switch_to.frame(iframes[i])
            try:

                first_field = self._wait_until_clickable(
                    self.lookup['contact_Method_Value'].locator,
                    self.lookup['contact_Method_Value'].locator_type,
                    wait_time=2
                ).click()

                break
            except TimeoutException:
                self._driver.switch_to.default_content()
                continue

    def click_validate_button(self):
        self._wait_for_ajax()

        self._wait_until_visible(
            self.lookup['validate_button'].locator,
            self.lookup['validate_button'].locator_type
        ).click()

        self._wait_for_ajax()

        return self._wait_until_visible(
            self.lookup['wrong_employee_id_error_message'].locator,
            self.lookup['wrong_employee_id_error_message'].locator_type
        ).text