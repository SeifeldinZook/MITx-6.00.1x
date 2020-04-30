'''s = "sdafdsadasfasi"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print('there is an i or u')'''


'''s = "sdafdsadasfas9899i"
for char in s:
    if char == 'i' or char == 'u':
        print('there is an i or u')'''


'''an_letters = "aefhsxAEFHIX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1

print("What does that spell?")

for i in range(times):
    print(word, '!!!')'''


'''iteration = 0
while iteration < 5:
    print("Iteration " + str(iteration))
    count = 0
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            print("Iteration " + str(iteration) + " has no reminder if divided by 2")
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1'''


'''cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 -cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses=', num_guesses)
if abs(guess ** 3 - cube ) >= epsilon:
    print( 'Failed on cube root of', cube )
else:
    print(guess, 'is close to the cube root of', cube)'''


'''x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2-x) >= epsilon:
    print('low= ' + str(low) + ' high = ' + str(high) + ' ans= ' + str(ans))
    numGuesses+= 1
    if ans**2< x:
        low = ans
    else:
        high = ans
    ans= (high + low)/2.0
print('numGuesses= ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))'''


'''cube = 27
epsilon = 0.01
num_guesses = 0
low = 1
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses+= 1
print('num_guesses=', num_guesses)
print(guess, 'is close to the cube root of', cube)'''


'''school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))'''

'''iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
print("-----------------------------------------")
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))'''

'''num = 3

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
        result = str(num % 2) + result
        num = num//2
if isNeg:
        result = '-' + result

print(result)'''

