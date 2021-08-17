from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    button = browser.find_element_by_id("book")
    expected_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()
    x_element = browser.find_element_by_id("input_value")
    print(type(x_element))
    x_text = x_element.text
    y = calc(x_text)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])

finally:

    browser.quit()
