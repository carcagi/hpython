# Arbitrary keyword arguments
# When you don't know the tye of arguments being passed.

def user_info_1(**info):
    print(info)


# You should always name the arguments name explicitly
user_info_1(name='Carlos', favorite_actors=['Cavill', 'Cruise'])

# The below code will throw error.
# user_info('Carlos')


def user_info_2(name, **info):
    print(info)


user_info_2(
    'Carlos',
    favorite_actors=['Cavill', 'Cruise'],
    twitter_handle='@carcargi'
    )
