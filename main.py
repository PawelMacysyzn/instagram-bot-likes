# project in Selenium

import guarded_file  # file with login and password
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def options_chrome():
    'Selects an option for chrome'
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


def login_to_insta(driver, verbose: str = ''):
    '''
     # Login to Insta # 
     * verbose:  for verbose == ('--verbose' or '-v') show execution time 
    '''
    username_box = (By.NAME, "username")
    # wait_to_load username box
    wait_to_load_element_by_locator(
        driver, username_box, 5, verbose)
    # finds the username box
    login = driver.find_element(*username_box)
    # send entered username
    login.send_keys(guarded_file.login)

    # wait_to_load password box
    password_box = (By.NAME, "password")
    wait_to_load_element_by_locator(
        driver, password_box, 5, verbose)
    # finds the password box
    password = driver.find_element(*password_box)
    # send entered username
    password.send_keys(guarded_file.password)

    # wait_to_load login buton
    login_buton_by_CSS_SELECTOR = (
        By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')
    login_buton_by_XPATH = (
        By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div')
    login_buton = login_buton_by_CSS_SELECTOR
    wait_to_load_element_by_locator(
        driver, login_buton, 15, verbose)
    # press login buton
    click_buton(driver, login_buton)


def wait_to_load_element_by_locator(driver, locator_and_element: tuple, time_to_load: int = 10, verbose: str = ''):
    '''
     # Wait for element # 
     * driver
     * locator: tuple 
        * (By.XPATH, "xpath")  e.g. (By.XPATH, "/html/body/div[4]/div/div/button[1]")
        * (By.NAME, "name")    e.g. (By.NAME, "username")
        * (By.CLASS_NAME, "class name")
     * time_to_load: by default 10 sek
     * verbose:  for verbose == ('--verbose' or '-v') show execution time 
    '''
    try:
        start = time()
        WebDriverWait(driver, time_to_load).until(
            EC.presence_of_element_located(locator_and_element))
        stop = time()
    except TimeoutException:
        print("\n--- Loading took too much time! By.{}---\n".format(locator_and_element))
    else:
        if (verbose == '--verbose') or (verbose == '-v'):
            print('--- elemet BY.{} = "{}" is ready! (in: {} sec) ---'.format(
                locator_and_element[0].upper(), locator_and_element[1], stop-start))
        else:
            pass


def click_buton(driver, locator_and_element: tuple):
    '''
    # Click buton
        * locator: tuple 
            * (By.XPATH, "xpath")  e.g. (By.XPATH, "/html/body/div[4]/div/div/button[1]")
            * (By.NAME, "name")    e.g. (By.NAME, "username")
            * (By.CLASS_NAME, "class name")
    '''
    try:
        driver.find_element(*locator_and_element).click()
    except Exception:
        print('>>> Something went wrong <<<')


###  pop-up windows ###

def turn_on_notifications(driver, option: str = 'NO'):
    '''
    option: str
    * 'NO' <default>
    * 'YES'
    '''
    XPATH_buton_yes = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]'
    XPATH_buton_no = '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'

    buton_yes = XPATH_buton_yes
    buton_no = XPATH_buton_no

    if option.upper() == 'NO':
        wait_to_load_element_by_locator(driver, (By.XPATH, buton_no))
        click_buton(driver, (By.XPATH, buton_no))

    elif option.upper() == 'YES':
        wait_to_load_element_by_locator(driver, (By.XPATH, buton_yes))
        click_buton(driver, (By.XPATH, buton_yes))
    else:
        raise "Bad choice!"


def allow_the_use_of_cookies_from_instagram_on_this_browser(driver, option: str = 'NO'):
    '''
    option: str
    * 'NO' <default>
    * 'YES'
    '''
    XPATH_buton_yes = '/html/body/div[4]/div/div/button[1]'
    XPATH_buton_no = '/html/body/div[4]/div/div/button[2]'

    buton_yes = XPATH_buton_yes
    buton_no = XPATH_buton_no

    if option.upper() == 'NO':
        wait_to_load_element_by_locator(driver, (By.XPATH, buton_no))
        click_buton(driver, (By.XPATH, buton_no))

    elif option.upper() == 'YES':
        wait_to_load_element_by_locator(driver, (By.XPATH, buton_yes))
        click_buton(driver, (By.XPATH, buton_yes))
    else:
        raise "Bad choice!"


def save_your_login_info(driver, option: str = 'NO'):
    '''
    option: str
    * 'NO' <default>
    * 'YES'
    '''
    buton_yes = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button'
    buton_no = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button'

    if option.upper() == 'NO':
        wait_to_load_element_by_locator(driver, (By.XPATH, buton_no))
        click_buton(driver, (By.XPATH, buton_no))
    elif option.upper() == 'YES':
        wait_to_load_element_by_locator(driver, (By.XPATH, buton_yes))
        click_buton(driver, (By.XPATH, buton_yes))
    else:
        raise "Bad choice!"

########################


url_google = 'https://www.google.com/'
url_insta = 'https://www.instagram.com/'
url_insta_log = 'https://www.instagram.com/accounts/login/?'


driver = webdriver.Chrome(chrome_options=options_chrome())

### OPEN PAGE ###
driver.get(url_insta_log)

allow_the_use_of_cookies_from_instagram_on_this_browser(driver)


login_to_insta(driver)


save_your_login_info(driver)


turn_on_notifications(driver)


### END ###
sleep(5)
