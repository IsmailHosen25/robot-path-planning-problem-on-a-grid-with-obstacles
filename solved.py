import heapq

def a_star_search(start, goals, blocked, rows, cols):
    # Define movements: direction -> (row_delta, col_delta)
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    # Heuristic: minimum Manhattan distance to any goal
    def heuristic(pos):
        return min(abs(pos[0] - g[0]) + abs(pos[1] - g[1]) for g in goals)

    open_set = []
    heapq.heappush(open_set, (heuristic(start), 0, start, ""))  # (f = g + h, g, position, path_so_far)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current in goals:
            return path  # Found the goal!

        for move, (dr, dc) in directions.items():
            nr, nc = current[0] + dr, current[1] + dc
            next_pos = (nr, nc)

            if 1 <= nr <= rows and 1 <= nc <= cols and next_pos not in blocked:
                if next_pos not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(next_pos)
                    heapq.heappush(open_set, (new_f, new_g, next_pos, path + move))

    return None  # No path found


def main():
    rows, cols = map(int, input().split())
    start = tuple(map(int, input().split()))
    num_goals = int(input())
    goals = set(tuple(map(int, input().split())) for _ in range(num_goals))
    num_blocked = int(input())
    blocked = set(tuple(map(int, input().split())) for _ in range(num_blocked))

    result = a_star_search(start, goals, blocked, rows, cols)
    if result is not None:
        print(result)
    else:
        print("No path found")


if __name__ == "__main__":
    main()
