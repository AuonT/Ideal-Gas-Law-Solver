import sys
import time

def calculate_ideal_gas():
    # Ideal gas constant in J/(mol·K) or (Pa·m³)/(mol·K)
    R = 8.314462618 

    options = {
        "1": "P",
        "2": "V",
        "3": "n",
        "4": "T"
    }
    
    print("Please select the variable to solve for:")
    print("1. Pressure (P)\n2. Volume (V)\n3. Number of moles (n)\n4. Temperature (T)")
    
    choice = input("\nEnter choice (1-4): ")
    while choice not in options:
        choice = input("Invalid choice. Please enter a number between 1 and 4: ")

    target = options[choice]
    variables = {"P": None, "V": None, "n": None, "T": None}

    # Collect input values with validation
    for var in variables:
        if var != target:
            while True:
                try:
                    val = float(input(f"Enter value for {var}: "))
                    if val <= 0:
                        print("Value must be strictly positive (> 0) for physical systems.")
                        continue
                    variables[var] = val
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid numerical value.")

    # Execute thermodynamic calculation based on target variable
    if target == "P":
        res = (variables["n"] * R * variables["T"]) / variables["V"]
        print(f"\nCalculated Pressure (P): {res} Pa")
    elif target == "V":
        res = (variables["n"] * R * variables["T"]) / variables["P"]
        print(f"\nCalculated Volume (V): {res} m³")
    elif target == "n":
        res = (variables["P"] * variables["V"]) / (R * variables["T"])
        print(f"\nCalculated Molar Amount (n): {res} mol")
    elif target == "T":
        res = (variables["P"] * variables["V"]) / (variables["n"] * R)
        print(f"\nCalculated Temperature (T): {res} K")


def main():
    start = input("Launch Ideal Gas Law Solver? (y/n): ").lower()
    while start not in ["y", "n"]:
        start = input("Invalid input. Enter 'y' or 'n': ").lower()

    if start == "y":
        print("\nIdeal Gas Law Solver initialized (PV = nRT).\n")
        time.sleep(1)
        calculate_ideal_gas()
    else:
        print("Exiting tool.")
        sys.exit()

if __name__ == "__main__":
    main()