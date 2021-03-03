def read_passport_file(file_path):
    passports = []
    passport = {}
    with open(file_path, "r") as passport_file:
        for line in passport_file:

            if line == "\n":
                passports.append(passport)
                passport = {}
            else:
                line = line.split()
                for item in line:
                    passport[item.split(":")[0]] = item.split(":")[1]

    if passport:
        passports.append(passport)

    return passports

def process_passports(passports):
    passed_field_check = []
    for passport in passports:
        if check_passport_fields(passport):
            passed_field_check.append(passport)
    print(f"Part one: {len(passed_field_check)}")

    passed_data_check = []
    for passport in passed_field_check:
        if check_passport_data(passport):
            passed_data_check.append(passport)
    print(f"Part two: {len(passed_data_check)}")

def check_passport_fields(passport):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in passport.keys():
            return False
    return True

def check_passport_data(passport):

    if not 1920 <= int(passport["byr"]) <= 2002:
        return False

    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False

    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False

    if passport["hgt"].endswith("cm"):
        if not 150 <= int(passport["hgt"].strip("cm")) <= 193:
            return False
    elif passport["hgt"].endswith("in"):
        if not 59 <= int(passport["hgt"].strip("in")) <= 76:
            return False
    else:
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not len(passport["pid"]) == 9:
        return False

    if len(passport["hcl"]) != 7:
        return False
    else:
        if passport["hcl"][0] != "#":
            return False
        valid_characters = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(1,7):
            if passport["hcl"][i] not in valid_characters:
                return False

    return True

if __name__ == "__main__":
    file_path = "Data/day4_input.txt"
    passports = read_passport_file(file_path)
    process_passports(passports)
