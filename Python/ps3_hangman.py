# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/rosacristobalcastro/Desktop/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    # FILL IN YOUR CODE HERE...
    result = True
    
    for char in secretWord:
        if not char in lettersGuessed: 
            result = False
            
            
    return result


def getGuessedWord(secretWord, lettersGuessed):

    result = ''
    
    
    for char in secretWord:
        if not char in lettersGuessed: 
            result += ' _ '
        else :
            result += char
            
    return result



def getAvailableLetters(lettersGuessed):

    import string
    result = ''
    for char in string.ascii_lowercase:
        if not char in lettersGuessed: 
            result += char
           
    return result
 


def hangman(secretWord):
    
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    
    n = 0
    
    newGuess = 0
    lettersguessed = []
    mistakesMade = 0
    finalScore = False
    chancesLeft = 8 - mistakesMade
    
    while mistakesMade < 8 and finalScore == False:
        print "------------"
        print "You have " + str(chancesLeft) + " guesses left."
        print "Available letters: " + getAvailableLetters(lettersguessed)
        newGuess = raw_input('Please guess a letter:')
             
        if newGuess in lettersguessed: 
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersguessed)
        elif newGuess in secretWord:
            lettersguessed.append(newGuess)
            print "Good guess: " + getGuessedWord(secretWord, lettersguessed)
        elif not newGuess in secretWord: 
            lettersguessed.append(newGuess)
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersguessed)
            mistakesMade += 1
        
        chancesLeft = 8 - mistakesMade
        finalScore = isWordGuessed(secretWord, lettersguessed)
            
    if finalScore == True:
        print "------------"
        print "Congratulations, you won!"
    else :
        print "------------"
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."

        #print "Good guess: " + letterGuess

hangman('vanessa')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
