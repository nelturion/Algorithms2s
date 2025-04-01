import heapq


def fastest_route(n, start, finish, routes):
    graph = {i: [] for i in range(1, n + 1)}  # создали набор узлов (деревень), пока не связаны между собой
    for departure, dep_time, dst, arr_time in routes:
        graph[departure].append((dep_time, dst, arr_time))  # связали деревни и маршрутки между ними

    pq = [(0, start)]  # Очередь с приоритетом. Первый элемент в Дейкстре - точка начала пути (время, место)
    min_time = {i: float('inf') for i in range(1, n + 1)}
    min_time[start] = 0

    while pq:
        curr_time, curr_village = heapq.heappop(pq)
        if curr_village == finish:
            return curr_time

        for dep_time, dst, arr_time in graph[curr_village]:
            if dep_time >= curr_time and arr_time < min_time[dst]:  # если не опоздали на абобус и время его прибытия в
                min_time[dst] = arr_time                            # пункт назначения меньше минимального вермени из
                heapq.heappush(pq, (arr_time, dst))                 # всех возможных временей прибытия в этот пункт
    return -1


if __name__ == '__main__':
    input_filename = "input1.txt"   # CHANGE THIS TO USE DIFFERENT INPUT GRAPH

    # чтение расписания рейсов
    with open("../txtf/"+input_filename, 'r') as f:
        lines = f.readlines()

    n = int(lines[0])                   # Количество деревень
    d, v = map(int, lines[1].split())   # Начальная и конечная деревня
    r = int(lines[2])                   # Количество автобусных рейсов

    routes = [tuple(map(int, line.strip().split())) for line in lines[3:3 + r]]  # Маршруты автобусов

    min_time = fastest_route(n, d, v, routes)
    print("fastest arrival: ", min_time)

    # вывод в файл
    with open("../txtf/output.txt", 'w') as f:
        if min_time == float('inf'):
            f.write('-1\n')  # Невозможно добраться
        else:
            f.write(str(min_time))


### ACMP stats (comma separated):
### id,23142393,01.04.2025,22:58:32,Андреюк Николай Ростиславович,0134,Python,Accepted,0.062,3138 Кб