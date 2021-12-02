def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def part_1():
    numbers = [int(x) for x in read_file().splitlines()]
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == 2020:
                return print("Solution for part 1 of day 1:", n1 * n2)


def part_2():
    numbers = [int(x) for x in read_file().splitlines()]
    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    return print("Solution for part 2 of day 1:", n1 * n2 * n3)


part_1()
part_2()
