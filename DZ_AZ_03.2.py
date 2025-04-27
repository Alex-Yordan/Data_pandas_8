import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)  #### Генерация 5 случайных чисел для оси X
y = np.random.rand(5)  #### Генерация 5 случайных чисел для оси Y

plt.scatter(x, y, color='skyblue') #### Построение диаграммы рассеяния

plt.title('Диаграмма рассеяния') #### Добавление заголовков и меток осей
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

plt.show() #### Выводим график
