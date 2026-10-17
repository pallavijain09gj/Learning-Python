import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def power(base, exponent):
    return base ** exponent


def logarithm(value, base):
    if value <= 0:
        raise ValueError("Logarithm input must be greater than zero.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be greater than zero and not equal to 1.")
    return math.log(value, base)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu():
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Logarithm")
    print("7. Exit")


def main():
    print("Welcome to the Professional Calculator")

    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid selection. Please choose a number from 1 to 7.")
            continue

        if choice == '6':
            value = get_number("Enter the value: ")
            base = get_number("Enter the logarithm base: ")
            try:
                result = logarithm(value, base)
                print(f"Logarithm: log({base}) {value} = {result}")
            except ValueError as error:
                print(f"Error: {error}")
        else:
            first_number = get_number("Enter the first number: ")
            second_number = get_number("Enter the second number: ")

            if choice == '1':
                result = add(first_number, second_number)
                print(f"Addition: {first_number} + {second_number} = {result}")
            elif choice == '2':
                result = subtract(first_number, second_number)
                print(f"Subtraction: {first_number} - {second_number} = {result}")
            elif choice == '3':
                result = multiply(first_number, second_number)
                print(f"Multiplication: {first_number} * {second_number} = {result}")
            elif choice == '4':
                try:
                    result = divide(first_number, second_number)
                    print(f"Division: {first_number} / {second_number} = {result}")
                except ValueError as error:
                    print(f"Error: {error}")
            elif choice == '5':
                result = power(first_number, second_number)
                print(f"Exponent: {first_number} ^ {second_number} = {result}")

        another_calculation = input("Would you like to perform another calculation? (y/n): ").strip().lower()
        if another_calculation != 'y':
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
