def fuelConsumption(mass):
    return (mass // 3) - 2


def totalFuelConsumption(mass):
    fuel = fuelConsumption(mass)
    while fuel > 0:
        yield fuel
        fuel = fuelConsumption(fuel)


input = map(int, open("input.txt", "r").read().splitlines())
print(sum([sum(totalFuelConsumption(mass)) for mass in input]))
