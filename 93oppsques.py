from math import *
class Calculator:

    def getin(self):
        self.num = int(input("Enter the number"))

    def square(self):
        sq=pow(self.num,2)
        print(f"The square root of {self.num} is ",sq)

    def cube(self):
        cu=pow(self.num,3)
        print(f"The cube root of {self.num} is ",cu)
    
    def squareroot(self):
        sqr=sqrt(self.num)
        print(f"The square root of {self.num} is ",sqr)

calc=Calculator()
calc.getin()
calc.square()
calc.cube()
calc.squareroot()