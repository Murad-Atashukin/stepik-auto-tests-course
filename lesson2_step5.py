from selenium.webdriver.support.ui import Select
import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str((abs(12*math.sin(int(x)))))
try:
    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    _calc = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(_calc)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    option1 = browser.find_element_by_id("robotCheckbox").click()
    option2 = browser.find_element_by_id("robotsRule").click()
    button1 = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()