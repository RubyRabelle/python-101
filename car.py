#Rabelle 
#This a car class that takes input values for year_model and make of car
#and initializes speed to 0.
#Methods acclerate() and brake() change the speed of the vehicle.


#Car class
class Car:
    #initialize class
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    #define setters
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    #define getters
    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    #define methods
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
    
