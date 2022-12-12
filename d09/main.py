import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        moves = [(e[0], int(e[1])) for e in [line.strip().split() for line in fd.readlines()]]

    n_knots = 10
    knots = [(0, 0) for _ in range(n_knots)]
    T_visited_positions = {(0,0)}
    for direction, n_moves in moves:
        for _ in range(n_moves):
            knots[0] = move_H(direction, knots[0])
            for i_knot in range(1, len(knots)):
                knots[i_knot] = move_T(knots[i_knot-1], knots[i_knot])
            T_visited_positions.add(knots[9])

    pretty_print_positions(knots, T_visited_positions)
    print("T visited", len(T_visited_positions), "positions")
    

def pretty_print_positions(knots, T_visited_positions):
    all_pos = knots.copy()
    all_pos.append((0, 0))
    all_pos.extend(T_visited_positions)
    min_x, max_x = min([knot[0] for knot in all_pos]), max([knot[0] for knot in all_pos])
    min_y, max_y = min([knot[1] for knot in all_pos]), max([knot[1] for knot in all_pos])
    pos_matrix = [['.']*(max_x - min_x + 1) for _ in range(min_y, max_y+1)]
    pos_matrix[-min_y][-min_x] = 's'
    for i_knot, knot in enumerate(knots):
        pos_matrix[knot[1]-min_y][knot[0]-min_x] = str(i_knot) if pos_matrix[knot[1]-min_y][knot[0]-min_x][0] == '.' else pos_matrix[knot[1]-min_y][knot[0]-min_x][0]
    for pos in T_visited_positions:
        pos_matrix[pos[1]-min_y][pos[0]-min_x] = '#' if pos_matrix[pos[1]-min_y][pos[0]-min_x][0] == '.' else pos_matrix[pos[1]-min_y][pos[0]-min_x][0]
    for i_row in range(len(pos_matrix)-1, -1, -1):
        print("".join(pos_matrix[i_row]))


def move_T(H, T):
    gap_x = T[0] - H[0]
    gap_y = T[1] - H[1]

    if abs(gap_x) >= 2:
        if abs(gap_y) == 1:
            return (T[0] - gap_x//2, T[1] - gap_y)
        elif abs(gap_y) == 2:
            return (T[0] - gap_x//2, T[1] - gap_y//2)
        else:
            return (T[0] - gap_x//2, T[1])
    elif abs(gap_y) >= 2:
        if abs(gap_x) == 1:
            return (T[0] - gap_x, T[1] - gap_y//2)
        elif abs(gap_x) == 2:
            return (T[0] - gap_x//2, T[1] - gap_y//2)
        else:
            return (T[0], T[1] - gap_y//2)
    else:
        return T


def move_H(direction, H):
    if direction == 'U':
        return (H[0], H[1]+1)
    elif direction == 'D':
        return (H[0], H[1]-1)
    elif direction == 'L':
        return (H[0]-1, H[1])
    elif direction == 'R':
        return (H[0]+1, H[1])


if __name__ == "__main__":
    main()