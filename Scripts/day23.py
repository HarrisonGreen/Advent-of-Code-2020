def index_cups(cups, num_cups):
    cup_to_right = {}

    for i in range(8):
        cup_to_right[cups[i]] = cups[i + 1]
    if num_cups == 9:
        cup_to_right[cups[-1]] = cups[0]
    else:
        cup_to_right[cups[-1]] = 10
        for i in range(10, num_cups):
            cup_to_right[i] = i + 1
        cup_to_right[num_cups] = cups[0]

    return cup_to_right

def run_game(cups, num_cups, cup_to_right, num_steps):
    current_cup = cups[0]
    
    for _ in range(num_steps):
        cup_one = cup_to_right[current_cup]
        cup_two = cup_to_right[cup_one]
        cup_three = cup_to_right[cup_two]

        cup_to_right[current_cup] = cup_to_right[cup_three]

        destination_cup = current_cup - 1
        while destination_cup == cup_one or destination_cup == cup_two or destination_cup == cup_three:
            destination_cup -= 1
        if destination_cup == 0:
            destination_cup = num_cups
            while destination_cup == cup_one or destination_cup == cup_two or destination_cup == cup_three:
                destination_cup -= 1

        cup_to_right[cup_three] = cup_to_right[destination_cup]
        cup_to_right[destination_cup] = cup_one

        current_cup = cup_to_right[current_cup]

    return cup_to_right

def create_cup_list(cup_to_right):
    current_cup, num = 1, 0
    for i in range(8):
        current_cup = cup_to_right[current_cup]
        num += current_cup * 10**(7 - i)
    print(f"Part one: {num}")

if __name__ == "__main__":
    cups = [1,3,7,8,2,6,4,9,5]
    cup_to_right = index_cups(cups, 9)
    cup_to_right = run_game(cups, 9, cup_to_right, 100)
    create_cup_list(cup_to_right)

    cup_to_right = index_cups(cups, 1000000)
    cup_to_right = run_game(cups, 1000000, cup_to_right, 10000000)
    print(f"Part two: {cup_to_right[1] * cup_to_right[cup_to_right[1]]}")
