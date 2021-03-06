from collections import Counter

def read_homework(file_path):
    homework_questions = []
    with open(file_path, "r") as homework_file:
        for line in homework_file:
            line = line.strip("\n")
            homework_questions.append(line)

    return homework_questions

def evaluate_homework(homework_questions, mode):
    total = 0
    for question in homework_questions:
        solution = evaluate_expression(question, mode)
        total += int(solution)

    if mode == "left_to_right":
        print(f"Part one: {total}")
    else:
        print(f"Part two: {total}")

def evaluate_expression(question, mode):
    question = remove_brackets(question, mode)
    if mode == "left_to_right":
        solution = left_to_right_evaluate(question)
    else:
        solution = add_first_evaluate(question)
    return solution

def remove_brackets(question, mode):
    while ")" in question:
        for i in range(len(question)):
            if question[i] == ")":
                close_location = i
                break

        for i in range(close_location):
            if question[i] == "(":
                open_location = i

        bracket_interior = question[open_location + 1: close_location]
        if mode == "left_to_right":
            replacement = left_to_right_evaluate(bracket_interior)
        else:
            replacement = add_first_evaluate(bracket_interior)
        question = question[:open_location] + replacement + question[close_location + 1:]

    return question

def left_to_right_evaluate(string):
    while "+" in string and "*" in string:
        if Counter(string)[" "] < 3:
            return str(eval(string))

        space_count = 0
        for i in range(len(string)):
            if string[i] == " ":
                space_count += 1
                if space_count == 3:
                    break

        first_operation = string[:i]
        new_string = str(eval(first_operation)) + string[i:]
        string = new_string

    return str(eval(string))

def add_first_evaluate(string):
    while "+" in string and "*" in string:
        for i in range(len(string)):
            if string[i] == "*":
                break
        string = add_first_evaluate(string[:i - 1]) + " * " + add_first_evaluate(string[i + 2:])
    return str(eval(string))

if __name__ == "__main__":
    file_path = "Data/day18_input.txt"
    homework_questions = read_homework(file_path)
    evaluate_homework(homework_questions, "left_to_right")
    evaluate_homework(homework_questions, "add_first")
