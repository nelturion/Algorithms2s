from lab1.task11.src.process_data import read_data, write_data, validate_data


def maximize_gold(capacity: int, weights: list[int]) -> int :
    """
    Помещает в сумку как можно больше слитков и возвращает массу слитков в сумке
    :param capacity: вместимость сумки
    :param weights: веса имеющихся слитков
    :return: максимальный вес слитков в сумке
    """
    taken = 0
    weights.sort(reverse=True)
    for weight in weights:
        if taken + weight <= capacity:
            taken += weight
        elif taken == capacity:
            break
    return taken

def main():
    w, n, wights = read_data('../files/input.txt')
    if not validate_data(w, n, wights):
        raise ValueError("Введите корректные данные")
    result = maximize_gold(w, wights)
    write_data(result, '../files/output.txt')

if __name__ == '__main__':
    import time
    import tracemalloc

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")