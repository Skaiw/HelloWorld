import time

import pdoc as pdoc
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://wikipedia.org')
driver.find_element(By.NAME, "search").send_keys("Python", Keys.ENTER)

time.sleep(50)