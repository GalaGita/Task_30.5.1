import pytest
from selenium.webdriver.common.by import By

def test_there_are_a_name_age_and_gender(go_to_my_pets):
    '''Поверяем, что на странице "Мои питомцы" у всех питомцев есть фото, имя, возраст и порода'''

    # Неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Передаем в переменные элементы карточек питомцев
    images = pytest.driver.find_elements(By.XPATH, '//div[@id="all+my_pets"]//img')
    names = pytest.driver.find_elements(By.XPATH, '//div[@id="all+my_pets"]//td[1]')
    breeds = pytest.driver.find_elements(By.XPATH, '//div[@id="all+my_pets"]//td[2]')
    ages = pytest.driver.find_elements(By.XPATH, '//div[@id="all+my_pets"]//td[3]')

    # Организуем цикл, перебирающий элементы, и проверяем, что элемент не пустой
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''







