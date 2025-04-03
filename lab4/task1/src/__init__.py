def naive_substring_search(pattern, text):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i : (i + len(pattern))] == pattern:
            occurrences.append(i+1)
    return " ".join(map(str, occurrences))


def custom_read(path):
    with open(path, "r") as f:
        p = f.readline().strip()
        t = f.readline().strip()
    return p, t


def custom_write(path, text):
    with open(path, "w") as f:
        f.write(text)


def is_data_valid(pattern, text):
    if len(pattern) < 1:
        return False
    if len(pattern) > len(text):
        return False
    if len(text) > 10 ** 4:
        return False
    return True


if __name__ == "__main__":
    p, t = custom_read("../txtf/input.txt")
    if not is_data_valid(p, t):
        custom_write("../txtf/output.txt", "invalid pattern...")
    else:
        res = naive_substring_search(p, t)
        custom_write("../txtf/output.txt", str(str(len(res)) + "\n" + str(res)))
