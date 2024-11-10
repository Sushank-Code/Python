class Employee:

    def __init__(self,name):                 # Constructor
        print("Employee is created")
        self.name=name

    def getd(self):
        print(f"Name : {self.name}")

abc = Employee("Mark")
abc.getd()
