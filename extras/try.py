# We can use try to surround dangerous code
# If the code inside the try block works the except part is ignored
# If the code inside the try block fails, the excepto part is executed

# The following code will fail on line 2 because I can't convert
# a non numerical string to integer, this happens, for example
# when the user enters a non valid number

# string = 'Something'
# istring = int(string)
# print('Number One: ', istring)
# string = '123'
# istring = int(string)
# print('Number Two:', istring)

# If I know the code on line two will fail somehow I can use
# the try block to work around this.
print()

string = 'Something'

try:
    istring = int(string)
except:
    istring = -1

print('Number One: ', istring)
string = '123'
istring = int(string)
print('Number Two:', istring)


# The code above will work, but it's not a good practice, we should
# handle the thrown exception and log it somewhere,
# Exception handles the exact error message

print()

string = 'Something'

try:
    istring = int(string)
except Exception as ex:
    istring = -1
    # This will print the error, but should be logged into a file or log system
    print(ex)

print('Number One: ', istring)
string = '123'
istring = int(string)
print('Number Two:', istring)

# The try statement has one else clause.

print()

string = '123'

try:
    istring = int(string)
except Exception as ex:
    istring = -1
    # This will print the error, but should be logged into a file or log system
    print(ex)
else:
    print('This worked')

# The else part won't get executed if the try block fails.
print()
string = 'Something'
try:
    istring = int(string)
except Exception:
    istring = -1
else:
    print('This does not show')
print('It didn\t got into the else')
