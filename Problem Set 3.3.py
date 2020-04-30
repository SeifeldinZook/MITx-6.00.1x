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

'''ps3_hangman
lettersGuessed: list, what letters have been guessed so far
returns: string, comprised of letters that represents what letters
have not yet been guessed.'''
# FILL IN YOUR CODE HERE...
'''Next, implement the function getAvailableLetters that takes in one parameter
- a list of letters, lettersGuessed.
This function returns a string that is comprised of lowercase English letters
- all lowercase English letters that are not in lettersGuessed.'''

'''Hint: You might consider using string.ascii_lowercase,
which is a string comprised of all lowercase letters:'''
import string
# print(string.ascii_lowercase)


def getAvailableLetters(lettersGuessed):
    # string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            temp += i
    return temp


print(getAvailableLetters(lettersGuessed=input("Please guess a letter: ")))
