# MoCalc v2.4 - Updated April 3, 2025
# -------------------------------------------------
# ✅ Added full VLSM subnetting support under option D
#    - User inputs multiple subnet sizes
#    - Tool calculates CIDR, total hosts, usable IPs, and broadcast addresses
#    - Subnetting plan is automatically sorted and assigned
# ✅ Improved logic flow for subnet planning and error handling
# ✅ Aligned behavior for returning to main menu in all calculator types
# ✅ Refactored prompts and comments for clarity
# -------------------------------------------------

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
                self.greeting.ask_calculator()
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
            print("B. Find the total and usable hosts from a CIDR")
            print("C. Determine the subnet address from IP and CIDR")
            print("D. Create classless subnets (VLSM) from base IP and device counts")
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
                    if again not in ['yes', 'y']:
                        print("Returning to Subnetting Calculator menu...\n")
                        break
            elif choice == 'b':
                while True:
                    try:
                        cidr = int(input("Enter the CIDR value (e.g., 24 for /24): "))
                        if 1 <= cidr <= 32:
                            total_hosts = 2 ** (32 - cidr)
                            usable_hosts = total_hosts - 2 if total_hosts > 2 else 0
                            print(f"Total hosts: {total_hosts}")
                            print(f"Usable hosts: {usable_hosts}")
                        else:
                            print("CIDR must be between 1 and 32.")
                    except ValueError:
                        print("Invalid input. Please enter an integer.")

                    again = input("Do you want to calculate another host range? (yes/no): ").strip().lower()
                    if again not in ['yes', 'y']:
                        print("Returning to Subnetting Calculator menu...\n")
                        break
            elif choice == 'c':
                while True:
                    try:
                        ip_input = input("Enter an IP address (e.g., 192.168.1.100): ")
                        cidr_input = int(input("Enter the CIDR value (e.g., 24 for /24): "))

                        if not (0 <= cidr_input <= 32):
                            print("CIDR must be between 0 and 32.")
                            continue

                        ip_parts = ip_input.split(".")
                        if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
                            print("Invalid IP address format.")
                            continue

                        ip_binary = ''.join(f"{int(part):08b}" for part in ip_parts)
                        subnet_mask_binary = '1' * cidr_input + '0' * (32 - cidr_input)

                        subnet_binary = ''.join(str(int(ip_binary[i]) & int(subnet_mask_binary[i])) for i in range(32))
                        subnet_decimal = '.'.join(str(int(subnet_binary[i:i+8], 2)) for i in range(0, 32, 8))

                        print(f"Subnet Address: {subnet_decimal}/{cidr_input}")

                    except ValueError:
                        print("Invalid input. Please enter valid IP and CIDR.")

                    again = input("Do you want to calculate another subnet? (yes/no): ").strip().lower()
                    if again not in ['yes', 'y']:
                        print("Returning to Subnetting Calculator menu...\n")
                        break
            elif choice == 'd':
                print("Enter the number of devices needed for each subnet (press Enter when done):")
                device_counts = []
                while True:
                    entry = input("Devices: ").strip()
                    if entry == "":
                        break
                    try:
                        count = int(entry)
                        if count < 1:
                            print("Please enter a positive integer.")
                            continue
                        device_counts.append(count)
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if not device_counts:
                    print("No device counts entered. Returning to Subnetting Calculator menu...\n")
                    continue

                try:
                    base_ip = input("Enter the base IP address (e.g., 192.168.1.0): ").strip()
                    base_parts = [int(part) for part in base_ip.split(".")]
                    if len(base_parts) != 4 or not all(0 <= part <= 255 for part in base_parts):
                        print("Invalid base IP address format.")
                        continue

                    base_binary = ''.join(f"{part:08b}" for part in base_parts)
                    # Convert base IP to binary for subnet block calculations
                    current_ip = int(base_binary, 2)

                    sorted_devices = sorted(device_counts, reverse=True)
                    # Loop through sorted device needs (largest to smallest) and generate subnets
                    print("\n--- Subnet Plan ---")
                    for idx, count in enumerate(sorted_devices):
                        needed_hosts = count + 2  # account for network and broadcast
                        subnet_bits = 0
                        while (2 ** subnet_bits) < needed_hosts:
                            subnet_bits += 1
                        cidr = 32 - subnet_bits
                        total_hosts = 2 ** subnet_bits

                        subnet_ip_binary = f"{current_ip:032b}"
                        subnet_ip = ".".join(str(int(subnet_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

                        # Calculate broadcast address by adding total_hosts - 1
                        broadcast_ip_binary = f"{current_ip + total_hosts - 1:032b}"
                        broadcast_ip = ".".join(str(int(broadcast_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

                        first_usable_ip = None
                        last_usable_ip = None

                        if total_hosts > 2:
                            first_usable_ip_binary = f"{current_ip + 1:032b}"
                            first_usable_ip = ".".join(str(int(first_usable_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

                            last_usable_ip_binary = f"{current_ip + total_hosts - 2:032b}"
                            last_usable_ip = ".".join(str(int(last_usable_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

                        print(f"\nSubnet {idx + 1}:")
                        print(f"  Network ID: {subnet_ip}/{cidr}")
                        print(f"  Total Hosts: {total_hosts}")
                        print(f"  Usable Hosts: {count}")
                        if first_usable_ip and last_usable_ip:
                            print(f"  First Usable IP: {first_usable_ip}")
                            print(f"  Last Usable IP: {last_usable_ip}")
                        print(f"  Broadcast Address: {broadcast_ip}")

                        # Move the current IP to the next available block after assigning this subnet
                        current_ip += total_hosts  # move to next available IP block

                except Exception as e:
                    print(f"An error occurred: {e}")

                # Ask if the user wants to generate another subnet plan
                again = input("\nDo you want to create another subnet plan? (yes/no): ").strip().lower()
                if again not in ['yes', 'y']:
                    print("Returning to Subnetting Calculator menu...\n")
            else:
                print("Sorry, that option isn't available. Try again?")

def main():
    greeting = Greeting()
    greeting.ask_calculator()

if __name__ == "__main__":
    main()