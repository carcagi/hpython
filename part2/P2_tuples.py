# Tuples are just like lists but they are immutable. This means you
# can’t add or update them. You can just read elements.
# And remember, like lists, Tuples are also sequential.
numbers = (0, 1, 2, 3)
print(numbers)
print(numbers[0])
print(len(numbers))
empty_tuple = ()


# An example of usage of an empty tuple and
# Convert a list into a tuple
def tuple_power_of_2_up_to_n(n):
    if n<= 3:
        return ()
    else:
        x = []
        p = 2
        r = p
        while r < n:
            x.append(r)
            r = p ** 2
            p += 1
        return x

print('Tuple:')
print(tuple_power_of_2_up_to_n(60))


# In order to define a single item tuple, we add a trailing comma.
num = (1, )
print(type(num))
num = (1)
print(type(num))

# Adding items to a tuple, we need to create a new one, and add the
# tuples
nums = (1, 2, 3)
othernum = (4, )
new_tuple = nums + othernum
print(new_tuple)
