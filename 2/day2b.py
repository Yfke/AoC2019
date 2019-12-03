program = list(map(int, open("input.txt", "r").read().split(",")))


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
    for verb in range(0, 100):
        for noun in range(0, 100):
            program[1] = noun
            program[2] = verb
            if(execute(program.copy()) == 19690720):
                print(verb, noun)
                print(100*noun+verb)

if __name__ == "__main__":
    main()
