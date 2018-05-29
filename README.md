# selenium-python

from selenium.webdriver.chrome.options import Options

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
