# class number:
#     def sum(self):
#         return self.a + self.b
    
# num=number()
# num.a =12
# num.b=12
# s= num.sum()
# print(s)

class profile:                                     # Self Parameter Example
    Gender = "male"
    def printd(self):
        print(f"Name : {self.name}")                
        print(f"Roll no : {self.roll}")

    @staticmethod                                    # static method
    def greet():
        print("Good Morning")

p=profile()         # object Instantiation
p.name="Sushank"
p.roll="100"
print(p.Gender)
p.printd()     # profile.printd(p)
p.greet()