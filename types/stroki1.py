# string - строки
# "hello word"
# """
# """
# строки это набор последовательных симвалов. которые мы используем для хранение и представление текстовой информации
# набор методов и операций которых мы можем использовать с данными ввиле текста 
# индекцация это набор последовательности симвалов 
# например 

# name ='tokami'
# t = 0
# o =1
# k =2
# a =3
# m =4
# i = 5
# print(name)
# print(name[1])
# print(name[-1])

# a = 'birthday'
# print(a[1], a[2], a[4])
# индекцация начинаетя с нуля c конца с -1

# # срезы по индекцам 
# # [start;end; <step>]
# a = 'birthday'
# b = a [0:5]
# print (b)
# print(a[5:8])
# print(len(a))

# print (a[:5])
# print (a[0:])

# a = "улыбок тебе дед макар"
# b = 'hello word i\'m kimg'
# # print (a)
# # print(len(a))
# # print(a[0:12])


# print(a[::2])
# print(a[::-1])
# print(a[:6:-1])

# # конкотенация слов (слияние либо соеденение)
# world = 'hello'
# world1= 'world'
# probel= ' '
# result = world + probel + world1
# print(result)


# формамтирование строк 
# 1 с помощю знака процента % 
# с помощю знака .format()
# 3 интерполяция строк(f - строки)
# %
# name = input("entire y name")
# lname = input('enter y last name') 
# print('hello, my name is, name, lname')
# print('hello, my name is, + ' ' + name + '' lname')

# print('hello, my name is %s %s' %(name, lname))
# print ("hello my name is %s > %s" %(name, lname))

# .format
# print('hello, my name is {} {}'.format(name, lname))
#  f строки 
# print(f'my name is {name} -> {lname} !')
# 
# экранирование строк - это миханизм при помощи котрого модно вставлять символы и строки которые сложно ввести с клавиатуры в строку
# \n перенос строки 
# \t - горизанальная тобуляция 
# \v вертикальная тобуляция 


# name = 'tokami\ndz'
# lName = '\vdz'
# llname = '\tdz'
# print(name)
# print(lName)
# print(llname)
a = 20
b = a + 4
a = b*100
print(a)

from math import fabs

positive = 5
negative = -6

print(fabs(positive))
print(fabs(negative))