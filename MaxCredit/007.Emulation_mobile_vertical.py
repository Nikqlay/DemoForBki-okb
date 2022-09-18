###############################
###Emulation_mobile_vertical###
###############################

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

#vertical

mobileEmulation = {'deviceName': 'iPhone X'}

options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver: WebDriver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 90)
driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
#driver.maximize_window()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Даем быстрый займ")) #Дождаться загрузки страницы

#user = ('6620830315@mail.ru')
#password = ('nq934946')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
card_num = ('2200200111114591')
card_date = ('0522')
card_cvc = ('426')

#registration():
try:
    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(-10, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()
    sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div//form//button')))
    driver.find_element(By.XPATH, '//div//form//button').click() #Получить деньги
    wait.until(EC.element_to_be_clickable((By.ID, "userregisterwelcomeform-last_name")))
    driver.find_element(By.ID, "userregisterwelcomeform-last_name").send_keys(str(random.choice(['Иванов', 'Петров', 'Сидоров', 'Орлов', 'Жуков', 'Васильев', 'Кузьнецов', 'Зуев'])))
    driver.find_element(By.ID, "userregisterwelcomeform-first_name").send_keys(str(random.choice(['Иван', 'Петр', 'Василий', 'Олег', 'Евгений', 'Алексей', 'Константин', 'Данил', 'Максим'])))
    driver.find_element(By.ID, "userregisterwelcomeform-middle_name").send_keys(str(random.choice(['Иваныч', 'Петрович', 'Васильевич', 'Артемович', 'Алексеевич', 'Олегович', 'Максимович', 'Юрьевич', 'Витальевич'])))
    driver.find_element(By.ID, "userregisterwelcomeform-phone").send_keys("1000000001")
    driver.find_element(By.ID, "userregisterwelcomeform-email").send_keys("semen203@mail.ru")
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[1].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[4].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[5].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[6].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[7].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    #driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[0].click()
    sleep(2)
    if driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']"):
        err_tel = driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']")
        print(err_tel.text)
        while err_tel != ("Номер телефона уже зарегистрирован"):
            if driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']"):
                err_tel = ('Номер телефона уже зарегистрирован')
            else:
                err_tel = ('')
            driver.find_element(By.ID, "userregisterwelcomeform-phone").clear()
            print("Очистим поле ввода")
            sleep(1)
            phone_u = random.randrange(10000000, 99999999, 1)
            driver.find_element(By.ID, "userregisterwelcomeform-phone").send_keys("00"+str(phone_u))
            print("Поменяем номер телефона", "00"+(str(phone_u)))
            sleep(1)
            driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[0].click()
    else:
        print("иначе продолжаем")
    sleep(2)
    if driver.find_element(By.XPATH, "//*[text()='E-mail уже зарегистрирован']"):
        err_email = driver.find_element(By.XPATH, "//*[text()='E-mail уже зарегистрирован']")
        print(err_email.text)
        while err_email != ("E-mail уже зарегистрирован"):
            if driver.find_element(By.XPATH, "//*[text()='E-mail уже зарегистрирован']"):
                err_email = ('E-mail уже зарегистрирован')
            else:
                err_email = ('')
            driver.find_element(By.ID, "userregisterwelcomeform-email").clear()
            print("Очистим поле ввода")
            sleep(1)
            driver.find_element(By.ID, "userregisterwelcomeform-email").send_keys(
                str(phone_u)+'@testmail.test')
            print("Поменяем номер телефона", (str(phone_u)+'@testmail.test'))
            sleep(1)
            driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[0].click()
    else:
        print("иначе продолжаем")

    sleep(2)
    print("Все поменяли, продолжаем")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]')))
    #sleep(1)
    driver.find_element(By.ID, "userregisterphoneform-phone_confirm").send_keys("1111")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"form-group field-userregistercommonform-gender_id required")]'))) #Дождаться формы регистрации
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[1].click() #Женский
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click() #Мужской
    driver.find_element(By.ID, "userregistercommonform-place_of_birth").send_keys("Россия")
    driver.find_element(By.ID, "userregistercommonform-date_of_birth").send_keys("01011991")
    driver.find_element(By.ID, "userregistercommonform-serial_p").send_keys("5001")
    driver.find_element(By.ID, "userregistercommonform-number_p").send_keys("000010")
    driver.find_element(By.ID, "userregistercommonform-place_of_issue").send_keys("Выдан ОВД 01")
    driver.find_element(By.ID, "userregistercommonform-date_of_issue").send_keys("01012013")
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click() #Постоянная
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click() #Временная
    Select(driver.find_element(By.ID, 'userregistercommonform-region')).select_by_value('Алтайский край')
    driver.find_element(By.ID, "userregistercommonform-city").send_keys("Алтай")
    driver.find_element(By.ID, "userregistercommonform-street").send_keys("Алтайская")
    driver.find_element(By.ID, "userregistercommonform-house_number").send_keys("10")
    driver.find_element(By.ID, "userregistercommonform-block").send_keys("101")
    driver.find_element(By.ID, "userregistercommonform-apartment").send_keys("123")
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[4].click() #Такой же
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[5].click() #В другом месте
    sleep(1)
    Select(driver.find_element(By.ID, 'userregistercommonform-region_fact')).select_by_value('Ярославская область')
    driver.find_element(By.ID, "userregistercommonform-city_fact").send_keys("Ярославль")
    driver.find_element(By.ID, "userregistercommonform-street_fact").send_keys("Ярославская")
    driver.find_element(By.ID, "userregistercommonform-house_number_fact").send_keys("101")
    driver.find_element(By.ID, "userregistercommonform-block_fact").send_keys("123")
    driver.find_element(By.ID, "userregistercommonform-apartment_fact").send_keys("1234")
    driver.find_element(By.ID, "userregistercommonform-home_phone").send_keys("1200000156")
    driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[0].click() #Продолжить
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Паспорт уже зарегистрирован']"))) #Дождаться кнопки загрузки фотографий
    sleep(2)
    if driver.find_element(By.XPATH, "//*[text()='Паспорт уже зарегистрирован']"):
        err_pas = driver.find_element(By.XPATH, "//*[text()='Паспорт уже зарегистрирован']")
        print(err_pas.text)
        while err_pas != ("Паспорт уже зарегистрирован"):
              if driver.find_element(By.XPATH, "//*[text()='Паспорт уже зарегистрирован']"):
                    err_pas = ('Паспорт уже зарегистрирован')
              else:
                    err_pas = ('')
              driver.find_element(By.ID, "userregistercommonform-serial_p").clear()
              driver.find_element(By.ID, "userregistercommonform-number_p").clear()
              print("Очистим поле ввода")
              sleep(1)
              pas_s1 = random.randrange(75, 99, 1)
              pas_s2 = random.randrange(10, 16, 1)
              pas_ser = (str(pas_s1) + str(pas_s2))
              driver.find_element(By.ID, "userregistercommonform-serial_p").send_keys(str(pas_ser))
              pas_num = random.randrange(100000, 999999, 1)
              driver.find_element(By.ID, "userregistercommonform-number_p").send_keys(str(pas_num))
              print("Поменяем серию", str(pas_ser), "и номер", str(pas_num), "паспорта")
              sleep(1)
              driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[
                    0].click()  # Продолжить
    else:
          print("иначе продолжаем")

    sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"form-group field-userregisteradditionalform-has_work required")]'))) #Дождаться формы регистрации
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click() #Пенсионер
    sleep(1)
    driver.find_element(By.XPATH, '//input[contains(@name,"ClientWorkData[7][monthly_income]")]').send_keys("13135") #Ежемесячный доход
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[1].click() #Не работаю
    sleep(1)
    Select(driver.find_element(By.ID, 'userregisteradditionalform-employment_type_id')).select_by_value('5') #Декрет
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click() #Работаю
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click() #Работа по найму
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click() #Работа по найму
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[4].click() #Свое дело
    sleep(1)
    driver.find_element(By.ID, "clientworkdata-8-organization_name").send_keys("ООО")
    driver.find_element(By.ID, "clientworkdata-8-number_phone").send_keys("1300000156")
    driver.find_element(By.ID, "clientworkdata-8-actual_address_id").send_keys("Адрес ООО")
    Select(driver.find_element(By.ID, 'clientworkdata-8-work_experience')).select_by_value('1') #От 6 месяцев до 1 года
    driver.find_element(By.ID, "clientworkdata-8-other_sources_income").send_keys("Специалист ООО")
    driver.find_element(By.ID, "clientworkdata-8-monthly_income").send_keys("987654")
    driver.find_element(By.ID, "clientworkdata-6-organization_name").send_keys("ИП")
    driver.find_element(By.ID, "clientworkdata-6-number_phone").send_keys("1400000156")
    driver.find_element(By.ID, "clientworkdata-6-actual_address_id").send_keys("Адрес ИП")
    driver.find_element(By.ID, "clientworkdata-6-monthly_income").send_keys("1234567")
    #driver.find_element(By.ID, "familiar-0-last_name").send_keys("Иванова")
    #driver.find_element(By.ID, "familiar-0-first_name").send_keys("Инна")
    #driver.find_element(By.ID, "familiar-0-middle_name").send_keys("Ивановна")
    #Select(driver.find_element(By.ID, 'familiar-0-familiar_type_id')).select_by_value('2')
    #driver.find_element(By.ID, "familiar-0-number_phone").send_keys("1500000156")

    driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]'))
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click() #Продолжить

    #recognition():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_r: WebDriver = webdriver.Chrome(options=options)
    wait_r = WebDriverWait(driver_r, 90)
    driver_r.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_r.maximize_window()
    wait_r.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]'))) #Дождаться кнопки Личный кабинет
    driver_r.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_r.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]'))) #Дождаться всплывающего окна
    driver_r.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_r.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_r.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click() #Войти
    wait_r.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]'))) #Дождаться появления кнопки выйти
    driver_r.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_r.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    driver_r.find_elements(By.XPATH, '//a[contains(@class,"btn-danger btn-xs")]')[0].click() #Клик по кнопке Отмена
    wait_r.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"col-12")]'))) #Дождаться всплывающего окна Вернуть заявку к рассмотрению
    driver_r.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Вернуть
    sleep(1)
    driver_r.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click() #Клик по первому юсеру
    driver_r.switch_to.window(driver_r.window_handles[1]) #Переход в окно профиля юсера
    wait_r.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]'))) #Дождаться загрузки формы окна пользователя
    driver_r.find_elements(By.XPATH, '//a[contains(@class,"btn-success")]')[0].click() #Клик по Одобрить
    wait_r.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-title")]'))) #Дождаться всплывающего окна Одобрения
    driver_r.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Всплывающее Одобрить
    wait_r.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-title")]'))) #Дождаться закрытия всплывающего окна Одобрения
    driver_r.quit()

    #def cont_reg():
    driver.refresh()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))# Дождаться кнопки Закончить регистрацию
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Клик по Закончить регистрацию
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"input-icon")]'))) #Дождаться открытия следующей формы
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click() #Идентификация по фотографиям
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()#Продолжить
    ####
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"image-select")]'))) #Дождаться кнопки загрузки фотографий
    sleep(2)
    down = driver.find_element(By.TAG_NAME, 'html')
    down.send_keys(Keys.PAGE_DOWN)
    sleep(1)
    down.send_keys(Keys.PAGE_DOWN)
    sleep(2)
    driver.find_element(By.ID, "userregisterfilesform-clientphoto").send_keys(path_img+"photo_1.jpg")
    driver.find_element(By.ID, "userregisterfilesform-passportphoto1").send_keys(path_img+"photo_2.jpg")
    driver.find_element(By.ID, "userregisterfilesform-passportphoto2").send_keys(path_img+"photo_3.jpg")
    driver.find_element(By.ID, "userregisterfilesform-passportphotopast").send_keys(path_img+"photo_4.jpg")

    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click() #Продолжить
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/register/card-add")]'))) #Дождаться кнопки загрузки карты
    driver.find_element(By.LINK_TEXT, "Добавить карту").click()
    wait.until(EC.visibility_of_element_located((By.ID, 'cardFrom'))) #Дождаться формы привязки карты
    driver.find_element(By.ID, 'cardFrom').send_keys(card_num)
    driver.find_element(By.ID, 'cardDate').send_keys(card_date)
    driver.find_element(By.ID, 'cvc').send_keys(card_cvc)
    driver.find_element(By.XPATH, '//input[contains(@id,"submitButton")]').click() #Оплата картой
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"image-select-view__empty-caption")]'))) #Дождаться формы привязки фото карты
    driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[0].send_keys(path_img+'card.jpg') #Добавление фото карты
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click() #Продолжить
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"bank-card")]'))) #Дождаться формы Отправить заявку
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click() #Отправить заявку

    #Adminka2
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 60)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]'))) #Дождаться кнопки Личный кабинет
    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]'))) #Дождаться всплывающего окна
    sleep(1)
    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click() #Войти
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]'))) #Дождаться появления кнопки выйти
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click() #Клик по первому юсеру
    driver_adm.switch_to.window(driver_adm.window_handles[1]) #Переход в окно профиля юсера
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]'))) #Дождаться загрузки формы окна пользователя
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click() #Идентификация
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-user_lock")]'))) #Дождаться формы Отправить заявку
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click() #Взять в работу
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-xs btn-danger js-ajax-modal")]'))) #Дождаться кнопки Отказ по причине КИ
    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('2') #Проверено: Пройдено
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Сохранить
    sleep(2)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/card")]')[0].click()
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"client-card-verify")]')[0].click() #Клик по кнопке Обновлено
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"btn btn-danger")]'))) #Дождаться кнопки Сохранить
    Select(driver_adm.find_element(By.ID, 'clientcardverifyform-verified')).select_by_value('3') #Проверено
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Сохранить
    sleep(2)
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn-primary js-ajax-modal")]'))) #Дождаться кнопки Одобрить
    driver_adm.find_element(By.LINK_TEXT, "Одобрить").click() #Клик по кнопке Одобрить
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]'))) #Дождаться всплывающего окна кнопки Одобрить
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Одобрить
    driver_adm.quit()
    #Получение и закрытие
    driver.refresh()
    sleep(3)
    driver.refresh()
    wait.until(EC.element_to_be_clickable((By.ID, "take-loan-danger-modal"))) #Ожидание кнопки Получить деньги
    driver.find_element(By.ID, "take-loan-danger-modal").click() #Получить деньги
    print("Ждем окно")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]'))) #Дождаться всплывающего окна кнопки Получить деньги
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click() #Получить деньги во всплывающем
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"input-icon")]'))) #Дождаться формы Ознакомлен
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click() #Ознакомлен
    driver.find_element(By.XPATH, '//button[contains(@class,"danger js-submit-button")]').click() #Подписать договор
    wait.until(EC.element_to_be_clickable((By.ID, "code")))
    sleep(1)
    driver.find_element(By.ID, "code").send_keys("1111") #Подтверждение получения займа
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click() #Продолжить
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"profile-menu__link active")]'))) #Дождаться перевода
    sleep(5)
    print("Займ получен")
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click() #Погасить займ
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]'))) #Дождаться перевода
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click() #Погасить
    sleep(3)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов")) #Дождаться погашения
    print("Займ закрыт")
finally:
    print("Выполнено")
    sleep(2)
    driver.quit()