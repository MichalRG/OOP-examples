class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Im {self.name} and Im {self.age} years old")

    def speak(self):
        print("I dont know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("MEOW")

    def show(self):
        print(f"Im {self.name} and Im {self.age} years old and Im {self.color}")


class Dog(Pet):
    def speak(self):
        print("BARK!")


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "Brown")
c.show()
d = Dog("Jill", 25)
d.show()

p.speak()
c.speak()
d.speak()
