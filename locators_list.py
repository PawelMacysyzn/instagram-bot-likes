from selenium.webdriver.common.by import By

class Box_allow_cookies:

        XPATH_buton_yes = (By.XPATH, '/html/body/div[4]/div/div/button[2]')
        XPATH_but_inquiry_en_buton_yes = (By.XPATH, "//button[contains(text(), 'Allow essential and optional cookies')]")
        XPATH_but_inquiry_pl_buton_yes = (By.XPATH, "//button[contains(text(), 'Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie')]")
        CSS_SELECTOR_buton_yes = (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.bIiDR')

        # list of (locator class, element)
        tuple_buton_yes = (XPATH_buton_yes, XPATH_but_inquiry_en_buton_yes, XPATH_but_inquiry_pl_buton_yes, CSS_SELECTOR_buton_yes)

        XPATH_buton_no = (By.XPATH, '/html/body/div[4]/div/div/button[1]')
        XPATH_but_inquiry_en_buton_no = (By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]")
        XPATH_but_inquiry_pl_buton_no = (By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne pliki cookie')]")
        CSS_SELECTOR_buton_no = (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.HoLwm')

        # list of (locator class, element)
        tuple_buton_no = (XPATH_buton_no, XPATH_but_inquiry_en_buton_no, XPATH_but_inquiry_pl_buton_no, CSS_SELECTOR_buton_no)


class Box_allow_cookies_fake:
    
        XPATH_buton_yes = (By.XPATH, '/html/body/div[4]/div/div/button[2]')
        XPATH_but_inquiry_en_buton_yes = (By.XPATH, "//button[contains(text(), 'Allow essential and optional cookies')]")
        XPATH_but_inquiry_pl_buton_yes = (By.XPATH, "//button[contains(text(), 'Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie')]")
        CSS_SELECTOR_buton_yes = (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.bIiDR')

        # list of (locator class, element)
        tuple_buton_yes = (XPATH_buton_yes, XPATH_but_inquiry_en_buton_yes, XPATH_but_inquiry_pl_buton_yes, CSS_SELECTOR_buton_yes)

        XPATH_buton_no = (By.XPATH, '/html/body/div[4]/div/div/button[100]')
        XPATH_but_inquiry_en_buton_no = (By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]")
        XPATH_but_inquiry_pl_buton_no = (By.XPATH, "//button[contains(text(), 'Zezwól tylko na niezbędne plidki cookie')]")
        CSS_SELECTOR_buton_no = (By.CSS_SELECTOR, 'body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOdlW.HoLwm')

        # list of (locator class, element)
        tuple_buton_no = (XPATH_buton_no, XPATH_but_inquiry_en_buton_no, XPATH_but_inquiry_pl_buton_no, CSS_SELECTOR_buton_no)