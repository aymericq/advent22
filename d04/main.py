import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        pairs = [line.strip().split(',') for line in fd.readlines()]
    pairs = list(map(lambda pair: ((int(pair[0].split('-')[0]), int(pair[0].split('-')[1])), (int(pair[1].split('-')[0]), int(pair[1].split('-')[1]))), pairs))
    n_fully_overlapping_pairs = find_number_of_fully_overlapping_pairs(pairs)
    print("There are", n_fully_overlapping_pairs, "fully overlapping pairs.")
    n_partially_overlapping_pairs = find_number_of_partially_overlapping_pairs(pairs)
    print("There are", n_partially_overlapping_pairs, "partially overlapping pairs.")
    print("There are", n_partially_overlapping_pairs + n_fully_overlapping_pairs, "overlapping pairs.")


def find_number_of_fully_overlapping_pairs(pairs):
    n_overlapping_pairs = 0
    for pair in pairs:
        (range_l_low, range_l_high), (range_r_low, range_r_high) = pair
        if (range_l_low <= range_r_low and range_r_high <= range_l_high) or (range_r_low <= range_l_low and range_l_high <= range_r_high):
            n_overlapping_pairs += 1
    return n_overlapping_pairs

def find_number_of_partially_overlapping_pairs(pairs):
    n_overlapping_pairs = 0
    for pair in pairs:
        (range_l_low, range_l_high), (range_r_low, range_r_high) = pair
        if range_l_low < range_r_low and (range_r_low <= range_l_high < range_r_high):
            n_overlapping_pairs += 1
        elif (range_r_low < range_l_low <= range_r_high) and range_r_high < range_l_high:
            n_overlapping_pairs += 1
    return n_overlapping_pairs

if __name__ == "__main__":
    main()