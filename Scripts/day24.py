def read_instructions(file_path):
    instructions = []
    with open(file_path, "r") as instructions_file:
        for line in instructions_file:
            line = line.strip("\n")
            instructions.append(line)

    return instructions

def flip_tiles(instructions):
    flipped = {}
    for instruction in instructions:
        position = tuple(find_tile(instruction))
        flipped[position] = 1 - flipped.get(position, 0)

    flipped_tiles = set()
    for tile in flipped.keys():
        if flipped[tile] == 1:
            flipped_tiles.add(tile)

    print(f"Part one: {len(flipped_tiles)}")
    return flipped_tiles

def find_tile(instruction):
    position = [0, 0]

    while len(instruction) >= 2:
        if instruction[:2] == "ne":
            position[0] += 1
            position[1] += 1
            instruction = instruction[2:]
        elif instruction[:2] == "se":
            position[0] += 1
            position[1] -= 1
            instruction = instruction[2:]
        elif instruction[:2] == "sw":
            position[0] -= 1
            position[1] -= 1
            instruction = instruction[2:]
        elif instruction[:2] == "nw":
            position[0] -= 1
            position[1] += 1
            instruction = instruction[2:]
        elif instruction[0] == "e":
            position[0] += 2
            instruction = instruction[1:]
        else:
            position[0] -= 2
            instruction = instruction[1:]

    if len(instruction) == 1:
        if instruction[0] == "e":
            position[0] += 2
            instruction = ""
        else:
            position[0] -= 2
            instruction = ""

    return position

def animate_tiles(flipped_tiles):
    time_steps = 100

    for _ in range(time_steps):
        flipped_neighbours = {}
        for tile in flipped_tiles:
            flipped_neighbours[(tile[0]+2, tile[1])] = flipped_neighbours.get((tile[0]+2, tile[1]),0) + 1
            flipped_neighbours[(tile[0]-2, tile[1])] = flipped_neighbours.get((tile[0]-2, tile[1]),0) + 1
            flipped_neighbours[(tile[0]+1, tile[1]+1)] = flipped_neighbours.get((tile[0]+1, tile[1]+1),0) + 1
            flipped_neighbours[(tile[0]+1, tile[1]-1)] = flipped_neighbours.get((tile[0]+1, tile[1]-1),0) + 1
            flipped_neighbours[(tile[0]-1, tile[1]+1)] = flipped_neighbours.get((tile[0]-1, tile[1]+1),0) + 1
            flipped_neighbours[(tile[0]-1, tile[1]-1)] = flipped_neighbours.get((tile[0]-1, tile[1]-1),0) + 1

        new_tiles = set()
        for tile in flipped_neighbours.keys():
            if flipped_neighbours[tile] == 2:
                new_tiles.add(tile)
            elif flipped_neighbours[tile] == 1 and tile in flipped_tiles:
                new_tiles.add(tile)

        flipped_tiles = new_tiles
    
    print(f"Part two: {len(flipped_tiles)}")

if __name__ == "__main__":
    file_path = "Data/day24_input.txt"
    instructions = read_instructions(file_path)
    flipped_tiles = flip_tiles(instructions)
    animate_tiles(flipped_tiles)
