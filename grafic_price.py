import pandas as pd
import matplotlib.pyplot as plt

file_path = 'conv_divans.csv'  #### Загружаем данные из CSV-файла
data = pd.read_csv(file_path)

prices = data['Цена товара']  #### Нужно знать точное название столбца с ценами

plt.hist(prices, bins=25, edgecolor='black')  #### Построение гистограммы
# Мы можем изменить количество bin-ов по своему усмотрению

plt.title('Гистограмма цен') #### Добавление заголовка и меток осей
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show() #### Вывод гистограммы