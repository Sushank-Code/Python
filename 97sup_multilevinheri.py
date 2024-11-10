class Animal:
    def eat(self):
        print("Animal is eating")


class Mammal(Animal):
    
    def walk(self):
        super().eat()                        # super method
        print("Mammal is walking")


class Dog(Mammal):
    def bark(self):
        super().walk()    
        print("Dog is barking")


d = Dog()
# d.eat()   # Inherited from Animal
# d.walk()  # Inherited from Mammal
d.bark()  

