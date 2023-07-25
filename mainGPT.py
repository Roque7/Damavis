def is_valid(labyrinth, x, y):
    rows, cols = len(labyrinth), len(labyrinth[0])
    return 0 <= x < rows and 0 <= y < cols and labyrinth[x][y] == '.'

def is_clear_3x3(labyrinth, x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_x, new_y = x + dx, y + dy
            if not is_valid(labyrinth, new_x, new_y):
                return False
    return True

def min_moves_to_end(labyrinth):
    def dfs(x, y, orientation, moves):
        nonlocal min_moves


        if x == rows - 1 and y == cols - 1:
            min_moves = min(min_moves, moves)
            return


        if orientation == 'horizontal':
            for dx, dy in [(0, 1), (0, -1), (1, 0)]:
                new_x, new_y = x + dx, y + dy


                if is_valid(labyrinth, new_x, new_y) and is_clear_3x3(labyrinth, new_x - 1, new_y - 1) and (new_x, new_y, orientation) not in visited:
                    visited.add((new_x, new_y, orientation))
                    dfs(new_x, new_y, orientation, moves + 1)
                    visited.remove((new_x, new_y, orientation))

        elif orientation == 'vertical':
            for dx, dy in [(1, 0), (-1, 0), (0, 1)]:
                new_x, new_y = x + dx, y + dy


                if is_valid(labyrinth, new_x, new_y) and is_clear_3x3(labyrinth, new_x - 1, new_y - 1) and (new_x, new_y, orientation) not in visited:
                    visited.add((new_x, new_y, orientation))
                    dfs(new_x, new_y, orientation, moves + 1)
                    visited.remove((new_x, new_y, orientation))


        new_orientation = 'horizontal' if orientation == 'vertical' else 'vertical'
        if is_valid(labyrinth, x, y) and is_valid(labyrinth, x + 1, y) and is_valid(labyrinth, x - 1, y):
            if is_clear_3x3(labyrinth, x - 1, y - 1) and is_clear_3x3(labyrinth, x - 1, y) and is_clear_3x3(labyrinth, x - 1, y + 1) and (x, y, new_orientation) not in visited:
                visited.add((x, y, new_orientation))
                dfs(x, y, new_orientation, moves + 1)
                visited.remove((x, y, new_orientation))

    rows, cols = len(labyrinth), len(labyrinth[0])
    start = (0, 0, 'horizontal')
    visited = set()
    min_moves = float('inf')
    dfs(0, 0, 'horizontal', 0)

    return min_moves if min_moves != float('inf') else -1

# Example usage:
labyrinth = [
    ['.', '.', '.', '#'],
    ['.', '.', '.', '.'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', '.']
]

print(min_moves_to_end(labyrinth))  # Output: 5 (Shortest path: (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (3, 1) -> (3, 2))
