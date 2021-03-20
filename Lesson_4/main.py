from sys import stdout


def first_function(max_index, range_end=10):
    for i in range(range_end):
        if i > max_index:
            return i
        # print(i)


res2 = first_function(10, 17)
# print("func", res2)


def func(arr: list = None):
    if arr is None:
        arr = []
    arr.append(1)
    return arr


arr1 = func([12])
arr2 = func()
arr3 = func()

arr3.append(3)


def print_fn(*value, sep=' ', end='\n', file=stdout):
    string = sep.join(map(str, value)) + end
    if type(file) is str:
        with open(file, 'a') as f:
            f.write(string)
    else:
        file.write(string)


print_fn([1, 2, 3], file='abc.txt')
