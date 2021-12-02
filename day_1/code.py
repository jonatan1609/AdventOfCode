def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def get_increases(numbers: list) -> int:
    return sum(1 for idx, number in enumerate(numbers) if idx and number > numbers[idx - 1])


def part_1():
    numbers = [int(x) for x in read_file().splitlines()]
    increases = get_increases(numbers)
    print("Solution for part 1 of day 1:", increases)


def part_2():
    numbers = [int(x) for x in read_file().splitlines()]
    grouped_numbers = [sum(numbers[x:x+3]) for x in range(len(numbers))]
    increases = get_increases(grouped_numbers)
    print("Solution for part 2 of day 1:", increases)


part_1()
part_2()
