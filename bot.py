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
        self.driver = webdriver.Chrome(chrome_options=self.options_chrome())

        ### OPEN PAGE ###
        self.driver.get(Url.url_insta_log)

    def options_chrome(self):
        'Selects an option for chrome'
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return options

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
                print("list len:     {}".format(
                    len(tuple_of_locator_and_element)))
                print("element:      {}\n".format(
                    tuple_of_locator_and_element[0]))
            else:
                pass
            return tuple_of_locator_and_element[0]

    def click_buton(self, locator_and_element: tuple, element_name: tuple = ('<NO_NAME>', '<NO_NAME>')):
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
            print("function:     {}".format(element_name[0]))
            print("for element:  {}".format(element_name[1]))
            # to do
            self.driver.close()
            sys.exit()

    def do_login(self):

        self.box_allow_cookies()

        self.box_login()

        self.box_save_login_info()

        self.box_notifications()

    def box_allow_cookies(self, option: str = 'NO', time_to_load: int = 5, verbose: str = ''):
        '''
        * option: str
                * 'NO' <default>
                * 'YES'
        * time_to_load: by default 5 sek
        * verbose:  for verbose == ('--verbose' or '-v') show execution time 
        '''
        tuple_buton_no = locators_list.Box_allow_cookies.Buton_no.tuple
        tuple_buton_yes = locators_list.Box_allow_cookies.Buton_yes.tuple

        if option.upper() == 'NO':
            element_name = (self.box_allow_cookies.__name__, 'buton_no')
            element_locator = self.wait_to_load_element_by_locator(
                tuple_buton_no, element_name, time_to_load, verbose)
            self.click_buton(element_locator, element_name)

        elif option.upper() == 'YES':
            element_name = (self.box_allow_cookies.__name__, 'buton_yes')
            element_locator = self.wait_to_load_element_by_locator(
                tuple_buton_no, element_name, time_to_load, verbose)
            self.click_buton(element_locator, element_name)
        else:
            raise "Bad choice!"

    def box_login(self, time_to_load: int = 5, verbose: str = ''):
        '''
        # Login to Insta #
        * time_to_load: by default 5 sek
        * verbose:  for verbose == ('--verbose' or '-v') show execution time 
        '''
        def do_username_box():
            element_name = (self.box_login.__name__, 'username_box')
            tuple_username_box = locators_list.Box_Login.Username_box.tuple
            # wait_to_load username box
            element_locator = self.wait_to_load_element_by_locator(tuple_username_box, element_name, time_to_load, verbose)
            # finds the username box
            login = self.driver.find_element(*element_locator)
            # send entered username
            login.send_keys(guarded_file.login)

        def do_password_box():
            element_name = (self.box_login.__name__, 'password_box')
            tuple_password_box = locators_list.Box_Login.Password_box.tuple
            # wait_to_load password box
            element_locator = self.wait_to_load_element_by_locator(tuple_password_box, element_name, time_to_load, verbose)
            # finds the password box
            password = self.driver.find_element(*element_locator)
            # send entered username
            password.send_keys(guarded_file.password)

        def do_login_buton():
            element_name = (self.box_login.__name__, 'login_buton')
            tuple_login_buton = locators_list.Box_Login.Login_buton.tuple
            # wait_to_load login buton
            element_locator = self.wait_to_load_element_by_locator(tuple_login_buton, element_name, time_to_load, verbose)
            # press login buton
            self.click_buton(element_locator, element_name)

        do_username_box()
        do_password_box()
        do_login_buton()

    def box_save_login_info(self, option: str = 'NO', time_to_load: int = 5, verbose: str = ''):
        '''
        * option: str
                * 'NO' <default>
                * 'YES'
        * time_to_load: by default 5 sek
        * verbose:  for verbose == ('--verbose' or '-v') show execution time 
        '''
        tuple_buton_no = locators_list.Box_save_login_info.Buton_no.tuple
        tuple_buton_yes = locators_list.Box_save_login_info.Buton_yes.tuple

        if option.upper() == 'NO':
            element_name = (self.box_save_login_info.__name__, 'buton_no')
            element_locator = self.wait_to_load_element_by_locator(tuple_buton_no, element_name, time_to_load, verbose)
            self.click_buton(element_locator, element_name)
        elif option.upper() == 'YES':
            element_name = (self.box_save_login_info.__name__, 'buton_yes')
            element_locator = self.wait_to_load_element_by_locator(tuple_buton_yes, element_name, time_to_load, verbose)
            self.click_buton(element_locator, element_name)
        else:
            raise "Bad choice!"

    def box_notifications(self, option: str = 'NO', time_to_load: int = 5, verbose: str = ''):
        '''
        * option: str
                * 'NO' <default>
                * 'YES'
        * time_to_load: by default 5 sek
        * verbose:  for verbose == ('--verbose' or '-v') show execution time               
        '''
        tuple_buton_no = locators_list.Box_notifications.Buton_no.tuple
        tuple_buton_yes = locators_list.Box_notifications.Buton_yes.tuple


        if option.upper() == 'NO':
            element_name = (self.box_notifications.__name__, 'buton_no')
            element_locator = self.wait_to_load_element_by_locator(tuple_buton_no, element_name, time_to_load, verbose)
            self.click_buton(element_locator, element_name)

        elif option.upper() == 'YES':
            element_name = (self.box_notifications.__name__, 'buton_yes')
            element_locator = self.wait_to_load_element_by_locator(tuple_buton_yes, element_name, time_to_load, verbose)
            self.click_buton(element_locator, element_name)
        else:
            raise "Bad choice!"

    def go_to_profile(self):
        self.driver.get(Url.url_insta + '/' + guarded_file.user)

    def get_basic_info(self):

        tuple_element = locators_list.Get_basic_info.tuple
        element_name = (self.get_basic_info.__name__, 'element')

        print(bc.OKGREEN, tuple_element, bc.ENDC)
        element_locator = self.wait_to_load_element_by_locator(tuple_element, element_name)
        x = self.driver.find_elements(*element_locator)
        print(len(x))       




##########################

def main():

    insta_bot = Bot()

    insta_bot.do_login()
    
    insta_bot.go_to_profile()

    insta_bot.get_basic_info()

    sleep(50)


if __name__ == '__main__':
    main()
