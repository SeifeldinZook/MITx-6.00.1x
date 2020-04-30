s = 'azcbo'

v = 'a', 'e', 'i', 'o', 'u'

numberofvowels = 0
x = 0
while len(v) > x:
    print("------x------", x)
    for i in range(len(s)):
        print("------i------", i)
        print(v[0])
        print(s[i])
        if v[0] == s[i]:
            numberofvowels += 1
            print("------numberofvowels------", numberofvowels)
            i += 1
        else:
            i += 1
            print("------numberofvowels------", numberofvowels)
    print('\n')
    x += 1
