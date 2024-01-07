def read_file_as_lines(filename: str = "input") -> list[str]:
    with open(filename, "r") as f:
        return list(map(str.strip, f))


def part_1() -> str:
    lines = read_file_as_lines()

    return f"The result for part 1 is {':('}"


def part_2() -> str:
    lines = read_file_as_lines()
    
    return f"The result for part 2 is {':('}"


def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
