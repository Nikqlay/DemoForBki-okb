##########################
###Chat_with_Registered###
##########################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
import random
import time
from tkinter import HIDDEN
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

user = ('boroda204@mail.ru')
password = ('rq227703')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
card_num = ('2200200111114591')
card_date = ('0522')
card_cvc = ('426')


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    driver.set_window_size(1920, 1080)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Max.Credit"))
    if True:
        try:
            driver.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)
    if True:
        try:
            driver.find_element(By.LINK_TEXT, "Личный кабинет").click()
        except:
            sleep(0)
    sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    driver.find_element(By.ID, "loginform-login").send_keys(user)
    driver.find_element(By.ID, "loginform-password").send_keys(password)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()#Войти

    sleep(2)
    user_login = driver.find_elements(By.XPATH, '//div//a//span')[0].text
    print(user_login)
    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(-10, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()
    sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div//form//button')))
    driver.find_element(By.XPATH, '//div[contains(@class,"hoverl_6R")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(@class,"consultant-chat")]')))
    print("Ждем")
    driver.find_element(By.CSS_SELECTOR, "#consultant-form > textarea").click()
    driver.find_element(By.CSS_SELECTOR, "#consultant-form > textarea").send_keys("Вас приветствует, " + user_login)
    sleep(2)
    print("Пишем")
    sleep(1)
    driver.find_element(By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]').click()
    print("Отправляем")
#    sleep(3)
#    driver.minimize_window()
#    print("Свернем клиента")

############Работает
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    driver_adm.set_window_size(1920, 1080)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__logo")]')))
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)

    sleep(1)
    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver_adm.find_element(By.ID, "loginform-login").send_keys(str(admin))
    driver_adm.find_element(By.ID, "loginform-password").send_keys(str(pas_adm))
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.XPATH, '//li[contains(@title,"Чаты")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/chat/all")]')))
    driver_adm.find_element(By.XPATH, '//a[contains(@href,"/manager/chat/all")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/chat/view")]')))
    sleep(1)
    driver_adm.find_element(By.LINK_TEXT, user_login).click()
    print("Клик по " + user_login)
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Вас приветствует, " + user_login))
    driver_adm.find_element(By.XPATH, '//i[contains(@class,"glyphicon-lock")]').click()
    sleep(1)
    print("Ждем")
    sleep(1)

    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]')))
    driver_adm.find_element(By.CSS_SELECTOR, "#w0 > textarea").click()
    driver_adm.find_element(By.CSS_SELECTOR, "#w0 > textarea").send_keys(user_login + ", Вас приветствует команда Max.Credit!")

    print("Пишем")
    sleep(3)
    driver_adm.find_element(By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]').click()
    print("Отправляем")
    sleep(3)
    driver_adm.minimize_window()
    print("Свернем админку")
#    sleep(2)

    #driver.maximize_window()
#    print("Развернем клиента")
    driver.execute_script("window.focus();")
    driver.set_window_size(1920, 1080)
    print("Переводим фокус на окно клиента")
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), user_login + ", Вас приветствует команда Max.Credit!"))
    driver_adm.find_element(By.XPATH, '//i[contains(@class,"glyphicon-lock")]').click()
    driver.find_element(By.CSS_SELECTOR, "#consultant-form > textarea").send_keys("Очень замечательно, что чат работает")
    print("Пишем")
    driver.find_element(By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]').click()
    sleep(3)
#    driver.minimize_window()
#    print("Свернем клиента")
#    sleep(2)

    #driver_adm.maximize_window()
#    print("Развернем админку")
    driver_adm.execute_script("window.focus();")
    driver_adm.set_window_size(1920, 1080)
    sleep(2)
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Очень замечательно, что чат работает"))
    driver_adm.find_element(By.XPATH, '//i[contains(@class,"glyphicon-lock")]').click()
    sleep(1)
    print("Ждем")
    sleep(1)
    driver_adm.find_element(By.CSS_SELECTOR, "#w0 > textarea").click()
    driver_adm.find_element(By.CSS_SELECTOR, "#w0 > textarea").send_keys(user_login + ", Чат проверен. Оцените, пожалуйста, нашу работу")
    print("Пишем")
    sleep(3)
    driver_adm.find_element(By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]').click()
    print("Отправляем")
    sleep(3)
    driver_adm.minimize_window()
    print("Свернем админку")
#    sleep(2)

    #driver.maximize_window()
    driver.execute_script("window.focus();")
    print("Развернем клиента")
    driver.set_window_size(1920, 1080)
    sleep(2)
    print("Переводим фокус на окно клиента")
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), ", Чат проверен. Оцените, пожалуйста, нашу работу"))
    driver.find_element(By.CSS_SELECTOR, "#consultant-form > textarea").send_keys("Обязательно!")
    print("Пишем")
    driver.find_element(By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]').click()
    sleep(3)
#    driver.minimize_window()
#    print("Свернем клиента")
#    sleep(2)

    #driver_adm.maximize_window()
    driver_adm.execute_script("window.focus();")
    print("Развернем админку")
    driver_adm.set_window_size(1920, 1080)
    sleep(2)
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Обязательно!"))
    sleep(3)
    driver_adm.find_element(By.XPATH, '//button[contains(@class,"js-send-chat-rate-request")]').click()

    WebDriverWait(driver_adm, 10).until(EC.alert_is_present())
    sleep(1)
    driver_adm.switch_to.alert.accept()
    sleep(1)
    #Клиенту отправлен запрос
    WebDriverWait(driver_adm, 10).until(EC.alert_is_present())
    sleep(1)
    driver_adm.switch_to.alert.accept()
    sleep(1)
    driver_adm.minimize_window()
    print("Свернем админку")

    #driver.maximize_window()
    driver.execute_script("window.focus();")
    print("Развернем клиента")
    driver.set_window_size(1920, 1080)
    sleep(2)
    print("Переводим фокус на окно клиента")
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Довольны ли вы обращением в службу поддержки?"))
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-success")]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//i[contains(@class,"fa fa-paper-plane")]').click()
    sleep(1)
    driver.quit()
    print("Закроем клиента")

    driver_adm.execute_script("window.focus();")
    print("Развернем админку")
    driver_adm.set_window_size(1920, 1080)
    sleep(1)
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Оценка чата: Хорошо"))
    sleep(2)
    driver_adm.find_element(By.XPATH, '//a[contains(@href,"/auth/logout")]').click()
    sleep(1)
    driver_adm.quit()
    # sleep(1000)

    print("Выход")
finally:
    print("Выполнил!")
    sleep(2)
    driver_adm.quit()
    driver.quit()
##########################
###Chat_with_Registered###
##########################