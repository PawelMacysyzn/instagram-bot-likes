from selenium.webdriver.common.by import By

class Box_allow_cookies:

        class Buton_yes:

                XPATH = (By.XPATH, '/html/body/div[4]/div/div/button[2]')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'Allow essential and optional cookies')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.bIiDR')

                # list of (locator class, element)
                tuple = (XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)

        class Buton_no:

                XPATH = (By.XPATH, '/html/body/div[4]/div/div/button[1]')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne pliki cookie')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm')

                # list of (locator class, element)
                tuple = (XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)


class Box_Login:

        class Username_box:

                XPATH = (By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
                NAME = (By.NAME, 'username')
                CSS_SELECTOR = (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
                XPATH_but_inquiry_en = (By.XPATH, "//aria-label[contains(text(), 'Phone number, username, or email')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//aria-label[contains(text(), 'Numer telefonu, nazwa użytkownika lub adres e-mail')]")

                # list of (locator class, element)
                tuple = (XPATH, NAME, CSS_SELECTOR, XPATH_but_inquiry_en, XPATH_but_inquiry_pl)


        class Password_box:

                XPATH = (By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
                NAME = (By.NAME, 'password')
                CSS_SELECTOR = (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
                XPATH_but_inquiry_en = (By.XPATH, "//aria-label[contains(text(), 'Password')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//aria-label[contains(text(), 'Hasło')]")

                # list of (locator class, element)
                tuple = (XPATH, NAME, CSS_SELECTOR, XPATH_but_inquiry_en, XPATH_but_inquiry_pl)


        class Login_buton:

                XPATH = (By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')
                CSS_SELECTOR_0 = (By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')
                CSS_SELECTOR_1 = (By.CSS_SELECTOR, 'button[type="submit"]')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'Log In')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Zaloguj się')]")
                XPATH_but_inquiry_pl_0 = (By.XPATH, "//*[contains(text(), 'Zaloguj się')]")
                XPATH_but_inquiry_pl_1 = (By.XPATH, "//*[contains(text(), 'submit')]")

                # list of (locator class, element)
                tuple = (XPATH, CSS_SELECTOR_0, CSS_SELECTOR_1, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, XPATH_but_inquiry_pl_0, XPATH_but_inquiry_pl_1)


class Box_save_login_info:

        class Buton_yes:

                XPATH = (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'Save Info')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Zapisz informacje')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, '#mount_0_0_fV > div > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div > div > div.alzwoclg.cqf1kptm.p1t2w4gn.fawcizw8.om3e55n1.g4tp4svg > section > main > div > div > div > section > div > button')

                # list of (locator class, element)
                tuple = (XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)

        class Buton_no:

                XPATH = (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'button')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Nie teraz')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, '#mount_0_0_fV > div > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div > div > div.alzwoclg.cqf1kptm.p1t2w4gn.fawcizw8.om3e55n1.g4tp4svg > section > main > div > div > div > div > button')

                # list of (locator class, element)
                tuple = (XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)


class Box_notifications:

        class Buton_yes:

                XPATH = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'Turn On')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Włącz')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, '#mount_0_0_RT > div > div > div > div:nth-child(4) > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div.th8rvtx1.f7rl1if4.adechonz.rufpak1n.qtovjlwq.qbmienfq.rfyhaz4c.rdmi1yqr.ohrdq8us.nswx41af.fawcizw8.l1aqi3e3.om3e55n1.sdu1flz4.dahkl6ri > div > div > div > div > div.f0dnt3l3.qrrecgo5.o69pmk6j.rt5af2x2.iriodytt.hw7435fk.ba4ynyj4.mm05nxu8.l2tm8nht > div > div > div._a9-z > button._a9--._a9_0')

                # list of (locator class, element)
                tuple = (XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)

        class Buton_no:

                XPATH = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                XPATH_but_inquiry_en = (By.XPATH, "//button[contains(text(), 'Not Now')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//button[contains(text(), 'Nie teraz')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, '#mount_0_0_RT > div > div > div > div:nth-child(4) > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div.th8rvtx1.f7rl1if4.adechonz.rufpak1n.qtovjlwq.qbmienfq.rfyhaz4c.rdmi1yqr.ohrdq8us.nswx41af.fawcizw8.l1aqi3e3.om3e55n1.sdu1flz4.dahkl6ri > div > div > div > div > div.f0dnt3l3.qrrecgo5.o69pmk6j.rt5af2x2.iriodytt.hw7435fk.ba4ynyj4.mm05nxu8.l2tm8nht > div > div > div._a9-z > button._a9--._a9_1')

                # list of (locator class, element)
                tuple = (XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)


class Go_to_profile:

        class Buton:

                CLASS_NAME_0 = (By.CLASS_NAME, 'qi72231t')
                XPATH = (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div/div[2]/div[1]/a/div/div[2]/div/div/div/div')
                XPATH_but_inquiry_en = (By.XPATH, "//*[contains(text(), 'Profile')]")
                XPATH_but_inquiry_pl = (By.XPATH, "//class[contains(text(), 'Profil')]")
                CSS_SELECTOR = (By.CSS_SELECTOR, '#f2e59e9cef2c99c > div > div > div')
                

                # list of (locator class, element)
                tuple = (CLASS_NAME_0,  XPATH, XPATH_but_inquiry_en, XPATH_but_inquiry_pl, CSS_SELECTOR)


class Get_basic_info:

        CLASS_NAME_0 = (By.CLASS_NAME, '_ac2a')
        CLASS_NAME_1 = (By.CLASS_NAME, '_ac2a')  
        
        # list of (locator class, element)
        tuple = (CLASS_NAME_0, CLASS_NAME_1)