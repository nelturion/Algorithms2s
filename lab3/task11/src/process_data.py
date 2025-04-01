def read_data(file_name: str) -> tuple[int, list[str], str, str]:
    with open(file_name, 'r') as file:
        m = int(file.readline().strip())
        moves = [file.readline().strip() for _ in range(m)]
        from_substance = file.readline().strip()
        to_substance = file.readline().strip()
    return m, moves, from_substance, to_substance


def write_data(data: int, file_name: str) -> None:
    with open(file_name, 'w') as file:
        file.write(str(data))

def validate_data(m: int, moves: list[str]) -> bool:
    if not (1 <= m <= 10 ** 4):
        return False

    if len(moves) != m:
        return False

    return True
