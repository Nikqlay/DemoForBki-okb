########################
###First_Registration###
########################
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

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 180)
driver.get(link)
#driver.maximize_window()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Быстрый займ"))  # Дождаться загрузки страницы

user = ('6620830315@mail.ru')
password = ('nq934946')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
card_num = ('2200200111114591')
card_date = ('0522')
card_cvc = ('426')

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div//form//button')))
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()

    ###Registration
    wait.until(EC.element_to_be_clickable((By.ID, "userregisterwelcomeform-last_name")))
    driver.find_element(By.ID, "userregisterwelcomeform-last_name").send_keys(str(random.choice(['Иванов', 'Петров', 'Сидоров', 'Орлов', 'Жуков', 'Васильев', 'Кузьнецов', 'Зуев', 'Кудряшов'])))
    driver.find_element(By.ID, "userregisterwelcomeform-first_name").send_keys(str(random.choice(['Иван', 'Петр', 'Василий', 'Олег', 'Евгений', 'Алексей', 'Константин', 'Данил', 'Максим', 'Глеб'])))
    driver.find_element(By.ID, "userregisterwelcomeform-middle_name").send_keys(str(random.choice(['Иваныч', 'Петрович', 'Васильевич', 'Артемович', 'Алексеевич', 'Олегович', 'Максимович', 'Юрьевич',' Витальевич', 'Генадьевич'])))
    phone_u = random.randrange(10000000, 99999999, 1)
    driver.find_element(By.ID, "userregisterwelcomeform-phone").send_keys("00" + str(phone_u))
    driver.find_element(By.ID, "userregisterwelcomeform-email").send_keys(str(phone_u) + '@testmail.test')
    driver.find_element(By.ID, "check-all").click()
    driver.find_element(By.XPATH, '//button[contains(@type,"button")]').click()

    try:
        if driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']"):
            err_tel = driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']")
            while err_tel != ("Номер телефона уже зарегистрирован"):
                if driver.find_element(By.XPATH, "//*[text()='Номер телефона уже зарегистрирован']"):
                    err_tel = ('Номер телефона уже зарегистрирован')
                else:
                    err_tel = ('')
                driver.find_element(By.ID, "userregisterwelcomeform-phone").clear()
                sleep(1)
                phone_u = random.randrange(10000000, 99999999, 1)
                driver.find_element(By.ID, "userregisterwelcomeform-phone").send_keys("00" + str(phone_u))
                driver.find_element(By.XPATH, '//button[contains(@type,"button")]').click()
        else:
            sleep(0)
    except NoSuchElementException:
        sleep(0)
    try:
        if driver.find_element(By.XPATH, "//*[text()='E-mail уже зарегистрирован']"):
            err_email = driver.find_element(By.XPATH, "//*[text()='E-mail уже зарегистрирован']")
            while err_email != ("E-mail уже зарегистрирован"):
                if driver.find_element(By.XPATH, "//*[text()='E-mail уже зарегистрирован']"):
                    err_email = ('E-mail уже зарегистрирован')
                else:
                    err_email = ('')
                driver.find_element(By.ID, "userregisterwelcomeform-email").clear()
                sleep(1)
                driver.find_element(By.ID, "userregisterwelcomeform-email").send_keys(
                    str(phone_u) + '@testmail.test')
                driver.find_element(By.XPATH, '//button[contains(@type,"button")]').click()
        else:
            sleep(0)
    except NoSuchElementException:
        sleep(0)
    print("Номер телефона:", "+700" + str(phone_u), "\n"
                                                    "e-mail:", str(phone_u) + "@testmail.test")

    sleep(1)


    sleep(1)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-dialog")]')))
    driver.find_element(By.ID, "userregisterphoneform-phone_confirm").send_keys("1111")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border")]').click()

###Общая информация
    wait.until(EC.visibility_of_element_located((By.ID, 'userregistercommonform-gender_id')))
    driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, '//button[contains(@type,"button")]'))
    driver.find_element(By.XPATH, "//*[text()='Мужской']").click()
# Место рождения
    driver.find_element(By.ID, "userregistercommonform-place_of_birth").send_keys("СССР")
# Дата рождения
    driver.find_element(By.ID, "userregistercommonform-date_of_birth").send_keys("01011981")
# Серия и номер паспорта
    driver.find_element(By.ID, "userregistercommonform-serial_p").send_keys("5001")
    driver.find_element(By.ID, "userregistercommonform-number_p").send_keys("000001")
# Кем выдан
    driver.find_element(By.ID, "userregistercommonform-place_of_issue").send_keys("Городским Отделением Выдачи Документов")
# Когда выдан
    driver.find_element(By.ID, "userregistercommonform-date_of_issue").send_keys("01012001")
# Адрес регистрации
    driver.find_element(By.XPATH, "//*[text()='Постоянная']").click()
    Select(driver.find_element(By.ID, 'userregistercommonform-region')).select_by_value('Москва')
    driver.find_element(By.ID, "userregistercommonform-city").send_keys("Американская область")
    driver.find_element(By.ID, "userregistercommonform-street").send_keys("Чистая")
    driver.find_element(By.ID, "userregistercommonform-house_number").send_keys("1")
    driver.find_element(By.ID, "userregistercommonform-block").send_keys("5")
    driver.find_element(By.ID, "userregistercommonform-apartment").send_keys("9")
    sleep(2)
    driver.find_element(By.XPATH, "//*[text()='Такой же']").click()
###
    pas_s1 = random.randrange(75, 99, 1)
    pas_s2 = random.randrange(10, 16, 1)
    pas_ser = (str(pas_s1) + str(pas_s2))
    driver.find_element(By.ID, "userregistercommonform-serial_p").send_keys(str(pas_ser))
    pas_num = random.randrange(100000, 999999, 1)
    driver.find_element(By.ID, "userregistercommonform-number_p").send_keys(str(pas_num))
    sleep(1)
    driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, '//button[contains(@type,"button")]'))
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@type,"button")]').click()
    sleep(2)

    try:
        if driver.find_element(By.XPATH, "//*[text()='Паспорт уже зарегистрирован']"):
            err_pas = driver.find_element(By.XPATH, "//*[text()='Паспорт уже зарегистрирован']")
            while err_pas != ("Паспорт уже зарегистрирован"):
                if driver.find_element(By.XPATH, "//*[text()='Паспорт уже зарегистрирован']"):
                    err_pas = ('Паспорт уже зарегистрирован')
                else:
                    err_pas = ('')
                driver.find_element(By.ID, "userregistercommonform-serial_p").clear()
                pas_s1 = random.randrange(75, 99, 1)
                pas_s2 = random.randrange(10, 16, 1)
                pas_ser = (str(pas_s1) + str(pas_s2))
                driver.find_element(By.ID, "userregistercommonform-serial_p").send_keys(str(pas_ser))
                sleep(1)
                driver.find_element(By.ID, "userregistercommonform-number_p").clear()
                pas_num = random.randrange(100000, 999999, 1)
                driver.find_element(By.ID, "userregistercommonform-number_p").send_keys(str(pas_num))
                driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[
                    0].click()
                sleep(1)
        else:
            sleep(0)
    except NoSuchElementException:
        sleep(0)
    sleep(1)


###Дополнительная информация
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Дополнительная информация"))  # Дождаться загрузки страницы
    Select(driver.find_element(By.ID, 'userregisteradditionalform-has_work')).select_by_value('1')
    sleep(1)

###Работа по найму
    driver.find_element(By.ID, 'clientworkdata-8-organization_name').send_keys("ООО РиК")
    driver.find_element(By.ID, 'clientworkdata-8-number_phone').send_keys("0010020001")
    driver.find_element(By.ID, 'clientworkdata-8-actual_address_id').send_keys("ул.Рабочая, дом 1")
    Select(driver.find_element(By.ID, 'clientworkdata-8-work_experience')).select_by_value('1')
    driver.find_element(By.ID, "clientworkdata-8-other_sources_income").send_keys("Специалист ООО")
    driver.find_element(By.ID, "clientworkdata-8-monthly_income").send_keys("987654")

    driver.find_element(By.XPATH, '//button[contains(@type,"button")]').click()
    sleep(1)

###Ожидаем автоматический отказ undefined
    #####

###Админка, первичное одобрение
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get(link)
    wait_adm.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Быстрый займ"))  # Дождаться загрузки страницы
    sleep(1)
    #driver_adm.set_window_size(550, 550)
    # driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
            driver_adm.find_elements(By.XPATH, '//a[contains(@data-href,"/auth/login")]')[1].click()
            wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-dialog")]')))
            sleep(1)
            driver_adm.find_elements(By.ID, "loginform-login")[1].send_keys(admin)
            driver_adm.find_elements(By.ID, "loginform-password")[1].send_keys(pas_adm)
            driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)
    if True:
        try:
            driver_adm.find_element(By.LINK_TEXT, "Войти").click()
            wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal__title")]')))
            sleep(1)
            driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
            driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
            sleep(1)
            driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)

    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    try:
        driver_adm.find_element(By.XPATH, '//a[contains(@data-href,"/manager/pre-request/reject-cancel")]').click()
        wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"col-12")]')))
        driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
        sleep(1)
    except NoSuchElementException:
        sleep(0)
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    uid = driver_adm.current_url.split("cid=")[-1]
    print("id - " + uid)
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"btn-success")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-title")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait_adm.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-title")]')))
    driver_adm.quit()
###END_Админка, первичное одобрение

    try:
        driver.find_element(By.XPATH, '//a[contains(@class,"sharp-word")]').click()
        print("CSS")
        sleep(1)
    except NoSuchElementException:
        sleep(0)




###Закончить регистрацию
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Закончить регистрацию']")))
    driver.find_element(By.XPATH, "//*[text()='Закончить регистрацию']").click()
###Выберите удобный способ идентификации
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*/h2"), "Идентификация"))
   
###Идентификация по паспорту
    driver.find_elements(By.XPATH, '//input[contains(@type,"radio")]')[2].click()
   
    driver.find_element(By.XPATH, "//*[text()='Продолжить']").click()
###Идентификация по фотографиям
    sleep(2)

    print(driver.find_element_by_xpath('//div[contains(text(), "Вы выбрали идентификацию по фотографиям")]').text)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"image-select-view")]')))
   

    driver.find_element(By.ID, 'userregisterfilesform-clientphoto').send_keys(path_img + "photo_1.jpg")
    driver.find_element(By.ID, 'userregisterfilesform-passportphoto1').send_keys(path_img + "photo_2.jpg")
    driver.find_element(By.ID, 'userregisterfilesform-passportphoto2').send_keys(path_img + "photo_3.jpg")
    driver.find_element(By.ID, 'userregisterfilesform-passportphotopast').send_keys(path_img + "photo_4.jpg")
    sleep(1)
    driver.find_element(By.XPATH, "//*[text()='Продолжить']").click()
   
###Привязка карты
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Привязка карты"))
    # driver.find_element(By.XPATH, "//*[text()='Добавить карту']").click()
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Оплата займа"))
    #
    # driver.find_element(By.ID, 'cardFrom').send_keys("8888555511113333")
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Неверный номер карты"))
    # sleep(2)
    # driver.find_element(By.ID, 'cardFrom').clear()
    #
    # driver.find_element(By.ID, 'cardFrom').send_keys("388555111133332455")
    # sleep(1)
    # driver.find_element(By.ID, 'cardFrom').click()
    # driver.find_element(By.ID, 'cardFrom').send_keys("55")
    # driver.find_element(By.ID, 'cardFrom').click()
    # driver.find_element(By.ID, 'cardFrom').send_keys("5")
    # driver.find_element(By.ID, 'cardDate').send_keys("8787")
    # driver.find_element(By.ID, 'cvc').send_keys("654")
    # driver.find_element(By.ID, 'submitButton').click()
    #
    # wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Привязать карту не получилось!"))
    # sleep(2)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Привязка карты"))
    driver.find_element(By.XPATH, "//*[text()='Добавить карту']").click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Оплата займа"))
    driver.find_element(By.ID, 'cardFrom').send_keys(card_num)
    driver.find_element(By.ID, 'cardDate').send_keys(card_date)
    driver.find_element(By.ID, 'cvc').send_keys(card_cvc)
    driver.find_element(By.ID, 'submitButton').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Назад']")))
    driver.find_element(By.XPATH, "//*[text()='Назад']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class,"btn-danger-border")]')))
    driver.find_element(By.XPATH, "//*[text()='Удалить карту']").click()
    sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class,"btn btn-default")]')))
    driver.find_element(By.XPATH, "//*[text()='Добавить карту']").click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*"), "Оплата займа"))
    driver.find_element(By.ID, 'cardFrom').send_keys(card_num)
    driver.find_element(By.ID, 'cardDate').send_keys(card_date)
    driver.find_element(By.ID, 'cvc').send_keys(card_cvc)
    driver.find_element(By.ID, 'submitButton').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"image-select-view__empty")]')))
    driver.find_element(By.ID, 'userregisterfilesform-cardphoto').send_keys(path_img + "card.jpg")
    sleep(1)
    driver.find_element(By.XPATH, "//*[text()='Продолжить']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"btn btn-danger")]')))
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

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
            driver_adm.find_elements(By.XPATH, '//a[contains(@data-href,"/auth/login")]')[1].click()
            wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-dialog")]')))
            sleep(1)
            driver_adm.find_elements(By.ID, "loginform-login")[1].send_keys(admin)
            driver_adm.find_elements(By.ID, "loginform-password")[1].send_keys(pas_adm)
            driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
        except:
            sleep(0)
    if True:
        try:
            driver_adm.find_element(By.LINK_TEXT, "Войти").click()
            wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal__title")]')))
            sleep(1)
            driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
            driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
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
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]')))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    sleep(1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa-sign-out")]')))
    driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
   
finally:
    print("Выполнил!")
    sleep(2)
    driver.quit()
########################
###First_Registration###
########################