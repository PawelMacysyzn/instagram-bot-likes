# project in Selenium

import guarded_file
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


url_insta = 'https://www.instagram.com/'
url_insta_log = 'https://www.instagram.com/accounts/login/?'
url_google = 'https://www.google.com/'


# from selenium.webdriver.support import expected_conditions

def chrome_options(options: str):
    'Selekt option for chrome'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(options)
    return chrome_options


def login_insta(time_sleep: int = 2):
    # finds the username box
    login = driver.find_element(By.NAME, "username")
    # send entered username
    login.send_keys(guarded_file.login)
    # finds the password box
    password = driver.find_element(By.NAME, "password")
    # send entered username
    password.send_keys(guarded_file.password)
    # press login buton
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div').click()
    sleep(time_sleep)


def navigation_in_account():
    # Query about login details, clicking the deny button
    driver.find_element(
        By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()


driver = webdriver.Chrome(chrome_options=chrome_options("--incognito"))

### OPEN PAGE ###
driver.get(url_insta_log)


# ### FIRST STEP ####
# wait for permission to use cookies, button

one_XPATH = '/html/body/div[4]/div/div'


try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(By.TAG_NAME, 'presentation'))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
except Exception:
    print ("###Wrong###! "*5)

# # permission to use cookies, button
# driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()

# # Tutaj zamiast sleep(2), trzeba poczekać na zlogowanie okienek do login_insta(2),
# # lub zaimportować odpowienią logikę w login_insta()
# sleep(2)  # to do
# login_insta(2)

# sleep(2)  # to do
# navigation_in_account()


### END ###
sleep(30)
