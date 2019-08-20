def main():
    total = 0
    items = int(input("Enter the number of items: "))
    while items <= 0:
        print("Invalid number of items!")
        items = int(input("Enter the number of items: "))

    for i in range(1, items + 1):
        price = float(input("Enter Price of each item: "))
        while price <= 0:
            print("Invalid price!")
            price = float(input("Enter price of item:"))
        total += price

    if total >= 100:
        total *= 0.9
    print("Total price for ", items, " is $", total, sep='')


main()
