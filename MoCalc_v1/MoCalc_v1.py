#Welcome to MoCalc! Here, I've designed a calculator that not only does basic calculations, but will also be a useful tool when it comes to
#different networking subnetting! 




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
    print("Welcome to the Basic Calculator!")

    def __init__(self):
        
        print("What would you like to do?")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
    
        choice = input("Enter your choice (A,B ,C ,D): ")
        
        if choice == 'A' or choice == 'a':
            print("Addition, no problem!")
            def __superinit__(x,y):
                x = input("What is the first number? ")
                print(f"{x} + ok, sounds good! ")
                y = input("What is the second number? ")
                print(f"{y} ok, got it!")
                answer = x + y
                print(f"Your answer is {answer}.")

                #Restart calculator
                decision = input("Any more calculations you would like to try? (Y or N)")
                if decision == 'Y' or decision == 'y':
                    self.decision()
                    

        
        elif choice == 'B' or choice == "b":
            print("Subtraction")

class SubnettingCalculator:
    print("Welcome to the Subnetting Calculator!")

    def __init__(self):
        
        print("What would you like to do?")
        print("A. Breakdown an IP into binary")
        print("B. Find the number of hosts in a subnet")
        print("C. Determine which subnet an IP belongs to")
        print("D. Calculate usable hosts in a subnet")

        choice = input("Enter your choice (A, B, C, D): ")
        print(f"Feature {choice} coming soon...")

# Start the program
greeting = Greeting()
greeting.ask_calculator()