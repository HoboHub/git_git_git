from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    x = browser.find_element(By.ID, 'input_value').text

    print(x)

    res = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")

    # скролим на нужное кол-во пикселей
    browser.execute_script("window.scrollBy(0, 200);")

    #     
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # 

    browser.find_element(By.ID, 'answer').send_keys(res)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    button.click()

finally:
    time.sleep(15)
    browser.quit()
