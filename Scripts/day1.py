def read_input(file_path):
    numbers = []
    with open(file_path, "r") as data_file:
        for line in data_file:
            numbers.append(int(line))
    return numbers

def find_products(numbers):
    n = len(numbers)
    solutions_found = [False, False]

    for i in range(n-1):
        if all(solutions_found):
            break

        a = numbers[i]

        if not solutions_found[0]:
            b = 2020 - a
            if b in numbers:
                print(f"Part one: {a * b}")
                solutions_found[0] = True

        if not solutions_found[1]:
            for j in range(i+1,n-1):
                b = numbers[j]
                c = 2020 - a - b
                if c in numbers:
                    print(f"Part two: {a * b * c}")
                    solutions_found[1] = True
                    break

if __name__ == "__main__":
    file_path = "Data/day1_input.txt"
    numbers = read_input(file_path)
    find_products(numbers)
