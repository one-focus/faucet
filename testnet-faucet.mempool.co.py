import sys

from selenium import webdriver
import urllib.request

import captcha


def get_captcha_image():
    img = driver.find_element_by_xpath('//form[@class="form-validation"]//img')
    src = img.get_attribute('src')
    urllib.request.urlretrieve(src, "captcha.jpg")


if __name__ == "__main__":
    address = sys.argv[1]
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://testnet-faucet.mempool.co/')
    errors = []
    for i in range(5):
        get_captcha_image()
        driver.find_element_by_id('taddress').send_keys(address)
        driver.find_element_by_id('captcha').send_keys(captcha.get_code("captcha.jpg").lower())
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        status = driver.find_element_by_xpath('//div[@class="form-title-row"]').text
        if 'Transaction sent' in status:
            break
        else:
            errors.append(status)
            driver.refresh()
    else:
        raise RuntimeError(f'Errors found:{errors}')
    driver.close()
