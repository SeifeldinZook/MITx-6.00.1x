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

''' ps3_hangman
secretWord: string, the word the user is guessing
lettersGuessed: list, what letters have been guessed so far
returns: string, comprised of letters and underscores that represents
what letters in secretWord have been guessed so far.
'''
# FILL IN YOUR CODE HERE...
'''
Next, implement the function getGuessedWord that takes in two parameters
- a string, secretWord, and a list of letters, lettersGuessed.
This function returns a string that is comprised of letters and underscores,
based on what letters in lettersGuessed are in secretWord.
This shouldn't be too different from isWordGuessed!
'''


def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += "_ "
    return string


print(getGuessedWord(secretWord, lettersGuessed=input("Please guess a letter: ")))
