import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_pets_are_present(go_to_my_pets):
   '''Проверяем, что на странице "Мои питомцы" присутствуют все питомцы'''

   # Явное ожидание присутствия элемента статистики
   element = WebDriverWait(pytest.driver, 3).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

   # Сохраняем элементы статистики в переменную "statistic"
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

   # Получаем количество питомцев из данных статистики
   number_in_stat = statistic[0].text.split('\n')
   number_in_stat = number_in_stat[1].split(' ')
   number_in_stat = int(number_in_stat[1])

   # Явное ожидание присутствия карточки питомца
   element = WebDriverWait(pytest.driver, 3).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

   # Сохраняем элементы карточек питомцев в переменную "pets"
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем количество карточек питомцев
   number_of_pets = len(pets)

   # Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number_in_stat == number_of_pets

