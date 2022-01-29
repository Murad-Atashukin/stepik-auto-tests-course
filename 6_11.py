from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.by import By
import time
from math import *

def calc(x):
    return log(abs(12 * sin(x)))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser, 12).until(
    ex.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book").click()
    x_element = int(browser.find_element_by_id("input_value").text)

    _calc = calc(x_element)
    input2 = browser.find_element_by_id("answer").send_keys(str(_calc))
    button1 = browser.find_element_by_id("solve").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
