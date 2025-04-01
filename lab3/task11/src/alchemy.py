from collections import deque, defaultdict

from lab3.task11.src.process_data import read_data, write_data, validate_data


def process_substances(input_moves: list[str], start: str, target: str) -> int:
    moves = defaultdict(list)

    for line in input_moves:
        from_substance, to_substance = line.split(' -> ')
        moves[from_substance].append(to_substance)

    distances = {start: 0}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == target:
            return distances[current]

        for next_substance in moves[current]:
            if next_substance not in distances:
                distances[next_substance] = distances[current] + 1
                queue.append(next_substance)

    return -1


def main():
    m, moves, from_substance, to_substance = read_data('../txt_files/input.txt')
    validate_data(m, moves)
    result = process_substances(moves, from_substance, to_substance)
    write_data(result, '../txt_files/output.txt')


if __name__ == '__main__':
    main()
