age = input('Введите ваш возраст: ')

if age.isnumeric():
    age = int(age)
    if age < 6:
        print("Вы ещё в дет. саду")
    elif age < 18:
        print("Вы уже школьник")
    else:
        print("Вы уже вступили во взрослую жизнь")
else:
    print("Вы ввели не число!")
