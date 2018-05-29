"""
Definition of the environment and actions shared between steps.
"""
import ConfigParser
import os
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import datetime
from selenium.webdriver.chrome.options import Options
from sys import platform

CONFIG = ConfigParser.ConfigParser()
CONFIG.read('../settings.cfg')

REMOTE_DRIVER = os.environ.get('REMOTE_DRIVER', None)


def before_all(context):
    """
    Executes once before all the tests.


    """
    context.test_url = CONFIG.get('SIT', 'sit url')


    context.scenario_dir = None
    context.screenshot_directory = os.environ.get('SCREENSHOT_DIR', None)


def before_scenario(context, scenario):
    """
    Execute before scenario

    :param context: current context
    :param scenario: current scenario

    :type context: behave.runner.Context
    :type scenario: behave.runner.Scenario
    """

    context.browser = _get_browser(headless=True)
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.test_start_time = str(int(time.time()))



def after_step(context, step):
    """
    Executes after each step

    :param context: current context
    :param step: current step

    :type context: behave.runner.Context
    :type step: behave.runner.Step
    """



    _take_screenshot(context, step)


def after_scenario(context, _):
    """
    Execute after scenario

    :param context: current context
    :param scenario: current scenario

    :type context: behave.runner.Context
    :type scenario: behave.runner.Scenario
    """
    context.browser.quit()



def _take_screenshot(context, step):
    """
    Captures a screenshot to the specified path.

    :param context: current context
    :param filename: path to which snapshot will be stored

    :type context: behave.runner.Context
    :type path: string

    :returns: None
    """

    all_steps = list(context.scenario.all_steps)
    filename = context.feature.name + "-Step_" + str(all_steps.index(step) + 1) + ".png"

    location = "./reports/" + filename

    print(location)

    context.browser.save_screenshot(location)
    print("Current url for "+"-Step_" + str(all_steps.index(step) + 1) +" is   " + context.browser.current_url)

    print ("current time is  "+str(datetime.datetime.now()))

def _get_browser(headless):
    if platform == "darwin":
        path_to_chromedriver = '/usr/local/bin/chromedriver'
    else:
        path_to_chromedriver = '/usr/lib/chromium-browser/chromedriver'

    chrome_options = Options()
    if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(path_to_chromedriver,
                                       chrome_options=chrome_options)
    browser.set_window_size(1280, 1696)
    return browser

