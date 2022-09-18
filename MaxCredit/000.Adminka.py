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

link = 'https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk'
#link = 'https://auto.dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk'




user = ('6620830315@mail.ru')
password = ('nq934946')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
card_num = ('2200200111114591')
card_date = ('0522')
card_cvc = ('426')


try:
###Админка, первичное одобрение
###Админка_принятие решения
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get(link)
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Быстрый займ"))  # Дождаться загрузки страницы
    sleep(1)
# driver_adm.set_window_size(550, 550)
# driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
            print("маленькое окно")
            driver_adm.find_elements(By.XPATH, '//a[contains(@data-href,"/auth/login")]')[1].click()
            print("click по иконке юсера")
            wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-dialog")]')))
            print("нашли модальное окно")
            sleep(1)
            print("надо ввести имя пользователя")
            driver_adm.find_elements(By.ID, "loginform-login")[1].send_keys(admin)
            print("надо ввести имя пользователя")
            driver_adm.find_elements(By.ID, "loginform-password")[1].send_keys(pas_adm)
            print("войти")
            driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)
    if True:
        try:
            driver_adm.find_element(By.LINK_TEXT, "Войти").click()
            print("большое окно")
            # driver_adm.find_elements(By.XPATH, '//a[contains(@data-href,"/auth/login")]')[1].click()
            print("ищем модальное окно")
            wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal__title")]')))
            print("нашли модальное окно")
            sleep(1)
            print("надо ввести имя пользователя")
            driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
            print("надо ввести пароль")
            driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
            print("войти")
            sleep(1)
            driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)

    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-user_lock")]')))
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-xs btn-danger js-ajax-modal")]')))
    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('2')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(2)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/card")]')[0].click()
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"client-card-verify")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"btn btn-danger")]')))
    Select(driver_adm.find_element(By.ID, 'clientcardverifyform-verified')).select_by_value('3')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(2)
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn-primary js-ajax-modal")]')))
    driver_adm.find_element(By.LINK_TEXT, "Одобрить").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    driver_adm.quit()
finally:
    print("Выполнил!")
    sleep(2)
    #driver.quit()
########################
###First_Registration###
########################


    #####

    ###
    print("Goods")
    sleep(10000)
    ###


    # wait.until(EC.element_to_be_clickable((By.ID, "take-loan-danger-modal")))
    # driver.find_element(By.ID, "take-loan-danger-modal").click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    # driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"input-icon")]')))
    # driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    # driver.find_element(By.XPATH, '//button[contains(@class,"danger js-submit-button")]').click()
    # wait.until(EC.element_to_be_clickable((By.ID, "code")))
    # sleep(1)
    # driver.find_element(By.ID, "code").send_keys("1111")
    # driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"profile-menu__link active")]')))
    #
    # print("Займ получен")
    # sleep(3)
    # driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    # wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]')))
    # driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    # sleep(1)
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    # print("Займ закрыт")
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa-sign-out")]')))
    # driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
    # print("Выход")
    # finally:
    # print("Выполнил!")
    # sleep(2)
    # driver.quit()
    # ########################
    # ###First_Registration###
    # ########################