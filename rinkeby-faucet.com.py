import sys
from time import sleep

import chromedriver
import urllib.request
import telebot

import captcha

if __name__ == "__main__":
    address = sys.argv[1]
    driver = chromedriver.init()
    driver.get(f'http://rinkeby-faucet.com/send?address={address}')
    errors = []
    bot = telebot.TeleBot("1275523107:AAF_5t_r80J55Pl-JcVeLcVVOsl7kadqAc4")
    driver.find_element_by_name('addresssz').send_keys(address)
    sleep(5)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(5)
    status = driver.find_element_by_xpath('//div[@role="alert"]').text
    if 'Congratulations, your address has been added to the queue' in status:
        bot.send_message(chat_id=-407923666, text=f'🟢 {status}')
    else:
        bot.send_message(chat_id=-407923666, text=f"🔴 {status} for {address}")
    driver.close()
