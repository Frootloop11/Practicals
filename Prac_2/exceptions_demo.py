"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("denominator can not be zero")
        denominator = int(input("Enter the denominator: "))
        # this line of code prevents the Zero Division Error to ever occur

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

# the Value error only occurs when the numerator and denominator is not a valid number

except ZeroDivisionError:
    print("Cannot divide by zero!")

# The Zero Division Error only occurs when the user adds a 0 to the denominator

print("Finished.")
