# This is a comment in python!

# String
msg_from_computer = "Hello"
# This is another string
another_msg = 'Hello in single quote'

print(msg_from_computer + " World!")

# Type returns the data type
print(type(msg_from_computer))
print(type(4))

# Math
print((2 + 3) * 4)
print(2 ** 3)
print(2 * 3)

# Flotantes
print(0.1 + 0.2)
print(2 + 0.1)
print(3.5 * 2)

# problems concatenating
count = 5
print("I need " + str(count) + " chocolates")

# Booleanos

true = True
false = False
print(bool("Something"))
print(bool(""))
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(true))
print(bool(false))

# if ..  else
a = 5
b = 10

# indentation defines blocks of code

if a == 5:
    print("This is true")

if a == 7:
    print("This should not be printed")

# This code has an error && is not used
# if a == 5 && b == 10:
# print("Using &&")

if a == 5 and b == 10:
    print('Using and')

# if else
if a == 5:
    print('Five')
elif a == 6:
    print('six')
elif a == 7:
    print('Seven')
else:
    print('Another number')

# using or
if a == 7 or b == 10:
    print('a is equal to 7 or b is equal to 10')

# not equal
if a != 10:
    print('a is different from 10')

# inline (considered bad practice)
if a == 5: print('a is 5')

# short hand (Ternary in C)
a = 7
print('verdadero') if a == 5 else print('falso')
print('verdadero' if a == 7 else 'falso')

# is keyword. Is used to check if the two terms refer the same object.
# This is true because both refer the same string
x = "apple"
y = x
print(x is y)

# This is also true
x = "apple"
y = "apple"
print(x is y)

# There is this behaviour, both objects have the same value, but are not
# the same object, so this one will be false.
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)
