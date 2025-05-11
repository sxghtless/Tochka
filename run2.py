import sys
import collections

keys_char = [chr(i) for i in range(ord("a"), ord("z") + 1)]
doors_char = [k.upper() for k in keys_char]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_input():
    return [list(line.strip()) for line in sys.stdin]

def solve(grid):
    rows, cols = len(grid), len(grid[0])
    all_keys = 0
    robots = []

    for r in range(rows):
        for c in range(cols):
            ch = grid[r][c]
            if ch == "@":
                robots.append((r, c))
            elif "a" <= ch <= "z":
                all_keys |= (1 << (ord(ch) - ord("a")))

    initial_state = (0, tuple(robots), 0)
    queue = collections.deque([initial_state])
    visited = set()
    visited.add((tuple(robots), 0))

    while queue:
        steps, positions, keys = queue.popleft()

        if keys == all_keys:
            return steps

        for i, (r, c) in enumerate(positions):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                ch = grid[nr][nc]
                if ch == "#":
                    continue
                if "A" <= ch <= "Z" and not (keys & (1 << (ord(ch.lower()) - ord("a")))):
                    continue
                new_keys = keys
                if "a" <= ch <= "z":
                    new_keys |= (1 << (ord(ch) - ord("a")))

                new_positions = list(positions)
                new_positions[i] = (nr, nc)
                new_positions_tuple = tuple(new_positions)

                state = (new_positions_tuple, new_keys)
                if state not in visited:
                    visited.add(state)
                    queue.append((steps + 1, new_positions_tuple, new_keys))

    return -1

def main():
    data = get_input()
    print(solve(data))

if __name__ == '__main__':
    main()
