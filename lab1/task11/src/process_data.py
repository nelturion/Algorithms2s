def read_data(file_name: str) -> tuple[int, int, list[int]]:
    with open(file_name, 'r') as file:
        w, n = map(int, file.readline().split())  # вместимость сумки и количество слитков
        weights = list(map(int, file.readline().split()))
    return w, n, weights


def write_data(data: int, file_name: str) -> None:
    with open(file_name, 'w') as file:
        file.write(str(data))

def validate_data(w: int, n: int, wights: list[int]) -> bool:
    # Проверяем ограничение для W: 1 ≤ w ≤ 10^4
    if not (1 <= w <= 10 ** 4):
        return False

    # Проверяем ограничение для n: 1 ≤ n ≤ 300
    if not (1 <= n <= 300):
        return False

    # Проверяем, что длина списка весов равна n
    if len(wights) != n:
        return False

    # Проверяем ограничение для каждого веса: 0 ≤ weight ≤ 10^5
    for weight in wights:
        if not (0 <= weight <= 10**5):
            return False

    return True
