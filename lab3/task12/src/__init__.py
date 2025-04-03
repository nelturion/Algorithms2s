def custom_read(input_file):
    with open(input_file, "r") as file_in:
        lines = file_in.read().splitlines()

    n, m = map(int, lines[0].split())

    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for i in range(1, m + 1):
        start_room, next_room, color = map(int, lines[i].split())
        graph[start_room].append((next_room, color))
        graph[next_room].append((start_room, color))

    colors = int(lines[m + 1])
    path = list(map(int, lines[m + 2].split())) if colors > 0 else []

    return graph, path


def custom_write(output_file, result):
    with open(output_file, "w") as file_out:
        file_out.write(result + "\n")
        file_out.close()


def read_maze(input_file, output_file):
    graph, path = custom_read(input_file)
    result = follow_path(graph, path)
    custom_write(output_file, result)


def follow_path(graph, path):
    current_room = 1
    for color in path:
        possible_paths = [next_room for next_room, path_color in graph[current_room] if path_color == color]
        if possible_paths:
            current_room = possible_paths[0]
        else:
            return "INCORRECT"

    return str(current_room)


def main():
    read_maze("../txtf/input.txt", "../txtf/output.txt")


if __name__ == "__main__":
    import time
    import tracemalloc

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")
