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
adm_saas = "admin"
pas_saas = "es1HYLt8QgiKIy23T18h"
admin = "hello@max.credit"
pas_adm = "tt762396"
path_img = 'c://test/img/'
numberDoc = "202204060004"


try:

    # SAAS
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver_saas: WebDriver = webdriver.Chrome(options=options)
    wait_saas = WebDriverWait(driver_saas, 60)
    driver_saas.get('https://mctest2.saascredit.ru/')
    #driver_adm.maximize_window()
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, '//div'), 'Введите ваши данные'))

    print('Введите ваши данные')
    sleep(1)
    driver_saas.find_element(By.ID, 'authform-username').send_keys(str(adm_saas))
    driver_saas.find_element(By.ID, 'authform-password').send_keys(str(pas_saas))
    driver_saas.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait_saas.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(text(), "Информационная сводка")]')))
    print('Информационная сводка')
    sleep(1)
    driver_saas.find_element(By.XPATH, '//a[contains(@class,"dropdown-toggle gid-operator")]').click() # Оператор
    print('Оператор')
    sleep(1)
    driver_saas.find_element(By.XPATH, '//a[contains(@href,"/index.php/interface/operator/all-questionnaires")]').click() # Все заявки
    print('Все заявки')
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, '//*'), 'Результаты по запросу "Все заявки"'))
    print('Результаты по запросу "Все заявки"')
    driver_saas.find_element(By.ID, 'inputNumberQue').send_keys(str(numberDoc))
    sleep(1)
    driver_saas.find_element(By.ID, 'searchButton').click()
    print('Результат')
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, '//*'), 'Показаны с 1 по 1 из 1 записей'))
    print('Показаны с 1 по 1 из 1 записей')
    driver_saas.find_element(By.ID, numberDoc).click()
    print('кликнуто по строчке с id', numberDoc)
    sleep(1)
    driver_saas.find_element(By.ID, 'edit-repayment-history').click()
    print('кликнуто по строчке редактирование платежей')
    wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Результаты по запросу "История погашений"'))
    print('Результаты по запросу "История погашений"')

    count_pay = len(driver_saas.find_elements(By.XPATH, '//button[contains(@class,"delete_record btn btn-danger editable-cancel")]'))
    print(count_pay)

    for i in range(1, count_pay):
        print('удаляем запись номер', i)
        driver_saas.find_elements(By.XPATH, '//button[contains(@class,"delete_record btn btn-danger editable-cancel")]')[i].click()
        sleep(1)
        wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Подтвердите проведение операции'))
        print('Подтвердите проведение операции')
        driver_saas.find_element(By.XPATH, '//button[contains(@data-bb-handler,"success")]').click()
        print('Подтвердить')
        sleep(1)
        wait_saas.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Запись успешно удалена'))
        print('Запись успешно удалена')
        sleep(1)
        driver_saas.find_element(By.XPATH, '//button[contains(@data-bb-handler,"success")]').click()
        print('Ок')
        sleep(1)
        print(f'Проход {i} выполнен')
    print('Удалили все записи кроме нулевой')

# Пересчитать
    driver_saas.find_element(By.ID, 'edit-account-debt').click()
    print('кликнуто по строчке редактирование начислений')
    wait_saas.until(EC.visibility_of_element_located((By.ID, 'accrual_calculation')))
    print('Нашли кнопку пересчитать')
    sleep(1)
    driver_saas.find_element(By.ID, 'accrual_calculation').click()

    sleep(2)

    print("Выход")
finally:
    print("Выполнено")
    sleep(2)
    driver_saas.quit()
####################
###loan extension###
####################