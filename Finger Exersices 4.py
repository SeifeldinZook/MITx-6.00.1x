# Exercise 1
def a(x):
   '''
   x: int or float.
   '''
   return x + 1


def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0


def c(x, y):
   '''
   x: int or float.
   y: int or float.
   '''
   return x + y


def d(x, y):
   '''
   x: Can be int or float.
   y: Can be int or float.
   '''
   return x > y


def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z


def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2


# Exercise: square
def square(x):
    '''
    x: int or float.
    '''
    return x**2


# Exercise: eval quadratic
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return (a*(x**2))+(b*x)+(c)


# Exercise 3
def a(x, y, z):  # although the function name is used before, but it is still iterable
    if x:
        return y
    else:
        return z


def b(q, r):
    return a(q > r, q, r)


# Exercise 4
z = 10


def f(x):
    return x + z


z = 3

x = 12


def g(x):
    x = x + 1

    def h(y):
        return x + y

    return h(6)

# Exercise 6

'''
s ='abc'
print(s.capitalize)
print(s.capitalize())
str1 = 'exterminate!'
str2 = 'number one - the larch'
print(str1.upper)
print(str1.upper())
print(str1)
print(str1.isupper())
print(str1.islower())
str2 = str2.capitalize()
print(str2)
print(str2.swapcase())
print(str1.index('e'))
print(str2.index('n'))
print(str2.find('n'))
# print(str2.index('!'))             # ValueError: substring not found
print(str2.find('!'))
print(str1.count('e'))
str1 = str1.replace('e', '*')
print(str1)
print(str2.replace('one', 'seven'))
'''


# Exercise: fourth power
def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(x)*square(x)


# Exercise: odd
def odd(x):
    '''
    x: int
    returns: True if x is odd, False otherwise
    '''
    return (x % 2 == 1)


# Exercise: power iter
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


# Exercise: power recur
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return
    #  base* base^(exp-1). This is the recursive case.
    return base * recurPower(base, exp - 1)


# Exercise: gcd iter
def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    list = []
    i = 1
    while i <= a:
        if a % i == 0 and b % i == 0:
            list.append(i)
        i += 1

    return max(list)


# Exercise: gcd recur
def gcdRecur2(c, d):
    if d % (c % d) == 0:
        return c
    else:
        return d % (c % d)


def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)



print(gcdRecur2(2, 12))
print(gcdRecur2(6, 12))
print(gcdRecur2(9, 12))
print(gcdRecur2(1071, 462))

print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(1071, 462))


# Exercise: is in
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code


#
aa = "AA"
aaa = "AAA"
c = "C"
d = "D"

import batteries
aa = "aa"
tripleA = "aaa"
print(batteries.aa)