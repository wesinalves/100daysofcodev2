# Python Journey - Chapter 23
# Instagram bot for automating

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
    
    def closeBrowser(self):
        self.driver.close()

if __name__ == "__main__":
    user_name = "wesinalves"
    password = "n@bucodonosor7"

    ig = InstagramBot(user_name, password)
    ig.login()