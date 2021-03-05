def read_input(file_path):
    seats = []

    with open(file_path, "r") as seating_file:
        row = -1
        for line in seating_file:
            row += 1
            column = -1
            for space in line:
                column += 1
                if space == "L":
                    seats.append((row,column))

    return seats

def get_dimensions(seats):
    row_max = 0
    column_max = 0

    for seat in seats:
        if seat[0] > row_max:
            row_max = seat[0]
        if seat[1] > column_max:
            column_max = seat[1]

    return (row_max + 1, column_max + 1)

def find_adjacent_neighbours(seats):
    neighbours = {}

    for seat in seats:
        neighbours[seat] = []
        adjacent = [(seat[0]+1,seat[1]),(seat[0]-1,seat[1]),(seat[0],seat[1]+1),(seat[0],seat[1]-1),
        (seat[0]+1,seat[1]+1),(seat[0]+1,seat[1]-1),(seat[0]-1,seat[1]+1),(seat[0]-1,seat[1]-1)]
        for position in adjacent:
            if position in seats:
                neighbours[seat].append(position)

    return neighbours

def find_direction_neighbours(seats, dims):
    neighbours = {}

    for seat in seats:
        neighbours[seat] = []
        steps = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        for step in steps:
            position = (seat[0]+step[0],seat[1]+step[1])
            while 0 <= position[0] < dims[0] and 0 <= position[1] < dims[1]:
                if position in seats:
                    neighbours[seat].append(position)
                    break
                position = (position[0]+step[0],position[1]+step[1])

    return neighbours

def run_simulation(seats, neighbours, tolerance):
    occupied = {seat: 0 for seat in seats}
    num_occupied = -1

    while sum(occupied.values()) != num_occupied:
        num_occupied = sum(occupied.values())
        to_flip = []

        for seat in seats:
            neighbour_count = 0
            for neighbour in neighbours[seat]:
                neighbour_count += occupied[neighbour]

            if occupied[seat] == 0 and neighbour_count == 0:
                to_flip.append(seat)

            if occupied[seat] == 1 and neighbour_count >= tolerance:
                to_flip.append(seat)

        for seat in to_flip:
            occupied[seat] = 1 - occupied[seat]

    return occupied

if __name__ == "__main__":
    file_path = "Data/day11_input.txt"
    seats = read_input(file_path)
    dims = get_dimensions(seats)

    adj_neighbours = find_adjacent_neighbours(seats)
    dir_neighbours = find_direction_neighbours(seats, dims)

    occupied = run_simulation(seats, adj_neighbours, 4)
    print(f"Part one: {sum(occupied.values())}")
    occupied = run_simulation(seats, dir_neighbours, 5)
    print(f"Part one: {sum(occupied.values())}")
