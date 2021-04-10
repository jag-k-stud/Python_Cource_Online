import sys

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s is %d years old." % (self.name, self.age)

    


dog1 = Dog("John", 4)
print(dog1)

dog2 = Dog("Unna", 2)
print(dog2)

dog2.age += sys.maxsize

print(dog1)
print(dog2)
