# საშინაო დავალება 9 

# 1

# int_list = [10,20,30,40]

# def func(num):
#     int_list.append(num)

# num = int(input("Enter a number to add in the list: "))
# func(num)
# print(int_list)




# 2

# my_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# def func(arr):
#     sum = 0
#     for i in arr:
#         sum += i

#     return sum

# print("Sum is", func(my_list))




# 3

# gl_str = "Global"

# def func():
#     gl_str = "local"

#     return gl_str

# print(func())




# 4

# def func(num):
#     if (num != 0):
#         return num % 10 + func(num // 10)
#     else:
#         return 0


# num = int(input("Enter a number: "))
# print(func(num))




# 5

# def func(str):
#     if(str != ""):
#         return func(str[1:]) + str[0]
#     else:
#         return ""

# text = input("Enter a string: ")
# print(func(text))





# ლექციის დავალება 

# def flatten(args):
#     for item in args:
#         if isinstance(item, (list, tuple, set, frozenset)):
#             yield from flatten(item)
#         elif isinstance(item, dict):
#             yield from flatten(item.values())
#         else:
#             yield item

# arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title': 'The wolf', 'pages': 256}, (8, [9, 0], True, {5, 8, False})]

# arr = list(flatten(arr))

# print(arr)