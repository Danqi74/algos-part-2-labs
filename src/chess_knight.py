from binary_tree_priority_queue import PriorityQueue
from typing import Tuple


def get_min_moves_count(input_path="src/input.txt", output_path="src/output.txt"):
    with open(input_path, "r") as file:
        board_size = int(next(file))
        start_pos = tuple(map(int, next(file).split(", ")))
        destination_pos = tuple(map(int, next(file).split(", ")))
    result = _get_min_moves_count(board_size, start_pos, destination_pos)
    with open(output_path, "w") as file:
        file.write(str(result))


def _get_min_moves_count(board_size: int, start_pos: Tuple[int, int], destination_pos: Tuple[int, int]):
    if (
        start_pos[0] < 0
        or start_pos[0] >= board_size
        or start_pos[1] < 0
        or start_pos[1] >= board_size
    ):
        return -1
    moves = ((2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
    queue = PriorityQueue()
    queue.insert(start_pos, 0)
    count_of_moves = {start_pos: 0}
    while queue.root:
        vertex = queue.pop()
        if vertex == destination_pos:
            count_of_moves[destination_pos] = count_of_moves[vertex]
            break
        for move in moves:
            new_vertex = (vertex[0] + move[0], vertex[1] + move[1])
            if (
                new_vertex[0] < 0
                or new_vertex[0] >= board_size
                or new_vertex[1] < 0
                or new_vertex[1] >= board_size
            ):
                continue
            if not new_vertex in count_of_moves:
                queue.insert(new_vertex, -count_of_moves[vertex])
                count_of_moves[new_vertex] = count_of_moves[vertex] + 1
    if not destination_pos in count_of_moves:
        return -1
    return count_of_moves[destination_pos]


if __name__ == "__main__":
    get_min_moves_count()
