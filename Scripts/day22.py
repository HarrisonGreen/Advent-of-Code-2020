def read_decks(file_path):
    cards = []
    with open(file_path, "r") as decks_file:
        for line in decks_file:
            line = line.strip("\n")
            if 1 <= len(line) <= 2:
                cards.append(int(line))

    length = len(cards)
    return cards[:length//2], cards[length//2:]

def play_game(first_deck, second_deck):
    while first_deck and second_deck:
        first_deck, second_deck = play_round(first_deck, second_deck)

    return first_deck, second_deck

def play_round(first_deck, second_deck):
    if first_deck[0] > second_deck[0]:
        first_deck = first_deck[1:] + [first_deck[0], second_deck[0]]
        second_deck = second_deck[1:]
    else:
        second_deck = second_deck[1:] + [second_deck[0], first_deck[0]]
        first_deck = first_deck[1:]

    return first_deck, second_deck

def play_recursive_game(first_deck, second_deck):
    positions = set()

    while first_deck and second_deck:
        current_position = (tuple(first_deck), tuple(second_deck))
        if current_position in positions:
            return 1, first_deck, second_deck
        positions.add(current_position)

        p_1, p_2 = first_deck[0], second_deck[0]
        if len(first_deck) >= p_1 + 1 and len(second_deck) >= p_2 + 1:
            sub_game_result = play_recursive_game(first_deck[1: p_1 + 1],second_deck[1: p_2 + 1])
            first_deck, second_deck = move_cards(first_deck, second_deck, sub_game_result[0])
        else:
            first_deck, second_deck = play_round(first_deck, second_deck)

    if len(first_deck) > 0:
        return 1, first_deck, second_deck
    else:
        return 2, first_deck, second_deck

def move_cards(first_deck, second_deck, winner):
    if winner == 1:
        first_deck = first_deck[1:] + [first_deck[0], second_deck[0]]
        second_deck = second_deck[1:]
    else:
        second_deck = second_deck[1:] + [second_deck[0], first_deck[0]]
        first_deck = first_deck[1:]

    return first_deck, second_deck

def calculate_score(first_deck, second_deck):
    if first_deck:
        first_deck.reverse()
        return sum((i+1) * card for i, card in enumerate(first_deck))
    second_deck.reverse()
    return sum((i+1) * card for i, card in enumerate(second_deck))

if __name__ == "__main__":
    file_path = "Data/day22_input.txt"
    first_deck, second_deck = read_decks(file_path)
    first_deck, second_deck = play_game(first_deck, second_deck)
    print(f"Part one: {calculate_score(first_deck, second_deck)}")
    
    first_deck, second_deck = read_decks(file_path)
    recursive_result = play_recursive_game(first_deck, second_deck)
    print(f"Part two: {calculate_score(recursive_result[1], recursive_result[2])}")
