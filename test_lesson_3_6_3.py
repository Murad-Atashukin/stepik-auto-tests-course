from selenium import webdriver
import time
from math import *
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.common.by import By

result = ''
@pytest.fixture(scope = "function")
def browser():
    print("start browser for test")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print('quit browser')
    print(result)

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    global result
    answer = log(int(time.time() - 1.7))
    browser.implicitly_wait(15)
    browser.get(links)
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(str(answer))

    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()

    text_1 = WebDriverWait(browser, 12).until(
    ex.visibility_of_element_located((By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div/div[2]/div/pre'))).text
    try:
        assert 'Correct!' == text_1, 'Error'
    except AssertionError:
        result += text_1



