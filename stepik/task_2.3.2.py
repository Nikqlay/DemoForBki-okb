import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
finally:
    browser.quit()