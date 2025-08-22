import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,                        #Here the functions are stored as values in the list.
    "-": subtract,                   #NOTE : Here these functions are not being triggered since no parenthesis after function name.
    "*": multiply,                   #NOTE : The functions reference are just stored as values in their respective keys in the list
    "/": divide,
}


def calculator():
    print(art.logo)       #Displaying logo of calculator imported from art.py
    should_accumulate = True
    num1 = float(input("What is the first number?: "))         # num_1 is placed out of loop for user to continue with the previous result. Previous result will act as num1 in that case

    while should_accumulate:
        for symbol in operations:     #printing the operation symbols +, - , *, /
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)      #Calls the appropriate function that matches the operation chosen by the user and the value returned by the function gets stored in variable answer.
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer      #If user wants to continue performing operation on the previous result then in that case the answer becomes num_1
        else:
            should_accumulate = False
            print("\n" * 50)
            calculator()             #Recursion is occurring  - Calling same function again until the user chooses something different


calculator()
