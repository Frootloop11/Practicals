"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_08.unreliable_car import UnreliableCar


def main():
    reliable = UnreliableCar("reliable", 100, 90)
    unreliable = UnreliableCar("Unreliable", 100, 30)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(reliable.name, reliable.drive(i)))
        print("{:12} drove {:2}km".format(unreliable.name, unreliable.drive(i)))

    print(reliable)
    print(unreliable)


main()
