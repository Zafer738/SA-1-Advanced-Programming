import random

# here's the Function: displayMenu
# Displays the "difficulty" menu wwhich the user can choose as per their liking
def displayMenu():
    print("\n" + "=" * 40)
    print("       MATHS QUIZ - SELECT DIFFICULTY")
    print("=" * 40)
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    print("=" * 40)

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


# next up is the function: randomInt
# Returns a random integer based on difficulty, its like level based so higher the difficult i added more zero's so its harder to calculate

def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)


# here's the function: decideOperation
# it randomly chooses whether to add + or subtract- 

def decideOperation():
    return random.choice(['+', '-'])


# this is Function: isCorrect
# it checks if the answer is correct or wrong and provides some feedback

def isCorrect(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("✅ Correct!\n")
        return True
    else:
        print("❌ Incorrect.\n")
        return False


# here is the function: displayProblem
# it displays one math problem, and then gets user’s answers
# once it gets that, it awards 10 or 5 points accordingly

def displayProblem(level):
    num1 = randomInt(level)
    num2 = randomInt(level)
    operation = decideOperation()

    #to calculate the correct answer
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    # to ask the user for their result & to check for any mistakes or errors
    print(f"{num1} {operation} {num2} = ?")

    for attempt in range(2):  # but keep in mind the user only gets max two tries
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if isCorrect(user_answer, correct_answer):
            return 10 if attempt == 0 else 5  # so the user gets 10 points if they get it right on 1st try, but only 5 points on 2nd try, since they got the first one wrong
        else:
            if attempt == 0:
                print("Try once more!")
            else:
                print(f"The correct answer was: {correct_answer}\n")

    return 0  # user/player gets no points if both wrong


# here's the function: displayResults
# this shows the total score and grade, like A, B, or F based on a scale from 1-100

def displayResults(score):
    print("\n" + "=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)
    print(f"Your total score: {score} / 100")

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Your grade: {grade}")
    print("=" * 40 + "\n")


# now here's the main function
# this runs the entire quiz and replay option

def main():
    print("\nWelcome to the Python Maths Quiz!")
    print("You’ll answer 10 arithmetic questions.\n")

    while True:
        level = displayMenu()
        total_score = 0

        for i in range(1, 11):
            print(f"Question {i}/10")
            total_score += displayProblem(level)

        displayResults(total_score)

        again = input("Would you like to play again? (yes/no): ").strip().lower()
        if again != 'y':
            print("\nThank you for playing! Goodbye!\n")
            break


#to run the program

if __name__ == "__main__":
    main()
