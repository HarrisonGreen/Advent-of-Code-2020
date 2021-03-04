def read_instructions(file_path):
    instructions = []
    with open(file_path, "r") as instructions_file:
        for line in instructions_file:
            line = line.split()
            line[1] = int(line[1])
            instructions.append(line)
    instructions.append(["end", 0])
    return instructions

def run_boot_code(instructions):
    accumulator = 0
    position = 0
    already_run = [0 for _ in range(len(instructions))]
    
    while already_run[position] == 0:
        instruction = instructions[position]
        already_run[position] = 1
        position, accumulator, terminate = run_instruction(instruction, position, accumulator)
        if terminate:
            break

    return accumulator, terminate

def run_instruction(instruction, position, accumulator):
    if instruction[0] == "nop":
        return position + 1, accumulator, False
    elif instruction[0] == "acc":
        return position + 1, accumulator + instruction[1], False
    elif instruction[0] == "jmp":
        return position + instruction[1], accumulator, False
    elif instruction[0] == "end":
        return position, accumulator, True

if __name__ == "__main__":
    file_path = "Data/day8_input.txt"
    instructions = read_instructions(file_path)

    value, termination = run_boot_code(instructions)
    print(f"Part one: {value}")

    for i in range(len(instructions)):
        if instructions[i][0] == "nop":
            instructions[i][0] = "jmp"
            value, termination = run_boot_code(instructions)
            instructions[i][0] = "nop"
        elif instructions[i][0] == "jmp":
            instructions[i][0] = "nop"
            value, termination = run_boot_code(instructions)
            instructions[i][0] = "jmp"

        if termination:
            print(f"Part two: {value}")
            break
