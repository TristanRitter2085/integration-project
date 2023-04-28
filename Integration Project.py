""" My First Python Project"""
__author__ = "Tristan Ritter"


# project inspired by the example on Professor Osheroff's course website
# also uses the try except example from the website
# https://sites.google.com/view/profosheroff/programming/languages/python/loops

def math_quiz():
    """
This function executes the math quiz when called.
    """
    divider_quiz = ("-" * 79)
    correct_answers = 0

    # Question 1: 9 to the power of 2
    answer1 = input("What is the answer to the following problem: 9^2?\n")
    answer1 = get_valid_int_input(answer1)
    if answer1 == (9 ** 2):
        print("Correct! The answer is 81\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 81\n" + divider_quiz)

    # Question 2: 10 to the power of two
    quest2 = input(
        "What is the answer to the following problem: 10 ^ 2\n")
    quest2 = get_valid_int_input(quest2)
    if quest2 == (10 ** 2):
        print("Correct! The answer is 100\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 100\n" + divider_quiz)

    # Question 3: 10 multiplied by 2
    answer3 = input(
        "What is the answer to the following problem: 10 * 2\n")
    answer3 = get_valid_int_input(answer3)
    if answer3 == (10 * 2):
        print("Correct! The answer is 20\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 20\n" + divider_quiz)

    # Question 4: 7 multiplied by 5
    answer4 = input(
        "What is the answer to the following problem: 7 * 5\n")
    answer4 = get_valid_int_input(answer4)
    if answer4 == (7 * 5):
        print("Correct! The answer is 35\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 35\n" + divider_quiz)
    # Question 5: 100 divided by 5
    answer5 = input(
        "What is the answer to the following problem: 100 / 5\n"
    )
    answer5 = get_valid_int_input(answer5)
    if answer5 == (100 / 5):
        print("Correct! The answer is 20\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 20\n" + divider_quiz)

    # Question 6: 50 divided by 5
    answer6 = input(
        "What is the answer to the following problem: 50 / 5\n")
    answer6 = get_valid_int_input(answer6)
    if answer6 == (50 / 5):
        print("Correct! The answer is 10\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 10\n" + divider_quiz)

    # Question 7: checks if 20 has remainders

    answer7 = input(
        "Is this number even or odd: 20\n" + "1.even\n" + "2.odd\n")

    answer7 = get_valid_int_input(answer7)
    if (20 % 2 == 0) and (answer7 == 1):
        print("Correct! 20 is an even number\n" + divider_quiz)

        correct_answers += 1
    else:
        print("Incorrect! 20 is an even number\n" + divider_quiz)

    # Question 8: checks if 13 has remainders
    answer8 = input(
        "Is this number even or odd: 13\n" + "1.even\n" + "2.odd\n")

    answer8 = get_valid_int_input(answer8)
    if (13 % 2 != 0) and (answer8 == 2):
        print("Correct! 13 is an odd number\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! 13 is an odd number\n" + divider_quiz)

    # Question 9:20 divided by 3 rounds the answer down to the nearest whole
    # number
    answer9 = input(
        "What is the answer to the following problem: 20// 3" + "\n")
    answer9 = get_valid_int_input(answer9)
    if answer9 == (20 // 3):
        print("Correct! The answer is 6\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 6\n" + divider_quiz)

    # Question 10: 480 divided by 60. rounds down to the nearest whole number
    answer10 = input(
        "What is the answer to the following problem: 480 // 60\n")
    answer10 = get_valid_int_input(answer10)
    if answer10 == (480 // 60):
        print("Correct! The answer is 8\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 8\n" + divider_quiz)

    # Question 11: 9 plus 10
    answer11 = input(
        "What is the answer to the following problem: 9 + 10\n"
    )
    answer11 = get_valid_int_input(answer11)
    if answer11 == (9 + 10):
        print("Correct! The answer is 19\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 19\n" + divider_quiz)

    # Question 12: 20 plus 50
    answer12 = input("What is the answer to the following problem: 20 + 50\n")
    answer12 = get_valid_int_input(answer12)
    if answer12 == (20 + 50):
        print("Correct! The answer is 70\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 70\n" + divider_quiz)

    # Question 13: 70 minus 35
    answer13 = input("What is the answer to the following problem: 70 - 35\n")
    answer13 = get_valid_int_input(answer13)
    if answer13 == (70 - 35):
        print("Correct! The answer is 35\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 35\n" + divider_quiz)

    # Question 14: 950 minus 75
    answer14 = input("What is the answer to the following problem: 950 - 75\n")
    answer14 = get_valid_int_input(answer14)
    if answer14 == (950 - 75):
        print("Correct! The answer is 875\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 875\n" + divider_quiz)
    grade = int(calculate_score(correct_answers))
    grade_string = str(grade)

    print("You made a " + grade_string + "%")


def make_rectangle():
    """
This function asks the user to enter 2 numbers and then produces a
     rectangle. Then the total number of x's are printed. """
    divider_rect = ("-" * 79)
    valid_input = False
    while not valid_input:
        try:
            user_row = int(input("Please enter a number: "))
            user_colum = int(input("please enter a number:"))
            valid_input = True
        except ValueError:
            print("Please enter a valid number.")
    for i in range(user_row):
        for j in range(user_colum):
            print("x" + " ", end="")
        print()
    total_x = user_row * user_colum
    print("There are", total_x, "x's " + "in the rectangle" + "\n",
          divider_rect)


def calculate_score(num_correct):
    """
This function calculates the score of the math quiz.
    num_correct - an integer
    return - returns grade as an integer
    """
    grade = num_correct / 14 * 100
    return grade


def list_definitions():
    """
Prints examples of boolean examples such as "not" and "or"
    """
    divider_explain = ("-" * 79)
    print("The not boolean operator reverses the result")
    print("For example: not(5 < 3) =", not (5 < 3), "\n", divider_explain)
    print(
        "The or boolean operator returns true if one of the statements is true"
    )
    print("For example: (5 > 3 or 6 < 2)=", (5 > 3 or 6 < 2), "\n",
          divider_explain)


def get_valid_int_input(user_input):
    """
This function checks for input that is an Integer
   user_input- takes in user input
    return - returns int_input if the userInput is an integer
    """
    valid_input = False
    new_input = user_input
    while not valid_input:
        try:
            int_input = int(new_input)
            valid_input = True
        except ValueError:
            print("Please enter a valid number.")
            new_input = input()
    return int_input


def intro():
    """
Prints the introduction when called
    """
    divider = ("-" * 79)
    name = input("Please enter your name: ")
    print("Welcome " + name + "!", end=" ")
    print("This is  my Integration Project!")
    print("Version: " + "1", "2", sep=".")
    print("Let's get started!" + "\n" + divider)


def main():
    """
This function is a menu that calls multiple other functions
    """
    intro()
    continue_loop = True
    while continue_loop:
        print("pick one of the options")
        print("1. Math Quiz")
        print("2. Make a rectangle")
        print("3. Some explanations")
        print("4. Exit Program")
        user_option = int(input())
        if user_option == 1:
            math_quiz()
        elif user_option == 2:
            make_rectangle()
        elif user_option == 3:
            definitions()
        elif user_option == 4:
            continue_loop = False
        else:
            print("invalid input. Please try again")


main()
