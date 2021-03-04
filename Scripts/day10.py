from collections import Counter

def read_input(file_path):
    adaptors = [0]
    with open(file_path, "r") as adaptors_file:
        for line in adaptors_file:
            adaptors.append(int(line))
    adaptors = sorted(adaptors)
    adaptors.append(adaptors[-1]+3)
    return adaptors

def count_differences(adaptors):
    diffs = [adaptors[i] - adaptors[i-1] for i in range(1, len(adaptors))]
    diff_counter = Counter(diffs)
    print(f"Part one: {diff_counter[1] * diff_counter[3]}")
    return diffs

def count_arrangements(diffs):
    possibilities = 1
    three_locations = [-1]
    for i in range(len(diffs)):
        if diffs[i] == 3:
            three_locations.append(i)

    for i in range(1,len(three_locations)):
        gap = three_locations[i] - three_locations[i-1] - 1
        if gap == 2:
            possibilities *= 2
        elif gap == 3:
            possibilities *= 4
        elif gap == 4:
            possibilities *= 7
            
    print(f"Part two: {possibilities}")

if __name__ == "__main__":
    file_path = "Data/day10_input.txt"
    adaptors = read_input(file_path)
    diffs = count_differences(adaptors)
    count_arrangements(diffs)
