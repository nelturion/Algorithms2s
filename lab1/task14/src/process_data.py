def read_data(input_path: str) -> list[str]:
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read().strip()
    return data


def write_data(result: int, output_path: str) -> None:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(result))


def validate_data(tokens: list[str]) -> bool:
    return all(char in "0123456789+-*" for char in tokens)