import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link "http://suninjuly.github.io/get_attribute.html"  

try:
    browser = webdriver.Chrome()
    browser.get (link)
    time.sleep(2)
    x_element = browser.find_element_by_id('treasure')
    x_checked = x_element.get_attribute('valuex')
    x=int(x_checked)
    y = calc(x)
    
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn-default').click()
    
    time.sleep(10)
finally:
    browser.quit()