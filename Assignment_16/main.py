# საშინაო დავალება 16 

from datetime import datetime

class Car:
    __number_of_cars = 0

    def __init__(self, brand, model, year):
        self.__brand=brand
        self.__model=model
        self.__year=year
        Car.__number_of_cars += 1

    def car_info(self):
        print("\nBrand: ", self.__brand)        
        print("Model: ", self.__model)        
        print("Year: ", self.__year)        
        print("Age: ", self.age_of_car())        

    def age_of_car(self):
        return datetime.now().year-self.__year
    
    @classmethod
    def total_cars(cls):
        print(f"Total cars: {Car.__number_of_cars}", '\n')
    

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.__battery_life=battery_life

    def battery_info(self):
        print(f"Battery life of this car is {self.__battery_life} hours", '\n')

c = Car("Porsche", "911", 1994)
c.car_info()

e_c = ElectricCar("Tesla", "Cybertruck", 2023, 11)
e_c.car_info()
e_c.battery_info()

Car.total_cars()