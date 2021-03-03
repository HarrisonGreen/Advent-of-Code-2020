def read_input(file_path):
    boarding_passes = []
    with open(file_path, "r") as boarding_pass_file:
        for line in boarding_pass_file:
            boarding_passes.append((line[0:7], line[7:10]))
    return boarding_passes

def process_boarding_passes(boarding_passes):
    min_id = 1000
    max_id = 0
    seat_ids = set()

    for boarding_pass in boarding_passes:
        seat_id = convert_to_num(boarding_pass)
        seat_ids.add(seat_id)

        if seat_id > max_id:
            max_id = seat_id
        if seat_id < min_id:
            min_id = seat_id

    print(f"Part one: {max_id}")

    for seat in range(min_id, max_id):
        if seat not in seat_ids:
            print(f"Part two: {seat}")

def convert_to_num(boarding_pass):
    row = boarding_pass[0].replace("F", "0").replace("B", "1")
    column = boarding_pass[1].replace("L", "0").replace("R", "1")

    row = int(row, base = 2)
    column = int(column, base = 2)
    return 8 * row + column

if __name__ == "__main__":
    file_path = "Data/day5_input.txt"
    boarding_passes = read_input(file_path)
    process_boarding_passes(boarding_passes)
