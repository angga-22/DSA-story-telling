# OOP

# class attributes without constructor
class Car:

    color = "Red"


car1 = Car()

# print("car 1", car1.color)

# class attributes with constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age




angga = Person("angga", 22)

# print(angga.name)

class Universe: 
    def __init__(self, name, mass, age):
        self.name = name
        self.mass = mass
        self.age = age

    # object methods
    def increase_age_by_ten(self): 
        self.age += 10

    # static methods
    @staticmethod
    def i_am_universe():
        print("this is method from class Unverse!")

    # class methods
    @classmethod
    def i_am_universe2(cls):
        print("hello bro")


earth = Universe("earth", 100, 400)
print(earth.age)
earth.increase_age_by_ten()

print(earth.age)

# INHERITANCE

class Car2:
    def __init__(self, name, brand, speed):
        self.name = name
        self.brand = brand
        self.speed = speed

    def increase_speed(self):
        self.speed += 10




class SportCar(Car2):
    def turbo(self):
        self.speed += 100
    
    # override method from its parent
    def increase_speed(self): 
        super().increase_speed() # this is if we want to invoke parent method
        self.speed += 50
    
    def tes(self):
        return f"{self.name} angga"



mySportCar = SportCar("agya", "toyota", 100)

print(mySportCar.tes()) 
