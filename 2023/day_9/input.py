from sys import argv
from functools import reduce


def read_file_as_lines(filename: str = argv[1]) -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def create_difference_series(series: list[int]) -> list[int]:
    return [b - a for a, b in zip(series, series[1:])]


def part_1() -> str:
    lines = read_file_as_lines()
    result = 0
    for line in lines:
        series = [int(number) for number in line.split()]
        all_series = [series]
        while any(all_series[-1]) and len(all_series[-1]) > 1:            
            all_series.append(create_difference_series(all_series[-1]))
        result += sum(diff_series[-1] for diff_series in all_series)
    return f"The result for part 1 is {result}"


def part_2() -> str:
    lines = read_file_as_lines()
    result = 0
    for line in lines:
        series = [int(number) for number in line.split()]
        all_series = [series]
        while any(all_series[-1]) and len(all_series[-1]) > 1:            
            all_series.append(create_difference_series(all_series[-1]))
        result += reduce(lambda total, current_series: current_series[0] - total, all_series[:-1][::-1], 0)
    return f"The result for part 2 is {result}"


def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()