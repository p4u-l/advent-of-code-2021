from collections import defaultdict, deque


def solve(graph: dict, start_vertex: str, visit_twice: bool) -> int:
    path_count = 0

    # Starting DFS with start_vertex, empty path travelled so far
    # and with nothing twice visited
    stack = deque([(start_vertex, [], False)])

    while stack:
        vertex, path, visited_twice = stack.pop()
        path.append(vertex)

        if vertex == "end":
            path_count += 1
            
        for next_vertex in graph[vertex]:
            visited_twice_new = visited_twice
            if next_vertex.islower() and next_vertex in path:
                if not visit_twice or visited_twice:
                    continue
                visited_twice_new = True
            stack.append((next_vertex, path[:], visited_twice_new))

    return path_count


def main():
    with open("day12/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read().splitlines()
    
    # Representation of graph by dictionary.
    # All vertices are double linked, except for start and end vertex.
    graph = defaultdict(set)

    for line in puzzle_input:
        edge_from, edge_to = line.split("-")
        if edge_from != "end" and edge_to != "start":
            graph[edge_from].add(edge_to)
        if edge_to != "end" and edge_from != "start":
            graph[edge_to].add(edge_from)

    print("Part 1:", solve(graph, "start", visit_twice=False))
    print("Part 2:", solve(graph, "start", visit_twice=True))


if __name__ == "__main__":
    main()
