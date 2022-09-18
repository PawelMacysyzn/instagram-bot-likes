# project in Selenium

import msvcrt
from selenium import webdriver
from time import sleep
url_insta = 'https://www.instagram.com/'
url_insta_log = 'https://www.instagram.com/accounts/login/?'
url_google = 'https://www.google.com/'


# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url_insta_log)

# if msvcrt.getch()[0] == 27:
#     print('End')
sleep(5)
