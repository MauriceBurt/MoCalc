# MoCalc - Version 2
# -------------------
# Differences from Version 1:
# - Modular structure introduced with Greeting, BasicCalculator, and SubnettingCalculator classes.
# - BasicCalculator now supports addition and subtraction functionality.
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

        if choice == "1":
            BasicCalculator()
        elif choice == "2":
            SubnettingCalculator()
        else:
            print("Invalid choice. Please try again.")
            self.ask_calculator()

class BasicCalculator:
    def __init__(self):
        print("Welcome to the Basic Calculator!")
        
        while True:
            print("What would you like to do?")
            print("A. Addition")
            print("B. Subtraction")
            print("C. Multiplication")
            print("D. Division")
            print("E. Exit")
            
            choice = input("Enter your choice (A, B, C, D, E): ").strip().upper()
            
            if choice == 'A':
                print("Addition, no problem!")
                x = int(input("What is the first number? "))
                y = int(input("What is the second number? "))
                answer = x + y
                print(f"Your answer is {answer}.")
            
            elif choice == 'B':
                print("Subtraction, no problem!")
                x = int(input("What is the first number? "))
                y = int(input("What is the second number? "))
                answer = x - y
                print(f"Your answer is {answer}.")
            
            elif choice == 'E':
                print("Returning to main menu...")
                break
            
            else:
                print("That option isn't available yet or is invalid.")
                continue

            decision = input("Any more calculations you would like to try? (Y/N): ").strip().upper()
            if decision != 'Y':
                print("Returning to main menu...")
                break

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