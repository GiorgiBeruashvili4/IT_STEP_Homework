# საშიანო დავალება 10

# 1 

# def func(arr1, arr2):
#     res = zip(arr1, arr2)
#     print([str(x) for x in res]) 

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c'] 

# func(list1, list2)




# 2

# from functools import reduce

# def func(list):
#     try:
#         return reduce(lambda x, y: x * y, list)
#     except TypeError as ex:
#         raise TypeError("Incorrect type. Pass function a list")

# my_list = [1, 2, 3, 4, 5]

# print(func(my_list))




# 3

# my_list = [1, 2, 3, 4, 5, 6, 7]

# result = lambda nums: [x for x in nums if x % 2 == 1]

# print(list(result(my_list)))




# 4

# def func(str_list, ending):
#     try:
#         return list(filter(lambda x: x.endswith(ending), str_list))
#     except TypeError as ex:
#         raise TypeError("Incorrect type. Pass function a list and string")


# my_list = ['hello', 'world', 'coding', 'nod']
# print(func(my_list, "ing"))