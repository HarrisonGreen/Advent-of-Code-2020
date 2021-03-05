def read_input(file_path):
    with open(file_path, "r") as bus_file:
        i = 0
        for line in bus_file:
            if i == 0:
                departure_time = int(line)
            else:
                buses = line.split(",")
            i += 1

    new_buses = []
    for i in range(len(buses)):
        if buses[i] == "x":
            pass
        else:
            new_buses.append((int(buses[i]), i))

    return departure_time, new_buses

def find_next_bus(departure_time, buses):
    waiting_time = {}
    for bus in buses:
        waiting_time[bus[0]] = (bus[0] - (departure_time % bus[0])) % bus[0]
    
    min_wait = min (waiting_time.values())
    for bus in waiting_time.keys():
        if waiting_time[bus] == min_wait:
            print(f"Part one: {min_wait * bus}")

def find_timestamp(buses):
    congruences = []
    modulo_product = 1
    for mod, wait in buses:
        modulo_product *= mod
        congruences.append(((mod - wait) % mod, mod))

    timestamp  = 0
    for remainder, mod in congruences:
        step = modulo_product//mod
        component = 0
        while True:
            if component % mod == remainder:
                timestamp += component
                break
            component += step

    timestamp %= modulo_product
    print(f"Part two: {timestamp}")

if __name__ == "__main__":
    file_path = "Data/day13_input.txt"
    departure_time, buses = read_input(file_path)
    find_next_bus(departure_time, buses)
    find_timestamp(buses)
    