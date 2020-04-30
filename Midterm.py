# Problem 5
# ---------

'''
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 10
l2 = []


def getSublists(L, n):
    l1 = []
    if 0 < n <= len(L):
        for j in range(len(l)-int(n)+1):
            print("j = ", j)
            for i in range(n):
                print("i = ",i)
                l1.extend(L[i+j:i+j+1])
                print(l1)
        l.remove(L[j])
    return l2

def getSublists(L, n):
	list_of_sublists = []
	for i in range(len(L)-n+1):
		list_of_sublists.append(L[i:i+n])
	return list_of_sublists


print(getSublists(L, n))
'''

# Problem 6
# ---------


t = (5, (1, 2), [[1], [9]], 6, 1, [[1], [10]], 1000)
'''
def max_val(t):
    l0 = t[0]
    l1 = max(t[1])
    l2 = max(t[2])
    l = l0, l1, l2[0]
    return max(l)


def max_val2(t):
    maxVal = 0
    for i in t:
        print("-----------")
        print("maximum value", maxVal)
        if type(i) == list or type(i) == tuple:
            print("i", i)
            maxValList = max_val2(i)
            print("value", max_val2(i), maxValList)
            if maxValList > maxVal:
                maxVal = max_val2(i)
        else:
            if i > maxVal:
                maxVal = i

    return maxVal


#print(max_val(t))
print(max_val2(t))

'''

# Problem 7
# ---------


def satisfiesF(L):
    rec_list = []

    for i in range( 0, len( L ) ):
        if (f( L[i] ) == False):
            rec_list.append(L[i])

    for j in rec_list:
        L.remove(j)

    return len( L )

def f(s):
    return 'a' in s


L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
