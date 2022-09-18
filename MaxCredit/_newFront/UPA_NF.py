#############################
###user's_personal_account###
#############################

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
user = ('ivan155@mail.ru')
password = ('pb408678')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 90)

try:
    driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    # driver.maximize_window()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))

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

    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"irs-handle single")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"irs-handle single")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(50, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()

    ActionChains(driver).click_and_hold(term_z).move_by_offset(-100, 0).release().perform()
    print("-100")
    sleep(1)
    ActionChains(driver).click_and_hold(term_z).move_by_offset(-50, 0).release().perform()
    print("-50")



    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/limits")]')[1].click()
    print("Лимиты")
    sleep(1)
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
        driver.find_element(By.XPATH, '//a[contains(@href,"/profile/history/index")]').click()
        print("Назад")
        sleep(2)
        print("Следующий займ")
    print("вышел из цикла")
    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/info")]')[1].click()
    print("клик по Ваши данные")

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Регистрация']")))
    print("вижу регистрация")
    driver.find_element(By.XPATH, "//*[text()='Регистрация']").click()
    print("клик по регистрации")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/profile/info/password")]')))
    driver.find_element(By.XPATH, '//a[contains(@href,"/profile/info/password")]').click()
    print("клик по сменим пароль")
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Изменение пароля"))
    print("вижу Изменение пароля")
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(2)
    driver.find_element(By.ID, "passwordform-password").send_keys("1!#$%&‘()*+,–./:;?@[]^_`'&|№~q")
    driver.find_element(By.ID, "passwordform-password_repeat").send_keys("1!#$%&‘()*+,–./:;?@[]^_`'&|№~q")
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Регистрация']")))
    print("вижу регистрация")
    sleep(1)

    #
    if True:
        try:
            driver.find_element(By.XPATH, '//div[contains(@class,"menu-mobile menu-call-btn app--menu-mobile-open")]').click()
            print("меню в мобилке")
            sleep(1)
            driver.find_elements(By.XPATH, '//a[contains(@href,"/auth/logout")]')[0].click()
        except:
            sleep(0)
    if True:
        try:
            driver.find_elements(By.XPATH, '//a[contains(@href,"/auth/logout")]')[1].click()
            print("Кнопка выход")
        except:
            sleep(0)
    #
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))
    sleep(2)

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

    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "E-mail, телефон или пароль введены неверно"))

    if driver.find_element(By.XPATH, "//*[text()='E-mail, телефон или пароль введены неверно']"):
        driver.find_element(By.ID, "loginform-password").clear()
        driver.find_element(By.ID, "loginform-password").send_keys("1!#$%&‘()*+,–./:;?@[]^_`'&|№~q")
        driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()#Войти
    else:
        print("Вход под старым паролем!!!")
        breakpoint()

    if True:
        try:
            driver.find_element(By.XPATH, '//div[contains(@class,"form__subtitle")]')
            sleep(1)
            driver.find_element(By.XPATH, '//a[contains(@data-href,"/profile/feedback/hide")]').click()
            sleep(1)
        except:
            sleep(0)


    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "У Вас нет непогашенных займов"))

    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/info")]')[1].click()
    print("клик по Ваши данные")

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Регистрация']")))
    print("вижу регистрация")
    driver.find_element(By.XPATH, "//*[text()='Регистрация']").click()
    print("клик по регистрации")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/profile/info/password")]')))
    driver.find_element(By.XPATH, '//a[contains(@href,"/profile/info/password")]').click()
    print("клик по сменим пароль")
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Изменение пароля"))
    print("вижу Изменение пароля")
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(2)
    driver.find_element(By.ID, "passwordform-password").send_keys(str(password))
    driver.find_element(By.ID, "passwordform-password_repeat").send_keys(str(password))
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Регистрация']")))
    print("вижу регистрация")


    # sleep(1)
    # driver.find_element(By.XPATH, '//a[contains(@data-target,"add-photo")]').click()
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*'), "Пожалуйста, выберите тип фотографий:"))
    # driver.find_element(By.XPATH, '//a[contains(@href,"/profile/info/photo")]').click()
    # driver.find_element(By.ID, "photodata-passportphoto1").send_keys(path_img+"new_pas_1.jpg")
    # driver.find_element(By.ID, "photodata-passportphoto2").send_keys(path_img+"new_pas_2.jpg")
    # driver.find_element(By.ID, "photodata-clientphoto").send_keys(path_img+"new_pas_3.jpg")
    # sleep(1)
    # driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Регистрация"))
    # driver.find_element(By.XPATH, '//a[contains(@data-target,"add-photo")]').click()
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*'), "Пожалуйста, выберите тип фотографий:"))
    # driver.find_element(By.XPATH, '//a[contains(@href,"/profile/card/photo")]').click()
    # driver.find_element(By.ID, "photodata-cardphoto").send_keys(path_img+"new_card.jpg")
    # sleep(1)
    # driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Регистрация"))
    # driver.find_element(By.XPATH, '//a[contains(@data-target,"add-photo")]').click()
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*'), "Пожалуйста, выберите тип фотографий:"))
    # driver.find_element(By.XPATH, '//a[contains(@href,"/profile/info/surname")]').click()
    # driver.find_element(By.ID, "photodata-documentscan").send_keys(path_img+"change_name.jpg")
    # sleep(1)



    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/credit")]')[1].click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@data-href,"/profile/card/select")]')))

    driver.find_element(By.XPATH, '//a[contains(@data-href,"/profile/card/select")]').click()
    #wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Карта для получения займа"))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-primary")]')))
    driver.find_element(By.XPATH, '//a[contains(@class,"btn btn-primary")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Данные карты будут переданы в зашифрованном виде"))
    print("wait")

    driver.find_element(By.ID, "cardFrom").send_keys("5211786751060557")
    driver.find_element(By.ID, "cardDate").send_keys("0122")
    driver.find_element(By.ID, "cvc").send_keys("012")
    driver.find_element(By.ID, "submitButton").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"image-select-view__empty")]')))

    print("Дождаться кнопки загрузки фото")
    driver.find_element(By.ID, 'photodata-cardphoto').send_keys(path_img + "card.jpg")
    print("Загрузка фото")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    print("Добавлена карта с неверным CVC")

    sleep(1)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@data-toggle,"tooltip")]')))
    driver.find_element(By.XPATH, '//a[contains(@data-toggle,"tooltip")]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"form__block")]')))

    count_card = len(driver.find_elements(By.XPATH, '//div[contains(@class,"form__block")]'))
    print(count_card)
    print(count_card-1)
    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/card/select?cardId")]')[count_card-1].click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@type,"submit")]')))


    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"irs-handle single")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"irs-handle single")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(50, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()
    sleep(1)
    ActionChains(driver).click_and_hold(term_z).move_by_offset(-100, 0).release().perform()
    print("-100")
    sleep(1)
    ActionChains(driver).click_and_hold(term_z).move_by_offset(-50, 0).release().perform()
    print("-50")
    sleep(1)
    ActionChains(driver).click_and_hold(term_z).move_by_offset(+10, 0).release().perform()
    print("+10")
    sleep(1)
    driver.find_element(By.ID, "creditcalcform-insuranceconfirm").click()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(+100, 0).release().perform()
    print("+100")
    sleep(1)
    ###continue
    print("проверим")
    sleep(1000)



    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))
    sleep(1)



    # Adminka
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 60)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)
    # поменять селектор ожидания
    # wait_r.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))
    # wait_r.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login btn-block js-login-button")]'))) #menu
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
    driver_adm.find_element(By.XPATH, '//input[contains(@name,"email")]').send_keys(str(user),"\n")
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
    # Перенести в свободные
    if True:
        try:
            driver_adm.find_element(By.ID, 'user_verify_check')
            driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
        except:
            sleep(0)
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class,"field-user_verify_check required")]')))
    wait_adm.until(EC.visibility_of_element_located((By.XPATH,
                                                  '//a[contains(@class,"btn btn-xs btn-danger js-ajax-modal")]')))
    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('2')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)

    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"btn-primary js-ajax-modal")]')))
    driver_adm.find_element(By.LINK_TEXT, "Одобрить").click()
    sleep(1)
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(text(), "Одобрение заявки")]')))
    Select(driver_adm.find_element(By.ID, 'userquestionnaireapproveform-amount')).select_by_value(
        '28000')
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.invisibility_of_element_located((By.XPATH,
                                                    '//div[contains(text(), "Одобрение заявки")]')))
    sleep(2)
    driver_adm.quit()
    sleep(2)
    # Получение и закрытие
    driver.refresh()
    sleep(1)
    driver.refresh()
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, "//div"), "Поздравляем, Вам одобрен займ"))
    summ_p = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    ActionChains(driver).click_and_hold(summ_p).move_by_offset(300, 0).release().perform()
    driver.find_element(By.ID, "take-loan-danger-modal").click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//button[contains(@type,"submit")]')))
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//span[contains(@class,"input-icon")]')))
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    driver.find_element(By.XPATH, '//button[contains(@class,"danger js-submit-button")]').click()
    wait.until(EC.element_to_be_clickable((By.ID, "code")))
    sleep(1)
    driver.find_element(By.ID, "code").send_keys("1111")
    driver.find_element(By.XPATH,
                        '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"profile-menu__link active")]')))
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(text(), "Погашение займа")]')))
    summ_o = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    ActionChains(driver).click_and_hold(summ_o).move_by_offset(-150, 0).release().perform()
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    wait.until(EC.invisibility_of_element_located(
        (By.XPATH, '//div[contains(text(), "Погашение займа")]')))
    sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa-sign-out")]')))
    driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
    sleep(2)
    driver.quit()
    sleep(1)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 120)
    driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    driver.maximize_window()
    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                 '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))
    driver.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver.find_element(By.ID, "loginform-login").send_keys(str(user))
    driver.find_element(By.ID, "loginform-password").send_keys(str(password))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Активный займ"))
    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/history")]')[1].click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Закрытые займы"))
    sleep(1)
    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/credit")]')[1].click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(text(), "Закрытые займы")]')))

    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Погашение займа")]')))
    #sleep(1)




    ###!!!!ПРОВЕРИТЬ




    driver.find_element(By.XPATH, '//a[contains(@href,"/profile/card/add-return")]').click()
    print("click")
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Данные карты будут переданы в зашифрованном виде"))
    print("wait")
    driver.find_element(By.ID, "cardFrom").send_keys("5211786751060557")
    driver.find_element(By.ID, "cardDate").send_keys("0122")
    driver.find_element(By.ID, "cvc").send_keys("012")
    print("Добавлена карта с неверным CVC")
    driver.find_element(By.ID, "submitButton").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver.find_element(By.XPATH, '//button[contains(@data-href,"/profile/return/")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Выберите сумму погашения")]')))
    driver.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    sleep(1)
    driver.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[1].click()
    sleep(1)

    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(text(), "Погашение займа")]')))
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    sleep(5)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa-sign-out")]')))
    driver.find_elements(By.XPATH, '//a[contains(@href,"/profile/history")]')[1].click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Закрытые займы"))
    sleep(1)
    count_loan = len(driver.find_elements(By.XPATH, '//tbody/tr'))
    driver.find_elements(By.XPATH, '//tbody/tr/td/a')[0].click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Закрытый займ"))
    sleep(1)
    driver.find_element(By.LINK_TEXT, "Назад").click()
    print("Назад", count_loan)
    sleep(1)
    driver.find_elements(By.XPATH, '//a[contains(@href,"/#about")]')[1].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//a[contains(@href,"/#work")]')[1].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//a[contains(@href,"/#questions")]')[1].click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-0")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-1")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-2")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-3")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-4")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-5")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-6")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-7")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-8")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-9")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(@class,"btn__closed-text")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-10")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-11")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-12")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-13")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-14")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-15")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-16")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[contains(@data-target,"#question-item-17")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(@class,"btn__opened-text")]').click()
    sleep(1)

    driver.find_element(By.XPATH, '//a[contains(@href,"doc=1&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=2&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=3&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=4&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=5&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=6&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=7&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=33&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=20&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=34&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=35&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=21&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=24&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    sleep(200)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=25&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=31&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=29&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=32&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.XPATH, '//a[contains(@href,"doc=13&")]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    # wait.until(EC.presence_of_element_located((By.ID, 'content')))
    sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
    print("Выход")
    sleep(2)

finally:
    print("Выполнено")
    sleep(2)
    driver.quit()
#############################
###user's_personal_account###
#############################