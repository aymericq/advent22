import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        map_trees = list(map(lambda row: [int(char) for char in row.strip()], fd.readlines()))
    
    size_x = len(map_trees[0])
    size_y = len(map_trees)
    
    map_visible_trees = compute_visibility_map_from_outside(map_trees)
    
    print("Visible trees:", sum([sum(map_visible_trees[i_col]) for i_col in range(size_y)]))

    best_scenic_score = compute_best_scenic_score(map_trees)

    print("Best scenic score :", best_scenic_score  )


def compute_scenic_score(map_trees, i_row, i_col):
    size_x = len(map_trees[0])
    size_y = len(map_trees)

    score = 1
    curr_height = map_trees[i_row][i_col]
    score_in_direction = 0
    for j_col in range(i_col+1, size_x):
        score_in_direction += 1
        if map_trees[i_row][j_col] >= curr_height:
            break
    score *= score_in_direction
    if i_row == 1 and i_col == 2:
        print(score)
    
    score_in_direction = 0
    for j_col in range(i_col-1, -1, -1):
        score_in_direction += 1
        if map_trees[i_row][j_col] >= curr_height:
            break
    score *= score_in_direction
    if i_row == 1 and i_col == 2:
        print(score)

    score_in_direction = 0
    for j_row in range(i_row+1, size_y):
        score_in_direction += 1
        if map_trees[j_row][i_col] >= curr_height:
            break
    score *= score_in_direction
    if i_row == 1 and i_col == 2:
        print(score)

    score_in_direction = 0
    for j_row in range(i_row-1, -1, -1):
        score_in_direction += 1
        if map_trees[j_row][i_col] >= curr_height:
            break
    score *= score_in_direction

    return score



def compute_best_scenic_score(map_trees):
    size_x = len(map_trees[0])
    size_y = len(map_trees)

    best_score = 0
    for i_row in range(size_y):
        for i_col in range(size_x):
            scenic_score = compute_scenic_score(map_trees, i_row, i_col)
            if scenic_score > best_score:
                best_score = scenic_score

    return best_score


def compute_visibility_map_from_outside(map_trees):
    size_x = len(map_trees[0])
    size_y = len(map_trees)
    
    map_visible_trees = [[0 for _ in range(size_x)] for _ in range(size_y)]
    for i_row in range(1, size_x-1):
        curr_height = map_trees[0][i_row]
        for i_col in range(1, size_y-1):
            if map_trees[i_col][i_row] > curr_height:
                curr_height = map_trees[i_col][i_row]
                map_visible_trees[i_col][i_row] = 1
        curr_height = map_trees[-1][i_row]
        for i_col in range(size_y-1, 0, -1):
            if map_trees[i_col][i_row] > curr_height:
                curr_height = map_trees[i_col][i_row]
                map_visible_trees[i_col][i_row] = 1
    for i_col in range(1, size_y-1):
        curr_height = curr_height = map_trees[i_col][0]
        for i_row in range(1, size_x-1):
            if map_trees[i_col][i_row] > curr_height:
                curr_height = map_trees[i_col][i_row]
                map_visible_trees[i_col][i_row] = 1
        curr_height = curr_height = map_trees[i_col][-1]
        for i_row in range(size_x-1, 0, -1):
            if map_trees[i_col][i_row] > curr_height:
                curr_height = map_trees[i_col][i_row]
                map_visible_trees[i_col][i_row] = 1
    
    for i_col in range(size_y):
        map_visible_trees[i_col][0] = 1
        map_visible_trees[i_col][-1] = 1
    for i_row in range(size_x):
        map_visible_trees[0][i_row] = 1
        map_visible_trees[-1][i_row] = 1
    
    return map_visible_trees


if __name__ == "__main__":
    main()
