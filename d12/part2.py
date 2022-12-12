import pathlib


def main():
    current_directory = str(pathlib.Path(__file__).parent.resolve())
    with open(current_directory + "/input", 'r') as fd:
        terrain = [[ord(char) for char in line.strip()] for line in fd.readlines()]

    start = None
    end = None
    for i_line, line in enumerate(terrain):
        for i_char, char in enumerate(line):
            if char == 83:  # 'S'
                start = (i_line, i_char)
            if char == 69:  #  'E'
                end = (i_line, i_char)
    
    print("Start:", start)
    print("End:", end)

    terrain[start[0]][start[1]] = 97
    terrain[end[0]][end[1]] = 122

    graph = {}
    for i_row, row in enumerate(terrain):
        for i_col, char in enumerate(row):
            neighbors = []
            if i_row > 0 and terrain[i_row-1][i_col] + 1 >= terrain[i_row][i_col]:
                neighbors.append((i_row-1, i_col))
            if i_row < len(terrain)-1 and terrain[i_row+1][i_col] + 1 >= terrain[i_row][i_col]:
                neighbors.append((i_row+1, i_col))
            if i_col > 0 and terrain[i_row][i_col-1] + 1 >= terrain[i_row][i_col]:
                neighbors.append((i_row, i_col-1))
            if i_col < len(row) - 1 and terrain[i_row][i_col+1] + 1 >= terrain[i_row][i_col]:
                neighbors.append((i_row, i_col+1))
            graph[(i_row, i_col)] = neighbors

    max_steps = len(terrain)*len(terrain[0])
    dists, prev = dijkstra(graph, end, max_steps)

    print(dists)

    min_steps = max_steps
    for vertex in dists:
        if terrain[vertex[0]][vertex[1]] == 97:
            if dists[vertex] < min_steps:
                min_steps = dists[vertex]
    print(min_steps)


def dijkstra(graph, start, max_dist):
    dist = {}
    prev = {}
    queue = []
    for vertex in graph:
        dist[vertex] = max_dist + 1
        prev[vertex] = None
        queue.append(vertex)
    dist[start] = 0

    while len(queue) > 0:
        vertex_with_min_dist = min(queue, key=lambda vertex: dist[vertex])
        del queue[queue.index(vertex_with_min_dist)]

        for neighbor in graph[vertex_with_min_dist]:
            if neighbor in queue:
                alt = dist[vertex_with_min_dist] + 1
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = vertex_with_min_dist
        
    return dist, prev



#  1  function Dijkstra(Graph, source):
#  2      
#  3      for each vertex v in Graph.Vertices:
#  4          dist[v] ← INFINITY
#  5          prev[v] ← UNDEFINED
#  6          add v to Q
#  7      dist[source] ← 0
#  8      
#  9      while Q is not empty:
# 10          u ← vertex in Q with min dist[u]
# 11          remove u from Q
# 12          
# 13          for each neighbor v of u still in Q:
# 14              alt ← dist[u] + Graph.Edges(u, v)
# 15              if alt < dist[v]:
# 16                  dist[v] ← alt
# 17                  prev[v] ← u
# 18
# 19      return dist[], prev[]


def pretty_print_terrain(terrain):
    for line in terrain:
        print(line)


if __name__ == "__main__":
    main()