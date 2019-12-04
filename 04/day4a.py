lower = 382345
upper = 843167


def meetsCriteria(n):
    password = [int(s) for s in str(n)]

    # check length:
    if len(password) != 6:
        return False

    # check adjacency:
    met = False
    for i in range(0, len(password)-1):
        if password[i] == password[i+1]:
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
