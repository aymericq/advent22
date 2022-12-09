import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        lines = [line.strip() for line in fd.readlines()]

    deer_amounts = []
    deer_amount = 0
    for line in lines:
        if len(line) == 0:
            deer_amounts.append(deer_amount)
            deer_amount = 0
        else:
            deer_amount += int(line)
    sorted_deer_amounts = sorted(deer_amounts)
    print("Deer with max amount of calories has:", sorted_deer_amounts[-1])
    print("Top 3 deers have total calories:", sum(sorted(deer_amounts)[-3:]))


if __name__ == "__main__":
    main()
