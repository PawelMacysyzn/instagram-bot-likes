# project in Selenium

import sys
import guarded_file  # file with login and password
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from url_list import Url
import locators_list
from bcolors import Bcolors as bc


class Bot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(chrome_options=options_chrome())

        ### OPEN PAGE ###
        self.driver.get(Url.url_insta_log)

    def wait_to_load_element_by_locator(self, tuple_of_locator_and_element: tuple, element_name: tuple = ('<NO_NAME>', '<NO_NAME>'), time_to_load: int = 5, verbose: str = '') -> tuple:
        '''
        # Wait for element # 
        <if>:_____find it return tuple (locator class, element)
        <elif>:___keep looking 
        <else>:__return an error
        * locator: tuple(tuple)
                * ((By.XPATH, "xpath"), (By.NAME, "name"))  e.g. ((By.XPATH, "/html/body/div[4]/div/div/button[1]"), (By.NAME, "username"))
        * element_name: tuple
                * ('<NO_NAME>','<NO_NAME>')    # default
        * time_to_load: by default 5 sek
        * verbose:  for verbose == ('--verbose' or '-v') show execution time 
        '''
        try:
            start = time()
            WebDriverWait(self.driver, time_to_load).until(
                EC.presence_of_element_located(tuple_of_locator_and_element[0]))
            stop = time()
        except TimeoutException:
            print(
                "\n{}--- Loading took too much time! ---{}".format(bc.WARNING, bc.ENDC))
            print("function:     {}".format(element_name[0]))
            print("for element:  {}".format(element_name[1]))
            print("list len:     {}".format(len(tuple_of_locator_and_element)))
            print("element:      {}".format(tuple_of_locator_and_element[0]))

            return self.wait_to_load_element_by_locator(
                tuple_of_locator_and_element[0+1:], element_name)

        except IndexError:
            print(
                '\n{}--- No item in the above list was found! ---{}\n'.format(bc.FAIL, bc.ENDC))
            self.driver.close()
            sys.exit()

        else:
            if (verbose == '--verbose') or (verbose == '-v'):
                print(
                    '\n{}--- elemet is ready! (in: {} sec) ---{}'.format(bc.OKGREEN, stop-start, bc.ENDC))
                print("function:     {}".format(element_name[0]))
                print("for element:  {}".format(element_name[1]))
                print("list len:     {}".format(len(tuple_of_locator_and_element)))
                print("element:      {}".format(
                    tuple_of_locator_and_element[0]))
            else:
                pass
            return tuple_of_locator_and_element[0]


    def click_buton(self, locator_and_element: tuple):
        '''
        # Click buton
            * locator: tuple 
                * (By.XPATH, "xpath")  e.g. (By.XPATH, "/html/body/div[4]/div/div/button[1]")
                * (By.NAME, "name")    e.g. (By.NAME, "username")
                * (By.CLASS_NAME, "class name")
        '''
        try:
            self.driver.find_element(*locator_and_element).click()
        except Exception:
            print('\n{}--- Something went wrong ---{}\n'.format(bc.FAIL, bc.ENDC))
            print("for: {}".format(locator_and_element))

    def do_login(self):

        self.box_allow_cookies()

    def box_allow_cookies(self, option: str = 'NO'):
        '''
        option: str
        * 'NO' <default>
        * 'YES'
        '''
        tuple_buton_no = locators_list.Box_allow_cookies.tuple_buton_no
        tuple_buton_yes = locators_list.Box_allow_cookies.tuple_buton_yes

        if option.upper() == 'NO':
            element_name = (self.box_allow_cookies.__name__, 'buton_no')
            element_locator = self.wait_to_load_element_by_locator(
                tuple_buton_no, element_name)
            self.click_buton(element_locator)

        elif option.upper() == 'YES':
            element_name = (self.box_allow_cookies.__name__, 'buton_yes')
            element_locator = self.wait_to_load_element_by_locator(
                tuple_buton_yes, element_name)
            self.click_buton(element_locator)
        else:
            raise "Bad choice!"


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
        driver, username_box, 'username_box', 5, verbose)
    # finds the username box
    login = driver.find_element(*username_box)
    # send entered username
    login.send_keys(guarded_file.login)

    # wait_to_load password box
    password_box = (By.NAME, "password")
    wait_to_load_element_by_locator(
        driver, password_box, 'password_box', 5, verbose)
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
        driver, login_buton, 'login_buton', 15, verbose)
    # press login buton
    click_buton(driver, login_buton)


####  pop-up windows ####

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


def save_your_login_info(driver, option: str = 'NO'):
    '''
    option: str
    * 'NO' <default>
    * 'YES'
    '''
    buton_yes = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button'
    buton_no = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button'

    if option.upper() == 'NO':
        wait_to_load_element_by_locator(
            driver, (By.XPATH, buton_no), 'buton_no')
        click_buton(driver, (By.XPATH, buton_no))
    elif option.upper() == 'YES':
        wait_to_load_element_by_locator(
            driver, (By.XPATH, buton_yes), 'buton_yes')
        click_buton(driver, (By.XPATH, buton_yes))
    else:
        raise "Bad choice!"


def go_to_profile(driver):
    XPATH_buton = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div/div[2]/div[1]/a/div/div[2]/div/div/div/div'
    XPATH_buton = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg'
    XPATH_buton = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div[2]/div[6]/div[1]/span/img[1]'
    CSS_SELECTOR_buton = '#f34553ebeaf9ff4 > div > div > div'
    wait_to_load_element_by_locator(
        driver, (By.XPATH, XPATH_buton), (go_to_profile.__name__, 'go_to_profile_buton'), 1)
    click_buton(driver, (By.XPATH, XPATH_buton))

##########################


# allow_cookies(driver)


# login_to_insta(driver)


# save_your_login_info(driver)


# turn_on_notifications(driver)


# go_to_profile(driver)

def main():

    insta_bot = Bot()

    insta_bot.do_login()

    sleep(5)


if __name__ == '__main__':
    main()
