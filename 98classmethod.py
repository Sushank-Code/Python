class Employee:
    Company = "Microsoft"
    salary = 25000

    @classmethod
    def chagesalary(cls,sal):
        cls.salary=sal

e = Employee()
print(e.salary)
e.chagesalary(30000)
print(e.salary)
print(Employee.salary)

