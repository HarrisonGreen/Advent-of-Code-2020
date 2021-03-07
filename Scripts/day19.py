def read_rules_file(rules_file_path):
    rules = {}
    with open(rules_file_path, "r") as rules_file:
        for line in rules_file:
            line = line.strip("\n")
            line = line.split(":")
            line[0] = int(line[0])

            if len(line[1]) == 4:
                line[1] = [[line[1][2]]]
            
            elif "|" in line[1]:
                line[1] = line[1].split("|")
                line[1] = [[int(i) for i in line[1][0].split()], [int(i) for i in line[1][1].split()]]
                
            else:
                line[1] = [[int(i) for i in line[1].split()]]
            
            rules[line[0]] = line[1]
    return rules

def read_messages_file(messages_file_path):
    messages = []
    with open(messages_file_path, "r") as messages_file:
        for line in messages_file:
            line = line.strip("\n")
            messages.append(line)
    return messages

def check_messages(messages, rules):
    valid = 0
    for message in messages:
        if check_message(message, rules[0][0], rules):
            valid += 1
    return valid

def check_message(message, pattern, rules):
    letter_count = count_letters(pattern)

    if letter_count == 0:
        for possible_pattern in rules[pattern[0]]:
            new_pattern = possible_pattern + pattern[1:]
            if check_message(message, new_pattern, rules):
                return True
        return False

    elif letter_count == len(pattern):
        if match_letters(message, pattern, letter_count) and len(message) == len(pattern):
            return True
        return False

    else:
        if match_letters(message, pattern, letter_count):
            return check_message(message[letter_count:], pattern[letter_count:], rules)
        return False

def count_letters(pattern):
    for i, item in enumerate(pattern):
        if type(item) != str:
            return i
    return i + 1

def match_letters(message, pattern, letter_count):
    match_string = ""
    for i in range(letter_count):
        match_string += pattern[i]
    if message[:letter_count] == match_string:
        return True
    return False

if __name__ == "__main__":
    rules_file_path = "Data/day19_rules.txt"
    messages_file_path = "Data/day19_messages.txt"
    rules = read_rules_file(rules_file_path)
    messages = read_messages_file(messages_file_path)

    print(f"Part one: {check_messages(messages, rules)}")
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    print(f"Part two: {check_messages(messages, rules)}")
