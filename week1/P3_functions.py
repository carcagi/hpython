def prints_hello():
    print('Hello')


prints_hello()


# return
def return_something_from_python(something):
    return something + ' from python'


value = return_something_from_python('something')
print(value)

# errors, uncomment below lines
# return_something_from_python()
# return_something_from_python('something','other')


# default param
def prints_string(string='hello world'):
    print(string)


prints_string()
prints_string('new hello world')


# pass arguments explicitily
def movie_info(title, director_name, ratings):
    print(title + " - " + director_name + " - " + ratings)


movie_info(ratings='11/10', director_name='David Fincher', title='Fight Club')


# arbitrary number of arguments
def careers(*titles):
    print(titles)
    return 'You have named ' + str(len(titles)) + ' careers'


print(careers('Medicine', 'Programming', 'Software Enginnering'))


def fav_superheroes(my_favorite, *the_rest):
    print(the_rest)
    return ("My favorite " + my_favorite)


print(fav_superheroes('Deadpool', 'Thor', 'Hawkeye', 'Amtman'))
