# MoCalc - Version 2.3
# -------------------
# What's New in Version 2.3:
# - Subnetting Calculator now includes Option A: Convert IP address to binary format.
# - Users can now exit the program at any time by typing 'exit'.
# - Added the ability to return to the main menu from both Basic and Subnetting Calculators.
# - Improved input validation and user prompts for a smoother experience.

# -------------------
# Differences from Previous Versions:
#
# Version 1.0:
# - Initial launch of MoCalc.
# - Contained only a basic calculator with limited operations (add, subtract, etc).
# - No modular structure — code was written in one script without class separation.
# - No menu system or user personalization.
#
# Version 2.0:
# - Major refactor introducing modular class structure:
#     - Greeting class for user intro and calculator selection.
#     - BasicCalculator class for all arithmetic functions.
#     - SubnettingCalculator class placeholder created for future subnetting tools.
# - Added looping structure allowing users to perform multiple operations.
# - Personalized greeting with user's name.
# - Clear menu system for calculator selection and returning to main menu.

class Greeting:
    def __init__(self):
        self.name = input("What is your name? ")
        print(f"Hey {self.name}, welcome to MoCalc! Let's get started.")
        print("Type 'exit' at any time to quit the program.")  # Note for exiting

    def ask_calculator(self):
        print("Which calculator do you need?")
        print("1. Basic Calculator")
        print("2. Subnetting Calculator")
        choice = input("Enter your choice (1 or 2): ").strip().lower()

        # Allow the user to exit the program
        if choice == "exit":
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm == "yes":
                print("Goodbye!")
                exit()

        # Direct the user to the selected calculator or prompt again for valid input
        if choice == "1":
            BasicCalculator(self)
        elif choice == "2":
            SubnettingCalculator(self)
        else:
            print("Invalid choice. Please try again.")
            self.ask_calculator()

class BasicCalculator:
    def __init__(self, greeting):
        self.greeting = greeting
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
            print("7. Exit Program")  # Added new menu option
            print("0. Return to Main Menu")

            choice = input("Choose an operation: ").strip().lower()

            # Handle returning to the main menu
            if choice == '0':
                print("Returning to main menu...\n")
                self.greeting.ask_calculator()
                return

            # Handle exiting the program
            if choice == '7':
                confirm = input("Are you sure you want to exit the program? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    print("Exiting program. Goodbye!")
                    exit()

            # Ensure the choice is one of the supported operations
            valid_choices = ['1', '2', '3', '4', '5', '6']
            if choice not in valid_choices:
                print("Invalid operation choice.")
                continue

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

            # Display the result of the calculation
            print(f"Result: {num1} {op} {num2} = {result}")

            # Ask if the user wants to perform another calculation
            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Returning to main menu...\n")
                return

class SubnettingCalculator:
    def __init__(self, greeting):
        self.greeting = greeting
        self.run()

    def run(self):
        while True:
            print("\n----- Subnetting Calculator ------")

            print("What would you like to do?")
            print("A. Breakdown an IP into binary")
            print("B. Find the number of hosts in a subnet")
            print("C. Determine which subnet an IP belongs to")
            print("D. Calculate usable hosts in a subnet")
            print("E. Exit Program")  # Added new menu option
            print("0. Return to Main Menu")  # New menu option to return

            choice = input("Enter your choice (A, B, C, D, E, 0): ").strip().lower()

            # Handle returning to the main menu
            if choice == '0':
                print("Returning to main menu...\n")
                self.greeting.ask_calculator()
                return

            # Handle exiting the program
            if choice == 'e':
                confirm = input("Are you sure you want to exit the program? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    print("Exiting program. Goodbye!")
                    exit()

            if choice == 'a':
                while True:
                    octets = []
                    for i in range(1, 5):
                        while True:
                            try:
                                octet = int(input(f"Enter octet {i} (0-255): "))
                                if 0 <= octet <= 255:
                                    octets.append(octet)
                                    break
                                else:
                                    print("Octet must be between 0 and 255.")
                            except ValueError:
                                print("Invalid input. Please enter an integer.")

                    binary_ip = '.'.join(f"{octet:08b}" for octet in octets)
                    print(f"Binary IP: {binary_ip}")

                    again = input("Do you want to perform another binary breakdown? (yes/no): ").strip().lower()
                    if again != 'yes':
                        print("Returning to Subnetting Calculator menu...\n")
                        break
            else:
                print("Sorry, that option isn't available. Try again?")

def main():
    greeting = Greeting()
    greeting.ask_calculator()

if __name__ == "__main__":
    main()