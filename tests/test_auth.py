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
        self.driver.implicitly_wait(5)
        # Присвоение локаторов перменным
        input_email = self.driver.find_element('xpath', "//*[@id='email']")
        input_password = self.driver.find_element('xpath', "//*[@id='password']")
        login_button = self.driver.find_element("xpath", "//button[text() = ' Log In ']")

        # Заполнение форм и авторизация
        input_email.send_keys(credentials.EMAIL)
        input_password.send_keys(credentials.PWD)
        login_button.send_keys(Keys.RETURN)

        # Поиск и проверка попадания на главную страницу
        time.sleep(5)
        button_start = self.driver.find_element('xpath', "//a[text() = ' Upgrade ']")
        Message.auth_message(button_start, 'Авторизация')

    # Переход к настройкам профиля
    def test_go_to_profile_settings(self):
        dropdown_menu = self.driver.find_element('xpath', "//*[@id='topbar-menu']/div/div[2]/div[4]/div[2]/a")
        dropdown_menu.click()
        self.driver.implicitly_wait(5)
        Message.drop_menu(dropdown_menu, 'Меню')
        self.driver.implicitly_wait(5)
        profile_settings = self.driver.find_element('xpath',
                                                    "//*[contains(text(), 'Profile settings') and @href='/user/settings']")
        profile_settings.click()

        # Проверка загрузки страницы натроек
        self.driver.implicitly_wait(5)
        profile_text = self.driver.find_element('xpath', "//*[contains(text(), 'Profile settings')]")
        Message.profile_settings(profile_text)

    # Взаимодействие с полем изменение имени профиля
    def test_field_interact(self):
        self.driver.implicitly_wait(5)
        name_field = self.driver.find_element('xpath', "//input[@data-cy = 'profile-name']")
        name_field.clear()
        name_field.send_keys("Helicopter")
        self.driver.find_element('xpath', "//html").click()
        Message.name_change(name_field)
        time.sleep(3)
