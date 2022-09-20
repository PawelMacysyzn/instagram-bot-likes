from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


url_google = 'https://www.google.com/'
url_twitter = 'https://www.twitter.com/hashtag/python?f=live'


driver = webdriver.Chrome()
driver.get(url_twitter)


posts_loaded = expected_conditions.presence_of_element_located((By.TAG_NAME, 'article'))
WebDriverWait(driver, 10).until(posts_loaded)



for enum, post in enumerate(driver.find_elements(By.TAG_NAME, 'article')):
    # print('-'*35)
    # print(enum+1,': ','\n', post.text)
    # post.find_elements(By.CSS_SELECTOR, '[lang="en"]')
    pass

sleep(5)
