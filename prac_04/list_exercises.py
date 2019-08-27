# numbers = []
#
# for i in range(5):
#     add_number = int(input("add a number"))
#     numbers.append(add_number)
#
# print(numbers)
#
# print("the first number is: {}".format(numbers[0]))
# print("the last number is: {}".format(numbers[-1]))
# print("the smallest number is: {}".format(min(numbers)))
# print("the largest number is: {}".format(max(numbers)))
# print("the average number is: {}".format(sum(numbers) / len(numbers)))

print("case sensitive")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

enter_username = input("enter user name:")

while enter_username not in usernames:
    print("access denied")
    enter_username = input("enter user name:")
print("Access granted")
