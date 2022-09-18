########################
######RepeadedLoan######
########################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.webdriver import ActionChains
import time
from tkinter import HIDDEN
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

user = ('semen203@mail.ru')
password = ('ue033234')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
# card_num = ('2200200111114591')
# card_date = ('0522')
# card_cvc = ('426')
card_num = ('4191523668686084')
card_date = ('0522')
card_cvc = ('426')


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 90)

try:
    driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    # driver.maximize_window()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))
    #if driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']"):

    driver.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver.find_element(By.ID, "loginform-login").send_keys(user)
    driver.find_element(By.ID, "loginform-password").send_keys(password)
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()#Войти
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(50, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()
    sleep(1)

    if True:
        try:
            driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[5].click() #Страховка
        except:
            sleep(0)

    print("Будем страховаться?")
    sleep(5)

    driver.find_element(By.XPATH, '//button[contains(@class,"btn-lg btn-primary")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))
    #Adminka
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))
    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.XPATH, '//li[contains(@title,"Клиенты")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//input[contains(@name,"email")]')))
    driver_adm.find_element(By.XPATH, '//input[contains(@name,"email")]').send_keys(user+"\n")
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/client/")]')))
    driver_adm.find_element(By.XPATH, '//a[contains(@href,"/manager/client/view")]').click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-user_lock")]')))
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"field-user_verify_check required")]')))
    print("Взял в работу")
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn-primary js-ajax-modal")]')))
    driver_adm.find_element(By.LINK_TEXT, "Одобрить").click()
    print("Одобрить")
    sleep(3)
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Одобрение заявки")]')))
    print("Окно Одобрение заявки")
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(text(), "Одобрение заявки")]')))
    print("Одобрено")
    sleep(3)
    print("Выдано")
    sleep(5)
    driver_adm.quit()
    #####
    while True:
        try:
            driver.find_element(By.ID, "take-loan-danger-modal")
            break
        except:
            driver.refresh()
            sleep(2)
    #####
    wait.until(EC.element_to_be_clickable((By.ID, "take-loan-danger-modal")))
    driver.find_element(By.ID, "take-loan-danger-modal").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"input-icon")]')))
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    driver.find_element(By.XPATH, '//button[contains(@class,"danger js-submit-button")]').click()
    wait.until(EC.element_to_be_clickable((By.ID, "code")))
    sleep(1)
    driver.find_element(By.ID, "code").send_keys("1111")
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"profile-menu__link active")]')))
    sleep(3)
    print("Займ получен")
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]')))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    sleep(3)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    print("Займ закрыт")
    sleep(5)
finally:
    print("Выполнил!")
    sleep(2)
    driver.quit()
########################
######RepeadedLoan######
########################