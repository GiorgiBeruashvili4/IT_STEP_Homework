# საშინაო დავალება 7


# 1

# nums = map(eval, input("Enter a sequence of numbers: ").split())

# my_set = set(nums)

# print(my_set)




# 2

# nums = map(eval, input("Enter a sequence of numbers: ").split())

# my_set = frozenset(nums)

# print(my_set)




# 3

# set1 = {0,6,2,8,4}
# set2 = {5,1,7,3,9}

# print(tuple(set1.union(set2)))




# 4 

# nums = map(eval, input("Enter a sequence of numbers: ").split())
# my_tuple = tuple(nums)

# print(my_tuple)
# print(list(set(my_tuple)))




# 5 

# my_list = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# for name, age in my_list:
#     print(f"Name: {name}, Age: {age}")




# 6

# list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
# list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

# print(*set(list1).intersection(set(list2)))