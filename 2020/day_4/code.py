import re


def read_file(path: str = "input") -> str:
    with open(path) as file:
        return file.read()


def part_1():
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    content = read_file().split("\n\n")
    print("Solution for part 1 of day 4:", sum((set(y.split(":")[0] for y in x.split()) - {"cid"}) == fields for x in content))


def part_2():
    rules = {
        "byr": re.compile(r"(19[2-9][0-9])|(200[0-2])"),
        "iyr": re.compile(r"20(1[0-9]|20)"),
        "eyr": re.compile(r"20(2[0-9]|30)"),
        "hgt": re.compile(r"((1[5-8][0-9])|(19[0-3]))cm|(([56][0-9])|(7[0-6]))in"),
        "hcl": re.compile(r"#[0-9a-f]{6}"),
        "ecl": re.compile(r"amb|blu|brn|gry|grn|hzl|oth"),
        "pid": re.compile(r"[0-9]{9}"),
    }
    content = read_file().split("\n\n")
    valid = 0
    for passport in content:
        passport = dict(x.split(":") for x in passport.split())
        if set(passport.keys()) - {"cid"} == set(rules.keys()):
            for field, value in passport.items():
                if field == "cid":
                    continue
                if not rules[field].fullmatch(value):
                    break
            else:
                valid += 1
    print("Solution for part 2 of day 4:", valid)


part_1()
part_2()
