from lab4.task7.src.process_data import read_data, write_data


def longest_common_substring(s: str, t: str) -> int:
    n, m = len(s), len(t)
    base = 257
    mod = 10 ** 9 + 7

    # Вычисляем массив степеней base для максимальной длины
    max_len = max(n, m)
    pow_base = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow_base[i] = (pow_base[i - 1] * base) % mod

    # Вычисляем префиксные хэши
    hash_s = [0] * (n + 1)
    for i in range(n):
        hash_s[i + 1] = (hash_s[i] * base + ord(s[i])) % mod

    hash_t = [0] * (m + 1)
    for i in range(m):
        hash_t[i + 1] = (hash_t[i] * base + ord(t[i])) % mod

    # Функция для вычисления хэша подстроки [i, j) по префиксному массиву
    def get_hash(prefix_hash, i, j):
        return (prefix_hash[j] - prefix_hash[i] * pow_base[j - i]) % mod

    def is_substring_exists(length: int) -> tuple[bool, int, int]:
        """Проверяет, существует ли общая подстрока длины length в строках s и t.
        Возвращает кортеж (True, i, j), где i - индекс начала подстроки в s, j - индекс начала подстроки в t."""

        if length == 0:
            return True, 0, 0

        seen_hashes = set()
        seen_index = dict()
        # Добавляем хэши всех подстрок длины length из строки s
        for i in range(n - length + 1):
            s_char_hash = get_hash(hash_s, i, i + length)
            seen_hashes.add(s_char_hash)
            seen_index[s_char_hash] = i
        # Проверяем, встречается ли хотя бы один из этих хэшей в строке t
        for j in range(m - length + 1):
            t_char_hash = get_hash(hash_t, j, j + length)
            if t_char_hash in seen_hashes:
                return True, seen_index[t_char_hash], j
        return False, -1, -1

    # Двоичный поиск по длине подстроки
    low, high = 0, min(n, m)
    result = (0, 0, 0)

    while low <= high:
        mid = (low + high) // 2
        is_exists, index_s, index_t = is_substring_exists(mid)
        if is_exists:
            result = index_s, index_t, mid
            low = mid + 1
        else:
            high = mid - 1

    return result


def main() -> None:
    words = read_data("../txt_files/input.txt")
    result = []
    for word_s, word_t in words:
        result.append(longest_common_substring(word_s, word_t))
    write_data(result, "../txt_files/output.txt")


if __name__ == "__main__":
    main()
