from re import compile
from functools import reduce
from operator import mul


COLOR_AND_AMOUNT_PATTEN = compile(r"(\d+) (\w+)")
configuration = {"red": 12, "green": 13, "blue": 14}
def read_file_as_lines(filename: str = "input") -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def part_1() -> str:
    lines = read_file_as_lines()
    sum = 0
    for game in lines:
        game_id, sets = game.split(" ", 1)[1].split(":")
        rounds = [set.strip() for set in sets.split(";")]
        for round in rounds:
            is_possible = all(configuration[color] >= int(amount) for amount, color in COLOR_AND_AMOUNT_PATTEN.findall(round))
            if not is_possible:
                break
        else:
            sum += int(game_id)
    return f"The result for part 1 is {sum}"


def part_2() -> str:
    lines = read_file_as_lines()
    power_sum = 0
    for game in lines:
        game_min_amount_of_cubes = {"red": 0, "blue": 0, "green": 0}
        game_id, sets = game.split(" ", 1)[1].split(":")
        rounds = [set.strip() for set in sets.split(";")]
        for round in rounds:
            for amount, color in COLOR_AND_AMOUNT_PATTEN.findall(round):
                game_min_amount_of_cubes[color] = max(game_min_amount_of_cubes[color], int(amount))
        power_sum += reduce(mul, game_min_amount_of_cubes.values())
    
    return f"The result for part 2 is {power_sum}"



def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()