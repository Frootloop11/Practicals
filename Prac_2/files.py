# user_name = input("Enter Name:")
# out_file = open('name.txt', 'w')
# print(user_name, file=out_file)
# out_file.close()


# in_file = open('name.txt', 'r')
# name = in_file.read().strip()
# in_file.close()
# print("your name is", name)


# in_file = open('numbers.txt', 'r')
# number_1 = int(in_file.readline())
# number_2 = int(in_file.readline())
# in_file.close()
# print(number_1 + number_2)


in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
