# Строки
s1 = """I'm Python dev, "Zen of python" -- best book!"""
s2 = 'Hello world! I\'m Python dev \"Zen of python\" -- best book!'
s3 = """I'm Python dev
"Zen of python" -- best book!"""

# print(s3)
str

# Числа
d1 = -12_345_712  # type: int
d2 = 123.0  # type: float

# print(2 * 8)
# print(2 ** 8)

# print(14 / 6)
# print(14 // 6)

# Булевые значения
True, False

a = 2
b = 2
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# Список
l1 = [1, "string", False]
# print(l1[-1])
l1.append(6)
# print(l1[-1])

# Словарь

d1 = {
    5: 'five',
    'programming': [
        {
            'language': 'Python',
            "type": 'interpritate',
            True: 1
        }
    ]
}



print(d1['programming'][0][True])

print(d1)
d1['index'] = 2
print(d1)