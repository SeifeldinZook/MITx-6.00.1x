# Exercise 1
'''
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

print('\n')

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

print('\n')

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

print('\n')

# Exercise 2

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    # print(guess)  it will take 50 lines
    if abs(guess**2 - x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

print('\n')

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    # print(guess)  it will take 50 lines
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

print('\n')

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

print('\n')
'''
# Exercise: guess my number


'''def guessmynumber(numberguessed):
    print("Please think of a number between 0 and 100! ")
    low = 0
    high = 100
    for i in range(10):
        mid = (low + high) / 2
        print("Is your secret number", int(mid), "?")
        print("Enter 'h' to indicate the guess is too high.", end=' ')
        print("Enter 'l' to indicate the guess is too low.", end=' ')
        print("Enter 'c' to indicate I guessed correctly.")
        result = input()
        if result == "c":
            print("Game over. Your secret number was:", numberguessed)
            break
        elif result == "h":
            high = int(mid)
        elif result == "l":
            low = int(mid)
        else:
            print("Sorry, I did not understand your input.")

    i += 1


guessmynumber(numberguessed=input("secret number is "))

print("Please think of a number between 0 and 100! ")
low = 0
high = 100
for i in range(10):
    mid = (low + high) / 2
    print("Is your secret number", int(mid), "?")
    result = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if result == "c":
        print("Game over. Your secret number was:", int(mid))
        break
    elif result == "h":
        high = int(mid)
    elif result == "l":
        low = int(mid)
    else:
        print("Sorry, I did not understand your input.")

i += 1'''

