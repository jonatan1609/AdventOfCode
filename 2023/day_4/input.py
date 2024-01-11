from sys import argv


def read_file_as_lines(filename: str = argv[1]) -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def part_1() -> str:
    lines = read_file_as_lines()
    points = 0
    for card in lines:
        card = card.split(': ')[1]
        winning_numbers, my_numbers = card.split(' | ')
        winning_numbers = list(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        points += int(2 ** ((total := sum(number in winning_numbers for number in my_numbers)) - 1)) * bool(total)
    return f"The result for part 1 is {points}"


def part_2() -> str:
    lines = read_file_as_lines()
    counters = {number: 1 for number in range(1, len(lines) + 1)}
    for card_number, card in enumerate(lines, 1):
        card = card.split(': ')[1]
        winning_numbers, my_numbers = card.split(' | ')
        winning_numbers = list(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        matches = sum(number in winning_numbers for number in my_numbers)
        for match_index in range(1, matches + 1):
            counters[card_number + match_index] += counters[card_number]
    total_cards = sum(counters.values())
    return f"The result for part 2 is {total_cards}"


def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()