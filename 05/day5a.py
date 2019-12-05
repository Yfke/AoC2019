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
            p[indices[2]] = p[indices[0]] + p[indices[1]]
            pointer += 4
        elif(instruction.operator == Operator.MULTIPLICATION):
            p[indices[2]] = p[indices[0]] * p[indices[1]]
            pointer += 4
        elif(instruction.operator == Operator.INPUT):
            p[indices[0]] = input[inputPointer]
            pointer += 2
            inputPointer += 1
        elif(instruction.operator == Operator.OUTPUT):
            print("Output:", p[indices[0]])
            pointer += 2
        elif(instruction.operator == Operator.HALT):
            return p[0]
        else:
            return None


def main():
    program = list(map(int, open("input.txt", "r").read().split(",")))
    # program = [3, 0, 4, 0, 99]
    # program = [1002, 4, 3, 4, 33]
    # program = [1101, 100, -1, 4, 0]
    print("Final state:", execute(program, [1]))


if __name__ == "__main__":
    main()
