# loop - циклы


# 2 вида циклов:
# while
# for

# range

# for i in range(10):
#     print(i)

# for i in range(20, 9 , -2):
#     print(i)

# for i in range(20):
#     print(i, end=" ")

# range(stop) -> [0; stop)
# range(start, stop) -> [start; stop)
# range(start, stop, step)



# for i in range(1, 11):
#     print(f'9 * {i} = {9 * i}')


# def print_mult_tabl(num, from_number, up_to):
#     for i in range(from_number, up_to + 1):
#         print(f'{num} x {i} = {num * i}')

# print_mult_tabl(44, 4, 10)


# def print_exp_tabl(num, from_number, up_to):
#     for i in range(from_number, up_to + 1):
#         print(f'{num} ** {i} = {num ** i}')

# print_exp_tabl(2, 1, 10)


# for i in range(5, 11):
#     print(i / 10)

# ! один проход цикла - итерация
# ? итерации можно пропускать с помощью слова continue

# for letter in 'Alimdjanov Umarjon':
#     if letter == ' ':
#         continue
#     else:
#         print(letter, end = '*')


# for letter in 'Alimdjanov Umarjon':
#     if letter == ' ':
#         break
#     else:
#         print(letter, end = '')


# print('Umarjon'.upper())
# print('UMARJON'.lower())
# print('Umarjon'.isupper())
# print('Umarjon'.islower())
# print('1'.isdigit())


# new_str = ''
# for letter in 'Elbek Khakimbekov is a teacher':
#     new_str = new_str + letter.swapcase()
# print(new_str)



