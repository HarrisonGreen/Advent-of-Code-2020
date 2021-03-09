def public_values():
    public_keys = (18356117, 5909654)
    mod = 20201227
    return public_keys, mod

def find_private_key(public_keys, mod):
    value = 1
    loops = 0

    while True:
        value = (7 * value) % mod
        loops += 1

        if value == public_keys[0]:
            return 0, loops
        if value == public_keys[1]:
            return 1, loops

def calculate_encryption_key(public_keys, mod, found, private_key):
    if found == 0:
        multiplier = public_keys[1]
    else:
        multiplier = public_keys[0]

    value = 1
    for _ in range(private_key):
        value = (multiplier * value) % mod
    
    print(f"Part one: {value}")

if __name__ == "__main__":
    public_keys, mod = public_values()
    found, private_key = find_private_key(public_keys, mod)
    calculate_encryption_key(public_keys, mod, found, private_key)
