import collections


def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def to_columns(binary):
    c = collections.defaultdict(list)
    for b in binary:
        for idx, i in enumerate(b):
            c[idx].append(i)
    return c


def part_1():
    binary = read_file().splitlines()
    c = to_columns(binary)
    gamma = int("".join(collections.Counter(c[i]).most_common(1)[0][0] for i in range(12)), 2)
    print("Solution for part 1 of day 3:", gamma * (0xfff ^ gamma))


def filter(bit, binary):
    for pos in range(len(binary[0])):
        common = collections.Counter(b[pos] for b in binary).most_common(2)
        if bit == "0": common.sort(key=lambda a: a[1])
        if len(common) > 1 and common[0][1] == common[1][1]:
            common[0] = bit
        for b in binary[:]:
            if b[pos] != common[0][0]:
                binary.remove(b)
    return binary[0]


def part_2():
    binary = read_file().splitlines()
    print("Solution for part 2 of day 3:", int(filter("1", binary.copy()), 2) * int(filter("0", binary.copy()), 2))


part_1()
part_2()
