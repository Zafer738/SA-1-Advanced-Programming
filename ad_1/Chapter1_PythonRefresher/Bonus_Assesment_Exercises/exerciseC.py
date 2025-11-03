# this program creates a calculator using functions and a loop
# it should allow the user to do addition, subtraction, multiplication, division, and modulus

# define to add numbers
def add(x, y):
    return x + y

# defining a function to subtract the second number from the first
def subtract(x, y):
    return x - y

# defining a function to multiply two numbers
def multiply(x, y):
    return x * y

# defining a function to divide the first number by the second
# also check if user tries to divide by zero
def divide(x, y):
    if y == 0:
        return "cannot divide by zero"
    return x / y

# now this function is to find the remainder (modulus)
#also checks if the user tries to divide by zero
def modulus(x, y):
    if y == 0:
        return "cannot find modulus with zero"
    return x % y

# using an infinite while loop so that the calculator runs until the user wants to stop
while True:
    # here is the calculator menu
    print("\ncalculator menu:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. modulus")

    # agive the user the option first
    choice = input("enter your choice (1-5): ")

    # to check if its in the option
    if choice in ['1', '2', '3', '4', '5']:
        # then asks the user to enter 2 numbers
        x = float(input("enter first number: "))
        y = float(input("enter second number: "))

        # does the correct calculation based on what the user picks
        if choice == '1':
            print("result:", add(x, y))
        elif choice == '2':
            print("result:", subtract(x, y))
        elif choice == '3':
            print("result:", multiply(x, y))
        elif choice == '4':
            print("result:", divide(x, y))
        elif choice == '5':
            print("result:", modulus(x, y))
    else:
        # incase to handle invalid menu
        print("invalid input")

    # asks the user if they want to perform another calculation
    again = input("would you like to perform another calculation? (yes/no): ").lower()

    # if the user enters anything other than 'yes', the program ends
    if again != 'yes':
        print("thank you for using the calculator.")
        break
