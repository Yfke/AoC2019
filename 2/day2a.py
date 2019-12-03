def indexError():
    print("Index out of bounds, abort execution")
    return None


def execute(p):
    pointer = 0
    while(pointer < len(p)):
        if(p[pointer] == 1):
            # addition
            try:
                p[p[pointer+3]] = p[p[pointer+1]] + p[p[pointer+2]]
                pointer += 4
            except IndexError:
                return indexError()
        elif(p[pointer] == 2):
            # multiplication
            try:
                p[p[pointer+3]] = p[p[pointer+1]] * p[p[pointer+2]]
                pointer += 4
            except IndexError:
                return indexError()
        elif(p[pointer] == 99):
            return p[0]
        else:
            return None


def main():
    program = list(map(int, open("input.txt", "r").read().split(",")))
    program[1] = 12
    program[2] = 2
    print(execute(program.copy()))

if __name__ == "__main__":
    main()
