lower = 382345
upper = 843167


def passArray(n):
    result = []
    while(n > 0):
        result.append(n % 10)
        n = n // 10
    result.reverse()
    return result


def meetsCriteria(n):
    password = passArray(n)

    # check length:
    if len(password) != 6:
        return False

    # check adjacency:
    met = False
    if password[0] == password[1] and password[1] != password[2]:
        met = True
    for i in range(1, len(password)-2):
        if (password[i-1] != password[i] and
              password[i] == password[i+1] and
              password[i+1] != password[i+2]):
            met = True
    if (password[-3] != password[-2] and
          password[-2] == password[-1]):
        met = True
    if not met:
        return False

    # check nondecreasingness:
    for i in range(0, len(password)-1):
        if password[i] > password[i+1]:
            return False

    # all conditions are met:
    return True


def main():
    print(len([p for p in range(lower, upper) if meetsCriteria(p)]))


if __name__ == "__main__":
    main()
