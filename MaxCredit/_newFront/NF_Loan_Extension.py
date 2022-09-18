####################
###loan extension###
####################

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


#user = ('6620830315@mail.ru')
#password = ('nq934946')
user = 'rj@hddd.yttr'
password = 'pz816433'
adm_saas = 'admin'
pas_saas = 'es1HYLt8QgiKIy23T18h'
admin = 'hello@max.credit'
pas_adm = 'tt762396'
path_img = 'c://test/img/'

numberDoc = ''

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 90)
try:
    driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    # driver.maximize_window()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))

    if True:
        try:
            driver.find_element(By.CSS_SELECTOR, 'span.title').click()
            driver.find_elements(By.XPATH, '//a[contains(@data-href,"/auth/login")]')[1].click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-dialog")]')))
            sleep(1)
            driver.find_elements(By.ID, "loginform-login")[1].send_keys(user)
            driver.find_elements(By.ID, "loginform-password")[1].send_keys(password)
            driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)
    if True:
        try:
            driver.find_element(By.LINK_TEXT, "Войти").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal__title")]')))
            sleep(1)
            driver.find_element(By.ID, "loginform-login").send_keys(user)
            driver.find_element(By.ID, "loginform-password").send_keys(password)
            sleep(1)
            driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)

    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "У Вас нет непогашенных займов"))

    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/history")]')[1].click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Закрытые займы"))

    sleep(1)
    count_loan = len(driver.find_elements(By.XPATH, '//div[contains(@class,"faq__item__title")]'))
    print(count_loan)

    #for i in range(0, count_loan):
    for i in range(0, 1):
        print(i)
        driver.find_elements(By.XPATH, '//div[contains(@class,"faq__item__title")]')[i].click()
        sleep(1)
        driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/history/detail")]')[i].click()
        print("Детализация", + i)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Закрытый займ"))


        sleep(1)
        numberDoc = driver.find_element(By.XPATH, '//a[contains(@href,"/profile/take/contract-download")]').text
        print(numberDoc)
        sleep(2)


        sleep(1)
        driver.find_element(By.XPATH, '//a[contains(@href,"/profile/history/index")]').click()
        print("Назад")
        sleep(2)
        print("Следующий займ")
    print("вышел из цикла")
    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/credit")]')[1].click()

    sleep(1)


    # SAAS
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver_saas: WebDriver = webdriver.Chrome(options=options)
    wait_saas = WebDriverWait(driver_saas, 60)
    driver_saas.get('https://mctest2.saascredit.ru/')
    # driver_adm.maximize_window()
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, '//div'), 'Введите ваши данные'))
    sleep(1)
    driver_saas.find_element(By.ID, 'authform-username').send_keys(str(adm_saas))
    driver_saas.find_element(By.ID, 'authform-password').send_keys(str(pas_saas))
    driver_saas.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait_saas.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(text(), "Информационная сводка")]')))

    sleep(1)
    driver_saas.find_element(By.XPATH, '//a[contains(@class,"dropdown-toggle gid-operator")]').click()  # Оператор
    sleep(1)
    driver_saas.find_element(By.XPATH,
                             '//a[contains(@href,"/index.php/interface/operator/all-questionnaires")]').click()  # Все заявки
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Результаты по запросу "Все заявки"'))

    sleep(1)
    driver_saas.find_element(By.ID, 'inputNumberQue').send_keys(str(numberDoc))
    sleep(1)
    driver_saas.find_element(By.ID, 'searchButton').click()
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Показаны с 1 по 1 из 1 записей'))
    driver_saas.find_element(By.ID, numberDoc).click()
    sleep(1)
    driver_saas.find_element(By.ID, 'edit-repayment-history').click()
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Результаты по запросу "История погашений"'))

    count_pay = len(driver_saas.find_elements(By.XPATH,
                                              '//button[contains(@class,"delete_record btn btn-danger editable-cancel")]'))
    print(count_pay)
    if count_pay > 1:
        for i in range(1, count_pay):
            driver_saas.find_elements(By.XPATH, '//button[contains(@class,"delete_record")]')[1].click()
            sleep(1)
            wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Подтвердите проведение операции'))
            driver_saas.find_element(By.XPATH, '//button[contains(@data-bb-handler,"success")]').click()
            sleep(1)
            wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Запись успешно удалена'))
            sleep(1)
            driver_saas.find_element(By.XPATH, '//button[contains(@data-bb-handler,"success")]').click()
            sleep(1)
            print(f'Проход {i} выполнен')
    else:
        print('Нет записей кроме нулевой')
    print('Удалили все записи кроме нулевой')

# Пролонгации

    driver_saas.find_element(By.ID, 'edit-prolongation').click()
    if True:
        try:
            WebDriverWait(driver_saas, 5).until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Результаты по запросу "Пролонгации"'))
            sleep(1)
            driver_saas.find_element(By.XPATH, '//i[contains(@class,"fa-trash-o")]').click()
            wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Подтвердите проведение операции'))
            sleep(1)
            driver_saas.find_element(By.XPATH, '//button[contains(@data-bb-handler,"success")]').click()
            sleep(1)
            wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Запись успешно удалена'))
            sleep(1)
            driver_saas.find_element(By.XPATH, '//button[contains(@data-bb-handler,"success")]').click()
            print('Ок')
            sleep(1)
        except:
            print('Нет результатов по запросу "Пролонгации"')
            sleep(0)
    sleep(2)

# Пересчитать
    driver_saas.find_element(By.ID, 'edit-account-debt').click()
    wait_saas.until(EC.visibility_of_element_located((By.ID, 'accrual_calculation')))
    sleep(1)
    driver_saas.find_element(By.ID, 'accrual_calculation').click()
    sleep(2)
    print("Выход")
    driver_saas.quit()

# Продление
    while True:
        try:
            driver.find_element(By.XPATH, '//button[contains(@data-href,"/profile/extend/extend")]')
            break
        except:
            driver.refresh()
            sleep(2)
    sleep(1)

    sleep(5010)
    driver.find_element(By.XPATH, '//button[contains(@data-href,"/profile/extend/extend")]').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'extendloanform-termdate-kvdate')))
    print('Дождались календарь')
    sleep(1)
    driver.find_element(By.ID, 'extendloanform-termdate-kvdate').click()
    sleep(1)
    count_day = len(driver.find_elements(By.XPATH, '//td[@class="day"]'))
    print(count_day)
    driver.find_elements(By.XPATH, '//td[@class="day"]')[0].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Договор продления займа'))
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-danger js-submit-button")]').click()
    wait.until(EC.element_to_be_clickable((By.ID, "extendloanform-code")))
    sleep(1)
    driver.find_element(By.ID, "extendloanform-code").send_keys("1111")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Сумма к погашению на сегодня'))
    sleep(3)
    print('А теперь мы его погасим')
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]')))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    sleep(1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//div'), 'У Вас нет непогашенных займов'))
    print('Займ закрыт')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa-sign-out")]')))
    driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
    print('Выход')

    sleep(2)
finally:
    print('Выполнено')
    sleep(2)
    #driver.quit()
####################
###loan extension###
####################