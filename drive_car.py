#Rabelle 
#COSC-1336 Lab 10 (Classes)
#04/28/2016

#This program creates a car object and then calls the accelerate method
#five times and shows the speed as the car accelerates.  Then calls the
#brake method 5 times and shows the speed after each brake.

import car

def main():
    #create instance of car
    my_car = car.Car(2003, 'Chevrolet')

    #speed it up and slow it down using class methods
    speed_up(my_car, 5)
    slow_down(my_car, 5)


def speed_up(my_car, times):
    print('The',my_car.get_year_model(), my_car.get_make(),'is speeding up now...')
    for i in range (times):
        my_car.accelerate()
        print('The speed is now:', my_car.get_speed(), 'mph.')

def slow_down(my_car, times):
    print('The',my_car.get_year_model(), my_car.get_make(),'is slowing down now...')
    for i in range(times):
        my_car.brake()
        print('The speed is now:', my_car.get_speed(), 'mph.')

main()    
