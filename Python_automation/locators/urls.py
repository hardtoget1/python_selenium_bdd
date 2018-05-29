"""
URLS lookup

URLS are independent of the page objects and deserve special treatment.
This file collects all the urls sitewide. Please do not define any
urls within other page object lookups.
"""

URLS_LOOKUP = {
    "HomePage": u"/",
    "LoginPage": u"sign-in",
    "LinkedRegister": u"register",
    "Register": u"register",
    "NewRegistration": u"new-registration",
    "ColleagueRegister": u"colleague-registration",
    "Dashboard": u"dashboard"
}
