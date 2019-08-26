"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def main():

    score = float(input("Enter score: "))
    if possible_score(score):
        print("Invalid score")
    elif possible_score(2):
        print("Excellent")
    elif possible_score(3):
        print("Passable")
    else:
        print("Bad")


def possible_score(score):
    if score < 0 or score > 100:
        return True
    elif score >= 90:
        return 2
    elif score >= 50:
        return 3
    else:
        return False


main()
