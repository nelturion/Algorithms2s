def prefix(s):
    n = len(s)
    prefix_list = [0]*n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = prefix_list[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix_list[i] = j

    return prefix_list


def main():
    with open("../txtf/input.txt", "r") as file_in:
        s = file_in.readline().strip()

    prefix_list = prefix(s)

    with open("../txtf/output.txt", "w") as file_out:
        file_out.write(" ".join(map(str, prefix_list)) + "\n")


if __name__ == "__main__":
    main()
