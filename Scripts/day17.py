def read_initial_state(file_path):
    starting_cubes = []
    with open(file_path, "r") as initial_state_file:
        row = 0
        for line in initial_state_file:
            column = 0
            for char in line:
                if char == "#":
                    starting_cubes.append((row,column,0,0))
                column += 1
            row += 1

    return starting_cubes

def run_cycles_3_dimensions(active_cubes):
    for _ in range(6):
        active_neighbours = {}

        for cube in active_cubes:
            for x in range(cube[0] - 1,cube[0] + 2):
                for y in range(cube[1] - 1,cube[1] + 2):
                    for z in range(cube[2] - 1,cube[2] + 2):
                            active_neighbours[(x,y,z,0)] = active_neighbours.get((x,y,z,0), 0) + 1
            active_neighbours[cube] -= 1

        new_active_cubes = []
        for item in active_neighbours.items():
            if item[1] == 3:
                new_active_cubes.append(item[0])
            elif item[1] == 2 and item[0] in active_cubes:
                    new_active_cubes.append(item[0])

        active_cubes = new_active_cubes

    print(f"Part one: {len(active_cubes)}")

def run_cycles_4_dimensions(active_cubes):
    for _ in range(6):
        active_neighbours = {}

        for cube in active_cubes:
            for x in range(cube[0] - 1,cube[0] + 2):
                for y in range(cube[1] - 1,cube[1] + 2):
                    for z in range(cube[2] - 1,cube[2] + 2):
                        for w in range(cube[3] - 1,cube[3] + 2):
                            active_neighbours[(x,y,z,w)] = active_neighbours.get((x,y,z,w), 0) + 1
            active_neighbours[cube] -= 1

        new_active_cubes = []
        for item in active_neighbours.items():
            if item[1] == 3:
                new_active_cubes.append(item[0])
            elif item[1] == 2 and item[0] in active_cubes:
                    new_active_cubes.append(item[0])

        active_cubes = new_active_cubes

    print(f"Part two: {len(active_cubes)}")

if __name__ == "__main__":
    file_path = "Data/day17_input.txt"
    starting_cubes = read_initial_state(file_path)
    run_cycles_3_dimensions(starting_cubes)
    run_cycles_4_dimensions(starting_cubes)
