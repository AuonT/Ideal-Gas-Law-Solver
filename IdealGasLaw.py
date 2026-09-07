import time

def IdealGasLaw():
    R = 8.314462618 #constant for ideal gas law

    variables = {"P":None, "V":None, "n":None,"T":None}
    target = input("Please enter the unit you would like to solve for:\n\n1. Pressure (P)\n2. Volume (V)\n3. Number of moles (n)\n4. Temperature (T)\n\nPlease enter the number corresponding to your choice: ")

    options = {
        "1": "P",
        "2": "V",
        "3": "n",
        "4":" T"
        }

    target = options[target]

    for var in variables:
        if var != target:
            variables[var] = float(input(f"Please enter the value for {var}: "))

    if target == "P":
        p = (variables["n"]*R*variables["T"])/variables["V"]
        print(f"\nThe calculated Pressure (P) is: {p} Pa")
    elif target == "V":
        v = (variables["n"]*R*variables["T"])/variables["P"]
        print(f"\nThe calculated Volume (V) is: {v} m³")
    elif target == "n":
        n = (variables["P"]*variables["V"])/(R*variables["T"])
        print(f"\nThe calculated Number of moles (n) is: {n} mol")
    elif target == "T":
        t = (variables["P"]*variables["V"])/(variables["n"]*R)
        print(f"\nThe calculated Temperature (T) is: {t} K")
        

start = input("Would you like to use my Ideal Gas Law Solver? (y/n): ")
time.sleep(1)

if start != "y" and start != "n":
    while start != "y" and start != "n":
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        print()
        start = input("Would you like to use my Ideal Gas Law Solver? (y/n): ")


if start == "y":
    print ("Hello! Welcome to my Ideal Gas Law Solver!\n\nThis program will help you calculate the missing variable in the Ideal Gas Law equation:\n\nPV = nRT.")
    print()
    time.sleep(3)
    print("Let's start with what variable you would like to solve for!")
    print()
    IdealGasLaw()
else:
    print("Thank you for using my Ideal Gas Law Solver! Goodbye!")
    exit()