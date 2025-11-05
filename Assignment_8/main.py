# საშინაო დავალება 8 


# 1

# def fibonaci(n):
#     a, b = 0, 1
#     i = 0
#     arr = []
#     while i < int(n):
#         arr.append(a)
#         fib = a + b
#         a = b
#         b = fib
#         i += 1
    
#     print(arr)


# n = input("Enter a number: ")
# fibonaci(n)



# 2

# def anagram(str1, str2):
#     if sorted(str1) == sorted(str2):
#         print("They are anagrams")
#     else:
#         print("They are not anagrams")

# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")

# anagram(s1, s2)




# 3

# def factorial(n):
#     i = result = 1
#     while i < int(n):
#         i += 1
#         result *= i

#     return result

# n = input("Enter the number: ")
# print(f"Factorial of {n} is", factorial(n))




# 4

# def func(st, ch):
#     counter = 0
#     for i in st:
#         if i == ch:
#             counter += 1
    
#     return counter

# st = input("Enter a string: ")
# ch = input("Enter a character: ")

# print(f"{ch} in {st} is", func(st, ch), "times")