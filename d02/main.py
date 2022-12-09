import pathlib

def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        rounds = [line.strip().split() for line in fd.readlines()]

    part1(rounds)
    part2(rounds)

def part1(rounds):
    score = 0
    for move_A, move_B in rounds:
        if move_B == 'X':
            score+=1
            if move_A == "A":
                score += 3
            elif move_A == "B":
                score += 0
            elif move_A == "C":
                score += 6
        elif move_B == 'Y':
            score += 2
            if move_A == "A":
                score += 6
            elif move_A == "B":
                score += 3
            elif move_A == "C":
                score += 0
        elif move_B == 'Z':
            score += 3
            if move_A == "A":
                score += 0
            elif move_A == "B":
                score += 6
            elif move_A == "C":
                score += 3

    print("Total score is:", score)


def part2(rounds):
    score = 0
    for move_A, move_B in rounds:
        if move_B == 'X':
            if move_A == "A":
                score += 3
            elif move_A == "B":
                score += 1
            elif move_A == "C":
                score += 2
        elif move_B == 'Y':
            score += 3
            if move_A == "A":
                score += 1
            elif move_A == "B":
                score += 2
            elif move_A == "C":
                score += 3
        elif move_B == 'Z':
            score += 6
            if move_A == "A":
                score += 2
            elif move_A == "B":
                score += 3
            elif move_A == "C":
                score += 1

    print("Total score is:", score)

if __name__ == "__main__":
    main()