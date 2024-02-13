x = 1
print(type("hello"))
print(type(x))


def hello():
    print("hello")


print(type(hello))
# Tworzac cokolwiek w pythonie zawsze tworzymy istnacje klasy co pokazuje printowanie typu prymitywow powyzej

string = "hello"
print(
    string.upper())  # poniewaz to jest obiekt typu string ma dostepna metode upper gdyby to byl int to nie miaby tej metody


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("Woaf!")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


dog = Dog("Tim", 8)
dog2 = Dog("Bill", 5)
print(type(dog))
print(dog.add_one(3))
print(dog2.name, dog2.get_name())
dog2.set_age(6)
print(dog2.get_age())
