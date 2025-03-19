# Кастомное чтение файла для этой задачи
def file_read(path):
    list:
    with open(path) as file:
        n = file.readline()
        for i in range(0, n):
            action, number = file.readline().split(" ")
            print(action, number)
            if action == "+1" or action == "1":

    file.close()

    return n


def main():
    n, m, lead, a, b = file_read("../txtf/input.txt")
    # print(n, m, lead, a, b)

    if int(9) in b.get(lead):
        print("У противника есть коз. туз\n")
        output = ["NO"]
    else:
        print("У противника нет коз. туза\n")
        output = check(n, m, lead, clear_dict(a), clear_dict(b))

    print(f"{output}\n")
    write_file("../txtf/output.txt", output)


if __name__ == "__main__":
    import time
    import tracemalloc
    from lab1.defs import *

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")