#############################
###Reject_remarks_FULL+Fix###
#############################
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


user = ('6620830315@mail.ru')
password = ('nq934946')
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
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "Даем быстрый займ"))
    driver.find_element(By.XPATH, '//div//form//button').click()
    wait.until(EC.element_to_be_clickable((By.ID, "userregisterwelcomeform-last_name")))
    driver.find_element(By.ID, "userregisterwelcomeform-last_name").send_keys(str(random.choice(['Иванов', 'Петров', 'Сидоров', 'Орлов', 'Жуков', 'Васильев', 'Кузьнецов', 'Зуев', 'Кудряшов'])))
    driver.find_element(By.ID, "userregisterwelcomeform-first_name").send_keys(str(random.choice(['Иван', 'Петр', 'Василий', 'Олег', 'Евгений', 'Алексей', 'Константин', 'Данил', 'Максим', 'Глеб'])))
    driver.find_element(By.ID, "userregisterwelcomeform-middle_name").send_keys(str(random.choice(['Иваныч', 'Петрович', 'Васильевич', 'Артемович', 'Алексеевич', 'Олегович', 'Максимович', 'Юрьевич', ' Витальевич', 'Генадьевич'])))
    phone_u = random.randrange(10000000, 99999999, 1)
    driver.find_element(By.ID, "userregisterwelcomeform-phone").send_keys("00" + str(phone_u))
    driver.find_element(By.ID, "userregisterwelcomeform-email").send_keys(str(phone_u) + '@testmail.test')
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
    Select(driver.find_element(By.ID, 'userregistercommonform-region')).select_by_value('Алтайский край')
    driver.find_element(By.ID, "userregistercommonform-city").send_keys("Алтай")
    driver.find_element(By.ID, "userregistercommonform-street").send_keys("Алтайская")
    driver.find_element(By.ID, "userregistercommonform-house_number").send_keys("10")
    driver.find_element(By.ID, "userregistercommonform-block").send_keys("101")
    driver.find_element(By.ID, "userregistercommonform-apartment").send_keys("123")
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[4].click()
    sleep(1)
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
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"form-group field-userregisteradditionalform-has_work required")]')))
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[0].click()
    sleep(1)
    driver.find_element(By.ID, "clientworkdata-8-organization_name").send_keys("ООО")
    driver.find_element(By.ID, "clientworkdata-8-number_phone").send_keys("1300000156")
    driver.find_element(By.ID, "clientworkdata-8-actual_address_id").send_keys("Адрес ООО")
    Select(driver.find_element(By.ID, 'clientworkdata-8-work_experience')).select_by_value('1')
    driver.find_element(By.ID, "clientworkdata-8-other_sources_income").send_keys("Специалист ООО")
    driver.find_element(By.ID, "clientworkdata-8-monthly_income").send_keys("987654")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 90)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)

    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
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
    sleep(1)
    try:
        driver_adm.find_element(By.XPATH, '//a[contains(@href,"/manager/pre-request/review")]').click()
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
    driver.find_elements(By.XPATH, '//span[contains(@class,"input-icon")]')[2].click()
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"image-select")]')))
    driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[0].send_keys(path_img + "photo_1.jpg")
    driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[1].send_keys(path_img + "photo_2.jpg")
    driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[2].send_keys(path_img + "photo_3.jpg")
    driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[3].send_keys(path_img + "photo_4.jpg")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/register/card-add")]')))
    driver.find_element(By.LINK_TEXT, "Добавить карту").click()
    wait.until(EC.visibility_of_element_located((By.ID, 'cardFrom')))
    driver.find_element(By.ID, 'cardFrom').send_keys(card_num)
    driver.find_element(By.ID, 'cardDate').send_keys(card_date)
    driver.find_element(By.ID, 'cvc').send_keys(card_cvc)
    driver.find_element(By.XPATH, '//input[contains(@id,"submitButton")]').click()
    wait.until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"image-select-view__empty-caption")]')))
    driver.find_elements(By.XPATH, '//input[contains(@type,"file")]')[0].send_keys(path_img + "card.jpg")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"bank-card")]')))
    driver.find_element(By.XPATH, '//button[contains(@class,"js-submit-button")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 60)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)

    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-user_lock")]')))
    #Перенести в свободные
    if True:
        try:
            driver_adm.find_element(By.ID, 'user_verify_check')
            driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
        except:
            sleep(0)

    sleep(1)
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(EC.visibility_of_element_located((By.ID, 'user_verify_check')))
    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('4')
    sleep(1)

    remarkA = Select(driver_adm.find_element(By.ID, 'user_verify_comment_data')).select_by_value('2')
    remarkB = Select(driver_adm.find_element(By.ID, 'user_verify_comment_data')).select_by_value('1')
    remarkC = Select(driver_adm.find_element(By.ID, 'user_verify_comment_data')).select_by_value('4')
    remarkD = Select(driver_adm.find_element(By.ID, 'user_verify_comment_data')).select_by_value('6')
    remarkE = Select(driver_adm.find_element(By.ID, 'user_verify_comment_data')).select_by_value('12')
    remarkF = Select(driver_adm.find_element(By.ID, 'user_verify_comment_data')).select_by_value('666')
    ActionChains(driver_adm).key_down(Keys.CONTROL).click(remarkA).key_up(Keys.CONTROL).perform()
    ActionChains(driver_adm).key_down(Keys.CONTROL).click(remarkB).key_up(Keys.CONTROL).perform()
    ActionChains(driver_adm).key_down(Keys.CONTROL).click(remarkC).key_up(Keys.CONTROL).perform()
    ActionChains(driver_adm).key_down(Keys.CONTROL).click(remarkD).key_up(Keys.CONTROL).perform()
    ActionChains(driver_adm).key_down(Keys.CONTROL).click(remarkE).key_up(Keys.CONTROL).perform()
    ActionChains(driver_adm).key_down(Keys.CONTROL).click(remarkF).key_up(Keys.CONTROL).perform()
    sleep(1)

    driver_adm.find_element(By.XPATH, "//textarea[@id='userverifyphotoform-comment_client']").send_keys(
        str("Исправь - Паспорт: Основное \n Исправь - Фотография клиента \n Исправь - Сведенья о ранее выданном паспорте \n Исправь - Паспорт: Прописка \n Исправь - Фото с ярлыком \n Исправь - Другое"))
    driver_adm.find_element(By.XPATH, "//textarea[@id='userverifyphotoform-comment_manager']").send_keys(
        str("Ждем: \n Исправь Паспорт: Основное \n, Исправь Фотография клиента \n, Исправь Сведенья о ранее выданном паспорте \n Исправь - Паспорт: Прописка \n Исправь - Фото с ярлыком \n Исправь - Другое"))
    sleep(1)
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)

    driver_adm.quit()

    #####
    while True:
        try:
            driver.find_element(By.XPATH, '//a[contains(@class,"btn-primary")]')
            break
        except:
            driver.refresh()
            sleep(2)
    #####
    driver.find_element(By.XPATH, '//a[contains(@class,"btn-primary")]').click()
    sleep(2)
    driver.find_element(By.ID, "photodata-passportphoto1").send_keys(path_img + "change_pas_2.jpg")
    driver.find_element(By.ID, "photodata-clientphoto").send_keys(path_img + "new_pas_3.jpg")
    driver.find_element(By.ID, "photodata-passportphotopast").send_keys(path_img + "about_previously_issued_passports.jpg")
    driver.find_element(By.ID, "photodata-passportphoto2").send_keys(path_img + "registration.jpg")
    driver.find_element(By.ID, "photodata-clientlabelphoto").send_keys(path_img + "costomer_tag.jpg")
    sleep(1)

    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "мы рассматриваем Вашу заявку"))

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 60)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)

    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    sleep(0)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-user_lock")]')))
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-xs btn-danger js-ajax-modal")]')))
    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('2')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/card")]')[0].click()
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"client-card-verify")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"btn btn-danger")]')))
    print("Вернуть карту")
    sleep(1)

    Select(driver_adm.find_element(By.ID, 'clientcardverifyform-verified')).select_by_value('5')
    print("ищем")
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="clientcardverifyform-commentclient"]')))
    driver_adm.find_element(By.ID, 'clientcardverifyform-commentclient').click()

    sleep(1)
    print("Найдено")
    driver_adm.find_element(By.XPATH, '//*[@id="clientcardverifyform-commentclient"]').send_keys("Исправь - Загрузить новое изображение карты \n")
    print("замечание")

    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    driver_adm.quit()
    #####
    while True:
        try:
            driver.find_element(By.XPATH, '//a[contains(@class,"btn-primary")]')
            break
        except:
            driver.refresh()
            sleep(1)
    #####
    driver.find_element(By.XPATH, '//a[contains(@class,"btn-primary")]').click()
    sleep(1)
    driver.find_element(By.ID, "photodata-cardphoto").send_keys(path_img + "new_card_1.jpg")
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver_adm: WebDriver = webdriver.Chrome(options=options)
    wait_adm = WebDriverWait(driver_adm, 60)
    driver_adm.get('https://dev.max.credit/jdfh47jhgyer746734jfyeonyebx3jk')
    #driver_adm.maximize_window()
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)

    driver_adm.find_element(By.LINK_TEXT, "Личный кабинет").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"h4 modal-title")]')))
    sleep(1)
    driver_adm.find_element(By.ID, "loginform-login").send_keys(admin)
    driver_adm.find_element(By.ID, "loginform-password").send_keys(pas_adm)
    driver_adm.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[1].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"header__profile-sign-out")]')))
    driver_adm.find_element(By.CSS_SELECTOR, '.select2-selection__arrow').click()
    driver_adm.find_elements(By.XPATH, '//li[contains(@class,"select2-results__option")]')[0].click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@target,"_blank")]')[0].click()
    driver_adm.switch_to.window(driver_adm.window_handles[1])
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/manager/credit-history/")]')))
    sleep(0)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/client")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"js-user_lock")]')))
    driver_adm.find_element(By.XPATH, '//a[contains(@class,"js-user_lock")]').click()
    wait_adm.until(
        EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn btn-xs btn-danger js-ajax-modal")]')))
    Select(driver_adm.find_element(By.ID, 'user_verify_check')).select_by_value('2')
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)
    driver_adm.find_elements(By.XPATH, '//a[contains(@href,"/manager/user-verify/card")]')[0].click()
    driver_adm.find_elements(By.XPATH, '//a[contains(@class,"client-card-verify")]')[0].click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"btn btn-danger")]')))
    print("Вернуть карту")
    Select(driver_adm.find_element(By.ID, 'clientcardverifyform-verified')).select_by_value('3')
    sleep(1)
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
    sleep(1)
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btn-primary js-ajax-modal")]')))
    driver_adm.find_element(By.LINK_TEXT, "Одобрить").click()
    wait_adm.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@type,"submit")]')))
    driver_adm.find_element(By.XPATH, '//button[contains(@type,"submit")]').click()
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

    print("Займ получен")
    sleep(3)
    driver.find_element(By.XPATH, '//button[contains(@class,"js-return-credit")]').click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//span[contains(@class,"ui-slider-handle ui-state-default ui-corner-all")]')))
    driver.find_elements(By.XPATH, '//button[contains(@type,"submit")]')[0].click()
    sleep(1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div"), "У Вас нет непогашенных займов"))
    print("Займ закрыт")
    if True:
        try:
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title')
            driver_adm.find_element(By.CSS_SELECTOR, 'span.title').click()
        except:
            sleep(0)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//i[contains(@class,"fa-sign-out")]')))
    driver.find_element(By.XPATH, '//i[contains(@class,"fa-sign-out")]').click()
    print("Выход")
finally:
    print("Выполнил!")
    sleep(2)
    driver.quit()
#############################
###Reject_remarks_FULL+Fix###
#############################