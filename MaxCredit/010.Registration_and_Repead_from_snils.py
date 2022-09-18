########################################
###Registration_and_Repead_from_snils###
########################################
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

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 90)
driver.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
#driver.maximize_window()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Даем быстрый займ"))  # Дождаться загрузки страницы

user = ('6620830315@mail.ru')
password = ('nq934946')
admin = ("hello@max.credit")
pas_adm = ("tt762396")
path_img = ('c://test/img/')
card_num = ('2200200111114591')
card_date = ('0522')
card_cvc = ('426')

try:
    summ_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[0]
    term_z = driver.find_elements(By.XPATH, '//span[contains(@class,"ui-slider-handle")]')[1]
    ActionChains(driver).click_and_hold(summ_z).move_by_offset(-10, 0).release().perform()
    ActionChains(driver).click_and_hold(term_z).move_by_offset(150, 0).release().perform()
    sleep(1)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div//form//button')))
    driver.find_element(By.XPATH, '//div//form//button').click()
    wait.until(EC.element_to_be_clickable((By.ID, "userregisterwelcomeform-last_name")))
    driver.find_element(By.ID, "userregisterwelcomeform-last_name").send_keys(str(random.choice(['Иванов', 'Петров', 'Сидоров', 'Орлов', 'Жуков', 'Васильев', 'Кузьнецов', 'Зуев', 'Кудряшов'])))
    driver.find_element(By.ID, "userregisterwelcomeform-first_name").send_keys(str(random.choice(['Иван', 'Петр', 'Василий', 'Олег', 'Евгений', 'Алексей', 'Константин', 'Данил', 'Максим', 'Глеб'])))
    driver.find_element(By.ID, "userregisterwelcomeform-middle_name").send_keys(str(random.choice(['Иваныч', 'Петрович', 'Васильевич', 'Артемович', 'Алексеевич', 'Олегович', 'Максимович', 'Юрьевич',' Витальевич', 'Генадьевич'])))
    phone_u = random.randrange(10000000, 99999999, 1)
    driver.find_element(By.ID, "userregisterwelcomeform-phone").send_keys("00" + str(phone_u))
    driver.find_element(By.ID, "userregisterwelcomeform-email").send_keys(
        str(phone_u) + '@testmail.test')
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    sleep(1)

    driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[0].click()
    sleep(1)
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
                driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[
                    0].click()
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
                driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[
                    0].click()
        else:
            sleep(0)
    except NoSuchElementException:
        sleep(0)
    print("Номер телефона:", "+700" + str(phone_u), "\n"
                                                    "e-mail:", str(phone_u) + "@testmail.test")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]')))
    sleep(1)
    driver.find_element(By.ID, "userregisterphoneform-phone_confirm").send_keys("1111")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"form-group field-userregistercommonform-gender_id required")]')))
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[1].click()
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    driver.find_element(By.ID, "userregistercommonform-place_of_birth").send_keys("Россия")
    driver.find_element(By.ID, "userregistercommonform-date_of_birth").send_keys("01011991")
    pas_s1 = random.randrange(75, 99, 1)
    pas_s2 = random.randrange(10, 16, 1)
    pas_ser = (str(pas_s1) + str(pas_s2))
    driver.find_element(By.ID, "userregistercommonform-serial_p").send_keys(str(pas_ser))
    pas_num = random.randrange(100000, 999999, 1)
    driver.find_element(By.ID, "userregistercommonform-number_p").send_keys(str(pas_num))
    driver.find_element(By.ID, "userregistercommonform-place_of_issue").send_keys("Выдан ОВД 01")
    driver.find_element(By.ID, "userregistercommonform-date_of_issue").send_keys("01012013")
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click()
    #driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click()
    Select(driver.find_element(By.ID, 'userregistercommonform-region')).select_by_value('Алтайский край')
    driver.find_element(By.ID, "userregistercommonform-city").send_keys("Алтай")
    driver.find_element(By.ID, "userregistercommonform-street").send_keys("Алтайская")
    driver.find_element(By.ID, "userregistercommonform-house_number").send_keys("10")
    driver.find_element(By.ID, "userregistercommonform-block").send_keys("101")
    driver.find_element(By.ID, "userregistercommonform-apartment").send_keys("123")
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[4].click()
    #driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[5].click()
    sleep(1)
    #Select(driver.find_element(By.ID, 'userregistercommonform-region_fact')).select_by_value('Ярославская область')
    #driver.find_element(By.ID, "userregistercommonform-city_fact").send_keys("Ярославль")
    #driver.find_element(By.ID, "userregistercommonform-street_fact").send_keys("Ярославская")
    #driver.find_element(By.ID, "userregistercommonform-house_number_fact").send_keys("101")
    #driver.find_element(By.ID, "userregistercommonform-block_fact").send_keys("123")
    #driver.find_element(By.ID, "userregistercommonform-apartment_fact").send_keys("1234")
    #driver.find_element(By.ID, "userregistercommonform-home_phone").send_keys("1200000156")
    #sleep(1)
    driver.find_elements(By.XPATH, '//button[contains(@class,"btn btn-default js-submit-button")]')[0].click()
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
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"form-group field-userregisteradditionalform-has_work required")]')))
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click()
    sleep(1)
    driver.find_element(By.XPATH, '//input[contains(@name,"ClientWorkData[7][monthly_income]")]').send_keys("13135")
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[1].click()
    sleep(1)
    Select(driver.find_element(By.ID, 'userregisteradditionalform-employment_type_id')).select_by_value('5')
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click()
    sleep(1)
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[3].click()
    #driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[4].click()
    sleep(1)
    driver.find_element(By.ID, "clientworkdata-8-organization_name").send_keys("ООО")
    driver.find_element(By.ID, "clientworkdata-8-number_phone").send_keys("1300000156")
    driver.find_element(By.ID, "clientworkdata-8-actual_address_id").send_keys("Адрес ООО")
    Select(driver.find_element(By.ID, 'clientworkdata-8-work_experience')).select_by_value('1')
    driver.find_element(By.ID, "clientworkdata-8-other_sources_income").send_keys("Специалист ООО")
    driver.find_element(By.ID, "clientworkdata-8-monthly_income").send_keys("987654")
    #driver.find_element(By.ID, "clientworkdata-6-organization_name").send_keys("ИП")
    #driver.find_element(By.ID, "clientworkdata-6-number_phone").send_keys("1400000156")
    #driver.find_element(By.ID, "clientworkdata-6-actual_address_id").send_keys("Адрес ИП")
    #driver.find_element(By.ID, "clientworkdata-6-monthly_income").send_keys("1234567")
    #driver.find_element(By.ID, "familiar-0-last_name").send_keys("Иванова")
    #driver.find_element(By.ID, "familiar-0-first_name").send_keys("Инна")
    #driver.find_element(By.ID, "familiar-0-middle_name").send_keys("Ивановна")
    #Select(driver.find_element(By.ID, 'familiar-0-familiar_type_id')).select_by_value('2')
    #driver.find_element(By.ID, "familiar-0-number_phone").send_keys("1500000156")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

# recognition():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-login header__profile-button js-login-button")]')))
    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))

    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.visibility_of_element_located(
        (By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()

    sleep(1)
    try:
        driver_adm.find_element(By.XPATH, '//a[contains(@href,"/manager/pre-request/review")]').click()
        #wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"col-12")]')))
        #driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
        sleep(1)
    except NoSuchElementException:
        sleep(0)


    try:
        driver_adm.find_element(By.XPATH, '//a[contains(@data-href,"/manager/pre-request/reject-cancel")]').click()
        wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"col-12")]')))
        driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
        sleep(1)
    except NoSuchElementException:
        sleep(0)
###



###
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    uid = driver_adm.current_url.split("cid=")[-1]
    print("id - " + uid)
    sleep(1)
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"btn btn-success")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-title")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait_adm.until(EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class,"modal-title")]')))
    driver_adm.quit()
    #####
    while True:
        try:
            driver.find_element(By.XPATH, '//button[contains(@type,"submit")]')
            break
        except:
            driver.refresh()
            sleep(2)
    #####
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"input-icon")]')))

######################
    sleep(2)
    print("загружаем фото СНИЛС")

    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[1].click()  # Идентификация по СНИЛС

    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()  # Продолжить
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"image-select")]')))  # Дождаться кнопки загрузки фотографий
    #driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[0].send_keys("c://test/photo/photo_1.jpg")
    driver.find_element(By.ID, "userregisterfilesform-passportphoto1").send_keys((path_img)+'pas_snils_1.jpg')
    driver.find_element(By.ID, "userregisterfilesform-passportphoto2").send_keys((path_img)+'pas_snils_2.jpg')
    driver.find_element(By.ID, "userregisterfilesform-passportphotopast").send_keys((path_img)+'pas_snils_3.jpg')
    driver.find_element(By.ID, "userregisterfilesform-painphoto").send_keys((path_img)+'pas_snils_4.jpg')
    sleep(2)
    driver.find_element(By.ID, "userregisterfilesform-snils").send_keys('00000000011')
    sleep(2)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()  # Продолжить
##################

    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]')))
    sleep(1)
    driver.find_element(By.ID, "usercheckpainform-code").send_keys("1111")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"btn-danger-border js-submit-button")]').click()
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"form-group field-userregistercommonform-gender_id required")]')))

    print("Дальше не идет")
finally:
    print("Выполнил!")
    sleep(2)
    driver.quit()
########################################
###Registration_and_Repead_from_snils###
########################################