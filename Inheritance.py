class Mammal:
    def walk(self):
        print(" walk")

class Dog(Mammal):
    def bark(self):
        print("Dog")

class Cat(Mammal):
    def noise(self):
        print("Cat")


dog = Dog()
dog.bark()
dog.walk()

cat = Cat()
cat.noise()
cat.walk()