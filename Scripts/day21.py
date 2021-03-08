def read_ingredients(file_path):
    ingredients_allergens = []
    with open(file_path, "r") as ingredients_file:
        for line in ingredients_file:
            line = line.strip(")\n")
            line = line.split("(")
            line[1] = line[1][9:]
            line[1] = line[1].split(", ")
            line[0] = line[0].split()
            ingredients_allergens.append(line)

    return ingredients_allergens

def find_allergenic_ingredients(ingredients_allergens):
    all_ingredients = set()
    all_allergens = set()
    for item in ingredients_allergens:
        all_ingredients = all_ingredients.union(item[0])
        all_allergens = all_allergens.union(item[1])

    possibles = {allergen: all_ingredients for allergen in all_allergens}
    for ingredients, allergens in ingredients_allergens:
        for allergen in allergens:
            possibles[allergen] = possibles[allergen].intersection(ingredients)

    all_possibles = set()
    for allergen in all_allergens:
        all_possibles = all_possibles.union(possibles[allergen])
    impossible = all_ingredients.difference(all_possibles)

    impossible_count = 0
    for ingredients, allergens in ingredients_allergens:
        for ingredient in ingredients:
            if ingredient in impossible:
                impossible_count += 1
    print(f"Part one: {impossible_count}")

    change = True
    while change:
        change = False
        for allergen in all_allergens:
            if len(possibles[allergen]) == 1:
                for ingredient in possibles[allergen]:
                    pass
                for other_allergen in all_allergens:
                    if allergen != other_allergen and ingredient in possibles[other_allergen]:
                        possibles[other_allergen] = possibles[other_allergen].difference(possibles[allergen])
                        change = True
    
    final_list = [possibles[allergen] for allergen in sorted(possibles.keys())]
    final_string = str(final_list).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(
                   "'", "").replace(" ", "")
    print(f"Part two: {final_string}")

if __name__ == "__main__":
    file_path = "Data/day21_input.txt"
    ingredients_allergens = read_ingredients(file_path)
    find_allergenic_ingredients(ingredients_allergens)
