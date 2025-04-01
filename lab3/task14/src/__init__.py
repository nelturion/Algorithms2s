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
            if dep_time >= curr_time and arr_time < min_time[dst]:  # если не опоздали на абобус и время его прибытия в пункт назначения меньше минимального вермени из всех возможных временей прибыытия в этот пункт
                min_time[dst] = arr_time
                heapq.heappush(pq, (arr_time, dst))
    return -1
        # if curr_time < min_time[curr_village]:
        #     min_time[curr_village] = curr_time
        #     heapq.heappush(pq, (curr_time, curr_village))

    # # Граф для хранения автобусных рейсов
    # graph = {i: [] for i in range(1, n + 1)}


#
# for i in range(3, 3 + r):
#     u, t1, t2, w = map(int, lines[i].split())
#     graph[u].append((t1, t2, w))
#
# # Алгоритм Дейкстры с учетом времени отправления и прибытия
# INF = float('inf')
# min_time = [INF] * (n + 1)
# min_time[d] = 0
# pq = [(0, d)]  # Очередь с приоритетом (текущее время, текущая деревня)
#
# while pq:
#     current_time, current_village = heapq.heappop(pq)
#
#     if current_time > min_time[current_village]:
#         continue
#
#     for t1, t2, w in graph[current_village]:
#         if current_time <= t1:  # Можно успеть на автобус
#             arrival_time = t2 + w
#             if arrival_time < min_time[w]:
#                 min_time[w] = arrival_time
#                 heapq.heappush(pq, (arrival_time, w))
#
# return min_time[d]


if __name__ == '__main__':
    input_filename = "input1.txt"   # CHANGE THIS TO USE DIFFERENT INPUT GRAPH

    # чтение расписания рейсов
    with open("../txtf/"+input_filename, 'r') as f:
        lines = f.readlines()

    n = int(lines[0])  # Количество деревень
    d, v = map(int, lines[1].split())  # Начальная и конечная деревня
    r = int(lines[2])  # Количество автобусных рейсов

    routes = [tuple(map(int, line.strip().split())) for line in lines[3:3 + r]]  # Маршруты автобусов

    min_time = fastest_route(n, d, v, routes)
    print("fastest arrival: ", min_time)

    # вывод в файл
    with open("../txtf/output.txt", 'w') as f:
        if min_time == float('inf'):
            f.write('-1\n')  # Невозможно добраться
        else:
            f.write(str(min_time))
