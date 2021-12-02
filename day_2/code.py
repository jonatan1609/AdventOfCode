def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def get_increases(numbers: list) -> int:
    return sum(1 for idx, number in enumerate(numbers) if idx and number > numbers[idx - 1])


def part_1():
    instructions = read_file().splitlines()
    forward, depth = 0, 0
    for instruction in instructions:
        name, value = instruction.split()
        if name == "up":
            depth -= int(value)
        elif name == "down":
            depth += int(value)
        elif name == "forward":
            forward += int(value)

    print("Solution for part 1 of day 2:", forward * depth)


def part_2():
    instructions = read_file().splitlines()
    forward, depth, aim = 0, 0, 0
    for instruction in instructions:
        name, value = instruction.split()
        if name == "up":
            aim -= int(value)
        elif name == "down":
            aim += int(value)
        elif name == "forward":
            forward += int(value)
            depth += aim * int(value)

    print("Solution for part 2 of day 2:", forward * depth)


part_1()
part_2()