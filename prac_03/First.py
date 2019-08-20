def main():

    password = input("enter a password:")

    password = get_password(password)

    get_length(password)


def get_length(password):
    for i in range(len(password)):
        print('*', end='')


def get_password(password):
    while len(password) < 10:
        print("password is not long enough")
        password = input("re-enter a password:")
    return password

