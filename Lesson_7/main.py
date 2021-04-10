class Animal:
    color = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s %s is %d years old" % (
            type(self).__name__,
            self.name,
            self.age
        )

    def voice(self):
        raise NotImplementedError()


class Cat(Animal):
    color = "white"

    def voice(self):
        print("mau")


class Dog(Animal):
    color = "black"

    def voice(self):
        print("aff")

class ShepherdDog(Dog):
    color = "brown"

    def voice(self):
        print("Rrrr")

class Corgi(Dog):
    color = "orange"

    def voice(self):
        print("afaf")


class GoldenFish(Animal):
    color = "gold"

    def voice(self):
        return None


jin = GoldenFish("Jin", 6)
print(jin)

dog2 = ShepherdDog("Joil", 3)
print(dog2)

dog2.age += 1
print(jin)
print(dog2)

jin.voice()
dog2.voice()
