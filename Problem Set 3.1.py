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
returns: boolean, True if all the letters of secretWord are in lettersGuessed;
  False otherwise.'''
# FILL IN YOUR CODE HERE...
'''Please read the Hangman Introduction before starting this problem.
We'll start by writing 3 simple functions that will help us easily code the Hangman problem.
First, implement the function isWordGuessed that takes in two parameters
- a string, secretWord, and a list of letters, lettersGuessed.
This function returns a boolean -
True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed)
and False otherwise.'''


def isWordGuessed(secretWord, lettersGuessed):

    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True


print(isWordGuessed(secretWord, lettersGuessed=input("Please guess a letter: ")))
