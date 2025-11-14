# საშინაო დავალება 17 


# დავალება 1 

# class Vector:
#     def __init__(self, x, y ):
#         self.__x = x
#         self.__y = y

#     def __add__(self, other):
#         return Vector(self.__x + other.__x, self.__y + other.__y)
    
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
    

# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2

# print(v3)





# დავალება 2

# class Book:
#     def __init__(self, title, author):
#         self.__title = title
#         self.__author = author

#     def __eq__(self, other):
#         if type(other) is not Book:
#             return False
#         return self.__title == other.__title and self.__author == other.__author    

# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  
# print(book1 == book3)  
# print(book2 == book3)





# დავალება 3

# import re

# class Car:
#     def __new__(cls, *args, **kwargs):
#         print("Object has been created")
#         instance = super().__new__(cls)
#         return instance

#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model= model
#         self.year= year

#     @property
#     def brand(self):
#         return self.__brand
    
#     @property
#     def model(self):
#         return self.__model
    
#     @property
#     def year(self):
#         return self.__year
    
#     @brand.setter
#     def brand(self, new_brand):
#         self.__brand = new_brand.strip() if re.fullmatch(r"[A-Za-z ]+", new_brand) else "The name must contain only letters."

#     @model.setter
#     def model(self, new_model):
#         self.__model = new_model

#     @year.setter
#     def year(self, new_year):
#         self.__year = new_year if type(new_year) is int and new_year > 0 else "Year must be positive integer."

#     def show(self):
#         print("\nBrand: ", self.brand)        
#         print("Model: ", self.model)        
#         print("Year: ", self.year)         

# car1 = Car("Porsche", "911", 1994)
# car2 = Car("Tesla", "Cybertruck", 2023)
# car3 = Car("BMW12345", "X6", -2018)

# car1.show()
# car2.show()
# car3.show()

# car1.year = 1996
# car2.model = "Model X"
# car3.brand = "BMW"
# car3.year = 2018

# car1.show()
# car2.show()
# car3.show()