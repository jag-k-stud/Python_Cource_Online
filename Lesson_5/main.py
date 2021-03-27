def div():
    inp = input('Введите число: ')
    if inp.isnumeric():
        number = int(inp)
        result = number / 2  # type: float
        if result.is_integer():
            return int(result)
        else:
            return result
    else:
        raise TypeError("Вы ввели не число! Повторите попытку")

def inf_div():
    while True:
        try:
            return div()
        except TypeError as err:
            print(err)


def main():
    print(inf_div())


if __name__ == "__main__":
    main()
