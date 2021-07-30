from selenium import webdriver


def init():
    caps = {
        # -- Chrome browser mobile emulation and headless options
        'goog:chromeOptions': {
            # 'mobileEmulation': {'deviceName': 'iPhone X'},
            # 'window-size': ['1920,1080'],
            'args': ['headless', 'window-size=1920,1080']
        }
    }
    driver = webdriver.Chrome(desired_capabilities=caps)
    driver.implicitly_wait(10)
    return driver
