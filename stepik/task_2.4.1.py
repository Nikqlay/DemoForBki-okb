import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)
    wait = WebDriverWait(browser, 20)
    wait.until(EC.text_to_be_present_in_element ((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
finally:
    browser.quit()