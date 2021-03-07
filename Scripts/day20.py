import numpy as np

def read_tiles(file_path, dim):
    tiles = {}
    with open(file_path, "r") as tiles_file:
        for line in tiles_file:

            if "Tile" in line:
                index = int(line[5:9])
                tile = np.zeros([dim, dim])
                row = 0

            elif line == "\n":
                tiles[index] = tile

            else:
                for i, char in enumerate(line):
                    if char == "#":
                        tile[row][i] = 1
                row += 1

    tiles[index] = tile
    return tiles

def count_borders(tiles):
    border_counts = {}
    for tile in tiles.values():
        borders = [tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1]]
        reverse_borders = [np.flip(border) for border in borders]
        for border in borders + reverse_borders:
            border = tuple(border)
            border_counts[border] = border_counts.get(border, 0) + 1

    return border_counts

def find_corners(tiles, border_counts):
    corners_product = 1
    for index, tile in tiles.items():
        borders = [tile[0, :], tile[-1, :], tile[:, 0], tile[:, -1]]
        if sum(border_counts[tuple(border)] for border in borders) == 6:
            corners_product *= index
            corner = index

    print(f"Part one: {corners_product}")
    return corner

def orient_first_corner(tiles, border_counts, corner, dim):
    for _ in range(4):
        tile = tiles[corner]
        borders = [tile[0, :], tile[:, 0]]
        if sum(border_counts[tuple(border)] for border in borders) == 2:
            return tiles
        tiles = rotate_tile(corner, tiles, dim)

    tiles = flip_tile(corner, tiles, dim)
    return orient_first_corner(tiles, border_counts, corner, dim)

def find_layout(tiles, corner, dim):
    layout = np.zeros([12, 12])
    layout[0, 0] = corner
    oriented = [corner]
    not_oriented = [index for index in tiles.keys()]
    not_oriented.remove(corner)    

    for i in range(1,12):
        border_to_match = tuple(tiles[layout[0, i-1]][:, -1])
        index, tiles = find_tile_to_right(border_to_match, tiles, not_oriented)
        layout[0, i] = index
        oriented.append(index)
        not_oriented.remove(index)

    for i in range(1,12):
        for j in range(12):
            border_to_match = tuple(tiles[layout[i-1, j]][-1, :])
            index, tiles = find_tile_below(border_to_match, tiles, not_oriented)
            layout[i, j] = index
            oriented.append(index)
            not_oriented.remove(index)

    return layout, tiles

def rotate_tile(index, tiles, dim):
    old_tile = tiles[index]
    new_tile = np.zeros([dim, dim])
    for i in range(dim):
        new_tile[:, -(i+1)] = old_tile[i, :]
        tiles[index] = new_tile
    return tiles

def flip_tile(index, tiles, dim):
    old_tile = tiles[index]
    new_tile = np.zeros([dim, dim])
    for i in range(dim):
        new_tile[:, i] = old_tile[i, :]
        tiles[index] = new_tile
    return tiles

def find_tile_to_right(border_to_match, tiles, not_oriented):
    for index in not_oriented:
        for _ in range(4):
            left_border = tuple(tiles[index][:, 0])
            if left_border == border_to_match:
                return index, tiles
            tiles = rotate_tile(index, tiles, dim)

    for index in not_oriented:
        tiles = flip_tile(index, tiles, dim)

    return find_tile_to_right(border_to_match, tiles, not_oriented)

def find_tile_below(border_to_match, tiles, not_oriented):
    for index in not_oriented:
        for _ in range(4):
            top_border = tuple(tiles[index][0, :])
            if top_border == border_to_match:
                return index, tiles
            tiles = rotate_tile(index, tiles, dim)

    for index in not_oriented:
        tiles = flip_tile(index, tiles, dim)

    return find_tile_below(border_to_match, tiles, not_oriented)

def create_image(layout, tiles, dim):
    new_dim = dim - 2
    image = np.zeros([12 * new_dim, 12 * new_dim])
    for i in range(12):
        for j in range(12):
            image[i * new_dim: (i+1) * new_dim, j * new_dim: (j+1) * new_dim] = tiles[layout[i, j]][1: -1, 1: -1]
    return image

def monster_pattern():
    top_row    = "                  # "
    middle_row = "#    ##    ##    ###"
    bottom_row = " #  #  #  #  #  #   "

    monster = []
    for i, char in enumerate(top_row):
        if char == "#":
            monster.append((0, i))
    for i, char in enumerate(middle_row):
        if char == "#":
            monster.append((1, i))
    for i, char in enumerate(bottom_row):
        if char == "#":
            monster.append((2, i))

    return monster

def orient_and_search(image, monster):
    for _ in range(4):
        found = monster_search(image, monster)
        if found > 0:
            return found
        image = rotate_image(image)

    image = flip_image(image)
    return orient_and_search(image, monster)

def monster_search(image, monster):
    monsters_found = 0
    for i in range(94):
        for j in range(77):
            for square in monster:
                if image[i + square[0], j + square[1]] == 0:
                    break
                if square == monster[-1]:
                    monsters_found += 1
    return monsters_found

def rotate_image(image):
    new_image = np.zeros([96, 96])
    for i in range(96):
        new_image[:, -(i+1)] = image[i, :]
    return new_image

def flip_image(index):
    new_image = np.zeros([96, 96])
    for i in range(96):
        new_image[:, i] = image[i, :]
    return new_image

if __name__ == "__main__":
    file_path = "Data/day20_input.txt"
    dim = 10

    tiles = read_tiles(file_path, dim)
    border_counts = count_borders(tiles)
    corner = find_corners(tiles, border_counts)
    tiles = orient_first_corner(tiles, border_counts, corner, dim)

    layout, tiles = find_layout(tiles, corner, dim)
    image = create_image(layout, tiles, dim)
    monster = monster_pattern()
    print(f"Part two: {int(sum(sum(image)) - 15 * orient_and_search(image, monster))}")
