# 1) С клавиатуры вводится натуральное число. Найти его наибольшую цифру.
# Например, введено число 764580. Наибольшая цифра в нем 8.

# def get_max(*numbers):
#     return (max(numbers))
# print(get_max(1,4,5,6,7,8))
#
# ##################################################

# 2) Вывести на экран ряд натуральных чисел от минимума до максимума с шагом. Например, если минимум 10,
#  максимум 35, шаг 5, то вывод должен быть таким: 10 15 20 25 30 35. Минимум, максимум и шаг указываются пользователем
# (считываются с клавиатуры).

# def calc(min, max, step):
#     result = ''
#     for number in range(min, max, step):
#         result += f"{str(number)}, "
#     return result
# print(calc(1, 10, 2))

# ###################################################

# 3) Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
#
# def get_fixed(number):
#     first_grade = number%10
#     second_grade = int(((number%100)/10))
#     third_grade = int((number/100)%10)
#     forth_grade = int((number/100)/10)
#     if third_grade == 0:
#         return str(first_grade) + str(second_grade)
#     elif forth_grade == 0:
#         return str(first_grade)+str(second_grade)+str(third_grade)
#     else:
#         return str(first_grade)+str(second_grade)+str(third_grade)+str(forth_grade)
#
# print(get_fixed(246))
# ##################################################

# 4) Найти сумму и произведение цифр, введенного натурального числа. Например, если введено число 325,
# то сумма его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).
# #
# def calc (number):
#     first_grade = number%10
#     second_grade = int(((number%100)/10))
#     third_grade = int((number/100)%10)
#     forth_grade = int((number/100)/10)
#     return f"{(forth_grade+third_grade+second_grade+first_grade)}\n" \
#            f"{(forth_grade*third_grade*second_grade*first_grade)}"
# print(calc(987))
# ##################################################

# 5) Вычислить факториал введенного числа
# #
# def calcFactorial(number):
#
#     faktorial = 0
#     while number >= 0:
#         faktorial += number
#         number -= 1
#     return faktorial
# print(calcFactorial(9))

# ##################################################


# 6) Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатурыa
#
#
# def cutHalf(n):
#     number = 1
#     storage = ''
#     for i in range(n):
#         result = number/2
#         number = result
#         storage += f"{str(number)}, "
#     return storage
# print(cutHalf(5))

# ##################################################

# 7) Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,  то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#
# def getResult(numbers):
#     outEven = ""
#     even = ""
#     for number in str(numbers):
#         if int(number)%2==0:
#             outEven += f"{number}, "
#         else:
#             even += f"{number}, "
#     return (f"четные цифры : {outEven}\nнечетные : {even}")
# print(getResult(56))
# ##################################################
#
# # 8) Вывести на экран столько элементов ряда Фибоначчи,
# # сколько указал пользователь. Например, если на ввод поступило число 6,
# # то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.
# #
#
# def Fibonacci(n):
#     fib1 = 0
#     fib2 = 1
#     result = ''
#     for procces in range(n):
#         fib_sum = fib1+fib2
#         fib1 = fib2
#         fib2 = fib_sum
#         result += f"{str(fib2)}, "
#     return result
# print(Fibonacci(5))

# ##################################################

# # 9) Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# #  Числа и знак операции вводятся пользователем.
# #  После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# #  Завершение программы должно выполняться при вводе символа ‘0’ в качестве знака операции.
# #  Если пользователь вводит неверный знак (не ‘0’, ‘+’, ‘-‘, ‘*’, ‘/’),
# #  то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# #  Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
# #
#
# def Calculator(a, b, operation):
#     while True:
#         if operation == '+':
#             return (int(a)+int(b))
#         elif operation == '-':
#             return (int(a)-int(b))
#         elif operation == '*':
#             return (int(a)*int(b))
#         elif operation == '/':
#             return (int(a)/int(b))
#         elif operation == '0':
#             break
#         else:
#             return ("Siz Qate Kiritdiniz!")
# print(Calculator(4,5,'+'))
#
# ##################################################
#
# 10) Необходимо суммировать все нечётные целые числа в диапазоне, который введёт пользователь с клавиатуры.

# def Sum(n):
#     number = 0
#     result = 0
#     while number < n:
#         number += 1
#         if number % 2 == 1:
#             result += number
#     return (f"сумма нечётные целые числа: {result}")
#
# print(Sum(5))
# ##################################################
#
# # 11) Организовать беспрерывный ввод чисел с клавиатуры, пока пользователь не введёт 0. После ввода нуля,
# # показать на экран количество чисел, которые были введены, их общую сумму и среднее арифметическое.
# # Подсказка: необходимо объявить переменную-счетчик, которая будет считать количество введенных чисел, и переменную,
# #  которая будет накапливать общую сумму чисел.
# #
# def getInfo():
#     storage = ''
#     sum = 0
#     while True:
#         number = (input("Enter your Number: "))
#         if number == '0':
#             print()
#             break
#         else:
#             storage += number
#             n_number = int(number)
#             sum += n_number
#     print(f"количество чисел: {len(storage)}")
#     print(f"общую сумму: {sum}")
#     print(f"среднее арифметическое: {float(sum/len(storage))}")
#
# getInfo()
# ##################################################

# 12) Напишите условие if для проверки, что значение переменной age НЕ находится в диапазоне 14 и 90 включительно.
# Напишите два варианта: первый с использованием оператора НЕ !, второй – без этого оператора

# def takeInfo(age):
#     while True:
#         allowed = 14 < age < 90
#         if not allowed:
#             return ("You are not alowed")
#         else:
#             return ("You are alowed")
#
# # print(takeInfo(15))
#
# def takeInfo(age):
#     while True:
#         allowed = 14 < age < 90
#         if allowed:
#             return ("You are alowed")
#         else:
#             return ("You are not alowed")
# print(takeInfo(25))
# ##################################################

# # 13) Напишите код, который будет спрашивать логин с помощью prompt.
# #  #  Если посетитель вводит «Админ», то prompt запрашивает пароль, если ничего не введено или нажата клавиша
# #  #  Esc – показать «Отменено», в противном случае отобразить «Я вас не знаю».
#   роль проверять так:
#
# Если введён пароль «Я главный», то выводить «Здравствуйте!»,
# Иначе – «Неверный пароль»,
# При отмене – «Отменено».
#
# def registrationBoard(login, password):
#     while True:
#         if login == "Админ":
#             if password == None:
#                 return "«Отменено»"
#             if password == "Я главный":
#                 return "«Здравствуйте!»"
#             else:
#                 return "«Неверный пароль»,"
#         else:
#             return "«Я вас не знаю»."
# print(registrationBoard("Админ", "Я главный"))

# ##################################################

# # 14)  С помощью цикла найдите сумму чисел от 1 до 100.

# def Sum1(n):
#     result = 0
#     for repeat in range(n+1):
#         result += repeat
#     return result
# print(Sum1(5))

# ##################################################

# # 15)
# Составьте программу, которая принимает с клавиатуры числа, пока не будет введено значение 0.
# Для каждого введенного с клавиатуры положительного числа, программа должна выводить на экран "плюс",
# # для каждого отрицательного – "минус".
#
# def checkNumbers(number):
#     while True:
#         if number < 0:
#             return "минус"
#         if number > 0:
#             return "плюс"
#         if number == 0:
#             return "Error"
# print(checkNumbers(0))
# ##################################################

# # 16) Составьте программу, которая принимает с клавиатуры числа, пока не будет введено значение 99.
# Программа должна подсчитать, сколько чисел было введено с клавиатуры (не считая значения 99)
# и вывести эту информацию на экран.

# def calcLen(*numbers):
#     storage = ''
#     for number in numbers:
#         if number != 99:
#             storage += str(number)
#         else:
#             return "_"
#
#     return f"{len(storage)} чисел было введено"
# print(calcLen(1, 2, 3, 4, 5, 3, 9, 8))

# ##################################################

# 17 Составьте программу, которая принимает с клавиатуры числа, пока их сумма остается меньше 100.
# По окончании ввода следует вывести на экран информацию о количестве введенных чисел и их сумме.

# def sendInfo (number):
#     a = 1
#     storage = ''
#     numbers = 0
#     for proces in range(number):
#         numbers += proces
#     storage += str(number)
#     if numbers < 100:
#         return (f"количестве введенных чисел: {len(storage)}\nи их суммa: {numbers}")
#     else:
#         return ""
# print(sendInfo(9))

# ##################################################

# # 18 Составьте программу, которая принимает с клавиатуры целое число, а затем выводит на экран последующие
# # ему целые числа, пока сумма этих чисел не превышает квадрата введённого числа.

# def getKvadrat(number):
#     summa = 0
#     kvadrat = number**2
#
#     for proces in range(number):
#         summa += proces
#
#     if summa < kvadrat:
#         return (int(number+1))
#
# print(getKvadrat(5))

# ##################################################

# # 19 Составьте программу, которая принимает с клавиатуры целые числа,
# # пока не будут введены друг за другом два одинаковых числа.
# # Программа должна вывести на экран сообщение о равенстве чисел, а также сумму этих чисел.
# //////////////////////////////////////////////////////////

# def getEqualNumbers(*numbers):
#     storage = ''
#     summa = 0
#     for number in numbers:
#         summa += number
#         if str(number) in storage:
#             return f"равенстве чисел: {number}\nсуммa: {summa}"
#         storage += f"{str(number)}, "
#
# print(getEqualNumbers(1, 2, 3, 4, 5, 6, 6))

# ##################################################

# # 20 Составьте программу, которая выводит на экран делители каждого числа от 1 до 9.
# //////////////////////////////////////////////////////////
# def dividerNumber(number):
#
#     result = ""
#     dividers = 1, 2, 3, 4, 5, 7, 8, 9
#     for divider in dividers:
#         if number % divider == 0:
#             result += f"{divider}, "
#     return result
#
# print(dividerNumber(80))



# ##################################################
# 21 Составьте программу, которая принимает с клавиатуры целое число, а затем проверяет, можно ли представить его
#  в виде суммы квадратов двух целых однозначных чисел.
# ввод: 98 ⇒ вывод: 98 можно представить в виде суммы квадратов 7 и 7)

# def cutHalf(number):
#     import math
#     half = number/2
#     result = int(math.sqrt(half))
#     if result:
#         return (f"ввод: {number}: ⇒ {number} можно представить в виде суммы квадратов {result} и {result}")
#
# print(cutHalf(20))

# ##################################################

# # 22 Составьте программу, которая принимает с клавиатуры количество очков, полученых в соревнованиях
# # по стрельбе каждым из 10 учеников класса, и выводит на экран лучший результат.
# # ввод: 92, 75, 83, 82, 96, 81, 88, 76, 93, 78 ⇒ вывод: лучший результат - 96 очков)

# def calculateScore(*score):
#     storage = ""
#     for n in score:
#         storage += f"{n}, "
#     return f"ввод: {storage} ⇒ вывод: лучший результат: {max(storage)}"
#
# print(calculateScore(3,4,5,6,7,8))


# /////////////////////////////////////////////////////////////////////////////////////////////


#   Class-Work TASK
#
# def getEvenNumbers(*numbers):
#
#     storage = ""
#     for number in numbers:
#         if number % 2 == 0:
#             storage += str(f"{number}, ")
#     return storage
#
# print(getEvenNumbers(1,2,3,4,5,6,7))
#
# def getOutEvenNumbers(*numbers):
#
#     storage = ""
#     for number in numbers:
#         if number % 2 == 1:
#             storage += str(f"{number}, ")
#     return storage
#
# print(getOutEvenNumbers(1,2,3,4,5,6,7))


# ##################################################
# ##################################################


