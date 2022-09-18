import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get (link)
    time.sleep(2)
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x)) # Находим по ID инпут и вводим в него значение, которое вернула функция
    browser.find_element(By.ID, "robotCheckbox").click() # Находим чек-бокс по ID и кликаем по нему
    browser.find_element(By.ID, "robotsRule").click() # Находим радиобаттон по ID и кликаем по нему
    browser.find_element(By.CSS_SELECTOR, "[type=\"submit\"]").click() # Находим кнопку по атрибуту и кликаем по нему

    time.sleep(10)
finally:
    browser.quit()