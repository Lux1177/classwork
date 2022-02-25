# 1 задача
# написать которая будет принимать 1 параметр - размер елки

#пример:
# draw_christmas_tree(5)
# output:

# *
# **
# ***
# ****
# *****


# # 
# def draw_christmas_tree(size):
#     if type(size) == str or size < 3:
#         print("Error")
#     for i in range(1, size + 1):
#         print('*' * i)

# draw_christmas_tree(5)

# ! Задача 2
# output
# *****
# *****
# *****

# def draw_rectangle(width, height):
#     for i in range(height):
#         print('*' * width)

# draw_rectangle(13, 5)


# ! Задача 3
# clear_text_from_upper_case('wddKKr4dKK4ofkkK')
# output

# def clear_text_from_upper_case(text):
#     new_text = ''
#     for letter in text:
#         if letter.isupper(): pass
#         else: new_text = new_text + letter
#     return new_text

# print(clear_text_from_upper_case('tttTTfFFjvhHHdgF'))


# ! Задача 4
# show_devisors(24)
# output 1 2 3 4 6 12 24

# def show_devisors(number):
#     for i in range(1, number + 1):
#         if number % i == 0:
#             print(i)
# show_devisors(11)


