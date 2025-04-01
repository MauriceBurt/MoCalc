# MoCalc - Version 2.1
# -------------------
# Differences from Version 1:
# - Modular structure introduced with Greeting, BasicCalculator, and SubnettingCalculator classes.
# - BasicCalculator now supports all basic math operations with a loop-back to the main menu.
# - Added looping and decision handling to restart calculator options.
# - Personalized greeting based on user input.
# - Placeholder for subnetting options implemented for future expansion.

class Greeting:
    def __init__(self):
        self.name = input("What is your name? ")
        print(f"Hey {self.name}, welcome to MoCalc! Let's get started.")

    def ask_calculator(self):
        print("Which calculator do you need?")
        print("1. Basic Calculator")
        print("2. Subnetting Calculator")
        choice = input("Enter your choice (1 or 2): ")

        # Direct the user to the selected calculator or prompt again for valid input
        if choice == "1":
            BasicCalculator()
        elif choice == "2":
            SubnettingCalculator()
        else:
            print("Invalid choice. Please try again.")
            self.ask_calculator()

class BasicCalculator:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            print("\n--- Basic Calculator ---")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus")
            print("6. Exponentiation")
            print("0. Return to Main Menu")

            choice = input("Choose an operation: ")

            # Handle returning to the main menu
            if choice == '0':
                print("Returning to main menu...\n")
                return

            # Prompt the user for numbers and handle any input errors
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            # Perform the selected operation and handle division by zero
            if choice == '1':
                result = num1 + num2
                op = '+'
            elif choice == '2':
                result = num1 - num2
                op = '-'
            elif choice == '3':
                result = num1 * num2
                op = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = num1 / num2
                op = '/'
            elif choice == '5':
                result = num1 % num2
                op = '%'
            elif choice == '6':
                result = num1 ** num2
                op = '**'
            else:
                print("Invalid operation choice.")
                continue

            # Display the result of the calculation
            print(f"Result: {num1} {op} {num2} = {result}")

            # Ask if the user wants to perform another calculation
            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                print("Returning to main menu...\n")
                return

class SubnettingCalculator:
    def __init__(self):
        print("Welcome to the Subnetting Calculator!")

        print("What would you like to do?")
        print("A. Breakdown an IP into binary")
        print("B. Find the number of hosts in a subnet")
        print("C. Determine which subnet an IP belongs to")
        print("D. Calculate usable hosts in a subnet")

        choice = input("Enter your choice (A, B, C, D): ")
        print(f"Feature {choice} coming soon...")

def main():
    greeting = Greeting()
    greeting.ask_calculator()

if __name__ == "__main__":
    main()