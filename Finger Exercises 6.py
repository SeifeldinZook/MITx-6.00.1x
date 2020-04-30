# Exercise 1

'''animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print(animals)
print(animals['c'])
# print(animals['elephant'])     #  error
# print(animals['baboon'])     #  error
print(len(animals))
animals['a'] = 'anteater'
print(animals['a'])
print(len(animals['a']))
print('baboon' in animals)
print('donkey' in animals.values())
print('b' in animals)
print(animals.keys())
del animals['b']
print(len(animals))
print(animals.values())
print('a' in animals.keys())
print(type(animals['c']))'''

# Exercise: how many


animals = {'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}
# animals = { 'a': ['aardvark', 'lion'], 'b': ['baboon', 'cat'], 'c': ['coati']}

print(animals)


def how_many(aDict):
    values = 0
    for v in animals.values():
        values += len(v)
    return values


print(how_many(animals))

# Exercise: biggest


def biggest(aDict):
    # big_key = None
    big = 0
    for k, v in animals.items():
        if len(v) > big:
            big = len(v)
            return k

print(biggest(animals))


def biggest2(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result


print(biggest2(animals))
