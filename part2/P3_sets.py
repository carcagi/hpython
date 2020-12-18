# Sets are unordered elements (order is not fixed)
# But with no duplicates

letters = {'a', 'h', 'k', 'b', 'a'}

print(letters)
# Duplicates are removed

# Accessing items in set
# You can't access items by indexm because of the unordered nature
# You have to use loops. :(
for char in letters:
    print(char)

# To add element into the set we use add()
letters.add('s')
print(letters)

# What happens if you try to add an existan item.
letters.add('a')
print(letters)

# add insert only one element.
# If you need to insert multiple elements use update instead
letters.update(['a', 'x', 'z'])
# Remember duplicated are removed. so only 'x' and 'z' are added
print(letters)

# Len works the same
print(len(letters))

# We need to pass the element value to remove the element from the set
letters.remove('a')
print(letters)
# Remove throws an error if element doesn't exist

# Discard won't throw an error if the element is not present.
# It's safer to use
letters.discard('x')
