def read_data(file_name: str) -> list[int]:
    with open(file_name, 'r') as file:
        sequence = list(map(int, file.readline().split()))
    return sequence


def write_data(value: int, expression: str, file_name: str) -> None:
    with open(file_name, 'w') as file:
        file.write(str(value) + '\n')
        file.write(expression + '\n')

def validate_data(sequence: list[int]) -> bool:
    return isinstance(sequence, list) and len(sequence) > 0