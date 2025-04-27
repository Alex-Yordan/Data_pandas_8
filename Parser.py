import time #### Импортируем модуль со временем
import csv #### Импортируем модуль csv
from selenium import webdriver #### Импортируем Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox() #### Инициализируем браузер
url = "https://www.divan.ru/volgograd/category/divany-i-kresla?types%5B%5D=54&types%5B%5D=1&types%5B%5D=4" #### В отдельной переменной указываем сайт, который будем просматривать
driver.get(url) #### Открываем веб-страницу

try:  #### Ожидаем загрузку карточек товаров
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'LlPhw'))
    )
except Exception as e:
    print(f"Ошибка при загрузке страницы: {str(e)}")
    driver.quit()
    exit()

#### Находим все карточки с помощью названия класса
divans = driver.find_elements(By.CLASS_NAME, 'LlPhw') #### Названия классов берём с кода сайта

print(divans) #### Выводим на экран товары

parsed_data = [] #### Создаём список, в который потом всё будет сохраняться

for divan in divans:
    try:
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text.replace('руб.', '').strip() #### Находим цену товара

        print(f"Цена: {price}") #### Выводим отладочную информацию

        parsed_data.append([price,])  #### Вносим найденную информацию в список

    except:  #### Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
        print(f"Произошла ошибка при парсинге")
        continue


driver.quit() #### Закрываем подключение браузер

#### Прописываем открытие нового файла, задаём ему название и форматирование
#### 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("divans.csv", 'w',newline='', encoding='utf-8-sig') as file:
    #### Используем модуль csv и настраиваем запись данных в виде таблицы
    writer = csv.writer(file) #### Создаём объект
    writer.writerow(['Цена товара']) #### Создаём первый ряд
    writer.writerows(parsed_data) #### Прописываем использование списка как источника для рядов таблицы

print("Парсинг завершен. Данные сохранены в файл divans.csv.")  #### Отчет