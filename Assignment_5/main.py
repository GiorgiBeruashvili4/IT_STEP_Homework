# საშინაო დავალება 5

# 1

# empty_list=[]

# while True:
#     element=input("Enter 'a', 'r' or 'e': ")

#     if element == 'a':
#         num=int(input("Enter a number to append: "))
#         empty_list.append(num)
#         print(empty_list)
#     elif element == 'r':
#         if len(empty_list) == 0:
#             print("List is empty")
#         else:
#             num=int(input("Enter a number to remove: "))
#             if num not in empty_list:
#                 print("Number is not in the list")
#             else:
#                 empty_list.remove(num)
#                 print(empty_list)
#     elif element == 'e':
#         break




# 2

# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# print("Index of '210' is", my_list_1.index(210))

# my_list_1.append("Hello")
# print(my_list_1)

# del my_list_1[2]
# print(my_list_1)

# my_list_2 = my_list_1
# my_list_2.clear()
# print(my_list_1)
# print(my_list_2)




# 3

# import re

# number = "(123) 456-789"
# pattern = r"\(\d{3}\) \d{3}-\d{3}"

# print(re.fullmatch(pattern, number))

# if re.fullmatch(pattern, number):
#     print(number)
# else:
#     print("Invalid format")