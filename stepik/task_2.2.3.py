import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
        #return str(math.log(abs(12*math.sin(int(x)))))
        return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
try:
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Ivanov")
    browser.find_element(By.NAME, "lastname").send_keys("Ivan")
    browser.find_element(By.NAME, "email").send_keys("Ivan@gog.dog")
    browser.find_element(By.NAME, "file").send_keys("C:\\_git_education\\Python\\file.txt")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)
finally:
    browser.quit()