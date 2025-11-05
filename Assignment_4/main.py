# საშინაო დავალება 4

# 1

# text=input("Enter a string: ")

# print(text.encode())




# 2

# text=input("Enter a string: ")

# text=text.strip()
# text=text.lower()
# text=text + " Python"

# if "python" in text:
#     text=text.replace("python", "Python")

# print(text)




# 3

# text=input("Enter a string: ")

# if len(text) % 2 == 0:
#     text1=text[:int((len(text)) / 2)]
#     print(text1)
# else:
#     print("string consists of an odd number of characters")




# 4

# import string

# text=input("Enter a string: ")

# digits=False
# letters=False
# chars=True

# for i in text:
#     if i in string.digits:
#         digits=True
#     elif i in string.ascii_letters:
#         letters=True
#     else:
#         chars=False

# if digits and letters and chars:
#     print("Valid")
# else: 
#     print("Not valid")




# 5

# text=input("Enter a string: ")

# text=text.encode()
# print(text)

# text=text.decode()
# print(text)