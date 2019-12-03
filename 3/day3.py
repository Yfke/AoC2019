class Line:
    def __init__(self, x1, y1, x2, y2, history):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.history = history

    def isVertical(self):
        return self.x1 == self.x2

    def isHorizontal(self):
        return self.y1 == self.y2

    def intersection(self, other):
        if self.isHorizontal() and other.isVertical():
            return intersect(self, other)
        elif self.isVertical() and other.isHorizontal():
            return intersect(other, self)
        else:
            return None


# Return the point of intersection between a horizontal and a vertical line,
# if it exists. Also return the combined number of steps it took to get there.
def intersect(h, v):
    if min(h.x1, h.x2) <= v.x1 <= max(h.x1, h.x2):
        if min(v.y1, v.y2) <= h.y1 <= max(v.y1, v.y2):
            steps = h.history + abs(v.x1 - h.x1) + v.history + abs(h.y1 - v.y1)
            return v.x1, h.y1, steps
    return None


# Turn a list of (string-formatted) instructions into a list of lines
def getLines(instructions):
    lines = []
    x, y = 0, 0
    history = 0
    for direction, *dist in instructions:
        distance = int(''.join(dist))
        xnew, ynew = x, y
        if(direction == 'U'):
            ynew += distance
        elif(direction == 'D'):
            ynew -= distance
        elif(direction == 'L'):
            xnew -= distance
        elif(direction == 'R'):
            xnew += distance
        else:
            print("Error: direction not found")
        lines.append(Line(x, y, xnew, ynew, history))
        x, y = xnew, ynew
        history += distance
    return lines


# The objective function for the first assignment
def objective1(t):
    return abs(t[0]) + abs(t[1])


# The objective function for the second assignment
def objective2(t):
    return t[2]


def main():
    input = "U1,L1,R1\nR1,U1,L1"
    input = "R8,U5,L5,D3\nU7,R6,D4,L4"
    input = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
    input = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    input = open("input.txt", "r").read()
    inst = [l.split(",") for l in input.splitlines()]
    intersections = [line1.intersection(line2) for line1 in getLines(inst[0])
                                               for line2 in getLines(inst[1])]
    intersections = list(filter(
        lambda x: x is not None and (x[0], x[1]) != (0, 0),
        intersections)
    )
    #print(intersections)
    print(min([objective1(i) for i in intersections]))


if __name__ == "__main__":
    main()
