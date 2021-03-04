def read_input(file_path):
    groups_responses = []
    group = []

    with open(file_path, "r") as data_file:
        for line in data_file:
            if line == "\n":
                groups_responses.append(group)
                group = []
            else:
                group.append(line.strip("\n"))

    if group:
        groups_responses.append(group)
    
    return groups_responses

def count_responses(groups_responses):
    anyone_count = sum(len(set().union(*group)) for group in groups_responses)
    everyone_count = sum(len(set(group[0]).intersection(*group)) for group in groups_responses)

    print(f"Part one: {anyone_count}\nPart two: {everyone_count}")

if __name__ == "__main__":
    file_path = "Data/day6_input.txt"
    groups_responses = read_input(file_path)
    count_responses(groups_responses)
