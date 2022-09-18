import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
        #return str(math.log(abs(12*math.sin(int(x)))))
        return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text

    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "answer"))
    browser.find_element(By.ID, "answer").send_keys(calc(x))

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.XPATH, "//button[@type='submit']"))
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
finally:
    browser.quit()