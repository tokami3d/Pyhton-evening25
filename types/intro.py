#типы данных в питоне

# 1.NoneType - Ничего, пустота -> None 
# 2. Boolean - истина или лож -> True/False 
# 3. str() -Строки -> 'Hello world', "Hello world"
# 4. Чтсловые типы данных:
    #    a. integer - int() -целое число(-1,-2,0,1,) 
    #    b. float() -Чисо в плавающей точкой (-1.2, 10.5, 2.7 ...)
    #    c. complex() - Koплексные числа (3+5i6)
#  5. списковые типы данных:  
    #    a. list(список/массив) - [1, 2, 3, None, 'Hello' True False]
    #    b. tuple (кортеж)  -> (1,2,3,None)
    #    c. range(последовательность) -> range(1, 10)
# 6. set() -> Множество     
# 7. dict(словари) -> содержит данные в виде ключа и значения -> {1: 'One', 2: 'Two'}
# *************************************************************************************************
# Mutable(изменяемые типы данных)
#     1. list
#     2. set
#     3. dict

# Immitable(Изменяемые типы данных)
#     1.NoneType
#     2. boolean
#     3. int float complex
#     4. Str 
#     5. range 
#     6. tuple 
#     7. frozenset
# ********************************************************************************************************
# стандартный вывод данный
# *****************
# в пайтоне для вывода данных на терминал используется встроенная функция print()
# ***************

# print ('whatupp word!')
# print ('20')

# '''стандарный ввод данных'''
# ,,,через терминал используется через функцию input()
# a = input ("введите число" )
# print (в а хранится ;'')
# print (a)

# print (input('введите свое имя:'))


# Name = tuple('helllo word')
# name = input('вавелите свое имя')
# age = input('сколько вам лет?')
# hobbi = input('и так,'+name +'  у тебя есть хобби?')
# h = input('name' +'знаком ли ты с моим создателем?')



# dir - возвращает методы обьекта или функуции определенного мводулья 
 
# import math

# print(dir(math)

# a, b ,c = 1,2,3

# v = 5
# n = 7
# d = 3
# v, d, n, = d, v, n
# print (v, n, d)



# num1 = 10
# num2 = 3
# num3 = num1 
# num1 = num2
# num2 = num3

# print('hello' * 3)

# print(strl + str(num1))

# инкремент - увелечение значение какой либо переменной пример a = 1 (a += >) =  a = a + 1

# a = 0
# a += 1
# print(a)

# декримент - уменьшение занчение какой либо переменной 

# a = 0
# a-= 1
# print (a)

# *
# a = 5
# a*=a
# print(a)

# /
# a = 10
# a /=2
# print (a)

# id() > номер ячейки памяти



# a = 1
# b = a
# print(id(a))
# print(id(b))

# print(id(b)), (id(a))

# type ()> выводит тип заданной преременной 
# a = 9
# b = 'hello'

# print(type(a))
# print(type(b))

# var = int(input('введите число'))

# kaka = int(input('сколько тебе лет'))
# kfkf = int(input('введи число'))
# print(kaka ** kfkf)

# # модуль random - предоставляет нам функции для генерации случайных чисел, букв, симвалов 

# import random
# # print(dir(random))

# num = random.randint(11111,99999)
# print(num)

# from random import choice
# import string 

# print(string.ascii_letters)
# a = choice(string.ascii_letters)
# print(a)

# переметр 2 * r * pi
#площадь зш * (к **2)

# r = int(input('веддиье радиус;'))
# result_(плозадь окрудности', round(resilt_s))
# print('перимерт окурдности')



# ; орераторы сравнение \
# ; условыне операторы
# ; логические опреаторы
# ;оператор сравнение
# ; ; <,>, ==(ровно) <=, >=, !=ыне равно
# ; 1 < 5 >true
# ; 7>9 >false
  


# n = 20
# n1 = 17
# print(n <= n1)

# st1 = 'hello'
# st2 = 'word'

# print(ord('H'))

# # print (st1 >     st2)



# # num = 15
# # num2 = 16
# # print(num == num2)

# print(chr(1080))
# print(len(st1) > len(st2))

# условные операторы 

# if, elif, else.

# if <condition>;  
# <dody if> #cрабатывыает если во всех выше стоящих условиях пришло false
# elif

# st = input('enter something')
# if st.lower == 'hello':
#     print('hello mazafucka!')
# elif st.lower == 'tooo':
#     print('welcom bake asdnasouecsacmsdivmeie')
# elif st.lower == 'abra karabra':
#     print ('sim salabim')
# else:
#     print( 'what the hall you tolking about')
    

# email = input('enter the email')
# pw = input('enter y e password')
    
# if len(pw) < 8:
#         raise ValueError('password too short!')

# pw2 = input('enter the password confirmation : ')

# if pw2 != pw:
#     raise ValueError ('password didnt match!')

# else:
# #     print('successfully sined up!')
# age = input('entire y age')
# if age.isdigit():
#     print ('urraaaaa')
# else:
#     raise Exception('Invalid values')
# else:
#     print('you can bay it!')

# длогические операторы 
# and > логическое и 
# or логическое или 
# not логическое отрицание 

myage = 20
youage = 18
result = myage == 20 and youage == 19
print( result)

result =myage == 20 or youage == 19
print (result)
result = not myage == 200
print(result)