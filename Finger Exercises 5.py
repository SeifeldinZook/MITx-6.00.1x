# Exercise 1

'''tup1 = (5)
print(tup1)
print(type(tup1))
tup2 = (5,)
print(tup2)
print(type(tup2))
print("---------------------")
x = (1, 2, (3, 'John', 4), 'Hi')
print("x[0]: ", x[0])
print("x[2]: ", x[2])
print("x[-1]: ", x[-1])
print("x[2][2]: ", x[2][2])
print("x[2][-1]: ", x[2][-1])
print("x[-1][-1]: ", x[-1][-1])
# print("x[-1][2]: ", x[-1][2])   # error
print("x[0:1]: ", x[0:1])
print("x[0:-1]: ", x[0:-1])
print("len(x): ", len(x))
print("2 in x: ", 2 in x)
print("3 in x: ", 3 in x)
# print("x[0] = 8: ", x[0] = 8)   # error '''

# Exercise: odd tuples

'''aTup = ('I', 'am', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    rTup = ()
    for element in aTup:
        if len(element) % 2 != 0:
            rTup += tuple(element)
    return rTup


print(oddTuples(aTup))


def oddTuples_ShowAnswer(aTup):
    rTup = ()
    index = 0
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2
    return rTup


print(oddTuples_ShowAnswer(aTup))'''

# Exercise 2

'''x = [1, 2, [3, 'John', 4], 'Hi']
print("x[0]: ", x[0])
print("x[2]: ", x[2])
print("x[-1]: ", x[-1])
print("x[2][2]: ", x[2][2])
print("x[0:1]: ", x[0:1])
print("2 in x: ", 2 in x)
print("3 in x: ", 3 in x)
x[0] = 8
print("if x[0] = 8, x:  ", x)'''

# Exercise 3

'''listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
print(listA.sort)
print(listA.sort())
print(listA)
print(listA.insert(0, 100))
print(listA.remove(3))
print(listA.append(7))
print(listA)
print(listA + listB)
print(listB.sort())
print(listB)
print(listB.pop())
print(listB.count('a'))
# print(listB.remove('a'))
print(listA.extend([4, 1, 6, 3, 4]))
print(listA)
print(listA.count(4))
print(listA.index(1))
print(listA.pop(4))
print(listA.reverse())
print(listA)'''

# Exercise 4

'''aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
print(aList == bList)
print(aList is bList)
print(aList)
print(bList)

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
    dList.append(num)
print(cList == dList)
print(cList is dList)
print(cList)
print(dList)
cList[2] = 20
print(cList)'''

# Exercise: apply to each

testList = [1, -4, 8, -9]
# print(testList * 5)
# print([testList] * 5)
# print(testList[:] * 5)


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return testList         # or return L


def timesFive(a):
    return a * 5

def inc(a):
    return a+1

def square(a):
    return a*a

# print(timesFive(testList))
# print(applyToEach(testList, timesFive))
# print(applyToEach(testList, abs))
# print(applyToEach(testList, inc))
print(applyToEach(testList, square))


# Exercise 5


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a


def halve(a):
    return a/2


def inc(a):
    return a+1


# print(applyEachTo([2, 4, 5], 5))
# print(applyEachTo([inc, square, halve, abs], -3))
# print(applyEachTo([inc, square, halve, abs], 3.0))
# print(applyEachTo([inc, max, int], -3))
