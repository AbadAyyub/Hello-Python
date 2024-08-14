class Person:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Hello this is {self.name}")

actualPerson = Person("Abad Ayyub")
actualPerson.speak()
