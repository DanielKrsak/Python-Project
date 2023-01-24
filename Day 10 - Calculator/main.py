def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


def calculator():
    still_calculating = True
    while still_calculating:
        first_num = int(input("What's the first number?: "))

        print("+\n-\n*\n/")

        operation = input("Pick an operation?: ")
        second_num = int(input("What's the next number?: "))

        final = calculate(first_num, second_num, operation)

        print(f"{first_num} {operation} {second_num} = {final}")

        decision = input(f"Type 'y' to continue calculating with {final}, or type 'n' to start a new calculation: ")
        while True:
            if decision == "y":
                operation = input("Pick an operation?: ")
                third_number = int(input("What's the next number?: "))
                new_final = calculate(final, third_number, operation)
                print(f"{final} {operation} {third_number} = {new_final}")
                decision = input(
                    f"Type 'y' to continue calculating with {new_final}, or type 'n' to start a new calculation: ")
            elif decision == "n":
                break
            else:
                still_calculating = False
                break


calculator()