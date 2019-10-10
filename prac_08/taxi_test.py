"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_08.taxi import Taxi


def main():
    prius_1 = Taxi("Taxi", 100)
    prius_1.drive(100)
    print(prius_1.get_fare())
    print(prius_1)


main()
