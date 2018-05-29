"""
Lookup for AdminSubnav page object. change
"""
from .base import Locator


LOGIN_PAGE_LOOKUP = {
    "username_field": Locator("id", "verify-member-email"),
    "password_field": Locator("id", "member-password"),
    "sign_in_button": Locator("xpath", "//button[@name='sign-in']"),
    "verify_email_button": Locator("css selector", ".verify-email-button"),
    "register_link": Locator("link text", "Not a member?"),
    "account_settings": Locator("css selector", "#view-member-details-button"),
    "forgotten_password": Locator("css selector", "#forgotten-password-button"),
    "forgotten_password_email": Locator("css selector", "#member-email"),
    "forgotten_password_submit": Locator("css selector", ".btn-primary.send-reset-link"),
    "reset_success_message": Locator("css selector", ".message-success"),
    "reset_error_message": Locator("css selector", "#parsley-id-5 > li"),
    "invalid_credentials": Locator("css selector", ".sign-in-js-errors"),
    "member_greeting": Locator("css selector", ".membership-information__greeting"),
    "email": Locator("css selector", "#member-email"),
    "password": Locator("css selector", "#member-password"),
    "new_password": Locator("xpath", "//*[@id='member-new-password']"),
    "confirm_password": Locator("xpath", "//*[@id='member-confirm-password']"),
    "save_password": Locator("xpath", "//*[@id='reset-password-form']/button")


}
