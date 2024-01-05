from itertools import count


conversion_chain = [
    "seed-to-soil map",
    "soil-to-fertilizer map",
    "fertilizer-to-water map",
    "water-to-light map",
    "light-to-temperature map",
    "temperature-to-humidity map",
    "humidity-to-location map",
]


def read_file_as_categories(filename: str = "input") -> list[str]:
    with open(filename, "r") as f:
        return f.read().split("\n\n")


def convert_category_values_to_ints(values: list[str]):
    for idx, value in enumerate(values[:]):
        values[idx] = list(map(int, value.split()))
    return values


def map_src_to_dest(range_lines: list[str], src: int) -> int:
    for range_line in range_lines:
        dest_start, src_start, range_length = range_line
        if src_start <= src < src_start + range_length:
            return dest_start + src - src_start
    return src


def map_dest_to_src(range_lines: list[str], dest: int) -> int:
    for range_line in range_lines:
        dest_start, src_start, range_length = range_line
        if dest_start <= dest < dest_start + range_length:
            return src_start + dest - dest_start
    return dest


def generate_seeds(seed_ranges):
    for seed_start, seed_length in seed_ranges:
        yield range(seed_start, seed_start + seed_length)


def part_1() -> str:
    categories = read_file_as_categories()
    categories_as_dict = {}
    for category in categories:
        title, values = category.split(":")
        categories_as_dict[title] = values.strip().split("\n")
        convert_category_values_to_ints(categories_as_dict[title])

    seeds = categories_as_dict["seeds"][0]
    results = []
    for seed in seeds:
        result = seed
        for category in conversion_chain:
            result = map_src_to_dest(categories_as_dict[category], result)
        results.append(result)
    return f"The result for part 1 is {min(results)}"


def part_2_slow() -> str:
    categories = read_file_as_categories()
    categories_as_dict = {}
    for category in categories:
        title, values = category.split(":")
        categories_as_dict[title] = values.strip().split("\n")
        convert_category_values_to_ints(categories_as_dict[title])

    seed_ranges = iter(categories_as_dict["seeds"][0])
    seed_ranges = zip(seed_ranges, seed_ranges)
    seeds = generate_seeds(seed_ranges)
    results = []
    for seed in seeds:
        result = seed
        for category in conversion_chain:
            result = map_src_to_dest(categories_as_dict[category], result)
        results.append(result)
    return f"The result for part 2 is {min(results)}"


def part_2() -> str:
    categories = read_file_as_categories()
    categories_as_dict = {}
    for category in categories:
        title, values = category.split(":")
        categories_as_dict[title] = values.strip().split("\n")
        convert_category_values_to_ints(categories_as_dict[title])

    seed_ranges = iter(categories_as_dict["seeds"][0])
    seed_ranges = list(zip(seed_ranges, seed_ranges))

    reversed_conversion_chain = conversion_chain[::-1]
    for location in count():
        result = location
        for conversion_entry in reversed_conversion_chain:
            result = map_dest_to_src(categories_as_dict[conversion_entry], result)
        for seed_start, seed_length in seed_ranges:
            if seed_start <= result < seed_start + seed_length:
                return f"The result for part 2 is {location}"
    # For any complaints, this line of code was written by @dabushori.
    return f"Unfortunately, we didn't find a solution :("


def main() -> None:
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
