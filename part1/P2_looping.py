# while loops
# Not i++ avaiable
i = 0
while i <= 5:
    # print(i)
    i += 1

# break and continue
i = 0
while i <= 5:
    i += 1
    if i == 2:
        continue
    print(i)
    if i == 4:
        break

# else
i = 0
while i <= 5:
    i += 1
    print(i)
else:
    print('Is more than 5')

# if you break before else you'll never get there
i = 0
while i <= 5:
    i += 1
    if i == 2:
        continue
    print(i)
    if i == 4:
        break
else:
    print('Is more than 5')

""" This is a Docstring, it's ignored, but used for help commands
For loops in the traditional form are not encouraged
for(i=0; i<5; i++)
Instead, Python insists on iterating over items using the for loop
"""
array = ['h', 'o', 'l', 'b', 'i', 'e']
for element in array:
    print(element)

# run on a string
string = "holbie"
for char in string:
    print(char)

# range
# range generates sequences
# range(7) generates 0..6
# range(1, 9) generates 1..8
# range(1, 8, 2) generates 1,3,5,7

for ele in range(3):
    print(ele)

# loop on index of array
# len returns len of structure (refer to line 43)
for index in range(0, len(array)):
    print(array[index])

# iterate on dictionaries
dict = {'name': 'Pepito perez'}
for key, value in dict.items():
    print(key + ' is ' + value)

# enumerate is used to return a tuple with indexes
for index, value in enumerate(array):
    print(value + ' is in ' + str(index))
