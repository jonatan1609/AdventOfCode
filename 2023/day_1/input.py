from re import compile

NUMBERS_TO_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
DIGITS_PATTERN = compile(r"\d")
NUMBERS_AND_DIGITS_PATTERN_LTR = compile("|".join(("|".join(NUMBERS_TO_DIGITS), "|".join(NUMBERS_TO_DIGITS.values()))))
NUMBERS_AND_DIGITS_PATTERN_RTL = compile(NUMBERS_AND_DIGITS_PATTERN_LTR.pattern[::-1])


def read_file_as_lines(filename: str = "input") -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def translate_numbers_to_digits(list_of_numbers: list[str]) -> str:
    return "".join(NUMBERS_TO_DIGITS.get(number, number) for number in list_of_numbers)


def find_numbers_in_line(line: str) -> list[str]:
    return (
        NUMBERS_AND_DIGITS_PATTERN_LTR.search(line).group(),
        NUMBERS_AND_DIGITS_PATTERN_RTL.search(line[::-1]).group()[::-1]
    )


def part_1() -> str:
    lines = read_file_as_lines()
    calibration_sum = 0
    for line in lines:
        numbers = DIGITS_PATTERN.findall(line)
        if numbers:
            first, last = numbers[0], numbers[-1]
            calibration_sum += int(first + last)
    return f"The result for part 1 is {calibration_sum}"


def part_2() -> str:
    lines = read_file_as_lines()
    calibration_sum = 0
    for line in lines:
        numbers = find_numbers_in_line(line)
        numbers = translate_numbers_to_digits(numbers)
        if numbers:
            first, last = numbers
            calibration_sum += int(first + last)
    return f"The result for part 2 is {calibration_sum}"



def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()