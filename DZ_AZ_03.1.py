import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000) #### Генерация случайных чисел

plt.hist(data, bins=50, color='skyblue', edgecolor='black')  #### Построение гистограммы

plt.title('Гистограмма нормального распределения') #### Добавление заголовков и меток
plt.xlabel('Значения')
plt.ylabel('Частота')

plt.show()  #### Выводим график
