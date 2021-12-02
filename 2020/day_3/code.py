def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def n_trees(area: list, slope: tuple, n_lines: int) -> int:
    trees = 0
    line = column = 0

    for i in range(n_lines):
        column += slope[0]  # three right
        line += slope[1]  # one down
        if len(area[line]) <= column:
            area[line] *= column
        if area[line][column] == "#":
            trees += 1
        if line == n_lines - 1:
            break

    return trees


def part_1():
    area = read_file().splitlines()
    n_lines = len(area)
    trees = 1
    for slope in (
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
    ):
        trees *= n_trees(area, slope, n_lines)

    print("Solution for part 2 of day 1:", trees)

part_1()
