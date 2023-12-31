# 21. Площадь треугольника
# Площадь треугольника может быть вычислена с использованием следующей формулы, где b – длина основания
# треугольника, а h – его высота: area = b*h/2

# Напишите программу, в которой пользователь сможет вводить значения для переменных b и h, после чего
# на экране будет отображена площадь треугольника с заявленными основанием и высотой.

b = int(input('Введите длину треугольника (см): '))   # Запрашиваем данные от пользователя
h = int(input('Высота треугольника (см): '))

area = b * h / 2     # Вычисляем площадь треугольника по формуле

print('Площадь треугольника равна %i см' % area)    # Выводим результат


# 22. Площадь треугольника (снова)
# В предыдущем упражнении мы вычисляли площадь треугольника при известных длинах его основания и высоты.
# Но можно рассчитать площадь и на основании длин всех трех сторон треугольника. Пусть s1, s2 и s3 – длины
# сторон, а s = (s1 + s2 + s3)/2. Тогда площадь треугольника может быть вычислена по следующей формуле:
# area = √ s * (s - s1) * (s - s2) * (s - s3)

# Разработайте программу, которая будет принимать на вход длины всех трех сторон
# треугольника и выводить его площадь.

from math import sqrt

s1 = float(input('Введите длину первой стороны треугольника (см): '))    # Запрашиваем данные
s2 = float(input('Введите длину первой стороны треугольника (см): '))
s3 = float(input('Введите длину первой стороны треугольника (см): '))

s = (s1 + s2 + s3)/2      # Производим вычисление площади всех сторон 

area = sqrt((s * (s - s1) * (s - s2) * (s - s3)))   # Вычисляем площадь треугольника 

print('Площадь треугольника равна %.1f см' % area)   # Выводим результат 


# 23. Площадь правильного многоугольника
# Многоугольник называется правильным, если все его стороны и углы равны. Площадь такой фигуры можно вычислить
# по следующей формуле, в которой s – длина стороны, а n – количество сторон: area = n*s^2 / 4*tan(pi/n)

# Напишите программу, которая будет запрашивать у пользователя значения переменных s и n и выводить
# на экран площадь правильного многоугольника, построенного на основании этих величин.

from math import tan, pi

s = int(input('Введите длину стороны многоугольника (см): '))     # Запрашиваем данные
n = int(input('Количество сторон: '))

area = (n * s**2 / (4 * tan(pi/n)))  # Производим вычисления

print(f'Площадь правильного многоугольника равна %i см' % area)   # Выводим результат 


# 24. Единицы времени
# Создайте программу, в которой пользователь сможет ввести временной промежуток в виде количества
# дней, часов, минут и секунд и узнать общее количество секунд, составляющее введенный отрезок.

a = 86400    # Переводим дни в секунды
b = 3600     # Переводим часы в секунды
c = 60       # Переводим минуты в секунды


deys = int(input('Введите количество дней: '))            # Запрашиваем данные от пользователя
watch = int(input('Введите количество часов: '))
minutes = int(input('Введите количество минут: '))
seconds = int(input('Введите количество секунд: '))

sum_ = deys * a + watch * b + minutes * c + seconds      # Производим вычисление

print(f'Общее количество секунд, составляющее введенный отрезок %i' % sum_)   # Выводим результат 


# 25. Единицы времени (снова)
# В данном упражнении мы развернем ситуацию из предыдущей задачи.
# На этот раз вам предстоит написать программу, в которой пользователь будет вводить временной промежуток
# в виде общего количества секунд, после чего на экране должна быть показана та же длительность в формате
# D:HH:MM:SS, где D, HH, MM и SS – это количество дней, часов, минут и секунд соответственно. При этом
# последние три значения должны быть выведены в формате из двух цифр, как мы привыкли видеть их на электронных
# часах. Попробуйте узнать сами, какие символы необходимо ввести в спецификатор формата, чтобы при
# необходимости числа дополнялись слева не пробелами, а нулями.

# Переводим секунды в дни, часы, минуты и секунды

second_day = 86400
second_hour = 3600
second_minute = 60

time = int(input('Введите временной промежуток с секундах: '))     # Запрашиваем ввод от пользователя

d = time / second_day             # Производим вычисление 
time = time % second_day
hh = time / second_hour
time = time % second_hour
mm = time / second_minute
ss = time % second_minute

print("Длительность:", "%d:%02d:%02d:%02d" % (d, hh, mm, ss))     # Выводим результат 

