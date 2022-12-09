import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        lines = [line.rstrip() for line in fd.readlines()]
    for i_line, line in enumerate(lines):
        if line[-1] in "123456789":
            max_height = i_line
            n_crate_tower = int(line.split()[-1])
            break
    print("Max height is", max_height)
    print("N towers is", n_crate_tower)

    crate_stacks = parse_stacks(lines, max_height, n_crate_tower)
    actions = parse_actions(lines, max_height)

    # stacks = move_stacks_9000(crate_stacks, actions)
    stacks = move_stacks_9001(crate_stacks, actions)

    result = []
    for stack in stacks:
        result.append(stacks[stack].pop())
    print("Top of stacks are:", "".join(result))


def move_stacks_9001(stacks, actions):
    for action in actions:
        n_moves, from_stack, to_stack = action
        stacks[to_stack].extend(stacks[from_stack][-n_moves:])
        for _ in range(n_moves):
            stacks[from_stack].pop()

    return stacks


def move_stacks_9000(stacks, actions):
    for action in actions:
        n_moves, from_stack, to_stack = action
        for _ in range(n_moves):
            e = stacks[from_stack].pop()
            stacks[to_stack].append(e)
    return stacks


def parse_actions(lines, max_height):
    actions = []
    for i_line in range(max_height + 2, len(lines)):
        line = lines[i_line].split()
        action = int(line[1]), int(line[3]), int(line[5])  # (n_moves, from, to)
        actions.append(action)
    return actions


def parse_stacks(lines, max_height, n_crate_tower):
    crate_stacks = {i_tower + 1: [] for i_tower in range(n_crate_tower)}
    for i_line in range(max_height - 1, -1, -1):
        for i_tower in range(n_crate_tower):
            line = lines[i_line]
            if 1 + 4 * i_tower < len(line) and str.isalpha(line[1 + 4 * i_tower]):
                crate_stacks[i_tower + 1].append(line[1 + 4 * i_tower])
    return crate_stacks


if __name__ == "__main__":
    main()
