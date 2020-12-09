# print(), prints the string passed as parameter to the standard output
print("This will show on screen")

# Using quoting marks inside another string
# we have a few options
print('String with a "text"')

print("String with a \"text\"")

# Special attention when you have to escape the "\"
print('C:\\Users\\jdoe')

# Things can get messy with char escaping, specially with regular
# expressions.
regexp = '^\\w:\\\\(?:(?:(?:[^\\\\]+)?|(?:[^\\\\]+)\\\\[^\\\\]+)*)$'

# But python is here to the rescue.
# you can prepend r to the strings to remove the character scaping.
# Use with CAUTION!
print(r'C:\Users\jdoe')
print(r'^\w:\\(?:(?:(?:[^\\]+)?|(?:[^\\]+)\\[^\\]+)*)$')

# Multiline strings. You can define multiline strings with """ or '''
multiline = """
This text 
has multiple
lines.
"""
print(multiline)

# To prevent the new line before the
multiline = """This text 
has multiple
lines.
"""
print(multiline)

# or use the scape char
multiline = """\
This text 
has multiple
lines.
"""
print(multiline)

# Concatenation
print("string1" + "string2" + "string3")  # Concatenate as it is passed
# string1string2string3
print("string1", "string2", "string3")  # Uses spaces to concatenate
# string1 string2 string3

# You can't concatenate numbers with strings.
# print("String" + number)  # Will show an error
# you need to cast the object to string using the str function
# if you are using the plus (+) sign to concatenate
print("My score should always be above " + str(80) + "%")

# You can concatenate, several items, without casting using parameters
# if you are using the print function, the degault glue is an empty space
print("My score should always be above", 80, "%")

# we can sue the sep parameter to glue the string with other symbol
print("My score should always be above", 80, "%", sep=' => ')
# My score should always be above => 80 => %

# All print calls end with a new line character "\n"
print("Line 1")
print("line 2")
print("...")
print("line n")

# We can remove this behaviour by using the parameter end,
# and we can even replace the line jump with any character
print("Line 1", end=' ')
print("line 2", end='*')
print("...", end='---')
print("line n", end='')
# Line 1 line 2*...---line n

# you can combine both arguments.
print('One', 'Two', sep=', ', end=', ')
print('Three', 'Four', sep=', ', end=', ')
print('Five', 'Six', sep=', ')

# print() with zero arguments generates an empty/blank line
print()

# One simple example of things that can be done with print
# Print a list as a string
userdata = ['Carlos', 'favorite', 'language', 'is C++']
print(*userdata)
print(*userdata, sep="\n")
