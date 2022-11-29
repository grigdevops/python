#Calculator by Grig



#ADD
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# Operations Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number? " ))


    for key in operations:
        print(key)

    want_continue = True

    while want_continue:
        operations_choose = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        answer = operations[operations_choose](num1, num2)

        print(f"{num1} {operations_choose} {num2} = {answer}")

        # operations_choose_2 = input("Pick an operation from the line above: ")
        # num3 = int(input("What is the third number? "))
        #
        # answer_second = operations[operations_choose_2](operations[operations_choose](num1, num2), num3)
        #
        # print(f"{answer} {operations_choose_2} {num3} = {answer_second}")
        if input(f"'Y' to continue with {answer}, type 'N' to exit. ") == "Y":
            num1 = answer
        else:
            want_continue = False
            calculator()


calculator()




