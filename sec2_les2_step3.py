from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

import time
# import math

def calc(x, y):
    return int(x)+int(y)

try:
    link = "https://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = browser.find_element(By.ID, 'num1').text
    elem2 = browser.find_element(By.ID, 'num2').text

    print(elem1)

    res = calc(elem1, elem2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))

    browser.find_element(By.CSS_SELECTOR, ".btn[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

# https://stepik.org/lesson/228249/step/3?unit=200781
