# Lists are basically like arrays.
# In the Python world, they call them List. And they are ordered.

letters = ["a", "b", "c"]

print(letters[0])
# Negative indexes start from the last item in -1
print(letters[-1])
print(letters[-2])

# The len() function returns the length of the List
len(letters)

# Append an element at end of list
letters.append("d")

# Insert one value and move the others
letters.insert(2, "z")
print(letters)

# Deleting a value using index
del letters[2]
print(letters)

# Pop will remove the las element from the list and return it
pop_letter = letters.pop()

print(letters)
print('Popped item:', pop_letter)

# Remove elements by value
letters.remove("b")

# Sorting
letters = ["d", "b", "a", "c"]
print(letters)
letters.sort()
print(letters)

# You can reverse a list
letters.sort(reverse=True)
print(letters)

# If you want to sort something just for printing, without modifying it.
# You can use the sorted method
letters = ["d", "b", "a", "c"]
# This will print sorted
print(sorted(letters))
# But the original list is still the same
print(letters)

# Reversing numbers, reverse does not order!!!
# it just changes the "chronological" order of elements
numbers = [11, 4, 8]
numbers.reverse()
print(numbers)

# Slicing elements
# Slicing cosist on return a portion of the list
vowels = ['a', 'e', 'i', 'o', 'u']
# To slice we use the brackets notation.
# The first index is the starting item.
# And Python stops in the item before the second index.
print(vowels[1:3])
print(vowels[2:5])
# You can ignore the first index, and it will start from 0
print(vowels[:4])
print(vowels[:3])
# Also, you can ignore the second index, keeping the ":" and
# it will travel to the end of the list
print(vowels[3:])

# You can ignore both indexes to travel the entire list
# This is useful when you want to copy the list
new_vowels = vowels[:]
# new vowels and vowels are two different objects

# WARNING A common mistake is copying a list like this
other_vowels = vowels

# In this case it's not a copy, both vars point to the same object.
# so any change to one, affects the other
print('vowels')
print(vowels)
print('other_vowels')
print(other_vowels)

vowels.remove('i')

print('vowels')
print(vowels)
print('other_vowels')
print(other_vowels)
