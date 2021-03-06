def find_number(target):
    numbers = [0,12,6,13,20,1,17]
    last_position = {numbers[i]: i for i in range(len(numbers) - 1)}
    current_num = numbers[-1]

    for current_pos in range(len(numbers) - 1, target - 1):
        next_num = current_pos - last_position.get(current_num, current_pos)
        last_position[current_num] = current_pos
        current_num = next_num

    return current_num

if __name__ == "__main__":
    print(f"Part one: {find_number(2020)}")
    print(f"Part two: {find_number(30000000)}")
