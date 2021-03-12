# Строки

s1 = '''I'm Python dev.
"Zen of Python" -- best book ever!'''
# print(s1)


# Числа
n1 = -12_123_4_5_6_7_3_1
# print(13 * 2)
# print(13 ** 2)

# Булевые значения
True, False

a = 1
b = 2
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# Списки
l1 = [[1], [2], [3]]
print(l1)
l1.append('v5')
print(l1)

del l1[-1]
print(l1)

# Словарь

d1 = {
    'items': {
        'count': 2,
        'result': [
            'first', 'second'
        ]
    }
}

print(d1)
print(d1['items']['result'][-1])

d1['input'] = 'data'
print(d1)

del d1['input']
print(d1)