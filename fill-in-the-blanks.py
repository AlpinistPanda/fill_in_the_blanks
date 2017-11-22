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


def play_game():
    """
    Plays a full game of fill in the blanks.  A player is prompted to find the missing words in a paragraph
    There are three levels easy, medium, hard
    """

    lifecount = numberOfGuesses()  # number of lives
    print("Please select a difficulty:")
    print("Possible choices are", levels)
    difficulty = input("Your choice is: ")

    while(difficulty not in levels):  # if the user types any other value than in levels ask again
        print("Wrong choice type it again,")
        difficulty = input("Your choice is: ")
    index = 0  # index to match the level in level list 0:easy
    for word in levels:
        if difficulty == word:
            break
        index += 1

    print("You have chosen", levels[index])
    print("You have", lifecount, "lives")
    print(" ")
    prompt(lifecount, index)

def numberOfGuesses():
    """
    Asks the user number of guesses/lives he/she will have in the game
    :return: numberOfGuesses: string number of lives a user gets
    """
    numberOfGuesses = input("Please select the number of guesses: ")
    if int(numberOfGuesses):
        numberOfGuesses = int(numberOfGuesses)
        print("You will get " + str(numberOfGuesses) + " lives.")
        return numberOfGuesses


def prompt(lifecount, index):
    """
    prompts user to enter the answer checks if it is correct and terminates the game if the user correctly guesses
    the question or he/she runs out of lives

    :param lifecount: int number of guesses
    :param index: int difficulty level from the list of levels
    """
    count = 0   # counts the guesses
    quiz = questions[index] # takes the string from questions list
    print(quiz)
    while lifecount > 0:
        while count < len(solutions[index]):
            text = ("What should" + str(blank(count+1)) + "be: ")
            answer = input(text)
            if answer == solutions[index][count]:
                print("Well done, You are correct!")
                quiz = replace(quiz, count+1, answer)
                wrapText(quiz)
                count += 1
                if count == len(solutions[index]):
                    print("Well DONE! You win")
                    exit()
            else: break
        lifecount = wrongAnswer(lifecount)


def wrongAnswer(lifecount):
    """
    Informs the user that he/she input wrong answer, if he/she is out of lives terminates the game
    :param lifecount: int number of guesses
    :return: lifecount: int updated lifecount
    """
    lifecount -= 1
    if lifecount > 0:
        print("Wrong answer please try again")
        print("You have", lifecount, "lives left")
    else:
        print("Game OVER!! Try again")
        exit()   # terminates the game
    return lifecount


def wrapText(string):
    """
    Wraps the text so that it fits nicely in the screen
    :param string: string string to be wrapped
    """
    quiz = textwrap.wrap(string, width=100)  # 100 characters width
    for element in quiz:
        print(element)


def replace(initial_string, index, replaced_string):
    """
    Replaces the correct answer with the blank
    :param initial_string: string initial string
    :param index: int number of the blank to be filled
    :param replaced_string: string replaced blank with correct answer
    :return: replaced: string
    """
    dictionary = initial_string.split() #split the initial string to its sub strings
    replaced = []
    for word in dictionary:
        if blank(index) in word:
            replaced.append(replaced_string)
        else: replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


def blank(index):
    """
    Creates the place holder string that is used as the blanks
    :param index: int the number of the blank
    :return: a place holder string ex; ___2___
    """
    blank = "___" + str(index) + "___"  # ex. ___2___
    return str(blank)

play_game()

