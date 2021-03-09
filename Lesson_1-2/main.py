# Типы данных

# Строки
s1 = "Hello world! I'm python dev. \"Zen of Python\" -- best book!"
s2 = 'Hello world! I"m python dev'
s3 = '''asd
asd
asd'''


# Числа
n1 = -30000  # type: int
n2 = 0.5  # type: float
print(1 / 3, 2 / 3, 1 / 3 + 2 / 3)


# Булевые значения
True, False
# Правда, Ложь


a = 2
print(a == 2)
print(a != 2)  # ! =
print(a > 2)
print(a < 2)
print(a <= 2)  # < =
print(a >= 2)  # > =


# Кортеж
t1 = 2, "s1", False
t2 = (2, "s1", False)


# Изменяемые типы
# Список
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # type: list
# print(l1)
l2 = l1[:]

# print(l2)
l3 = l1.copy()

# print(l3)
l1.append("1")
l2.append("2")
l3.append("3")

print(l1)
print(l2)
print(l3)

# Словари
d1 = {
    "list": [
        1,
        123,
        [
            "s"
        ]
    ],
    "dict": {
        "1": True
    }
}

print(d1)
from pprint import pprint
pprint(d1)
from json import dumps
print(dumps(d1, indent=2))


# Методы
f1 = "{key}:\t({message}),\t{value}"

print(s1.replace(' ', '__'))
print(f1.format(key="12", value="String", message="New message"))
print(f1.format(key="14", value="String", message="New message"))
print(f1.format(key="13", value="asd", message="New message"))
print(f1.format(key="11", value="String", message="New mqwdqwdessage"))
print(f1.format(key="10", value="String", message="New message"))
print(f1.format(key="18", value="ad", message="New message"))

print("%s, %d %.2f" % ([12], 12, 121))

print(f"{l1=}")

# Преобразование
inp = input('Введите число: ')
if inp.isnumeric():
    number = int(inp)
    result = number / 2  # type: float
    if result.is_integer():
        print(int(result))
    else:
        print(result)
else:
    print("Вы ввели не число! Повторите попытку")
