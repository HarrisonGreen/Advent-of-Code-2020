import numpy as np

def get_map_dimensions(file_path):
    with open(file_path, "r") as map_file:
        for row, line in enumerate(map_file):
            pass
        return row + 1, len(line)

def load_map(file_path, height, width):
    local_map = np.zeros([height, width], dtype = int)

    with open(file_path, "r") as map_file:
        for row, line in enumerate(map_file):
            for column, character in enumerate(line):
                if (character == "#"):
                    local_map[row][column] = 1
    return local_map

def count_trees(local_map, row_step, column_step, height, width):
    tree_count = 0
    column = 0
    row = 0

    while (row + row_step < height):
        row += row_step
        column += column_step
        column %= width
        tree_count += local_map[row][column]

    if column_step == 3:
        print(f"Part one: {tree_count}")
    return tree_count

if __name__ == "__main__":
    file_path = "Data/day3_input.txt"
    height, width = get_map_dimensions(file_path)
    local_map = load_map(file_path, height, width)

    paths = [(1,7), (1,5), (1,3), (1,1), (2,1)]
    tree_product = 1

    for path in paths:
        tree_product *= int(count_trees(local_map, path[0], path[1], height, width))

    print(f"Part two: {tree_product}")
