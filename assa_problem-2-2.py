print("Hello, Assa!")       #приветствие, вход в программу

print("Домашнее задание № 2. Программа учёта времени учёбы за неделю")

some_number = 7                     # Критерий годности

some_zero = 0                       # Критерий годности

some_day = int(input("Количество учебных дней: \n? =  " ))
print("Количество учебных дней:" , some_day)

while some_day > some_number:
    print("Ошибка! Повторить ввод")
    some_day = input("Количество учебных дней \n? =  ")
    print("Количество учебных дней:" , some_day)

# Кортеж с наименованием дней недели
day_week_tuple = (
    "понедельник" ,   
    "вторник" ,
    "среда" ,
    "четверг" ,
    "пятница" ,
    "суббота" ,
    "воскресенье"
                   ) 

day_week_hour = [0,0,0,0,0,0,0]    # Количество учебных часов в учебный день

total = 0                           # Начальное значение суммы часов за неделю

for i in range(some_number):
    print(day_week_tuple[i], end = "\n")

    day_week_hour[i] = int(input("Количество учебных часов: \n? =  " ))

for i in range(some_day):    
            print(day_week_tuple[i] , day_week_hour[i] , end = " \n ")

for i in range(some_number):

    result = day_week_hour[i]
    
    try:
    
        result = some_zero

        # Исключение при равенстве элемента массива 0
                
    except ValueError:

       print("Количество учебных часов не может быть равным нулю!")

       # Этот блок не будет выполнен, так как возникло исключение

    else:

        print("Ошибок нет, результат:" , result)

    finally:

        print("Блок finally выполнен")

# Объявление класса пользовательского исключения

class NegativeNumberError (Exception):

    """Класс для пользовательского исключения при отрицательном числе."""

pass

def check_positive(some_element):
    
    if some_element < 0:

        # генерируем пользовательское исключение
        
        raise NegativeNumberError("Число не должно быть отрицательным!")
    
    return some_element

for i in range(some_number):

    try:
    
        check_positive(day_week_hour[i])
    
    except NegativeNumberError as e:
    
        print(f"Ошибка: {e}")

# Вывод отредактированного массива данных

for i in range(some_number):
    print(day_week_tuple[i], end = "\n")

    day_week_hour[i] = int(input("Количество учебных часов: \n? =  " ))

    print("Элемент массива:" , day_week_hour[i])

    for i in range(some_day):    
            print(day_week_tuple[i] , day_week_hour[i] , end = " \n ")

for num in day_week_hour:
    
    total += int(num)

    num = 0
     
print("Общее количество часов за неделю:" , total , end = ' \n ')

print("Конец программы")





