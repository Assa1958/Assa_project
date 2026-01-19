print("Hello, Assa!")       #приветствие, вход в программу

some_day = input("Day, \n? =")          #запрос даты работы - день
print(some_day)

some_month = input("Month, \n? =")         #запрос даты работы - месяц
print(some_month)

some_year = input("Year, \n? =")          #запрос даты работы - год
print(some_year)

print("some_data1, some_data2, some_data3" , some_day , some_month , some_year )  #дата работы с программой


# Модуль добавления товара в список
some_kind = input("Введите тип учебного материала (книга/видео): книга \n? =")      # вид товара (книга, видеофайл, другое)
print(some_kind)

while some_kind != 'книга':
    print("Это не книга!")
    some_kind = input("Введите тип учебного материала (книга/видео): книга \n? =")      # вид товара (книга, видеофайл, другое)
print(some_kind)

some_price = int(input("Введите стоимость материала (положительное число): 300   \n? ="))       # стоимость (цена) товара
print(some_price)    

while some_price < 0:
    print("Стоимость товара не может быть отрицательной величиной")
    print("Повторить ввод")        # новое значение стоимости
    some_price = int(input("Введите стоимость материала (положительное число): 300   \n? ="))
    print(some_price)

some_type = input("Введите категорию материала: математика   ? =")     # категория товара (математика, история)
print(some_type)

while some_type != 'математика':
    some_type = input("Введите категорию материала: математика   ? =")     # категория товара (математика, история)
print(some_type)

# Ожидаемый результат
print("Материал добавлен: Тип - книга, Стоимость - 300, Категория – математика" , some_kind, some_price, some_type)   


print("End programme")      # Конец работы программы
