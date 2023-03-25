# Tristan Ritter
# Menu inspired by the example on Professor Osheroff's course website
# also uses the try except example from the website
# https://sites.google.com/view/profosheroff/programming/languages/python/loops
def mathQuiz():
    divider_quiz = ("-" * 79)
    correct_answers = 0
    grade = str(calculateScore(correct_answers))

    # Question 1: 9 to the power of 2
    print("What is the answer to the following problem: 9^2?")
    user_answer1 = int(input())
    if user_answer1 == (9 ** 2):
        print("Correct! The answer is 81\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 81\n" + divider_quiz)
    # Question 2: 10 to the power of two
    print("What is the answer to the following problem: 10 ^ 2")
    user_answer2 = int(input())
    if user_answer2 == (10 ** 2):
        print("Correct! The answer is 100\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 100\n" + divider_quiz)
    # Question 3: 10 multiplied by 2
    print("What is the answer to the following problem: 10 * 2")
    user_answer3 = int(input())
    if user_answer3 == (10 * 2):
        print("Correct! The answer is 20\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 20\n" + divider_quiz)
    # Question 4: 7 multiplied by 5
    print("What is the answer to the following problem: 7 * 5")
    user_answer4 = int(input())
    if user_answer4 == (7 * 5):
        print("Correct! The answer is 35\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 35\n" + divider_quiz)
    # Question 5: 100 divided by 5
    print("What is the answer to the following problem: 100 / 5")
    user_answer5 = int(input())
    if user_answer5 == (100 / 5):
        print("Correct! The answer is 20\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 20\n" + divider_quiz)
    # Question 6: 50 divided by 5
    print("What is the answer to the following problem: 50 / 5")
    user_answer6 = int(input())
    if user_answer6 == (50 / 5):
        print("Correct! The answer is 10\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 10\n" + divider_quiz)
    # Question 7: checks if 20 has remainders
    print("Is this number even or odd: 20")
    user_answer7 = input()
    if (20 % 2 == 0) and (user_answer7 == "even"):
        print("Correct! 20 is an even number\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! 20 is an even number\n" + divider_quiz)
    # Question 8: checks if 13 has remainders
    print("Is this number even or odd: 13")
    user_answer8 = input()
    if (13 % 2 != 0) and (user_answer8 == "odd"):
        print("Correct! 13 is an odd number\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! 13 is an odd number\n" + divider_quiz)
    # Question 9:20 divided by 3 rounds the answer down to the nearest whole
    # number
    print("What is the answer to the following problem: 20// 3")
    user_answer9 = int(input())
    if user_answer9 == (20 // 3):
        print("Correct! The answer is 6\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 6\n" + divider_quiz)
    # Question 10: 480 divided by 60. rounds down to the nearest whole number
    print("What is the answer to the following problem: 480 // 60")
    user_answer10 = int(input())
    if user_answer10 == (480 // 60):
        print("Correct! The answer is 8\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 8\n" + divider_quiz)
    # Question 11: 9 plus 10
    print("What is the answer to the following problem: 9 + 10")
    user_answer11 = int(input())
    if user_answer11 == (9 + 10):
        print("Correct! The answer is 19\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 19\n" + divider_quiz)
    # Question 12: 20 plus 50
    print("What is the answer to the following problem: 20 + 50")
    user_answer12 = int(input())
    if user_answer12 == (20 + 50):
        print("Correct! The answer is 70\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 70\n" + divider_quiz)
    # Question 13: 70 minus 35
    print("What is the answer to the following problem: 70 - 35")
    user_answer13 = int(input())
    if user_answer13 == (70 - 35):
        print("Correct! The answer is 35\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 35\n" + divider_quiz)
    # Question 14: 950 minus 75
    print("What is the answer to the following problem: 950 - 75")
    user_answer14 = int(input())
    if user_answer14 == (950 - 75):
        print("Correct! The answer is 875\n" + divider_quiz)
        correct_answers += 1
    else:
        print("Incorrect! The answer is 875\n" + divider_quiz)
    print("You made a " + grade + "%")


def rectangle():
    divider_rect = ("-" * 79)
    validInput = False
    while validInput == False:
        try:
            userRow = int(input("Please enter a number: "))
            userColum = int(input("please enter a number:"))
            validInput = True
        except ValueError:
            print("Please enter a valid number.")
    totalx = userRow * userColum
    for i in range(userRow):
        for j in range(userColum):
            print("x" + " ", end="")
        print()
    print("There are", totalx, "x's " + "in the rectangle" + "\n",
          divider_rect)


def calculateScore(num_correct):
    grade = num_correct / 14 * 100
    return grade


def definitions():
    divider_explain = ("-" * 79)
    print("The not boolean operator reverses the result")
    print("For example: not(5 < 3) =", not (5 < 3), "\n", divider_explain)
    print(
        "The or boolean operator returns true if one of the statements is true"
    )
    print("For example: (5 > 3 or 6 < 2)=", (5 > 3 or 6 < 2), "\n",
          divider_explain)


def main():
    divider = ("-" * 79)
    name = input("Please enter your name: ")
    # adds the name string to the print statement
    print("Welcome " + name + "!", end=" ")
    print("This is  my Integration Project!")
    print("Version: " + "1", "2", sep=".")
    print("Let's get started!" + "\n" + divider)
    continue_loop = True
    while continue_loop:
        print("pick one of the options")
        print("1. Math Quiz")
        print("2. Make a rectangle")
        print("3. Some explanations")
        print("4. Exit Program")
        user_option = int(input())
        if user_option == 1:
            mathQuiz()
        elif user_option == 2:
            rectangle()
        elif user_option == 3:
            definitions()
        elif user_option == 4:
            continue_loop = False
        else:
            print("invalid input. Please try again")


main()
