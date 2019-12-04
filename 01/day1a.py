def fuelConsumption(mass):
    return (mass // 3) - 2


def main():
    input = [int(mass) for mass in open("input.txt", "r").read().splitlines()]
    print(sum([fuelConsumption(mass) for mass in input]))


if __name__ == "__main__":
    main()
