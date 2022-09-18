
from time import sleep
from selenium import webdriver


url_google = 'https://www.google.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url_google)


sleep(5)
