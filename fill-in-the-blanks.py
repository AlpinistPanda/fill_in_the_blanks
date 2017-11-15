# IPND Fill in the blanks Project
# 12/11/2017 Author: Ozgun Balaban

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

import textwrap
# List of questions
questions = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
'''___1___ officially the Republic of ___1___ is a transcontinental country in Eurasia, mainly
in Anatolia in Western Asia, with a smaller portion on the Balkan peninsula in Southeast Europe.
The country is encircled by seas on three sides with the Aegean Sea to the west, the Black Sea to the north,
and the ___2___ Sea to the south. ___3___ is the capital while ___4___ is the country's largest city
and main cultural and commercial centre. ''',
'''___1___, officially the Republic of ___1___, is a sovereign city-state and island country in Southeast Asia.
It lies one degree (137 km) north of the equator, at the southern tip of the ___2___ Peninsula, with ___3___'s Riau Islands to the south
 and ___4___ to the north. ''']

levels = ["easy", "medium", "hard"]  # levels list so that it is easy to add remove levels

# list of solutions
solutions = [["function", "arguments", "None", "list"],
             ["Turkey", "Mediterranean", "Ankara", "Istanbul"],
             ["Singapore", "Malay", "Indonesia", "Malaysia"]]


# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/


# Plays a full game of fill in the blanks.  A player is prompted to find the missing words in a paragraph
# There are three levels easy, medium, hard

def play_game():
    lifecount = numberOfGuesses()  # number of lives
    print "Please select a difficulty:"
    print "Possible choices are",levels
    difficulty = raw_input("Your choice is: ")
    while(difficulty not in levels): # if the user types any other value than in levels ask again
        print "Wrong choice type it again,"
        difficulty = raw_input("Your choice is: ")
    i = 0
    for word in levels:
        if difficulty == word:
            break
        i += 1

    print "You have chosen", levels[i]
    print "You have", lifecount, "lives"
    print " "
    prompt(difficulty, lifecount, i)

# asks the user number of guesses/lives he/she will have in the game
def numberOfGuesses():
    numberOfGuesses = raw_input("Please select the number of guesses: ")
    if int(numberOfGuesses):
        numberOfGuesses = int(numberOfGuesses)
        guess_text = "\nYou will get " + str(numberOfGuesses) + " chances."
        print "You will get " + str(numberOfGuesses) + " lives."
        return numberOfGuesses

# prompts user to enter the answer checks if it is correct and terminates the game if the user correctly guesses
# the question or he/she runs out of lives
def prompt(difficulty, lifecount, i):
    count = 0   # counts the guesses
    quiz = questions[i] # takes the string from questions list
    print quiz
    if difficulty == levels[i]:
        while lifecount > 0:
            while count < len(solutions[i]):
                text = ("What should" + str(blank(count+1)) + "be: ")
                answer = raw_input(text)
                if answer == solutions[i][count]:
                    print "Well done, You are correct!"
                    quiz = replace(quiz, count+1, answer)
                    wrapText(quiz)
                    count += 1
                    if count == len(solutions[i]):
                        print "Well DONE! You win"
                        exit()
                else: break
            lifecount = wrongAnswer(lifecount)

#  informs the user that he/she input wrong answer, if he/she is out of lives terminates the game
def wrongAnswer(lifecount):
    lifecount -= 1
    if lifecount > 0:
        print "Wrong answer please try again"
        print "You have", lifecount, "lives left"
    else:
        print "Game OVER!! Try again"
        exit()   # terminates the game
    return lifecount

# wraps the text so that it fits nicely in the screen
def wrapText(str):
    quiz = textwrap.wrap(str, width=100)  # 100 characters width
    for element in quiz:
        print(element)

# This replaces the correct answer with the blank

def replace(str2, i, str1):
    dictionary = str2.split()
    replaced = []
    for word in dictionary:
        if blank(i) in word:
            replaced.append(str1)
        else: replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

# Creates the blanks with the required numbers, used to check the blanks
def blank(i):
    blank = "___" + str(i) + "___"  # ex. ___2___
    return str(blank)

play_game()

