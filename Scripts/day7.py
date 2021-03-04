def read_input(file_path):
    contains_dict = {}
    contained_in_dict = {}

    with open(file_path, "r") as regulations_file:
        for line in regulations_file:
            line = line.replace(" bag,", " bags,").replace(" bag.", " bags.")
            line = line.split("bags")
            line.remove(line[-1])
            line[0] = line[0][:-1]
            try:
                line[1] = (int(line[1][9]), line[1][11:-1])
                for i in range(2, len(line)):
                    line[i] = (int(line[i][2]), line[i][4:-1])
            except ValueError:
                line = [line[0]]

            contains_dict[line[0]] = contains_dict.get(line[0], [])
            contained_in_dict[line[0]] = contained_in_dict.get(line[0], [])

            for i in range(1,len(line)):
                contains_dict[line[i][1]] = contains_dict.get(line[i][1], [])
                contained_in_dict[line[i][1]] = contained_in_dict.get(line[i][1], [])
                contains_dict[line[0]].append(line[i])
                contained_in_dict[line[i][1]].append(line[0])

    return contains_dict, contained_in_dict

def count_containers(contained_in_dict, bag_colour):
    containers = set(contained_in_dict[bag_colour])
    old_size = 0

    while len(containers) > old_size:
        old_size = len(containers)
        for colour in containers:
            containers = containers.union(set(contained_in_dict[colour]))

    print(f"Part one: {old_size}")

def count_contained_bags(contains_dict, bag_colour):
    contained_bags = {colour: number for number, colour in contains_dict[bag_colour]}
    total_count = 0

    while contained_bags:
        new_bags = {}
        for colour, number in contained_bags.items():
            total_count += number
            for item in contains_dict[colour]:
                new_bags[item[1]] = new_bags.get(item[1], 0) + (item[0] * number)
        contained_bags = new_bags

    print(f"Part two: {total_count}")

if __name__ == "__main__":
    file_path = "Data/day7_input.txt"
    contains_dict, contained_in_dict = read_input(file_path)
    count_containers(contained_in_dict, "shiny gold")
    count_contained_bags(contains_dict, "shiny gold")
