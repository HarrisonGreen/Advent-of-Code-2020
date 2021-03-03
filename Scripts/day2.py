from collections import Counter

def read_input(file_path):
    passwords = []
    with open(file_path, "r") as password_file:
        for line in password_file:
            line = line.split()
            line[0] = line[0].split("-")
            line[0][0] = int(line[0][0])
            line[0][1] = int(line[0][1])
            line[1] = line[1].strip(":")
            passwords.append(line)
    return passwords

def count_valid_passwords(passwords):
    valid = [0, 0]
    for password in passwords:
        valid = check_password(password, valid)
    print(f"Part one: {valid[0]}\nPart two: {valid[1]}")

def check_password(item, valid):
    policy = item[0:2]
    password = item[2]

    if policy[0][0] <= Counter(password)[policy[1]] <= policy[0][1]:
        valid[0] += 1

    if (password[policy[0][0] - 1] == policy[1]) ^ (password[policy[0][1] - 1] == policy[1]):
        valid[1] += 1

    return valid
    
if __name__ == "__main__":
    file_path = "Data/day2_input.txt"
    passwords = read_input(file_path)
    count_valid_passwords(passwords)
