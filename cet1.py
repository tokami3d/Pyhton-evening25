# # множесто на пайтоне - это некий контейнер который содердит в себе уникальные элементы в не упорядоченом ввиде 
# {}!!!

# a = {a: 'a'} = словарь
# a = {1,2,3} = множество 


# set_ = {8,1,2,3,4,5,6,7,7,7,7,7}
# print(set_)
# print(type(set_))

# ls = [1,2, 'a', 0,False, True, 'n']
# str1 = 'my name is tokami'
# ls.extend(str1)
# # print(ls)
# # res =  list(set(ls))
# # print(res)

# set1 = {*ls}
# # print(set1)
# # print(type(set1))

# res = [*set1]
# print(type(res))
# # print (res)

# # fif0
# rint(a)
# a.pop()
# print(a)

# remove/discard
#  remove - Error
# discard - none


# set_ = {1,2,3,4,5,6,7}
# set_.discard(4)
# set_.remove(8)
# print(set_)


# frozenset
# a =  {1,2,3,4,5}
# # f_set = frozenset([1,2,3,4,5])
# print(type(a))
# print(type(f_set))
# print(a)
# print(f_set)


# a = set('qwerty')
# b = frozenset('qwerty')
# a.add(1)
# print(a)
# b.add(1)
# print(b)


months = {
    1: 'january',
    2: 'february',
    3: 'marth',
    4: 'april',
    5: 'may',
    6: 'july',
    7:'august',
    8: 'august',
    9: 'september',
    10: 'octember',
    11: 'november',
    12: 'dectember'
}
while True:
    number = input("enter the nomber")
    if number == 'stop':
        break

    if not number.isdigit():
        print('y neet enter the real month number')
        continue
    number = int(number)


    if number not in range (1,13):
        print('y neet enter the real month number')
        continue
    if number in range(3,6):
        print(f'вы родились {months[number]}, птицы пели прекрастные песни.')
    elif number in range(6,9):
        print(f'вы родились {months[number]}, соднце светило как не когда ярче.')
    elif number in range(9,12):
        print(f'вы родились {months[number]}, тЫ любишь Аяну.')

        