
def change_to_diff(func):
    def inner(a, b):
        return a - b
    return inner


@change_to_diff
def sum(a, b):
    return a + b


print(sum(2, 3))
