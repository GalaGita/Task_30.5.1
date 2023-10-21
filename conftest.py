import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('E://Python/pythonProject3/chromedriver.exe')

   # Открываем страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():

    # Явное ожидание активности поля "email"
    element = WebDriverWait(pytest.driver, 3).until(
        EC.element_to_be_clickable((By.ID, 'email')))

    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Явное ожидание активности поля "пароль"
    element = WebDriverWait(pytest.driver, 3).until(
        EC.element_to_be_clickable((By.ID, 'pass')))

    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Явное ожидание активности кнопки "Войти"
    element = WebDriverWait(pytest.driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

    # Нажимаем на кнопку "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Явное ожидание активности ссылки "Мои питомцы"
    element = WebDriverWait(pytest.driver, 3).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Мои питомцы')))

    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
