def read_data(file_name: str) -> list[[str, str]]:
    with open(file_name, 'r') as file:
        words = [line.strip().split() for line in file.readlines()]
    return words


def write_data(data: tuple[int], file_name: str) -> None:
    with open(file_name, 'w') as file:
        for line in data:
            file.write(' '.join(map(str, line)) + "\n")


def validate_data(words: list[str, str]) -> bool:
    return all(len(word_list) == 2 for word_list in words)
