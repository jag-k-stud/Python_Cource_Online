class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__dogs__.append(self)

    def __str__(self):
        return "%s is %d year old" % (self.name, self.age)


jin = Dog("Jin", 6)
print(jin)

dog2 = Dog("Joil", 3)
print(dog2)

dog2.age += 1
print(jin)
print(dog2)
