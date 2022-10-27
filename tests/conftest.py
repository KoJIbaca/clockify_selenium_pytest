import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver_init(request):
      driver = webdriver.Chrome(executable_path=r'.\driver\chromedriver.exe')
      driver.get("https://www.clockify.me/")
      request.cls.driver = driver
      yield driver
      driver.quit()