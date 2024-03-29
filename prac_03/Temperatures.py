"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU) 
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit(fahrenheit):
    celsius = 5.0 / 9 * (fahrenheit - 32)
    return celsius
