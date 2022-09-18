from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
try:
    driver = webdriver.Chrome()
    driver.get(link)
    x = driver.find_element(By.ID, 'num1').text
    y = driver.find_element(By.ID, 'num2').text
    z = (int(x)+int(y))
    print(z)
    Select(driver.find_element(By.ID, 'dropdown')).select_by_visible_text(str(z))
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    time.sleep(10)
finally:
    browser.quit()