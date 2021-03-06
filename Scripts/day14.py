from collections import Counter

def read_input(file_path):
    instructions = []
    with open(file_path, "r") as initialization_file:
        for line in initialization_file:
            line  = line.split("=")
            if line[0] == "mask ":
                line = [0,0,line[-1].strip("\n")[1:]]
            else:
                line = [1,int(line[0][4:-2]),int(line[-1].strip("\n"))]
            instructions.append(line)

    return instructions

def convert_to_binary(num, length):
    num_string = bin(num)[2:]
    output_string = ""
    for _ in range(length - len(num_string)):
        output_string += "0"
    return output_string + num_string

def bitmask_value_program(instructions):
    memory = {}

    for instruction in instructions:
        if instruction[0] == 0:
            mask = {}

            for i in range(36):
                if instruction[2][i] == "X":
                   continue
                mask[i] = instruction[2][i]

        else:
            num_string = convert_to_binary(instruction[2], 36)
            masked_string = ""
            for i in range(36):
                if i in mask.keys():
                    masked_string += mask[i]
                else:
                    masked_string += num_string[i]

            num = int(masked_string, base=2)
            memory[instruction[1]] = num

    print(f"Part one: {sum(memory.values())}")

def bitmask_address_program(instructions):
    memory = {}

    for instruction in instructions:
        if instruction[0] == 0:
            mask = instruction[2]

        else:
            address_string = convert_to_binary(instruction[1], 36)
            masked_string = ""
            for i in range(36):
                if mask[i] == "1":
                    masked_string += "1"
                elif mask[i] == "X":
                    masked_string += "X"
                else:
                    masked_string += address_string[i]

            memory = write_to_memory(masked_string, instruction[2], memory)

    print(f"Part two: {sum(memory.values())}")

def write_to_memory(address_string, value, memory):
    x_count = Counter(address_string)["X"]
    possibilities = 2**x_count

    for i in range(possibilities):
        sub_values = convert_to_binary(i, x_count)
        new_string = ""
        sub_position = 0

        for j in range(36):
            if address_string[j] == "X":
                new_string += sub_values[sub_position]
                sub_position += 1

            else:
                new_string += address_string[j]

        address = int(new_string, base=2)
        memory[address] = value

    return memory

if __name__ == "__main__":
    file_path = "Data/day14_input.txt"
    instructions = read_input(file_path)
    bitmask_value_program(instructions)
    bitmask_address_program(instructions)
