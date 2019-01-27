#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:57:51 2019

@author: scttohara
"""
#import playDecision
#used for printing spaceship to clean up code
def printDecision( totalWrongGuesses,  spaceship):
   
    if totalWrongGuesses == 0:
       print spaceship[0]
    elif totalWrongGuesses == 1:
        print spaceship[1]
    elif totalWrongGuesses == 2:
        print spaceship[2]
    elif totalWrongGuesses == 3:
        print spaceship[3]
    elif totalWrongGuesses == 4:
        print spaceship[4]
    elif totalWrongGuesses == 5:
        print spaceship[5]
    elif totalWrongGuesses == 6:
            print spaceship[6]
        
            print "\nNOOOOOOO!!!! They got Judy!!!!\nCan't win em' all!!!" 
            print "\nThe codeword was: ", codeWord.upper()
            import playDecision
            playDecision.py
            '''
            playDecision = raw_input("\n\nWould you like to play again (Y/N)? ").lower() 
            
            if playDecision == 'y':
                #needed for .execl
                import os 
                #needed for .executable
                import sys
                os.execl(sys.executable, "python", 'TheGameImpl.py')
                
                #found above three lines of code in first answer here:
                #https://stackoverflow.com/questions/34393714/run-python-script-from-another-python-script-but-not-as-an-child-process
                
                
            else: #playDecision == 'n'
                print "\n\nGoodbye!"
                from sys import exit
                exit();
            '''    
    
import random
#generates a random number between 1 and 4300
randomNumber = random.randint(1,4301) 

'''
opens and reads from nouns.txt into readData which is a list
'''
with open("nouns.txt") as f:  
    readData = f.read()

#splits the list by the \n character in readData list
workingDictionary = readData.split() 

count = 0
for line in workingDictionary:
    count += 1

print workingDictionary[randomNumber]

print count

# code word 
codeWord = workingDictionary[randomNumber]
print codeWord
# code word length
codeWordCount = len(workingDictionary[randomNumber])

'''
Start of game prompt
'''
print "UFO: The Game"
print "Instructions: save us from alien abduction by guessing letters in the codeword.\n\n"

from ufo import x #import the spaceship animation 
#sets x equal to spaceship for clearer code
spaceship = x 

print spaceship[0]

print "\nIncorrect Guesses:\nNone\n\nCodeword:"

x = 0
while x < len(workingDictionary[randomNumber]):
    print "_",
    x+=1

#gets users for guess    
guess = raw_input("\nPlease enter your guess: ") 
   

#total guesses wrong limit 6
totalWrongGuesses = 0
#total guesses right
totalRightGuesses = 0
#import the spaceship animation
from ufo import x
#Wrong letters entered
wrongLetters = ""

#completeGuessesList
completeGuessesList = []

count = 0
while count < codeWordCount:
    
    completeGuessesList += '_'
    count+=1
    
#print completeGuessesList
#print 'hello'

while totalWrongGuesses < 6 and totalRightGuesses < codeWordCount:
    
    '''
    code inside the if statement handles correct guesses
    '''
    if guess in codeWord:
        totalRightGuesses += 1
        
        currentGuessesIndexes = [pos for pos, char in enumerate(codeWord) if char == guess]
        
        #get count and index of where the guess shows up in the codeword
        lengthOfCurrentGuessesIndexes = len(currentGuessesIndexes)
        
        print "\nUFO: The Game"
        print "Instructions: save us from alien abduction by guessing letters in the codeword.\n\n"
        
        #uses function to print correct spaceship
        printDecision( totalWrongGuesses,  spaceship)
         
        if totalWrongGuesses == 0:
            print "\nIncorrect Guesses:\nNone\n\nCodeword:"
        else:
            print "\nIncorrect Guesses:\n", wrongLetters.upper(), " "  
        
            print "\nCodeword: "
            
            
        step = 0
        while step < lengthOfCurrentGuessesIndexes:
            
            completeGuessesList[currentGuessesIndexes[step]] = guess.upper()
            totalRightGuesses+=1
            step +=1
        
        
        print completeGuessesList
        
        if totalRightGuesses == codeWordCount:
            print "Correct! You saved the person and earned a medal of honor!"
            print "The codeword is: ", codeWord
            
            import playDecision
            playDecision.py
            
        #gets user guess
        guess = raw_input("\nPlease enter your guess: ") 
        
        '''
        code inside the else statement handles incorrect guesses
        '''    
    else: #If guess is incorrect
        wrongLetters += guess
        wrongLetters += ' '
        totalWrongGuesses += 1
        print "\nUFO: The Game"
        print "Instructions: save us from alien abduction by guessing letters in the codeword.\n\n"
        
        #uses function to print correct spaceship
        printDecision( totalWrongGuesses,  spaceship)
        '''
        if totalWrongGuesses == 6:
            print spaceship[6]
        
            print "\nNOOOOOOO!!!! They got Judy!!!! (Who's judy?)\nCan't win em' all!!!" 
            print "\nThe codeword was: ", codeWord.upper()
            
            playDecision = raw_input("\n\nWould you like to play again (Y/N)? ").lower() 
            
            if playDecision == 'y':
                #needed for .execl
                import os 
                #needed for .executable
                import sys
                os.execl(sys.executable, "python", 'TheGameImpl.py')
            
                
                #found above three lines of code in first answer here:
                #https://stackoverflow.com/questions/34393714/run-python-script-from-another-python-script-but-not-as-an-child-process
                
            else: #playDecision == 'n'
                print "\n\nGoodbye!"
                from sys import exit
                exit();
        '''     

        print "\nIncorrect Guesses:\n", wrongLetters.upper(), " "  
        
        print "\nCodeword: "

        print completeGuessesList
        
        
        #gets users for guess    
        guess = raw_input("\nPlease enter your guess: ") 
        print codeWord.upper()
    
    '''
    end of else statement, returns to while loop 
    '''
    






