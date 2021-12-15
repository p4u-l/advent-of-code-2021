from heapq import heappop, heappush
import math


class CaveMap:
    def __init__(self, cave_map_arr):
        self.cave_arr = cave_map_arr
        self.max_y = len(self.cave_arr) - 1
        self.max_x = len(self.cave_arr[0]) - 1

    def __getitem__(self, coords):
        x, y = coords
        return self.cave_arr[y][x]

    def __iter__(self):
        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                yield (x, y)

    def max_coords(self):
        return (self.max_x, self.max_y)

    def adj_coords(self, coords):
        x, y = coords
        if x > 0:
            yield (x - 1, y)
        if x < self.max_x:
            yield (x + 1, y)
        if y > 0:
            yield (x, y - 1)
        if y < self.max_y:
            yield (x, y + 1)

    def dijkstra(self, start, end):
        # Dijkstra algorithm using a heap queue that returns the
        # smallest distance between the start and end points.
        distances = {coord: math.inf for coord in self}
        distances[start] = 0
        heapqueue = [(distances[start], start)]

        while heapqueue:
            distance_u, u = heappop(heapqueue)
            if u == end:
                return distance_u

            for adj in self.adj_coords(u):
                alt = distance_u + self[adj]
                if alt < distances[adj]:
                    distances[adj] = alt
                    heappush(heapqueue, (alt, adj))
        
        return -1


def expand_2d_arr(arr, n=5):
    expanded = []
    for y in range(n):
        for row in arr:
            new_row = []
            for x in range(n):
                row_seg = map(lambda a: (a-1+x+y)%9+1, row)
                new_row += row_seg
            expanded.append(new_row)
    return expanded


def solve():
    with open("day15/input.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read().splitlines()
    cavemap_arr = [[int(n) for n in line] for line in puzzle_input]

    cavemap1 = CaveMap(cavemap_arr)
    print("Part 1:", cavemap1.dijkstra((0, 0), cavemap1.max_coords()))

    cavemap_arr_expanded = expand_2d_arr(cavemap_arr)
    cavemap2 = CaveMap(cavemap_arr_expanded)
    print("Part 2:", cavemap2.dijkstra((0, 0), cavemap2.max_coords()))


if __name__ == "__main__":
    solve()
