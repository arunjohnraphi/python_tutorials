class Car:
    #class variable
    wheels =4
    def __init__(self):
        #instance variable
        self.mil =10
        self.com = "BMW"

    def print_wheels(self):
        print("number of wheels")
        print( wheels)

c1=Car()
Car.print_wheels()