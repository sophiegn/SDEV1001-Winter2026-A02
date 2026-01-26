print("Welcome to the Ultimate gym")
package = input(""" Please select a membership package (A/B/C/D):
    - Package A: $40/month, 4 months (short-term package)
    - Package B: $55/month, 8 months (standard package)
    - Package C: $75/month, 12 months (regular package)
    - Package D: $100/month, 12 months (premium package, includes 4 free personal training sessions)                 

""").upper()

print(F"You have selected Package {package}")

match package:
    case "A":
        time = 4
        fee = 40
    case "B":
        time = 8
        fee = 55
    case "C":
        time = 12
        fee = 75
    case "D":
        time = 12
        fee = 100
    case _:
        print("Invalid input")
        fee = 0
        time = 0

print(f"Your monthly fee is ${fee}")
print(f"Your total fee is ${fee*time}")