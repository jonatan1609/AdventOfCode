from sys import argv
from itertools import product
from re import compile
from string import digits
from collections import defaultdict
from operator import mul

DIGITS_PATTERN = compile(r"(\d+)")


def read_file_as_lines(filename: str = argv[1]) -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))
    

def is_special_symbol_around(lines: list[str], current_line: int, start_pos: int, end_pos: int) -> bool:
    directions = list(product(range(start_pos - 1, end_pos + 1), (current_line + 1, current_line - 1)))
    directions += [(start_pos - 1, current_line), (end_pos, current_line)]
    line_length = len(lines[current_line])
    amount_of_lines = len(lines)
    for x, y in directions:
        if x < 0 or x >= line_length or y >= amount_of_lines or y < 0:
            continue
        if lines[y][x] not in digits + ".":
            return True


def find_asterisk_around(lines: list[str], current_line: int, start_pos: int, end_pos: int) -> tuple[int, int]:
    directions = list(product(range(start_pos - 1, end_pos + 1), (current_line + 1, current_line - 1)))
    directions += [(start_pos - 1, current_line), (end_pos, current_line)]
    line_length = len(lines[current_line])
    amount_of_lines = len(lines)
    for x, y in directions:
        if x < 0 or x >= line_length or y >= amount_of_lines or y < 0:
            continue
        if lines[y][x] == '*':
            return x, y


def part_1() -> str:
    result_sum = 0
    lines = read_file_as_lines()
    for line_index, line in enumerate(lines):
        digits_in_line = DIGITS_PATTERN.finditer(line)
        for number_match in digits_in_line:
            if is_special_symbol_around(lines, line_index, *number_match.span()):
                result_sum += int(number_match.groups()[0])
    return f"The result for part 1 is {result_sum}"


def part_2() -> str:
    lines = read_file_as_lines()
    results = defaultdict(list)  # (x, y) -> [number1, number2]
    for line_index, line in enumerate(lines):
        digits_in_line = DIGITS_PATTERN.finditer(line)
        for number_match in digits_in_line:
            pos = find_asterisk_around(lines, line_index, *number_match.span())
            if not pos:
                continue
            results[pos].append(int(number_match.groups()[0]))
    gear_ratio = sum(mul(*numbers) for numbers in results.values() if len(numbers) > 1)
    return f"The result for part 2 is {gear_ratio}"


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()