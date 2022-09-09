from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
#construct driver
PATH = Service('/home/emirali/Desktop/chromedriver')
driver = webdriver.Chrome(service=PATH)
url = "http://orteil.dashnet.org/cookieclicker/"
driver.get(url)

driver.implicitly_wait(5)  # wait for load

lang = driver.find_element(By.ID, 'langSelect-EN')
lang.click()

driver.implicitly_wait(5)

cookie = WebDriverWait(driver, 10).until(  # get the big cookie
    EC.presence_of_element_located((By.ID, "bigCookie")))
cookie_count = WebDriverWait(driver, 10).until(  # get cookie count
    EC.presence_of_element_located((By.ID, "cookies")))
items = [
    driver.find_element(By.ID, 'productPrice' + str(i))
    for i in range(1, -1, -1)
]

actions = ActionChains(driver)

for i in range(5000):
    actions.double_click(cookie).perform()

    count = int(cookie_count.text.split(' ')[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()