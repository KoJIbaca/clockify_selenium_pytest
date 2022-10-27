import time
import pytest
import requests
from selenium.webdriver import Keys
import credentials
from info_message import Message


@pytest.mark.usefixtures("driver_init")
class Test_Web_UI:

    # Проверка стаутс-кода сервера
    def test_server_response(self):
        response = requests.get("https://www.clockify.me/")
        if response.status_code == 200:
            print('Запрос выполнен успешно!')
            assert True
        elif response.status_code == 404:
            print('Запрос не завершился успехом!')
            assert False

    # Процесс авторизации
    def test_auth_user(self):
        time.sleep(4)
        # Присвоение локаторов перменным
        input_email = self.driver.find_element('xpath', "//*[@id='email']")
        input_password = self.driver.find_element('xpath', "//*[@id='password']")
        login_button = self.driver.find_element("css selector",
                                                "[class='cl-btn cl-btn-block cl-btn-primary ng-tns-c428-1']")

        # Заполнение форм и авторизация
        input_email.send_keys(credentials.EMAIL)
        input_password.send_keys(credentials.PWD)
        login_button.send_keys(Keys.RETURN)

        # Поиск и проверка попадания на главную страницу
        time.sleep(4)
        button_start = self.driver.find_element('css selector',
                                                "[class='cl-btn cl-btn-primary cl-btn-sm cl-d-block cl-d-lg-custom-none ng-star-inserted']")
        Message.auth_message(button_start, 'Авторизация')

    # Переход к настройкам профиля
    def test_go_to_profile_settings(self):
        dropdown_menu = self.driver.find_element('css selector',
                                                 "[class='cl-p-0 cl-dropdown-toggle cl-no-arrow cl-d-flex']")
        dropdown_menu.click()
        Message.drop_menu(dropdown_menu, 'Меню')
        time.sleep(4)
        profile_settings = self.driver.find_element('xpath',
                                                    "//*[contains(text(), 'Profile settings') and @href='/user/settings']")
        profile_settings.click()

        # Проверка загрузки страницы натроек
        time.sleep(4)
        profile_text = self.driver.find_element('xpath', "//*[contains(text(), 'Profile settings')]")
        Message.profile_settings(profile_text)

    # Взаимодействие с полем изменение имени профиля
    def test_field_interact(self):
        time.sleep(4)
        name_field = self.driver.find_element('css selector',
                                              "[class='cl-form-control ng-untouched ng-pristine ng-valid']")
        change_button = self.driver.find_element('css selector',
                                                 "[class='cl-input-group-text cl-bg-white ng-star-inserted']")
        name_field.clear()
        name_field.send_keys("Helicopter")
        change_button.click()
        time.sleep(4)
        self.driver.find_element('css selector', "[class='cl-close cl-no-outline']").click()
        Message.name_change(name_field)
