"""
Data transport tuple for locators
"""
from collections import namedtuple


Locator = namedtuple(
    'Locator',
    (
        'locator_type',
        'locator',
    )
)
