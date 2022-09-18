##################################
###Remarks_Card_wrong_image+Fix###
##################################
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

#user = ('21813075@testmail.test')
#password = ('wh588928')
user = ('48964026@testmail.test')
password = ('da112674')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
card_num = ('2200200111114591')
card_date = ('0522')
card_cvc = ('426')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 90)

try:
    
    driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    # driver.maximize_window()
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
    ####
    if True:
        try:
            driver.find_element(By.XPATH, '//a[contains(@href,"/profile/cancel/")]').click()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            sleep(2)
            driver.switch_to.alert.accept()
            sleep(1)
        except:
            sleep(0)
    ####
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-select-card-modal")]')))
    sleep(0)
    driver.find_element(By.XPATH, '//a[contains(@class,"js-select-card-modal")]').click()

    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Карта для получения займа"))
    driver.find_element(By.XPATH, '//a[contains(@href,"/profile/card/add-transfer")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Данные карты будут переданы в зашифрованном виде"))
    driver.find_element(By.ID, "cardFrom").send_keys("5211786751060557")
    driver.find_element(By.ID, "cardDate").send_keys("0122")
    driver.find_element(By.ID, "cvc").send_keys("012")
    print("Добавлена карта с неверным CVC")
    driver.find_element(By.XPATH, '//span[contains(@class,"checkbox-custom")]').click()
    driver.find_element(By.ID, "submitButton").click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Сфотографируйте лицевую сторону банковской карты"))
    driver.find_element(By.ID, "photodata-cardphoto").send_keys(path_img + "new_card_1.jpg")
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Выбрать карту"))
    driver.find_element(By.XPATH, '//a[contains(@class,"js-select-card-modal")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Карта для получения займа"))
    count_card = len(driver.find_elements(By.XPATH, '//span[contains(@class,"card-number")]'))
    print(count_card)

    sleep(1)

    driver.find_elements(By.XPATH, '//a[contains(@class,"btn-primary")]')[count_card].click()
    sleep(1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(50, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-lg btn-primary")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 60)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__logo")]')))
    #driver_adm.maximize_window()
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
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.XPATH, '//li[contains(@title,"Клиенты")]').click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[contains(@name,"email")]')))
    driver_adm.find_element(By.XPATH, '//input[contains(@name,"email")]').send_keys(str(user), "\n")
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@href,"/manager/client/")]')))
    driver_adm.find_element(By.XPATH,
                            '//a[contains(@href,"/manager/client/view")]').click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"js-user_lock")]')))

    if True:
        try:
            driver_adm.find_element(By.ID, 'user_verify_check')
            driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
        except:
            sleep(0)

    sleep(1)
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.ID, 'user_verify_check')))

    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('2')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/card")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-client-card-verify")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"client-card-verify")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"btn btn-danger")]')))

    sleep(1)

    Select(driver_adm.find_element(By.ID, 'clientcardverifyform-verified')).select_by_value('5')
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="clientcardverifyform-commentclient"]')))
    driver_adm.find_element(By.ID, 'clientcardverifyform-commentclient').click()
    sleep(1)
    driver_adm.find_element(By.XPATH, '//*[@id="clientcardverifyform-commentclient"]').send_keys("Не верное изображение \n")
    sleep(2)

    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()

    wait_adm.until_not(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Проверка карты:'))
    driver_adm.quit()

    while True:
        try:
            driver.find_element(By.XPATH, '//a[contains(@class,"btn-primary")]')
            break
        except:
            driver.refresh()
            sleep(1)

    driver.find_element(By.XPATH, '//a[contains(@class,"btn-primary")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Загрузить'))
    driver.find_element(By.ID, "photodata-cardphoto").send_keys(path_img + "new_card.jpg")
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
#    sleep(1000)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

    sleep(1)

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__logo")]')))
    #driver_adm.maximize_window()
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
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.XPATH, '//li[contains(@title,"Клиенты")]').click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//input[contains(@name,"email")]')))
    driver_adm.find_element(By.XPATH, '//input[contains(@name,"email")]').send_keys(str(user), "\n")
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@href,"/manager/client/")]')))
    driver_adm.find_element(By.XPATH,
                            '//a[contains(@href,"/manager/client/view")]').click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"js-user_lock")]')))

    if True:
        try:
            driver_adm.find_element(By.ID, 'user_verify_check')
            driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
            wait_adm.until(EC.visibility_of_element_located(
                (By.XPATH, '//a[contains(@class,"js-user_lock")]')))
        except:
            sleep(0)
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class,"field-user_verify_check required")]')))
    wait_adm.until(EC.visibility_of_element_located((By.XPATH,
                                                     '//a[contains(@class,"btn btn-xs btn-danger js-ajax-modal")]')))

    driver_adm.find_element(By.XPATH, '//a[contains(@href,"/manager/user-verify/card")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-client-card-verify")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"client-card-verify")]')[0].click()
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Проверка карты:'))
    Select(driver_adm.find_element(By.ID, 'clientcardverifyform-verified')).select_by_value('3')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait_adm.until_not(EC.text_to_be_present_in_element((By.XPATH, "//*"), 'Проверка карты:'))

    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn-primary js-ajax-modal")]')))

    driver_adm.find_element(By.LINK_TEXT, "Одобрить").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))

    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(2)
    driver_adm.quit()

    while True:
        try:
            driver.find_element(By.ID, "take-loan-danger-modal")
            break
        except:
            driver.refresh()
            sleep(2)

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
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]')))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    sleep(1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))

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

    driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
    print("Выход")
finally:
    print("Выполнил!")
    sleep(2)
    driver.quit()
##################################
###Remarks_Card_wrong_image+Fix###
##################################