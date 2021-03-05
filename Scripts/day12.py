def read_instructions(file_path):
    instructions = []
    with open(file_path, "r") as instructions_file:
        for line in instructions_file:
            line = line.strip("\n")
            instructions.append([line[0],int(line[1:])])

    return instructions

def calculate_location(instructions):
    position = [0,0]
    direction = 0

    for instruction in instructions:
        if instruction[0] == "E":
            position[0] += instruction[1]
        elif instruction[0] == "N":
            position[1] += instruction[1]
        elif instruction[0] == "W":
            position[0] -= instruction[1]
        elif instruction[0] == "S":
            position[1] -= instruction[1]
        elif instruction[0] == "L":
            direction += instruction[1]//90
            direction %= 4
        elif instruction[0] == "R":
            direction -= instruction[1]//90
            direction %= 4

        elif instruction[0] == "F":
            if direction == 0:
                position[0] += instruction[1]
            elif direction == 1:
                position[1] += instruction[1]
            elif direction == 2:
                position[0] -= instruction[1]
            elif direction == 3:
                position[1] -= instruction[1]

    print(f"Part one: {abs(position[0]) + abs(position[1])}")

def calculate_location_waypoint(instructions):
    position = [0,0]
    waypoint = [10,1]

    for instruction in instructions:
        if instruction[0] == "E":
            waypoint[0] += instruction[1]
        elif instruction[0] == "N":
            waypoint[1] += instruction[1]
        elif instruction[0] == "W":
            waypoint[0] -= instruction[1]
        elif instruction[0] == "S":
            waypoint[1] -= instruction[1]
            
        elif instruction[0] == "L":
            for _ in range(instruction[1]//90):
                waypoint = [-waypoint[1],waypoint[0]]

        elif instruction[0] == "R":
            for _ in range(instruction[1]//90):
                waypoint = [waypoint[1],-waypoint[0]]

        elif instruction[0] == "F":
            position[0] += instruction[1]*waypoint[0]
            position[1] += instruction[1]*waypoint[1]

    print(f"Part two: {abs(position[0]) + abs(position[1])}")

if __name__ == "__main__":
    file_path = "Data/day12_input.txt"
    instructions = read_instructions(file_path)
    calculate_location(instructions)
    calculate_location_waypoint(instructions)
