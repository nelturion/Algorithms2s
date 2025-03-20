# # Кастомное чтение файла для этой задачи
# def file_read(path):
#     a = []
#     with open(path) as file:
#         n = file.readline()
#         for i in range(0, n):
#             action, number = file.readline().split(" ")
#             print(action, number)
#             if action == "+1" or action == "1":
#                 a.append(["+", number])
#             elif action == "0":
#                 a.append(["=", number])
#             else:
#                 a.append(["-", number])
#         file.close()
#     return n, a


def read_list(path_in, path_out):
    sorted_storage = []
    with open(path_in) as file_in:
        n = int(file_in.readline())
        with open(path_out, "w") as file_out:
            for i in range(0, n):
                action, number = file_in.readline().split(" ")
                number = int(number)
                print(action, number)
                if action == "+1" or action == "1":
                    sorted_storage.append(number)
                    sorted_storage.sort(reverse=True)
                elif action == "0":
                    print(sorted_storage, sorted_storage[number-1])
                    file_out.write(str(sorted_storage[number-1]) + "\n")
                else:
                    sorted_storage.remove(number)
            file_out.close()
        file_in.close()


def main():
    read_list("../txtf/input.txt", "../txtf/output.txt")


if __name__ == "__main__":
    import time
    import tracemalloc

    t_start = time.perf_counter()
    tracemalloc.start()
    main()
    print(time.perf_counter() - t_start)
    print(tracemalloc.get_tracemalloc_memory() / 2 ** 20, "MB")