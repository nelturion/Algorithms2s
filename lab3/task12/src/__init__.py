def custom_read(input_file):
    with open(input_file, "r") as file_in:
        lines = file_in.read().splitlines()

    n, m = map(int, lines[0].split())
    print(f"Комнат: {n}\nКоридоров: {m}")

    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    for i in range(1, m+1):
        u, v, c = map(int, lines[i].split())
        graph[u].append((v, c))
        graph[v].append((u, c))

    colors = int(lines[m+1])
    if colors > 0:
        path = list(map(int, lines[m+2].split()))
    else:
        path = []

    print(f"Граф: {graph}\nМаршрут: {path}")
    return graph, path


def custom_write(output_file, result):
    with open(output_file, "w") as file_out:
        file_out.write(result + "\n")
        file_out.close()


def check_maze(input_file, output_file):
    graph, path = custom_read(input_file)
    result = follow_path(graph, path)
    custom_write(output_file, result)


def follow_path(graph, path):
    current_room = 1
    for color in path:
        possible_paths = []
        for next_room, path_color in graph[current_room]:
            if path_color == color:
                possible_paths.append(next_room)
        if possible_paths:
            next_room = possible_paths[0]
            print(f"Переходим из {current_room} в {next_room} | Цвет {color}")
            current_room = next_room
        else:
            print(f"Осуществить переход невозможно")
            return "INCORRECT"

    return str(current_room)


def main():
    check_maze("../txtf/input.txt", "../txtf/output.txt")


if __name__ == "__main__":
    import time
    import tracemalloc

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")
