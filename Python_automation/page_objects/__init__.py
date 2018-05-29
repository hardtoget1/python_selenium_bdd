"""
We want the imports to be as simple as possible. That's why we are
collecting all the objects which can be interacted with from
ther outside world specifically here.

Please import all the PageObject derivatives using a relative import
and expose them using `__all__`.
"""
from .dashboard import Dashboard
from .login_page import LoginPage
from .registration import  Register
from .salesforce_dash import SalesforceDash

__all__ = [
    'LoginPage',
    'Dashboard',
    'Register',
    'SalesforceDash'
]
