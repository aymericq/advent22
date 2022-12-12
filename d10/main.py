import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        ops = [line.strip() for line in fd.readlines()]
    
    X = 1
    sig_strengths = []
    op_list_empty = False
    cycle = 1
    i_op = 0
    add_cycle = 1
    crt_matrix = [['.' for _ in range(40)] for _ in range(6)]
    while not op_list_empty:
        if cycle%40 == 20:
            sig_strengths.append((cycle, X))
        if cycle // 40 == 6:
            break
        crt_matrix[cycle//40][cycle%40 - 1] = '#' if X - 1 <= (cycle%40 - 1) <= X + 1 else '.'
        op = ops[i_op]
        if op == "noop":
            i_op += 1
        elif op[:4] == "addx":
            if add_cycle == 1:
                add_cycle = 2
            else:
                X += int(op.split()[-1])
                add_cycle = 1
                i_op += 1
        print(cycle, X)
        cycle += 1
        if i_op == len(ops):
            op_list_empty = True
    print(sig_strengths)
    print("Sum of signal strenghts is:", sum(map(lambda x: x[0]*x[1], sig_strengths)))
    for row in crt_matrix:
        print("".join(row))
        



if __name__ == "__main__":
    main()