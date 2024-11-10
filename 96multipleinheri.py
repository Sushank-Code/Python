class Freelancer:
    company = "Fiverr"
    level=0

    def upgrade(self):
        self.level=self.level+1

class Employee:
    company = "Visa"
    ecode=120

class programmer(Employee,Freelancer):
    name="Mark"

p=programmer()
p.upgrade()
print(p.level)
print(p.company)