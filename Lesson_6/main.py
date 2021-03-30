class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks {sound}"

    def older(self):
        self.age += 1


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    def speak(self, sound="Yap"):
        return super().speak(sound)


class Bulldog(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)


rick = Bulldog("Rick", 6)
miles = Dachshund("Miles", 8)

print(rick.speak())
print(miles.speak("Grrr"))

print(type(rick))
print(isinstance(miles, Dog))
print(isinstance(miles, Bulldog))
print(isinstance(miles, Dachshund))

print(rick, miles)
rick.older()
print(rick, miles)

