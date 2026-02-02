print("Hello, Assa!")       #приветствие, вход в программу

print("Домашнее задание № 2. Программа учёта времени учёбы за неделю")

# Ввод количества учебных дней (должно быть введено значение 7)

some_number = 7                     # Критерий годности

some_zero = 0                       # Критерий годности

some_day = int(input("Количество учебных дней: \n? =  " ))

# Ввод числа учебных дней и организация повторных запросов данных для получения корректного ввода

def get_valid_some_day():
while True: # Бесконечный цикл
try:
some_day = int(input("Введите количество учебных дней: "))
if age < 0:
print("Возраст не может быть отрицательным!")
continue # Возврат к началу цикла
if age > 120:
print("Укажите реальный возраст!")
continue
return age # Корректный ввод – выход из функции
except ValueError:
print("Введите числовое значение!")






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

class ValidationError(Exception):
    pass

def some_neg_element (element):

for i in range(some_number):
        print(day_week_tuple[i], end = "\n")

    try:
        day_week_hour[i] = int(input("Количество учебных часов: \n? =  " ))

        print('Число' , day_week_hour[i])

    except ValueError:

    print('Количество учебных часов не может быть равно нулю!')

    else:
    print(f'Вы ввели число {day_week_hour[i]}')

for i in range(some_number):
    
    if element < 0:

        raise ValidationError("Количество учебных часов не может быть отрицательным")

        enter
        
    
for i in range(some_day):    
            print(day_week_tuple[i] , day_week_hour[i] , end = " \n ")

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





