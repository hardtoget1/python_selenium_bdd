"""
Please import all the lookups and expose them
using `__all__`.
"""
from .dashboard import DASHBOARD_LOOKUP
from .login_page import LOGIN_PAGE_LOOKUP
from .registration import REGISTRATION_PAGE_LOOKUP

__all__ = [
    'LOGIN_PAGE_LOOKUP',
    'DASHBOARD_LOOKUP',
    'REGISTRATION_PAGE_LOOKUP'
]
