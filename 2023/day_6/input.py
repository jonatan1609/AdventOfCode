from math import ceil, floor


def read_file_as_lines(filename: str = "input") -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def part_1() -> str:
    lines = read_file_as_lines()
    times, records = [[int(v) for v in line.split(":")[1].split(" ") if v] for line in lines]
    result = 1
    for time, record in zip(times, records):
        """
        t, r = time, record
        x is the time we charge the boat
        we want: 
        x * (t - x) > r
        x ^ 2 - t * x + r < 0
        (t - sqrt(t ^ 2 - 4 * r)) /2 < x < (t + sqrt(t ^ 2 - 4 * r)) / 2 
        This solution is O(π)
        """
        upper_limit = ceil((time + ((time ** 2) - 4 * record) ** 0.5) / 2 - 1)
        lower_limit = floor((time - ((time ** 2) - 4 * record) ** 0.5) / 2 + 1)
        number_of_options = upper_limit - lower_limit + 1
        result *= number_of_options
    return f"The result for part 1 is {result}"


def part_2() -> str:
    lines = read_file_as_lines()
    time, record = [int(line.split(":")[1].replace(" ", "")) for line in lines]
    """
    t, r = time, record
    x is the time we charge the boat
    we want: 
    x * (t - x) > r
    x ^ 2 - t * x + r < 0
    (t - sqrt(t ^ 2 - 4 * r)) /2 < x < (t + sqrt(t ^ 2 - 4 * r)) / 2 
    This solution is O(π)
    """
    upper_limit = ceil((time + ((time ** 2) - 4 * record) ** 0.5) / 2 - 1)
    lower_limit = floor((time - ((time ** 2) - 4 * record) ** 0.5) / 2 + 1)
    number_of_options = upper_limit - lower_limit + 1
    return f"The result for part 2 is {number_of_options}"


def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()