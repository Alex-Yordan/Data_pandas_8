import csv

def conv_price(price): #### Преобразуем цену в целое число
    return int(price.replace(' ', '').replace('руб.', '').strip())

input_file = 'divans.csv'  #### Чтение данных из исходного CSV файла и их обработка
output_file = 'conv_divans.csv'

with (open(input_file, mode='r', encoding='utf-8-sig') as infile, #### Читаем и записываем преобразованные данные в новый файл
      open(output_file, mode='w', newline='',encoding='utf-8-sig') as outfile):
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)    #### Читаем заголовок и записываем его в новый файл
    writer.writerow(header)

    for row in reader:       #### Обрабатываем и записываем данные строк
        clean_row = [conv_price(row[0])]
        writer.writerow(clean_row)

print(f"Данные успешно преобразованы и сохранены в файл {output_file}.")