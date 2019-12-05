from enum import IntEnum


class Operator(IntEnum):
    ADDITION = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JUMPIFTRUE = 5
    JUMPIFFALSE = 6
    LESSTHAN = 7
    EQUALS = 8
    HALT = 99


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


parameterCount = {
                    Operator.ADDITION: 3,
                    Operator.MULTIPLICATION: 3,
                    Operator.INPUT: 1,
                    Operator.OUTPUT: 1,
                    Operator.JUMPIFTRUE: 2,
                    Operator.JUMPIFFALSE: 2,
                    Operator.LESSTHAN: 3,
                    Operator.EQUALS: 3,
                    Operator.HALT: 0
                 }


class Instruction():
    def __init__(self, number):
        self.operator = number % 100
        self.modes = []
        cur = number // 100
        for i in range(0, parameterCount[self.operator]):
            self.modes.append(cur % 10)
            cur = cur // 10


def getIndex(mode, program):
    if mode == Mode.POSITION:
        return lambda x: program[x]
    if mode == Mode.IMMEDIATE:
        return lambda x: x


def indexError():
    print("Index out of bounds, abort execution")
    return None


def execute(p, input):
    pointer = 0
    inputPointer = 0
    while(pointer < len(p)):
        instruction = Instruction(p[pointer])

        indices = []
        for i in range(0, parameterCount[instruction.operator]):
            if instruction.modes[i] == Mode.POSITION:
                indices.append(p[pointer+i+1])
            elif instruction.modes[i] == Mode.IMMEDIATE:
                indices.append(pointer+i+1)

        if(instruction.operator == Operator.ADDITION):
            p[p[pointer+3]] = p[indices[0]] + p[indices[1]]
            pointer += 4

        elif(instruction.operator == Operator.MULTIPLICATION):
            p[p[pointer+3]] = p[indices[0]] * p[indices[1]]
            pointer += 4

        elif(instruction.operator == Operator.INPUT):
            p[p[pointer+1]] = input[inputPointer]
            pointer += 2
            inputPointer += 1

        elif(instruction.operator == Operator.OUTPUT):
            print("OUTPUT:", p[indices[0]])
            pointer += 2

        elif(instruction.operator == Operator.JUMPIFTRUE):
            if p[indices[0]] != 0:
                pointer = p[indices[1]]
            else:
                pointer += 3

        elif(instruction.operator == Operator.JUMPIFFALSE):
            if p[indices[0]] == 0:
                pointer = p[indices[1]]
            else:
                pointer += 3

        elif(instruction.operator == Operator.LESSTHAN):
            p[p[pointer+3]] = 1 if p[indices[0]] < p[indices[1]] else 0
            pointer += 4

        elif(instruction.operator == Operator.EQUALS):
            p[p[pointer+3]] = 1 if p[indices[0]] == p[indices[1]] else 0
            pointer += 4

        elif(instruction.operator == Operator.HALT):
            return p[0]

        else:
            return None


def main():
    # check if input equals 8: (position)
    test1 = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    # check if input is less than 8: (poisition)
    test2 = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    # check if input equals 8: (immediate)
    test3 = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    # check if input is less than 8: (immediate)
    test4 = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    # check if input is zero (then output 0) (jump/position):
    test5 = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    # check if input is zero (then output 0) (jump/immediate):
    test6 = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    # check if input is below 8 (999), equal to 8 (1000), or greater than 8 (1001):
    test7 = list(map(int, open("testinput.txt", "r").read().split(",")))
    program = list(map(int, open("input.txt", "r").read().split(",")))
    print("Final state:", execute(program, [5]))


if __name__ == "__main__":
    main()
