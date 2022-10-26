import time
import pytest
from selenium.webdriver import Keys
from credentials import credentials
from info_message import messages


@pytest.mark.usefixtures("driver_init")
class Test_Web_UI:
# Процесс авторизации
   def test_auth_user (self):
      time.sleep(4)
      input_email = self.driver.find_element('xpath', "//*[@id='email']")
      input_password = self.driver.find_element('xpath', "//*[@id='password']")
      login_button = self.driver.find_element("css selector", "[class='cl-btn cl-btn-block cl-btn-primary ng-tns-c424-1']")

      # Заполнение форм и авторизация
      input_email.send_keys(credentials.EMAIL)
      input_password.send_keys(credentials.PASSWORD)
      login_button.send_keys(Keys.RETURN)

      # Поиск и проверка попадания на главную страницу
      time.sleep(4)
      button_start = self.driver.find_element('css selector', "[class='cl-btn cl-btn-primary cl-btn-sm cl-d-block cl-d-lg-custom-none ng-star-inserted']")
      messages.auth_message(button_start,'Авторизация')


# Переход к настройкам профиля
   def test_go_to_profile_settings(self):
      dropdown_menu = self.driver.find_element('css selector', "[class='cl-p-0 cl-dropdown-toggle cl-no-arrow cl-d-flex']")
      dropdown_menu.click()
      messages.drop_menu(dropdown_menu, 'Меню')
      time.sleep(4)
      profile_settings = self.driver.find_element('xpath', "//*[contains(text(), 'Profile settings') and @href='/user/settings']")
      profile_settings.click()

      # Проверка загрузки страницы натроек
      time.sleep(4)
      profile_text = self.driver.find_element('xpath', "//*[contains(text(), 'Profile settings')]")
      messages.profile_settings(profile_text)

# Взаимодействие с полем изменение имени профиля
   def test_field_interact(self):
      time.sleep(4)
      name_field = self.driver.find_element('css selector', "[class='cl-form-control ng-untouched ng-pristine ng-valid']")
      change_button = self.driver.find_element('css selector', "[class='cl-input-group-text cl-bg-white ng-star-inserted']")
      name_field.clear()
      name_field.send_keys("Helicopter")
      change_button.click()
      time.sleep(4)
      self.driver.find_element('css selector', "[class='cl-close cl-no-outline']").click()
      messages.name_change(name_field)