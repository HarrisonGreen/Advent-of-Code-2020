def read_fields(fields_file_path):
    fields = {}
    with open(fields_file_path, "r") as fields_file:
        for line in fields_file:
            line = line.split(":")
            line[1] = line[1].split()
            line[1] = [line[1][0].split("-"),line[1][2].split("-")]
            fields[line[0]] = [(int(line[1][0][0]),int(line[1][0][1])), (int(line[1][1][0]),int(line[1][1][1]))]
            
    return fields

def read_tickets(tickets_file_path):
    tickets = []
    with open(tickets_file_path, "r") as tickets_file:
        for line in tickets_file:
            line = line.strip("\n")
            line = line.split(",")
            for i in range(len(line)):
                line[i] = int(line[i])
            tickets.append(line)

    return tickets

def check_valid_tickets(tickets, fields):
    to_remove = []
    error_rate = 0

    for ticket in tickets:
        for value in ticket:
            invalid, value = check_number(value, fields)
            if invalid:
                error_rate += value
                to_remove.append(ticket)
                break

    print(f"Part one: {error_rate}")

    for ticket in to_remove:
        tickets.remove(ticket)
    return tickets

def check_number(value, fields):
    for item in fields.values():
        for valid_range in item:
            if valid_range[0] <= value <= valid_range[1]:
                return False, 0
    return True, value

def determine_field_order(tickets, fields):
    possible_fields = {i:[] for i in range(len(tickets[0]))}
    for position in possible_fields.keys():
        for field in fields.keys():
            possible_fields[position].append(field)

    for ticket in tickets:
        for position in possible_fields.keys():
            value = ticket[position]
            for field in possible_fields[position]:
                discard = True
                for valid_range in fields[field]:
                    if valid_range[0] <= value <= valid_range[1]:
                        discard = False
                if discard:
                    possible_fields[position].remove(field)

    change = True
    while change:
        change = False
        for position in possible_fields.keys():
            if len(possible_fields[position]) == 1:
                field = possible_fields[position][0]
                for i in range(position):
                    try:
                        possible_fields[i].remove(field)
                        change = 1
                    except:
                        pass
                for i in range(position+1,len(tickets[0])):
                    try:
                        possible_fields[i].remove(field)
                        change = 1
                    except:
                        pass

    departure_product = 1
    for position in possible_fields.keys():
        if "departure" in possible_fields[position][0]:
            departure_product *= tickets[0][position]
    print(f"Part two: {departure_product}")

if __name__ == "__main__":
    fields_file_path = "Data/day16_fields.txt"
    tickets_file_path = "Data/day16_tickets.txt"
    fields = read_fields(fields_file_path)
    tickets = read_tickets(tickets_file_path)
    tickets = check_valid_tickets(tickets, fields)
    determine_field_order(tickets, fields)
