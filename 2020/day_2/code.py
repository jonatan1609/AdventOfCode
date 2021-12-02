def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def part_1():
    ranges = [
        (
            [int(y) for y in x.split()[0].split('-')],
            x.split()[1].strip(":"),
            x.split()[2]
        ) for x in read_file().splitlines()
    ]
    print("Solution for part 1 of day 2:", sum(r1 <= string.count(letter) <= r2 for (r1, r2), letter, string in ranges))


def part_2():
    ranges = [
        (
            [int(y) for y in x.split()[0].split('-')],
            x.split()[1].strip(":"),
            x.split()[2]
        ) for x in read_file().splitlines()
    ]

    print("Solution for part 2 of day 2:", sum((string[r1-1] == letter) ^ (string[r2-1] == letter) for (r1, r2), letter, string in ranges))


part_1()
part_2()
