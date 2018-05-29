"""
Main module with tests.

The structure:

* features/
    * feat1.feature
    * feat2.feature
* steps/
    * actions.py
    * feat1.py
    * feat2.py
* environment.py

Where:

* feat1.feature, feat2.feature - feature files
* feat1.py, feat2.py - step files
* actions.py - shared actions, usually common combinations of calls to
    page objects
* environment.py - main behave context initialization and pre and post
    actions for suite, scenarios, tags and steps
"""
