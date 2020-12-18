# Dictionaries are key, value maps. Unordered
peer = {'id': 4422, 'name': 'Pepito Perez', 'email': 'pepe@gmail.com'}

print(peer['id'])
print(peer['name'])

print(len(peer))

# Add key and value for that key
peer['age'] = 27

# Get the keys from dictionary, returns a list
keys = peer.keys()
print(type(keys))
print(keys)
print()

# Get the values, also returns a list
values = peer.values()
print(type(values))
print(values)
print()

# Delete a key and it's value
del peer['age']

# You can nest one dict inside another.
# and nest all kind of ds
me = {
  'id': 100,
  'name': 'Adam Sandler',
  'consoles': ['ps3', 'wii', 'switch'],
  'projects': [
    {
      'id': 1,
      'name': 'Automate projects recalification'
    },
    {
      'id': 2,
      'name': 'Email checker and auto reply'
    }
  ],
  'debts': (10000, 50000, 100000),
  'pets': {'mili', 'toti', 'michi'}
}

print(me)
print()
print(me['projects'][0]['id'])

baddie = {'name': 'John wick'}
print()
# You can iterate through a dictionary. items() will return both keys
# and values. You can also use keys() and values() if needed.
for key, value in baddie.items():
    print(key + " is " + value)

# Homework enumerate()
