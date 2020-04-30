import random

WORDLIST_FILENAME = "ps3_hangman words.txt"


def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


wordlist = loadWords()
secretWord = chooseWord(wordlist)
print(secretWord)

print("Welcome to the game Hangman!")
print("I am thinking of a word that is", len(secretWord), "letters long.")
print("-------------")
guesses = 8
Availableletters = 'abcdefghijklmnopqrstuvwxyz'
print("Available letters:", Availableletters)
l = list(Availableletters)

guessedWord = ["_ "] * len(secretWord)
compareGuess = []


def getGuessedWord(secretWord, lettersGuessed):
    zeroguess = ["_ "] * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] == lettersGuessed:
            guessedWord[i] = lettersGuessed

    l.remove(lettersGuessed)
    strguessedWord = ''.join(guessedWord)

    if guessedWord != zeroguess:
        if guessedWord != compareGuess:
            print("Good guess:", strguessedWord)
            compareGuess[:] = guessedWord[:]
            return True
        elif guessedWord == compareGuess:
            print("Oops! That letter is not in my word:", strguessedWord)
            return False
    elif guessedWord == zeroguess:
        print("Oops! That letter is not in my word:", strguessedWord)
        return False


while guesses >= 0:
    print(guesses)
    if getGuessedWord(secretWord, lettersGuessed=input("Please guess a letter: ")):
        strguessedWord = ''.join(guessedWord)
        if strguessedWord == secretWord:
            print("Congratulations, you won!")
            break
    else:
        guesses -= 1
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was else.")
            break


