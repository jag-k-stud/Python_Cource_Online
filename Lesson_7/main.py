class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s %s is %d years old." % (
            type(self).__name__,
            self.name,
            self.age
        )

    def voice(self):
        raise NotImplementedError()


class Cat(Animal):
    def voice(self):
        print("May")

class Dog(Animal):
    def voice(self):
        print("Gaf")


class Buldog(Dog):
    def voice(self):
        print("buf")


class Corgi(Dog):
    def voice(self):
        print("Awaf")


dog1 = Buldog("John", 4)
dog2 = Corgi("Unna", 2)
cat = Cat("Norman", 5)

print(dog1)
print(dog2)
print(cat)

dog1.voice()
dog2.voice()
cat.voice()

