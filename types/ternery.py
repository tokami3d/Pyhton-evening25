# sents = input('tell me something ')

# if sents [-1] == '?':
#     print('предлодение вопросительно ')
# else:
#     print ('обычное предложение')sents = 

# # ------------------
# # тернарный оператор это конструкцция которая аналогична по своим свойствам и дейтсвию конструкции if/else/
# # но при жтом записывается в одну строчку кода

# # <выражение если в условии тру> if <eусловие >  else < выраэение если false>n
 
# # num = 15
# # res = 'even' if num % 2 == 0 else 'odd number'

# # print(res)

# # from string import digits
# # num = input('add sentens')
# # if num.isdigit():
# #     num = int(num)
# #     print('yup you right')
# # else:
# #     print('вы ввели не число')
# # print (digits)
# # print(type(digits))
# # is_correct = True
# # symbols = digits + '-'
# # print(symbols)

# # for i in num:
# #     print(i)
# #     if i not in symbols:
# #         is_correct = False
    
# # if is_correct:
# #     print('yes number')
# #     number = int(num)
# #     print('your number:', number)
# #     result = number if number >= 0 else -number
# # else: 
# #     print('invalid values')

# from string import digits

# flag = True
# symbols = digits + '-' + '.'
# # i = 0
# # while flag:
# #     choise = input('enter yes or not')
# #     if choice == 'not':
# #         flag = false

# while flag:
#     is_correct_number = True
#     num1 = input('enter the firs sentens')
    
#     for x in num1:
#         if len(num1) <= 1 and num1 == '.' and num1 == '-' and not num1:
#           if x not in symbols:
#                 print('вы ввели неправельнон число')
               
#     if is_correct_number:
#         num2 = input('enter the second')
#     for x in num2:
#         if len(num1) <= 1 and num1 == '.' and num1 == '-' and not num1:
#             if x not in symbols:
#                 print('вы ввели неправельнон число')
#                 is_correct_number = False
#                 break
#             if not is_correct_number:
#                 continue
#     num1 = float(num1) if '.' in num1 else int(num1)
#     print(num1)
#     print(num2)
#     operator = input ('enter the operation(+,-,*,/)')
#     if operator == '+':
#         print(f'результат: {num1} + {num2}')
#     elif operator == '-':
#         print(f'результат: {num1} - {num2}')
#     elif operator == '*':
#         print(f'результат: {num1} * {num2}')
#     elif operator == '/':
#         print(f'результат: {num1} / {num2}')



# a = input float ('введите число')
# b = input float ('второе число')
# d = a * b
# print (d)

# name= input('введите свое имя')
# age = input('сколько тебе лощадь бует?')
# dd = input(f'и так {name} ты пидор?')
