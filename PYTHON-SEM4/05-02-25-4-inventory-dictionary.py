inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# a) and b) Add pocket key with items
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# c) Sort backpack items
inventory['backpack'].sort()

# d) Remove dagger
inventory['backpack'].remove('dagger')

# e) Add 50 to gold
inventory['gold'] += 50

print("Modified inventory:", inventory)
