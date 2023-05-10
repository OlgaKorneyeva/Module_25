from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(r'./chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('barsik@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('barsik123')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   #time.sleep(7)
   pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
   #time.sleep(7)

   #Определить, что у питомцев есть фото
   #//*[@id="all_my_pets"]/table/tbody/tr[1]/th/img
   photo = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')
   name = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   type = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
   age = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

   pet_info = pytest.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]')[0].text.splitlines()
   print ("photo=", len(photo))

   #1
   print (pet_info[1], ' = ',  ('Питомцев: ' + str(len(photo))))
   assert pet_info[1] == ('Питомцев: ' + str(len(photo)))

   count_photo = 0
   count_not_photo = 0

   unique_names = []
   for i in range(len(photo)):
      #2
      if photo[i].get_attribute('src') != ' ':
         count_photo = count_photo + 1
         print(i, end=";")
      else:
         count_not_photo = count_not_photo + 1

      #3
      assert (name[i].text.strip() != '' and type[i].text.strip() and age[i].text.strip())

      #4
      pet_name = name[i].text.strip()
      assert (not (pet_name in unique_names))
      unique_names.append(pet_name)

   assert count_photo >= count_not_photo



# Неявные ожидания
   driver = webdriver.Chrome()  # Pet photo
   driver.implicity_wait(10)
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   card_img_top = driver.find_element(By.CLASS_NAME, "card-img-top")
   print(card_img_top.text)

   driver = webdriver.Chrome() #Pet name
   driver.implicity_wait(10)
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   card_title = driver.find_element(By.CLASS_NAME, "card-title")
   print(card_title.text)

   driver = webdriver.Chrome() #Pet age
   driver.implicity_wait(10)
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   card_text = driver.find_element(By.CLASS_NAME, "card-text")
   print(card_text.text)


   #Явные ожидания
   driver = webdriver.Chrome()
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "navbar-brand header2"))
   )
   print(element)

   driver = webdriver.Chrome()
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "navbar-toggler-icon"))
   )
   print(element)

   driver = webdriver.Chrome()
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "btn btn-outline-secondary"))
   )
   print(element)

   driver = webdriver.Chrome()
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "btn btn-outline-success"))
   )
   print(element)

   driver = webdriver.Chrome()
   driver.get("https://petfriends.skillfactory.ru/my_pets")
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )
   print(element)


