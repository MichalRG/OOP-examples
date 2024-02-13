class Person:
    number_of_people = 0
    GRAVITY = 9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # dekorator do dzialnaia na zmiennych klasy, a nie obiektu, nie otrzymuje self czyli instancji obiektu, a cls czyli
    # class instnace gdzie dziala na zmiennych dal wszystkich klas
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
print(p1.number_of_people)
p2 = Person("jill")
print(p2.number_of_people)

Person.number_of_people = 8
print(p1.number_of_people)

print(p1.GRAVITY)

print(Person.number_of_people_())  # calluje klase, a nie obiekt


class Math:
    @staticmethod
    def add(x1, x2):
        return x1 + x2

    @staticmethod
    def pr():
        print("run")


print(Math.add(1, 2))
