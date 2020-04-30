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


def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += "_ "
    return string


def getAvailableLetters(lettersGuessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp


def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesLeft = 8
    print("------------")
    while True:
        print("You have " + str(guessesLeft) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print("------------")
        if guessesLeft <= 0:
            print("Sorry, You've ran out of guesses. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations! You've won!")
            break


hangman(secretWord)