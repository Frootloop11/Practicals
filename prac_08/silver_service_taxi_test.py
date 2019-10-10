from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("total cost is ${}".format(taxi.get_fare()))


main()
