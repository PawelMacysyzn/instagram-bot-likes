from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep


url_google = 'https://www.google.com/'
url_twitter = 'https://www.twitter.com/hashtag/python?f=live'


driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url_twitter)


posts_loaded = expected_conditions.presence_of_element_located((By.TAG_NAME, 'article'))




sleep(5)
