import pathlib

def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        rucksacks = [line.strip() for line in fd.readlines()]
    
    sum_of_priorities = compute_priority_for_duplicates(rucksacks)
    print("Sum of priorities for part I is:", sum_of_priorities)
    sum_of_priorities = compute_priority_for_badges(rucksacks)
    print("Sum of priorities for part II is:", sum_of_priorities)


def compute_priority_for_duplicates(rucksacks):
    sum_priorities = 0
    priority_dict = load_priority_dict()
    for rucksack in rucksacks:
        set_letters_left = set(rucksack[:-len(rucksack)//2])
        set_letters_right = set(rucksack[-len(rucksack)//2:])
        letter = set_letters_left.intersection(set_letters_right).pop()
        sum_priorities += priority_dict[letter]
    return sum_priorities


def compute_priority_for_badges(rucksacks):
    priority_dict = load_priority_dict()
    sum_of_priorities = 0

    letter_set = set()
    for i_sack, rucksack in enumerate(rucksacks):
        if i_sack%3 == 0:
            letter_set = set(rucksack)
        else:
            letter_set = letter_set.intersection(rucksack)
        if i_sack%3 == 2:
            sum_of_priorities += priority_dict[letter_set.pop()]
    return sum_of_priorities



def load_priority_dict():
    priority_dict = {char: ord(char)-96 for char in "abcdefghijklmnopqrstuvwxyz"}
    priority_dict_uppercase = {char: ord(char)-64+26 for char in str.upper("abcdefghijklmnopqrstuvwxyz")}
    priority_dict.update(priority_dict_uppercase)
    return priority_dict


if __name__ == "__main__":
    main()