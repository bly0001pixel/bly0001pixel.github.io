from chords import chords

def format_word_with_letters(word, letters):
    sorted_letters = tuple(sorted(letters))
    output = f"{sorted_letters}:'{word}',"
    return output

def find_duplicate_values(dictionary):
    value_count = {}
    
    for key, value in dictionary.items():
        if value in value_count:
            value_count[value].append(key)
        else:
            value_count[value] = [key]
    duplicates_found = False
    for value, keys in value_count.items():
        if len(keys) > 1:
            duplicates_found = True
            print(f"Value: {value} has {len(keys)} occurrences, Keys: {keys}")
    
    if not duplicates_found:
        print("No duplicate values found.")

copy = ""

choice = input("1.File 2.Input 3.Duplicates: ")

if choice == "1":
    with open('Raw Chords.txt', 'r') as file:
        for line in file:
            key = line.strip()
            letters = input(f"Chord for {key}: ")
            result = format_word_with_letters(key, letters)
            copy += result
            copy += "\n"
    print(copy)

if choice == "2":
    word = input('Word: ')
    letters = input(f"Chord for {word}: ")
    result = format_word_with_letters(word, letters)
    print(result)

if choice == "3":
    find_duplicate_values(chords)