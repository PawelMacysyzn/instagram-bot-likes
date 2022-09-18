# project in Selenium

from selenium import webdriver
from time import sleep
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome('./chromedriver.exe')

chrome_options = webdriver.ChromeOptions('/chromedriver.exe', chrome_options = chrome_options)
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome()


url_insta = 'https://www.instagram.com/'
url_google = 'https://www.google.com/'

browser.get(url_google)
sleep(2)

browser.close()
