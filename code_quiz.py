#You can assess some python skills with this interactive quiz


#Modules and packages.
from random import randint

#Tests and answers by levels.
correct_answers_beginner  = ["text editor" , "Indentation" , "HTML" , "browser"]

test_string_beginner = "The best way to type the code in a readable form is by using a ___1___.\
___2___ is the technique that makes the code even more reabable and organized because it allows \
to distinguigh clearly the logic of the loops and the statements by aligning properly each of the \
elements. The first language that we learnt in this course was ___3___ and one of its main features \
is that it is interpreted by a ___4___."

correct_answers_intermediate  = ["python" , "interpreted" , "loops" , "condition"]

test_string_intermediate = "The ___1___ language is a general - purpose programming language that \
uses indentation to delimit blocks of code instead of curly brackets. There are ___2___ and compiled \
languages, this characteristic defines the way the language gives instructions to the CPU. The ___3___ \
play a very important role in programming because they allow to repeat a series of instructions as many \
times as needed. It important to mention that the instructions will be repeated until a ___4___ is met."

correct_answers_advanced = ["if" , "for" , "while" , "list"]

test_string_advanced = "An ___1___ statement is run once is if its condition evaluates to true. When the number \
of times that an instruction should be repeated is known is suitable to use a ___2___ loop. When the number of \
times an instruction should be repeated is not known, it is better to use a ___3___ loop. A ___4___ is a set of \
elements that are indexed."

blanks = ["___1___","___2___","___3___","___4___"]

#Functions section.

def game(test_string,correct_answers,number_guesses,blanks):
    #Runs the game, evalueates the answer, and gives more chances.
    """ def game(test_string,correct_answers,number_guesses):
    This function runs the game, evaluates if the answer is correct. When the answer is wrong, it gives
    as many more chances as the user has selected.

    Arguments received:
    test_string: is the text with the blanks to fill in to answer the quiz
    correct_answers: is the list with the correct answers by levels
    number_guesses: is the number of guesses selected by the user_answer

    Functions called:
    type_your_answer, compliment, rebuke, score.

    Returns:
    The complete string with right and wrong answers and the score obtained by the
    contestant."""

    correct = 0
    for index_of_blank, blank in enumerate(blanks):
        for attempt in range(int(number_guesses)):

            user_answer = type_your_answer(test_string,number_guesses,blank,attempt)

            if user_answer == correct_answers[index_of_blank]:
                test_string = test_string.replace(blanks[index_of_blank],user_answer)
                print(compliment())
                correct += 1
                break
            elif attempt != int(number_guesses)-1:
                print(rebuke() + "\n")
                print("Try one more time...")
                continue
            else:
                print(rebuke() + "\n")
                continue

        test_string = test_string.replace(blanks[index_of_blank] , "_Failed_")
    return "\n" + test_string + "\n" + "\n" + score(correct)

def type_your_answer(test_string,number_guesses,blank,attempt):

    #Allows the users to type their answers.
    """ def type_your_answer(test_string,number_guesses,blank,attempt):
    This function allows the users to type their answers.

    Arguments received:
    test_string: is the text with the blanks to fill in to answer the quiz
    number_guesses: is the number of guesses selected by the user_answer
    blank: this is the blank that corresponds to the question
    attempt: is the number of the trial the user is in

    Returns:
    The user's answer"""

    print("\n" + test_string)
    print("\n" + "Watch the uppercase for the beginning of a sentence and acronyms!!!")
    user_answer = input("\n" + "You have " + str(int(number_guesses)-attempt) + " attempts. Type in your answer for " + blank + ":")
    return user_answer

def compliment():
    #If the answer is right compliments.
    """ def compliment():
    This function compliments when answer is correct.

    Arguments received:
    None

    Returns:
    A random compliment."""

    random_num = randint(0,2)
    if random_num == 0:
        return "\n" + "You rock!!"
    elif random_num == 1:
        return "\n" + "Great!!"
    elif random_num == 2:
        return "\n" + "You genius!!"

def rebuke():

    #If the answer is wrong rebukes.
    """ def rebuke():
    This function rebukes when the answer is wrong.

    Arguments received:
    None

    Returns:
    A random rebuke."""

    random_num = randint(0,2)
    if random_num == 0:
        return "\n" + "Too bad!!"
    elif random_num == 1:
        return "\n" + "Not your day!!"
    elif random_num == 2:
        return "\n" + "Focus!!"

def score(correct):

    #Returns the score of the game according to the correct answers.
    """ def score(correct):
    This function calculates the score obtained by the user.

    Arguments received:
    correct: is the number of correct answers of the user

    Returns:
    The score."""

    score = correct*25
    return "Your score: " + str(score) + "/100"

def select_level():
    #this function allows the user to select a level and then returns this information
    """ def select_level():
    This function allows the user to select a difficulty level of the quiz. It keeps asking if
    the level is not in the valid list.

    Arguments received:
    None

    Returns:
    A level of difficulty."""

    level_selected = input("Please, select your level (1 for beginner, 2 for intermediate, 3 for advanced):")
    while level_selected not in ["1" , "2" , "3"]:
        print("That's not a valid option!! Try again.")
        level_selected = input("Please, select your level (1 for beginner, 2 for intermediate, 3 for advanced):")
    return level_selected

def game_level(level_selected):
    #Once the user has selected the level this function takes this information and returns the test and answers by level-
    """ def game_level(level_selected):
    This function returns the test and the answers according to the level selected by the user.

    Arguments received:
    level_selected: level chosen by the user

    Returns:
    Test and answers according to level."""

    if level_selected == "1":
        return (test_string_beginner , correct_answers_beginner)
    elif level_selected == "2":
        return (test_string_intermediate , correct_answers_intermediate)
    elif level_selected == "3":
        return (test_string_advanced , correct_answers_advanced)
    else:
        return "invalid"

def number_of_guesses():

    #The user defines the number of guesses before failing a question.
    """ def number_of_guesses():
    This function allows the user to choose a number of guesses before failing a question.

    Arguments received:
    None

    Returns:
    The number of guesses selected."""

    number_of_guesses = input("Select the number of guesses before failing (the sky's the limit):")
    return number_of_guesses

def the_main_menu():

    #this function follows the main flow of the game
    """ def the_main_menu():
    This function follows the main flow of the game.

    Arguments received:
    None

    Functions called:
    level, number_guesses, game

    Returns:
    The finalization of the game."""

    level = select_level()
    test_string , correct_answers = game_level(level)
    number_guesses = number_of_guesses()
    print(game(test_string,correct_answers,number_guesses,blanks))
    return "\n" + "Always keep learning!!!"

#This command runs the game.
print(the_main_menu())
