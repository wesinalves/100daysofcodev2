# Python Journey - Chapter 22
# Filling google form login

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://gmail.com")
email_elem = browser.find_element_by_name('identifier')
email_elem.send_keys('not_my_real_email@gmail.com')
button = browser.find_element_by_id('identifierNext')
button.send_keys(Keys.ENTER)

time.sleep(2)

passwd_elem = browser.find_element_by_name('password')
passwd_elem.send_keys('12345')
button = browser.find_element_by_id('passwordNext')
button.send_keys(Keys.ENTER)

