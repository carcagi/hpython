# List comprehension is just creating a list based on another list
# You can think of it as filling a list using a cicle without
# using the cicle syntactically.
# Each example given has the equivalent using a for cicle

# Using a cicle
print()
cubics = []

for x in range(10):
    cubics.append(x ** 3)

print(cubics)

shortcubics = [x ** 3 for x in range(10)]

print(shortcubics)

# This structure can be resumed in [operation_using_item for item in the_list]

# Example with a string

print()

string = 'SERENDIPITY'
string_list = []
for letter in string:
    string_list.append(letter)

print(string_list)

string_list = [letter for letter in string]
print(string_list)

print()
string_list = []
for letter in string:
    string_list.append(letter*2)

print(string_list)
string_list = [letter*2 for letter in string]
print(string_list)

# With conditionals [ expression for item in list if condition ]
# The example removes the 'I' char from string
print()

string_list = []
for letter in string:
    if letter != 'I':
        string_list.append(letter)
print(string_list)
string_list = [letter for letter in string if letter != 'I']
print(string_list)

# Using else, it changes compared to the if structure.
print()
string_list = []
for letter in string:
    if letter != 'I':
        string_list.append('X')
    else:
        string_list.append('Y')
print(string_list)

string_list = ['X' if letter == 'I' else 'Y' for letter in string]
print(string_list)
