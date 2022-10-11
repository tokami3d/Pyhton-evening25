# replase(old, new, (count)) - меняем  встроке old na new значение, если вы укажите count, то он заменит уго ровно count раз

# text = 'ha ha ha ha'
# res = text.replace('a', 'i',2)
# print(text)
# peint(f'res afternreplace: {res}')


# str1 = "hi my name is tokami"
# res = str1.replace('tokami', 'marsel')
# res = res.replace('marsel', ('tokami'))
# print(res)

# print(id("H"))
# print(id("H"))
# print(id("h"))
# print (id('j'))

# strip() убирает пробельные символы в начале и в конце строки 
# rstrip, lstrip
# text = input('enter the text:\n')
# print (text)
# print(len(text))
# res = text.strip()
# print(res)

# text = '     hello            '
# print(len(text))
# res = text.rstrip()
# print (res)
# print(len(res))

# print(dir(str))

# isdigit         проверяют 
# isnumeric          все ли наши строки 
# isdecimal   состоят из чисел
# from curses.ascii import isalnum


# text = '888jjm,mk'
# print(text.isdigit())
# num = int(text)
# print (num)
# print (type(num))
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
    # print('oops')

    # text = '\0030'
    # print(text)
    # print (text.isnumeric())

    # isalnum() - состоит ли наща строка их символов и чисел авфавита и керилиццы
# str1 = '56_a'

# print(str1.isalnum())

# isalpha()- состоит ли наша строка из латинского или кирилица алфовита
# text= 'hello'
# print(text.isalpha())

# islower()
# isapper
# istitle
# strl = 'My Name '
# print(strl.istitle())
# index(value, [start], [end], - выводит индекс значения value которым мы передаем в нашей строке

# text = 'Hello Woed! My name is tokami'
# print(text.index('tokami'))
# print(text[24])
# print(text.index('o')
# print(text.index('o')
# count(value, [start]) считает количество вхожденной value в нашей строки

# res = 0
# # text = 'hulla o o hulla'
# # print(text.count('hulla'))"
# kk= ('hello word my name is tokami')

# i = 1
# while i <= kk.count('o'):

#     # print(i)
#     i += 1   #инкремент
#     res = kk.index('o', res+1)
#     print(res)

# text = 'oooHello World! My name is John Snowooo'
# i = 0
# res = -1
# while i <   text.count('o'): #4
#     res = text.index('o', res+1)
#     print(res)
#     i += 1 # инкремент

# find(value  [start] [end] делает таэе самое что и индекс но есть одно отличие в том что 

# если value нет в строке то он возвращается в -1

# text = "hello"
# print(text.find('l'))
# print(text.find('hi'))

# swapcase() переводит все символы в противоположенный регистр
# upper() > все символы в верхний регистр , lower() анологично

# text = 'hello my naZe is marsel'
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# capitalize() переводит буквы в верхний регистр

# name = input('entere y name').capitalize()
# print(f' hello mr {name}') 

# title () переводит первые символы всех слов в первый регистр
# text = 'johne jamy dadsfmw fjnvnee ciojdsfne  siofjsdfh cijdosfn'
# print(text.title())
# print(text.capitalize())

#  split () дробит строку на несколько частей по разделителю который находится в строе все чсти строки созраняются в тип данных
text = ' i got secret and noo body know body know body know'
ls = text.split('secret')
print (ls)
print(len(ls))

# 'разжедитель .join(intrable(list))' - соеденяет строки которые находятся в лисет по разделителю'
result ='@'.join(ls)
print(result)