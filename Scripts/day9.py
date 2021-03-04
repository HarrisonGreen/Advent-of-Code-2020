def read_input(file_path):
    xmas_data = []
    with open(file_path, "r") as data_file:
        for line in data_file:
            xmas_data.append(int(line))
    return xmas_data

def find_first_number(xmas_data):
    preamble_length = 25
    for position in range(preamble_length, len(xmas_data)):
        if check_number(position, xmas_data, preamble_length):
            return xmas_data[position]

def check_number(position, xmas_data, preamble_length):
    target = xmas_data[position]

    for i in range(position - preamble_length, position - 1):
        for j in range(i + 1, position):
            if xmas_data[i] + xmas_data[j] == target:
                return False
    return True

def find_weakness(xmas_data, target):
    for i in range(len(xmas_data)):
        total = xmas_data[i]
        numbers = [total]
        position = i

        while total < target:
            position += 1
            total += xmas_data[position]
            numbers.append(xmas_data[position])
            
            if total == target:
                return max(numbers) + min(numbers)

if __name__ == "__main__":
    file_path = "Data/day9_input.txt"
    xmas_data = read_input(file_path)
    first_number = find_first_number(xmas_data)
    print(f"Part one: {first_number}")

    weakness = find_weakness(xmas_data, first_number)
    print(f"Part two: {weakness}")
